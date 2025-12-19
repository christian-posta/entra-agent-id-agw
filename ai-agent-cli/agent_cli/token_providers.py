"""Token provider abstraction for pluggable token acquisition strategies."""

from typing import Protocol, Optional, runtime_checkable

import httpx
from rich.console import Console

from .auth import OBOTokenManager, AZURE_COGNITIVE_SERVICES_SCOPE
from .models import TokenResult


console = Console()


@runtime_checkable
class TokenProvider(Protocol):
    """Protocol for token acquisition strategies.
    
    Implementations can either perform direct OBO token exchange
    or delegate to the Microsoft Entra SDK sidecar.
    """
    
    def initialize(self, user_token: str) -> bool:
        """Initialize the provider with the user's token (Tc).
        
        Args:
            user_token: The user's access token with Blueprint as audience
            
        Returns:
            True if initialization successful, False otherwise
        """
        ...
    
    def get_openai_token(self) -> Optional[str]:
        """Get an OBO token (T2) for Azure OpenAI / Cognitive Services.
        
        Returns:
            Access token string if successful, None otherwise
        """
        ...
    
    def get_mcp_token(self) -> Optional[str]:
        """Get an OBO token (T2) for MCP server.
        
        Returns:
            Access token string if successful, None otherwise
        """
        ...


class DirectTokenProvider:
    """Token provider using direct OBO exchange.
    
    This wraps the existing OBOTokenManager and performs T1/T2
    token exchange directly against Microsoft Entra ID.
    
    Requires:
        - BLUEPRINT_APP_ID
        - BLUEPRINT_CLIENT_SECRET
        - AGENT_IDENTITY_APP_ID
        - MCP_SERVER_APP_ID (optional, for MCP tokens)
    """
    
    def __init__(
        self,
        tenant_id: str,
        blueprint_app_id: str,
        blueprint_client_secret: str,
        agent_identity_app_id: str,
        mcp_server_app_id: Optional[str] = None,
    ):
        """Initialize direct token provider.
        
        Args:
            tenant_id: Azure AD tenant ID
            blueprint_app_id: Blueprint application ID
            blueprint_client_secret: Blueprint client secret
            agent_identity_app_id: Agent identity application ID
            mcp_server_app_id: MCP server application ID (optional)
        """
        self.tenant_id = tenant_id
        self.blueprint_app_id = blueprint_app_id
        self.blueprint_client_secret = blueprint_client_secret
        self.agent_identity_app_id = agent_identity_app_id
        self.mcp_server_app_id = mcp_server_app_id
        
        self._obo_manager: Optional[OBOTokenManager] = None
        self._initialized = False
    
    def initialize(self, user_token: str) -> bool:
        """Initialize with user token and create OBO manager.
        
        Args:
            user_token: User's access token (Tc) with Blueprint audience
            
        Returns:
            True if successful
        """
        try:
            self._obo_manager = OBOTokenManager(
                tenant_id=self.tenant_id,
                blueprint_app_id=self.blueprint_app_id,
                blueprint_client_secret=self.blueprint_client_secret,
                agent_identity_app_id=self.agent_identity_app_id,
                user_token=user_token,
            )
            self._initialized = True
            console.print("[green]✓ DirectTokenProvider initialized[/green]")
            return True
        except Exception as e:
            console.print(f"[red]Failed to initialize DirectTokenProvider: {e}[/red]")
            return False
    
    def get_openai_token(self) -> Optional[str]:
        """Get OBO token for Azure OpenAI using direct exchange.
        
        Returns:
            Access token string if successful, None otherwise
        """
        if not self._initialized or not self._obo_manager:
            console.print("[red]DirectTokenProvider not initialized[/red]")
            return None
        
        token = self._obo_manager.get_azure_openai_token()
        return token.access_token if token else None
    
    def get_mcp_token(self) -> Optional[str]:
        """Get OBO token for MCP server using direct exchange.
        
        Returns:
            Access token string if successful, None otherwise
        """
        if not self._initialized or not self._obo_manager:
            console.print("[red]DirectTokenProvider not initialized[/red]")
            return None
        
        if not self.mcp_server_app_id:
            console.print("[dim]No MCP_SERVER_APP_ID configured, skipping MCP token[/dim]")
            return None
        
        mcp_scope = f"api://{self.mcp_server_app_id}/.default"
        token = self._obo_manager.get_token_for_scope(mcp_scope)
        return token.access_token if token else None
    
    def clear_cache(self) -> None:
        """Clear cached tokens."""
        if self._obo_manager:
            self._obo_manager.clear_cache()


