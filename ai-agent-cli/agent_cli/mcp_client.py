"""MCP (Model Context Protocol) client using official SDK with Streamable HTTP transport."""

import asyncio
from typing import Optional, Any, Callable
from dataclasses import dataclass

from rich.console import Console

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.types import Implementation

from .models import MCPTool, MCPServer


console = Console()


@dataclass
class MCPResponse:
    """Response from an MCP server."""
    
    id: str
    result: Optional[dict] = None
    error: Optional[dict] = None


class MCPClient:
    """Client for connecting to MCP servers via Streamable HTTP with optional Bearer auth."""
    
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
        self._tools: list[MCPTool] = []
        self._connected = False
        self._session: Optional[ClientSession] = None
        self._read_stream = None
        self._write_stream = None
        self._context_stack = None
    
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
            # Run the async connection in a new event loop
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                # If there's no event loop, create one
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            return loop.run_until_complete(self._connect_async())
        except asyncio.CancelledError:
            console.print(f"[yellow]⚠ Connection to {self.server.name} was cancelled (server may be unavailable)[/yellow]")
            return False
        except Exception as e:
            console.print(f"[yellow]⚠ Failed to connect to {self.server.name}: {e}[/yellow]")
            return False
    
    async def _connect_async(self) -> bool:
        """Async implementation of connect."""
        try:
            headers = self._get_auth_headers()
            
            # Use the official MCP SDK's streamablehttp_client
            # We need to keep the context manager open, so we manually enter it
            self._context_stack = streamablehttp_client(
                url=self.server.url,
                headers=headers if headers else None,
                timeout=30,
                sse_read_timeout=300,
            )
            
            # Enter the async context manager
            self._read_stream, self._write_stream, self._get_session_id = await self._context_stack.__aenter__()
            
            # Create the session
            self._session = ClientSession(
                self._read_stream, 
                self._write_stream,
                client_info=Implementation(name="ai-agent-cli", version="0.1.0"),
            )
            
            # Enter the session context
            await self._session.__aenter__()
            
            # Initialize the MCP session
            init_result = await self._session.initialize()
            
            if init_result:
                self._connected = True
                
                # Fetch available tools
                await self._fetch_tools_async()
                
                console.print(f"[green]✓ Connected to MCP server: {self.server.name}[/green]")
                console.print(f"[dim]  Server: {init_result.serverInfo.name} v{init_result.serverInfo.version}[/dim]")
                console.print(f"[dim]  Protocol: {init_result.protocolVersion}[/dim]")
                return True
            
            return False
            
        except asyncio.CancelledError:
            # Re-raise to be caught by the sync wrapper
            raise
        except Exception as e:
            error_msg = str(e)
            if "401" in error_msg:
                console.print(f"[red]Authentication failed for {self.server.name}: Unauthorized[/red]")
            elif "403" in error_msg:
                console.print(f"[red]Access denied to {self.server.name}: Forbidden[/red]")
            elif "422" in error_msg:
                console.print(f"[red]Failed to connect to {self.server.name}: HTTP 422 - Server rejected request[/red]")
                console.print(f"[yellow]This may indicate a protocol version mismatch.[/yellow]")
            else:
                console.print(f"[red]Failed to connect to {self.server.name}: {e}[/red]")
            return False
    
    async def _fetch_tools_async(self) -> None:
        """Fetch available tools from the server."""
        if not self._session:
            return
            
        try:
            result = await self._session.list_tools()
            self._tools = []
            
            for tool in result.tools:
                mcp_tool = MCPTool(
                    name=tool.name,
                    description=tool.description or "",
                    input_schema=tool.inputSchema if hasattr(tool, 'inputSchema') else {},
                    server_name=self.server.name
                )
                self._tools.append(mcp_tool)
        except Exception as e:
            console.print(f"[yellow]Warning: Could not fetch tools: {e}[/yellow]")
    
    def call_tool(self, name: str, arguments: dict) -> Optional[Any]:
        """Call a tool on the MCP server.
        
        Args:
            name: Tool name
            arguments: Tool arguments
            
        Returns:
            Tool result if successful, None otherwise
        """
        try:
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(self._call_tool_async(name, arguments))
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return loop.run_until_complete(self._call_tool_async(name, arguments))
    
    async def _call_tool_async(self, name: str, arguments: dict) -> Optional[Any]:
        """Async implementation of call_tool."""
        if not self._session:
            console.print(f"[red]Not connected to MCP server[/red]")
            return None
        
        try:
            result = await self._session.call_tool(name, arguments)
            
            if result.isError:
                error_content = result.content[0] if result.content else None
                error_msg = error_content.text if error_content and hasattr(error_content, 'text') else 'Unknown error'
                console.print(f"[red]Tool error: {error_msg}[/red]")
                return None
            
            # Extract text content from result
            if result.content:
                text_parts = []
                for item in result.content:
                    if hasattr(item, 'text'):
                        text_parts.append(item.text)
                return "\n".join(text_parts) if text_parts else result.content
            
            return None
            
        except Exception as e:
            console.print(f"[red]Tool call error: {e}[/red]")
            return None
    
    def disconnect(self) -> None:
        """Disconnect from the MCP server."""
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self._disconnect_async())
        except RuntimeError:
            pass
        finally:
            self._connected = False
            self._session = None
            self._tools = []
    
    async def _disconnect_async(self) -> None:
        """Async implementation of disconnect."""
        try:
            if self._session:
                await self._session.__aexit__(None, None, None)
            if self._context_stack:
                await self._context_stack.__aexit__(None, None, None)
        except Exception:
            pass  # Ignore errors during cleanup


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
