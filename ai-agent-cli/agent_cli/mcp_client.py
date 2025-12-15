"""MCP (Model Context Protocol) SSE client for connecting to remote tool servers."""

import json
import uuid
from typing import Optional, Any, Callable
from dataclasses import dataclass

import httpx
from httpx_sse import connect_sse
from rich.console import Console

from .models import MCPTool, MCPServer


console = Console()


@dataclass
class MCPResponse:
    """Response from an MCP server."""
    
    id: str
    result: Optional[dict] = None
    error: Optional[dict] = None


class MCPClient:
    """Client for connecting to MCP servers via SSE with optional Bearer auth."""
    
    def __init__(
        self,
        server: MCPServer,
        access_token: Optional[str] = None,
        token_provider: Optional[Callable[[], Optional[str]]] = None,
    ):
        """Initialize MCP client.
        
        Args:
            server: MCP server configuration
            access_token: Static Bearer token for authentication
            token_provider: Callable that returns a fresh token (for dynamic auth)
        """
        self.server = server
        self._access_token = access_token
        self._token_provider = token_provider
        self._session_url: Optional[str] = None
        self._tools: list[MCPTool] = []
        self._connected = False
    
    def _get_auth_headers(self) -> dict[str, str]:
        """Get authentication headers for requests.
        
        Returns:
            Dictionary of headers including Authorization if token is available
        """
        headers = {}
        
        # Get token from provider or static token
        token = None
        if self._token_provider:
            token = self._token_provider()
        elif self._access_token:
            token = self._access_token
        
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        return headers
    
    def update_token(self, token: str) -> None:
        """Update the access token.
        
        Args:
            token: New Bearer token
        """
        self._access_token = token
        self._token_provider = None  # Clear provider, use static token
    
    @property
    def is_connected(self) -> bool:
        """Check if connected to the server."""
        return self._connected
    
    @property
    def tools(self) -> list[MCPTool]:
        """Get cached tools from this server."""
        return self._tools
    
    def connect(self) -> bool:
        """Connect to the MCP server and initialize the session.
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            auth_headers = self._get_auth_headers()
            
            # First, establish SSE connection to get the session endpoint
            with httpx.Client(timeout=30.0) as client:
                # Send initial connection request
                headers = {"Accept": "text/event-stream"}
                headers.update(auth_headers)
                
                response = client.get(
                    self.server.url,
                    headers=headers,
                )
                
                if response.status_code == 401:
                    console.print(f"[red]Authentication failed for {self.server.name}: Unauthorized[/red]")
                    return False
                
                if response.status_code == 403:
                    console.print(f"[red]Access denied to {self.server.name}: Forbidden[/red]")
                    return False
                
                if response.status_code != 200:
                    console.print(f"[red]Failed to connect to {self.server.name}: HTTP {response.status_code}[/red]")
                    return False
                
                # Parse the SSE stream to get the session URL
                # The server should send an 'endpoint' event with the session URL
                for line in response.iter_lines():
                    if line.startswith("data:"):
                        data = json.loads(line[5:].strip())
                        if "endpoint" in data:
                            self._session_url = data["endpoint"]
                            break
                
                if not self._session_url:
                    # If no separate endpoint, use the base URL for requests
                    self._session_url = self.server.url.replace("/sse", "")
            
            # Initialize the MCP session
            init_result = self._send_request("initialize", {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "clientInfo": {
                    "name": "ai-agent-cli",
                    "version": "0.1.0"
                }
            })
            
            if init_result and init_result.result:
                # Send initialized notification
                self._send_notification("notifications/initialized", {})
                self._connected = True
                
                # Fetch available tools
                self._fetch_tools()
                
                console.print(f"[green]✓ Connected to MCP server: {self.server.name}[/green]")
                return True
            
            return False
            
        except Exception as e:
            console.print(f"[red]Failed to connect to {self.server.name}: {e}[/red]")
            return False
    
    def _send_request(self, method: str, params: dict) -> Optional[MCPResponse]:
        """Send a JSON-RPC request to the MCP server.
        
        Args:
            method: JSON-RPC method name
            params: Method parameters
            
        Returns:
            MCPResponse if successful, None otherwise
        """
        if not self._session_url:
            return None
        
        request_id = str(uuid.uuid4())
        payload = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": method,
            "params": params
        }
        
        try:
            auth_headers = self._get_auth_headers()
            headers = {"Content-Type": "application/json"}
            headers.update(auth_headers)
            
            with httpx.Client(timeout=60.0) as client:
                response = client.post(
                    self._session_url,
                    json=payload,
                    headers=headers,
                )
                
                if response.status_code == 401:
                    console.print(f"[red]MCP request unauthorized - token may be expired[/red]")
                    return None
                
                if response.status_code == 200:
                    data = response.json()
                    return MCPResponse(
                        id=data.get("id", request_id),
                        result=data.get("result"),
                        error=data.get("error")
                    )
                elif response.status_code == 202:
                    # Accepted - need to poll for result via SSE
                    return self._poll_for_response(request_id)
                    
        except Exception as e:
            console.print(f"[red]MCP request error: {e}[/red]")
        
        return None
    
    def _poll_for_response(self, request_id: str) -> Optional[MCPResponse]:
        """Poll SSE endpoint for a response to a pending request.
        
        Args:
            request_id: The request ID to wait for
            
        Returns:
            MCPResponse when received, None on timeout
        """
        try:
            auth_headers = self._get_auth_headers()
            
            with httpx.Client(timeout=60.0) as client:
                with connect_sse(client, "GET", self.server.url, headers=auth_headers) as event_source:
                    for sse in event_source.iter_sse():
                        if sse.event == "message":
                            data = json.loads(sse.data)
                            if data.get("id") == request_id:
                                return MCPResponse(
                                    id=request_id,
                                    result=data.get("result"),
                                    error=data.get("error")
                                )
        except Exception as e:
            console.print(f"[red]SSE polling error: {e}[/red]")
        
        return None
    
    def _send_notification(self, method: str, params: dict) -> None:
        """Send a JSON-RPC notification (no response expected).
        
        Args:
            method: Notification method name
            params: Notification parameters
        """
        if not self._session_url:
            return
        
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        }
        
        try:
            auth_headers = self._get_auth_headers()
            headers = {"Content-Type": "application/json"}
            headers.update(auth_headers)
            
            with httpx.Client(timeout=30.0) as client:
                client.post(
                    self._session_url,
                    json=payload,
                    headers=headers,
                )
        except Exception:
            pass  # Notifications don't require acknowledgment
    
    def _fetch_tools(self) -> None:
        """Fetch available tools from the server."""
        result = self._send_request("tools/list", {})
        
        if result and result.result:
            tools_data = result.result.get("tools", [])
            self._tools = []
            
            for tool_data in tools_data:
                tool = MCPTool(
                    name=tool_data.get("name", ""),
                    description=tool_data.get("description", ""),
                    input_schema=tool_data.get("inputSchema", {}),
                    server_name=self.server.name
                )
                self._tools.append(tool)
    
    def call_tool(self, name: str, arguments: dict) -> Optional[Any]:
        """Call a tool on the MCP server.
        
        Args:
            name: Tool name
            arguments: Tool arguments
            
        Returns:
            Tool result if successful, None otherwise
        """
        result = self._send_request("tools/call", {
            "name": name,
            "arguments": arguments
        })
        
        if result:
            if result.error:
                console.print(f"[red]Tool error: {result.error.get('message', 'Unknown error')}[/red]")
                return None
            
            if result.result:
                # MCP tools return content array
                content = result.result.get("content", [])
                if content:
                    # Combine text content
                    text_parts = []
                    for item in content:
                        if item.get("type") == "text":
                            text_parts.append(item.get("text", ""))
                    return "\n".join(text_parts) if text_parts else content
                return result.result
        
        return None
    
    def disconnect(self) -> None:
        """Disconnect from the MCP server."""
        self._connected = False
        self._session_url = None
        self._tools = []


class MCPManager:
    """Manages multiple MCP server connections with optional authentication."""
    
    def __init__(
        self,
        token_provider: Optional[Callable[[], Optional[str]]] = None,
    ):
        """Initialize MCP manager.
        
        Args:
            token_provider: Optional callable that returns a Bearer token for MCP/Gateway auth.
                           If provided, all MCP server connections will use this token.
        """
        self._clients: dict[str, MCPClient] = {}
        self._token_provider = token_provider
    
    def set_token_provider(self, provider: Callable[[], Optional[str]]) -> None:
        """Set the token provider for MCP authentication.
        
        Args:
            provider: Callable that returns a Bearer token
        """
        self._token_provider = provider
        
        # Update existing clients
        for client in self._clients.values():
            client._token_provider = provider
    
    def add_server(self, server: MCPServer, access_token: Optional[str] = None) -> bool:
        """Add and connect to an MCP server.
        
        Args:
            server: MCP server configuration
            access_token: Optional static Bearer token (overrides token_provider for this server)
            
        Returns:
            True if connection successful, False otherwise
        """
        client = MCPClient(
            server=server,
            access_token=access_token,
            token_provider=self._token_provider if not access_token else None,
        )
        if client.connect():
            self._clients[server.name] = client
            return True
        return False
    
    def remove_server(self, name: str) -> None:
        """Remove an MCP server.
        
        Args:
            name: Server name
        """
        if name in self._clients:
            self._clients[name].disconnect()
            del self._clients[name]
    
    def get_client(self, name: str) -> Optional[MCPClient]:
        """Get a specific MCP client.
        
        Args:
            name: Server name
            
        Returns:
            MCPClient if found, None otherwise
        """
        return self._clients.get(name)
    
    def list_all_tools(self) -> list[MCPTool]:
        """Get all tools from all connected servers.
        
        Returns:
            List of all available tools
        """
        tools = []
        for client in self._clients.values():
            tools.extend(client.tools)
        return tools
    
    def get_openai_tools(self) -> list[dict]:
        """Get all tools in OpenAI format.
        
        Returns:
            List of tool definitions for OpenAI API
        """
        return [tool.to_openai_tool() for tool in self.list_all_tools()]
    
    def call_tool(self, name: str, arguments: dict) -> Optional[Any]:
        """Call a tool by name, finding the appropriate server.
        
        Args:
            name: Tool name
            arguments: Tool arguments
            
        Returns:
            Tool result if successful, None otherwise
        """
        # Find which server has this tool
        for client in self._clients.values():
            for tool in client.tools:
                if tool.name == name:
                    return client.call_tool(name, arguments)
        
        console.print(f"[red]Tool not found: {name}[/red]")
        return None
    
    def disconnect_all(self) -> None:
        """Disconnect from all servers."""
        for client in self._clients.values():
            client.disconnect()
        self._clients.clear()
    
    @property
    def connected_servers(self) -> list[str]:
        """Get list of connected server names."""
        return list(self._clients.keys())