class SidecarTokenProvider:
    """Token provider delegating to Microsoft Entra SDK sidecar.
    
    This calls the sidecar's HTTP API to perform token exchange,
    offloading the T1/T2 exchange logic to the sidecar container.
    
    Requires:
        - SIDECAR_URL
        - SIDECAR_OPENAI_API_NAME
        - SIDECAR_MCP_API_NAME
        - AGENT_IDENTITY_APP_ID (optional, to pass ?AgentIdentity= param)
    """
    
    def __init__(
        self,
        sidecar_url: str = "http://localhost:5000",
        openai_api_name: str = "openai",
        mcp_api_name: str = "mcp",
        agent_identity_app_id: Optional[str] = None,
    ):
        """Initialize sidecar token provider.
        
        Args:
            sidecar_url: Base URL of the sidecar (e.g., http://localhost:5000)
            openai_api_name: Name of the OpenAI downstream API in sidecar config
            mcp_api_name: Name of the MCP downstream API in sidecar config
            agent_identity_app_id: Optional agent identity to pass to sidecar
        """
        self.sidecar_url = sidecar_url.rstrip("/")
        self.openai_api_name = openai_api_name
        self.mcp_api_name = mcp_api_name
        self.agent_identity_app_id = agent_identity_app_id
        
        self._user_token: Optional[str] = None
        self._initialized = False
        
        # Cache tokens to avoid repeated sidecar calls
        self._openai_token: Optional[str] = None
        self._mcp_token: Optional[str] = None
    
    def initialize(self, user_token: str) -> bool:
        """Initialize with user token.
        
        Args:
            user_token: User's access token (Tc) with Blueprint audience
            
        Returns:
            True if sidecar is healthy and ready
        """
        self._user_token = user_token
        
        # Verify sidecar is reachable
        try:
            with httpx.Client(timeout=10) as client:
                response = client.get(f"{self.sidecar_url}/healthz")
                if response.status_code == 200:
                    self._initialized = True
                    console.print(f"[green]✓ SidecarTokenProvider initialized (sidecar at {self.sidecar_url})[/green]")
                    return True
                else:
                    console.print(f"[red]Sidecar health check failed: HTTP {response.status_code}[/red]")
                    return False
        except httpx.RequestError as e:
            console.print(f"[red]Failed to connect to sidecar at {self.sidecar_url}: {e}[/red]")
            return False
    
    def _get_authorization_header(self, api_name: str) -> Optional[str]:
        """Call sidecar to get authorization header for a downstream API.
        
        Args:
            api_name: Name of the downstream API in sidecar config
            
        Returns:
            Access token string (without "Bearer " prefix) if successful, None otherwise
        """
        if not self._initialized or not self._user_token:
            console.print("[red]SidecarTokenProvider not initialized[/red]")
            return None
        
        # Build URL with query parameters
        url = f"{self.sidecar_url}/AuthorizationHeader/{api_name}"
        params = {
            "optionsOverride.RequestAppToken": "false",  # Explicitly request OBO flow
        }
        
        # Add agent identity if configured
        if self.agent_identity_app_id:
            params["AgentIdentity"] = self.agent_identity_app_id
        
        headers = {
            "Authorization": f"Bearer {self._user_token}",
        }
        
        try:
            console.print(f"[dim]Calling sidecar: GET /AuthorizationHeader/{api_name}[/dim]")
            
            with httpx.Client(timeout=30) as client:
                response = client.get(url, params=params, headers=headers)
                
                if response.status_code == 200:
                    # Response is JSON: {"authorizationHeader": "Bearer <token>"}
                    try:
                        data = response.json()
                        auth_header = data.get("authorizationHeader", "")
                    except Exception:
                        # Fallback: treat as plain text if not JSON
                        auth_header = response.text.strip()
                    
                    # Strip "Bearer " prefix if present
                    if auth_header.lower().startswith("bearer "):
                        token = auth_header[7:]  # Remove "Bearer " prefix
                    else:
                        token = auth_header
                    
                    console.print(f"[green]✓ Got token from sidecar for {api_name}[/green]")
                    return token
                else:
                    error_text = response.text[:200] if response.text else "No error details"
                    console.print(f"[red]Sidecar request failed: HTTP {response.status_code}[/red]")
                    console.print(f"[red]Error: {error_text}[/red]")
                    return None
                    
        except httpx.RequestError as e:
            console.print(f"[red]Failed to call sidecar: {e}[/red]")
            return None
    
    def get_openai_token(self) -> Optional[str]:
        """Get OBO token for Azure OpenAI via sidecar.
        
        Returns:
            Access token string if successful, None otherwise
        """
        if self._openai_token:
            return self._openai_token
        
        self._openai_token = self._get_authorization_header(self.openai_api_name)
        return self._openai_token
    
    def get_mcp_token(self) -> Optional[str]:
        """Get OBO token for MCP server via sidecar.
        
        Returns:
            Access token string if successful, None otherwise
        """
        if self._mcp_token:
            return self._mcp_token
        
        self._mcp_token = self._get_authorization_header(self.mcp_api_name)
        return self._mcp_token
    
    def clear_cache(self) -> None:
        """Clear cached tokens."""
        self._openai_token = None
        self._mcp_token = None


