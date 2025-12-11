"""Authentication helpers for the AI Agent CLI."""

import atexit
import json
from pathlib import Path
from typing import Optional

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
AZURE_OPENAI_SCOPES = [
    "https://cognitiveservices.azure.com/.default",
]


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
    scopes: Optional[list[str]] = None,
    client_id: str = GRAPH_POWERSHELL_CLIENT_ID,
    force_refresh: bool = False,
) -> Optional[TokenResult]:
    """Acquire a token using device code flow with caching.
    
    First attempts to get a cached token silently. If that fails,
    falls back to device code flow.
    
    Args:
        tenant_id: Azure AD tenant ID
        scopes: Scopes to request (defaults to AZURE_OPENAI_SCOPES)
        client_id: Client ID to use (defaults to Graph PowerShell client)
        force_refresh: If True, skip cache and force new authentication
        
    Returns:
        TokenResult if successful, None otherwise
    """
    if scopes is None:
        scopes = AZURE_OPENAI_SCOPES
    
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

