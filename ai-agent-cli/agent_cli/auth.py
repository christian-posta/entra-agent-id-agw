"""Authentication helpers for the AI Agent CLI."""

import atexit
import json
from pathlib import Path
from typing import Optional

import httpx
from msal import PublicClientApplication, SerializableTokenCache
from rich.console import Console

from .models import TokenResult


console = Console()

# Microsoft Graph PowerShell client ID (well-known public client)
# This is the same client used by Connect-MgGraph
GRAPH_POWERSHELL_CLIENT_ID = "14d82eec-204b-4c2f-b7e8-296a70dab67e"

# Token cache file location
TOKEN_CACHE_PATH = Path.home() / ".ai-agent-cli-tokens.json"

# Azure OpenAI / Cognitive Services scope
AZURE_COGNITIVE_SERVICES_SCOPE = "https://cognitiveservices.azure.com/.default"


class TokenCache:
    """Persistent token cache for MSAL."""
    
    _instance: Optional["TokenCache"] = None
    _cache: Optional[SerializableTokenCache] = None
    
    @classmethod
    def get_instance(cls) -> "TokenCache":
        """Get singleton instance."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        """Initialize token cache."""
        self._cache = SerializableTokenCache()
        self._load()
        # Register save on exit
        atexit.register(self._save)
    
    def _load(self) -> None:
        """Load cache from disk."""
        if TOKEN_CACHE_PATH.exists():
            try:
                with open(TOKEN_CACHE_PATH, "r") as f:
                    self._cache.deserialize(f.read())
            except (json.JSONDecodeError, IOError) as e:
                console.print(f"[dim]Warning: Could not load token cache: {e}[/dim]")
    
    def _save(self) -> None:
        """Save cache to disk if modified."""
        if self._cache.has_state_changed:
            try:
                TOKEN_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
                with open(TOKEN_CACHE_PATH, "w") as f:
                    f.write(self._cache.serialize())
            except IOError as e:
                console.print(f"[dim]Warning: Could not save token cache: {e}[/dim]")
    
    @property
    def cache(self) -> SerializableTokenCache:
        """Get the underlying MSAL cache."""
        return self._cache
    
    def clear(self) -> None:
        """Clear the token cache."""
        # Create a new empty cache
        self._cache = SerializableTokenCache()
        # Delete the cache file
        if TOKEN_CACHE_PATH.exists():
            try:
                TOKEN_CACHE_PATH.unlink()
                console.print("[green]✓ Token cache cleared[/green]")
            except IOError as e:
                console.print(f"[red]Failed to delete token cache: {e}[/red]")


def get_msal_app(
    tenant_id: str,
    client_id: str = GRAPH_POWERSHELL_CLIENT_ID,
) -> PublicClientApplication:
    """Get MSAL PublicClientApplication with persistent token cache.
    
    Args:
        tenant_id: Azure AD tenant ID
        client_id: Client ID to use
        
    Returns:
        Configured PublicClientApplication
    """
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    token_cache = TokenCache.get_instance()
    
    return PublicClientApplication(
        client_id=client_id,
        authority=authority,
        token_cache=token_cache.cache,
    )


def get_device_code_token(
    tenant_id: str,
    scopes: list[str],
    client_id: str = GRAPH_POWERSHELL_CLIENT_ID,
    force_refresh: bool = False,
) -> Optional[TokenResult]:
    """Acquire a token using device code flow with caching.
    
    First attempts to get a cached token silently. If that fails,
    falls back to device code flow.
    
    Args:
        tenant_id: Azure AD tenant ID
        scopes: Scopes to request
        client_id: Client ID to use (defaults to Graph PowerShell client)
        force_refresh: If True, skip cache and force new authentication
        
    Returns:
        TokenResult if successful, None otherwise
    """
    app = get_msal_app(tenant_id, client_id)
    
    # Try to get token silently from cache first
    if not force_refresh:
        accounts = app.get_accounts()
        if accounts:
            console.print(f"[dim]Found {len(accounts)} cached account(s), attempting silent token acquisition...[/dim]")
            
            for account in accounts:
                result = app.acquire_token_silent(scopes=scopes, account=account)
                if result and "access_token" in result:
                    console.print(f"[green]✓ Using cached token for {account.get('username', 'unknown')}[/green]")
                    return TokenResult(
                        access_token=result["access_token"],
                        token_type=result.get("token_type", "Bearer"),
                        expires_in=result.get("expires_in", 0),
                    )
            
            console.print("[dim]Cached tokens expired or insufficient scopes, requesting new token...[/dim]")
    
    # Fall back to device code flow
    flow = app.initiate_device_flow(scopes=scopes)
    
    if "user_code" not in flow:
        console.print(f"[red]Failed to create device flow: {flow.get('error_description', 'Unknown error')}[/red]")
        return None
    
    # Display device code instructions
    console.print(f"\n[bold yellow]{flow['message']}[/bold yellow]\n")
    
    # Wait for user to complete authentication
    result = app.acquire_token_by_device_flow(flow)
    
    if "access_token" in result:
        # Cache is automatically updated by MSAL
        console.print("[green]✓ Authentication successful, token cached for future use[/green]")
        return TokenResult(
            access_token=result["access_token"],
            token_type=result.get("token_type", "Bearer"),
            expires_in=result.get("expires_in", 0),
        )
    else:
        error = result.get("error_description", result.get("error", "Unknown error"))
        console.print(f"[red]Authentication failed: {error}[/red]")
        return None


def clear_token_cache() -> None:
    """Clear the persistent token cache (logout)."""
    token_cache = TokenCache.get_instance()
    token_cache.clear()


def get_cached_accounts(tenant_id: str) -> list[dict]:
    """Get list of cached accounts.
    
    Args:
        tenant_id: Azure AD tenant ID
        
    Returns:
        List of account dictionaries
    """
    app = get_msal_app(tenant_id)
    return app.get_accounts()


def get_current_username(tenant_id: str) -> Optional[str]:
    """Get the username of the currently cached account.
    
    Args:
        tenant_id: Azure AD tenant ID
        
    Returns:
        Username if available, None otherwise
    """
    accounts = get_cached_accounts(tenant_id)
    if accounts:
        return accounts[0].get("username")
    return None


# =============================================================================
# OBO (On-Behalf-Of) Flow Functions
# =============================================================================


def get_user_token_for_blueprint(
    tenant_id: str,
    blueprint_app_id: str,
    force_refresh: bool = False,
) -> Optional[TokenResult]:
    """Get a user token with the Blueprint as the audience (Tc).
    
    This is the Tc token used in OBO flows. Uses device code flow
    with scope api://{blueprint_app_id}/access_as_user.
    
    Args:
        tenant_id: Azure AD tenant ID
        blueprint_app_id: Blueprint application ID (used as audience)
        force_refresh: If True, skip cache and force new authentication
        
    Returns:
        TokenResult (Tc) if successful, None otherwise
    """
    # The scope must target the Blueprint's exposed API
    scopes = [f"api://{blueprint_app_id}/access_as_user"]
    
    console.print(f"[dim]Requesting user token with Blueprint audience: api://{blueprint_app_id}[/dim]")
    
    return get_device_code_token(
        tenant_id=tenant_id,
        scopes=scopes,
        force_refresh=force_refresh,
    )


def get_blueprint_token_with_fmi_path(
    tenant_id: str,
    blueprint_app_id: str,
    client_secret: str,
    agent_identity_app_id: str,
) -> Optional[TokenResult]:
    """Get T1 token: Blueprint token with fmi_path pointing to agent identity.
    
    This is the first step in the OBO token exchange to get an agent identity token.
    
    Args:
        tenant_id: Azure AD tenant ID
        blueprint_app_id: Blueprint application ID
        client_secret: Blueprint client secret
        agent_identity_app_id: Agent identity application ID (used as fmi_path)
        
    Returns:
        TokenResult (T1) if successful, None otherwise
    """
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    
    data = {
        "client_id": blueprint_app_id,
        "scope": "api://AzureADTokenExchange/.default",
        "grant_type": "client_credentials",
        "client_secret": client_secret,
        "fmi_path": agent_identity_app_id,
    }
    
    with httpx.Client() as client:
        response = client.post(
            token_url,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        
        if response.status_code == 200:
            result = response.json()
            return TokenResult(
                access_token=result["access_token"],
                token_type=result.get("token_type", "Bearer"),
                expires_in=result.get("expires_in", 0),
            )
        else:
            error = response.json()
            console.print(f"[red]T1 token request failed: {error.get('error_description', error.get('error', 'Unknown error'))}[/red]")
            return None


def perform_obo_exchange(
    tenant_id: str,
    agent_identity_app_id: str,
    t1_token: str,
    user_token: str,
    scope: str,
) -> Optional[TokenResult]:
    """Perform OBO exchange to get resource token (T2) for agent acting on behalf of user.
    
    This exchanges:
    - T1 (blueprint impersonation token) as client_assertion
    - Tc (user token) as assertion
    
    For a resource token where the agent identity acts on behalf of the user.
    
    Args:
        tenant_id: Azure AD tenant ID
        agent_identity_app_id: Agent identity application ID
        t1_token: Blueprint impersonation token (T1)
        user_token: User token with Blueprint audience (Tc)
        scope: Target resource scope (e.g., https://cognitiveservices.azure.com/.default)
        
    Returns:
        TokenResult (T2 - OBO token) if successful, None otherwise
    """
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    
    data = {
        "client_id": agent_identity_app_id,
        "scope": scope,
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": t1_token,
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": user_token,
        "requested_token_use": "on_behalf_of",
    }
    
    with httpx.Client() as client:
        response = client.post(
            token_url,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        
        if response.status_code == 200:
            result = response.json()
            return TokenResult(
                access_token=result["access_token"],
                token_type=result.get("token_type", "Bearer"),
                expires_in=result.get("expires_in", 0),
            )
        else:
            error = response.json()
            console.print(f"[red]OBO exchange failed: {error.get('error_description', error.get('error', 'Unknown error'))}[/red]")
            return None


def get_obo_token(
    tenant_id: str,
    blueprint_app_id: str,
    client_secret: str,
    agent_identity_app_id: str,
    user_token: str,
    scope: str,
) -> tuple[Optional[TokenResult], Optional[TokenResult]]:
    """Get an OBO token for an agent identity acting on behalf of a user.
    
    This performs the Agent Identity OBO flow:
    1. Get T1: Blueprint token with fmi_path pointing to agent identity
    2. Get T2: OBO exchange using T1 (as client_assertion) and Tc (user token as assertion)
    
    Args:
        tenant_id: Azure AD tenant ID
        blueprint_app_id: Blueprint application ID
        client_secret: Blueprint client secret
        agent_identity_app_id: Agent identity application ID
        user_token: User token with Blueprint audience (Tc)
        scope: Target resource scope for the OBO token
        
    Returns:
        Tuple of (t1_token, t2_obo_token)
    """
    # Step 1: Get T1 token (blueprint impersonation token)
    console.print("[bold blue]Step 1: Getting T1 (blueprint impersonation token with fmi_path)...[/bold blue]")
    t1_token = get_blueprint_token_with_fmi_path(
        tenant_id=tenant_id,
        blueprint_app_id=blueprint_app_id,
        client_secret=client_secret,
        agent_identity_app_id=agent_identity_app_id,
    )
    
    if not t1_token:
        return None, None
    
    console.print("[green]✓ Got T1 token[/green]")
    
    # Step 2: OBO exchange for T2
    console.print(f"[bold blue]Step 2: Performing OBO exchange for T2 (scope: {scope})...[/bold blue]")
    t2_token = perform_obo_exchange(
        tenant_id=tenant_id,
        agent_identity_app_id=agent_identity_app_id,
        t1_token=t1_token.access_token,
        user_token=user_token,
        scope=scope,
    )
    
    if t2_token:
        console.print("[green]✓ Got T2 (OBO) token[/green]")
    
    return t1_token, t2_token


class OBOTokenManager:
    """Manages OBO tokens for multiple resource scopes."""
    
    def __init__(
        self,
        tenant_id: str,
        blueprint_app_id: str,
        blueprint_client_secret: str,
        agent_identity_app_id: str,
        user_token: str,
    ):
        """Initialize OBO token manager.
        
        Args:
            tenant_id: Azure AD tenant ID
            blueprint_app_id: Blueprint application ID
            blueprint_client_secret: Blueprint client secret
            agent_identity_app_id: Agent identity application ID
            user_token: User token (Tc) with Blueprint audience
        """
        self.tenant_id = tenant_id
        self.blueprint_app_id = blueprint_app_id
        self.blueprint_client_secret = blueprint_client_secret
        self.agent_identity_app_id = agent_identity_app_id
        self.user_token = user_token
        
        # Cache T1 token (reusable for different scopes)
        self._t1_token: Optional[TokenResult] = None
        
        # Cache T2 tokens by scope
        self._t2_tokens: dict[str, TokenResult] = {}
    
    def _get_t1_token(self) -> Optional[TokenResult]:
        """Get or cache T1 token."""
        if self._t1_token is None:
            console.print("[dim]Getting T1 token (blueprint impersonation)...[/dim]")
            self._t1_token = get_blueprint_token_with_fmi_path(
                tenant_id=self.tenant_id,
                blueprint_app_id=self.blueprint_app_id,
                client_secret=self.blueprint_client_secret,
                agent_identity_app_id=self.agent_identity_app_id,
            )
            if self._t1_token:
                console.print("[green]✓ T1 token acquired[/green]")
        return self._t1_token
    
    def get_token_for_scope(self, scope: str) -> Optional[TokenResult]:
        """Get an OBO token for the specified scope.
        
        Caches tokens to avoid repeated OBO exchanges for the same scope.
        
        Args:
            scope: Target resource scope (e.g., https://cognitiveservices.azure.com/.default)
            
        Returns:
            TokenResult (T2) for the scope, or None if exchange fails
        """
        # Check cache first
        if scope in self._t2_tokens:
            # TODO: Check expiration and refresh if needed
            return self._t2_tokens[scope]
        
        # Get T1 if not already cached
        t1_token = self._get_t1_token()
        if not t1_token:
            console.print("[red]Failed to get T1 token[/red]")
            return None
        
        # Perform OBO exchange
        console.print(f"[dim]Getting OBO token for scope: {scope}[/dim]")
        t2_token = perform_obo_exchange(
            tenant_id=self.tenant_id,
            agent_identity_app_id=self.agent_identity_app_id,
            t1_token=t1_token.access_token,
            user_token=self.user_token,
            scope=scope,
        )
        
        if t2_token:
            self._t2_tokens[scope] = t2_token
            console.print(f"[green]✓ OBO token acquired for {scope}[/green]")
        
        return t2_token
    
    def get_azure_openai_token(self) -> Optional[TokenResult]:
        """Get OBO token for Azure OpenAI / Cognitive Services.
        
        Returns:
            TokenResult for Azure Cognitive Services scope
        """
        return self.get_token_for_scope(AZURE_COGNITIVE_SERVICES_SCOPE)
    
    def get_mcp_gateway_token(self, gateway_scope: str) -> Optional[TokenResult]:
        """Get OBO token for MCP Gateway.
        
        Args:
            gateway_scope: The gateway's scope (e.g., api://{gateway-app-id}/.default)
            
        Returns:
            TokenResult for the gateway scope
        """
        return self.get_token_for_scope(gateway_scope)
    
    def clear_cache(self) -> None:
        """Clear all cached tokens."""
        self._t1_token = None
        self._t2_tokens.clear()