def create_token_provider(
    mode: str,
    # Direct mode parameters
    tenant_id: Optional[str] = None,
    blueprint_app_id: Optional[str] = None,
    blueprint_client_secret: Optional[str] = None,
    agent_identity_app_id: Optional[str] = None,
    mcp_server_app_id: Optional[str] = None,
    # Sidecar mode parameters
    sidecar_url: str = "http://localhost:5000",
    sidecar_openai_api_name: str = "openai",
    sidecar_mcp_api_name: str = "mcp",
) -> TokenProvider:
    """Factory function to create the appropriate token provider.
    
    Args:
        mode: "direct" or "sidecar"
        tenant_id: Azure AD tenant ID (direct mode)
        blueprint_app_id: Blueprint application ID (direct mode)
        blueprint_client_secret: Blueprint client secret (direct mode)
        agent_identity_app_id: Agent identity application ID (both modes)
        mcp_server_app_id: MCP server application ID (direct mode)
        sidecar_url: Sidecar URL (sidecar mode)
        sidecar_openai_api_name: OpenAI API name in sidecar config (sidecar mode)
        sidecar_mcp_api_name: MCP API name in sidecar config (sidecar mode)
        
    Returns:
        Configured TokenProvider instance
        
    Raises:
        ValueError: If mode is invalid or required parameters are missing
    """
    if mode == "direct":
        if not all([tenant_id, blueprint_app_id, blueprint_client_secret, agent_identity_app_id]):
            raise ValueError(
                "Direct mode requires: tenant_id, blueprint_app_id, "
                "blueprint_client_secret, agent_identity_app_id"
            )
        
        console.print("[bold blue]Using DirectTokenProvider (direct OBO exchange)[/bold blue]")
        return DirectTokenProvider(
            tenant_id=tenant_id,
            blueprint_app_id=blueprint_app_id,
            blueprint_client_secret=blueprint_client_secret,
            agent_identity_app_id=agent_identity_app_id,
            mcp_server_app_id=mcp_server_app_id,
        )
    
    elif mode == "sidecar":
        console.print("[bold blue]Using SidecarTokenProvider (delegating to sidecar)[/bold blue]")
        return SidecarTokenProvider(
            sidecar_url=sidecar_url,
            openai_api_name=sidecar_openai_api_name,
            mcp_api_name=sidecar_mcp_api_name,
            agent_identity_app_id=agent_identity_app_id,
        )
    
    else:
        raise ValueError(f"Invalid token provider mode: {mode}. Must be 'direct' or 'sidecar'")

