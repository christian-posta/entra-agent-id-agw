"""Authentication helpers for the Agent Identity CLI."""

import httpx
from msal import PublicClientApplication
from rich.console import Console
from typing import Optional

from .models import TokenResult


console = Console()

# Microsoft Graph PowerShell client ID (well-known public client)
# This is the same client used by Connect-MgGraph
GRAPH_POWERSHELL_CLIENT_ID = "14d82eec-204b-4c2f-b7e8-296a70dab67e"

# Required scopes for blueprint operations
BLUEPRINT_SCOPES = [
    "AgentIdentityBlueprint.AddRemoveCreds.All",
    "AgentIdentityBlueprint.Create",
    "DelegatedPermissionGrant.ReadWrite.All",
    "Application.Read.All",
    "AgentIdentityBlueprintPrincipal.Create",
    "User.Read",
]


def get_device_code_token(
    tenant_id: str,
    scopes: Optional[list[str]] = None,
    client_id: str = GRAPH_POWERSHELL_CLIENT_ID,
) -> Optional[TokenResult]:
    """Acquire a token using device code flow.
    
    Args:
        tenant_id: Azure AD tenant ID
        scopes: Scopes to request (defaults to BLUEPRINT_SCOPES)
        client_id: Client ID to use (defaults to Graph PowerShell client)
        
    Returns:
        TokenResult if successful, None otherwise
    """
    if scopes is None:
        scopes = BLUEPRINT_SCOPES
    
    # Create public client application
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    app = PublicClientApplication(
        client_id=client_id,
        authority=authority,
    )
    
    # Initiate device code flow
    flow = app.initiate_device_flow(scopes=scopes)
    
    if "user_code" not in flow:
        console.print(f"[red]Failed to create device flow: {flow.get('error_description', 'Unknown error')}[/red]")
        return None
    
    # Display device code instructions
    console.print(f"\n[bold yellow]{flow['message']}[/bold yellow]\n")
    
    # Wait for user to complete authentication
    result = app.acquire_token_by_device_flow(flow)
    
    if "access_token" in result:
        return TokenResult(
            access_token=result["access_token"],
            token_type=result.get("token_type", "Bearer"),
            expires_in=result.get("expires_in", 0),
        )
    else:
        error = result.get("error_description", result.get("error", "Unknown error"))
        console.print(f"[red]Authentication failed: {error}[/red]")
        return None


def get_client_credentials_token(
    tenant_id: str,
    client_id: str,
    client_secret: str,
    scope: str = "https://graph.microsoft.com/.default",
) -> Optional[TokenResult]:
    """Acquire a token using client credentials flow.
    
    Args:
        tenant_id: Azure AD tenant ID
        client_id: Application (client) ID
        client_secret: Client secret
        scope: Scope to request
        
    Returns:
        TokenResult if successful, None otherwise
    """
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    
    data = {
        "client_id": client_id,
        "scope": scope,
        "grant_type": "client_credentials",
        "client_secret": client_secret,
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
            console.print(f"[red]Token request failed: {error.get('error_description', error.get('error', 'Unknown error'))}[/red]")
            return None


def get_blueprint_token_with_fmi_path(
    tenant_id: str,
    blueprint_app_id: str,
    client_secret: str,
    agent_identity_app_id: str,
) -> Optional[TokenResult]:
    """Get T1 token: Blueprint token with fmi_path pointing to agent identity.
    
    This is the first step in the token exchange to get an agent identity token.
    
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


def exchange_token_for_agent_identity(
    tenant_id: str,
    agent_identity_app_id: str,
    t1_token: str,
    scope: str = "https://graph.microsoft.com/.default",
) -> Optional[TokenResult]:
    """Exchange T1 for T2: Get the final agent identity token.
    
    Args:
        tenant_id: Azure AD tenant ID
        agent_identity_app_id: Agent identity application ID
        t1_token: The T1 token (blueprint token with fmi_path)
        scope: Scope to request for the agent identity token
        
    Returns:
        TokenResult (T2) if successful, None otherwise
    """
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    
    data = {
        "client_id": agent_identity_app_id,
        "scope": scope,
        "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": t1_token,
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
            console.print(f"[red]T2 token request failed: {error.get('error_description', error.get('error', 'Unknown error'))}[/red]")
            return None


def get_agent_identity_token(
    tenant_id: str,
    blueprint_app_id: str,
    client_secret: str,
    agent_identity_app_id: str,
    scope: str = "https://graph.microsoft.com/.default",
    show_intermediate: bool = True,
) -> tuple[Optional[TokenResult], Optional[TokenResult], Optional[TokenResult]]:
    """Get an access token for an agent identity using the two-step exchange.
    
    This performs the full token exchange:
    1. Get blueprint token (for reference)
    2. Get T1: Blueprint token with fmi_path
    3. Get T2: Exchange T1 for agent identity token
    
    Args:
        tenant_id: Azure AD tenant ID
        blueprint_app_id: Blueprint application ID
        client_secret: Blueprint client secret
        agent_identity_app_id: Agent identity application ID
        scope: Scope for the final token
        show_intermediate: Whether to display intermediate tokens
        
    Returns:
        Tuple of (blueprint_token, t1_token, t2_token)
    """
    # Step 0: Get blueprint token (optional, for display)
    blueprint_token = None
    if show_intermediate:
        console.print("[bold blue]Step 0: Getting blueprint access token...[/bold blue]")
        blueprint_token = get_client_credentials_token(
            tenant_id=tenant_id,
            client_id=blueprint_app_id,
            client_secret=client_secret,
            scope="https://graph.microsoft.com/.default",
        )
        if blueprint_token:
            console.print("[green]✓ Got blueprint access token[/green]")
    
    # Step 1: Get T1 token
    console.print("[bold blue]Step 1: Getting T1 (blueprint token with fmi_path)...[/bold blue]")
    t1_token = get_blueprint_token_with_fmi_path(
        tenant_id=tenant_id,
        blueprint_app_id=blueprint_app_id,
        client_secret=client_secret,
        agent_identity_app_id=agent_identity_app_id,
    )
    
    if not t1_token:
        return blueprint_token, None, None
    
    console.print("[green]✓ Got T1 token[/green]")
    
    # Step 2: Exchange T1 for T2
    console.print("[bold blue]Step 2: Exchanging T1 for T2 (agent identity token)...[/bold blue]")
    t2_token = exchange_token_for_agent_identity(
        tenant_id=tenant_id,
        agent_identity_app_id=agent_identity_app_id,
        t1_token=t1_token.access_token,
        scope=scope,
    )
    
    if t2_token:
        console.print("[green]✓ Got T2 (agent identity) token[/green]")
    
    return blueprint_token, t1_token, t2_token

