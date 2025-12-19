"""Agent Identity Blueprint CLI - Main entry point."""

import json
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax

from .auth import (
    get_device_code_token,
    get_client_credentials_token,
    get_agent_identity_token,
    get_user_token_for_blueprint,
    get_obo_token,
    clear_token_cache,
    get_cached_accounts,
    READ_ONLY_SCOPES,
    TOKEN_CACHE_PATH,
)
from .config import get_config
from .graph_client import (
    GraphClient,
    create_full_blueprint,
    create_agent_identity_from_blueprint,
    grant_agent_admin_consent,
    create_mcp_server_app,
    grant_agent_permission_to_mcp,
    MICROSOFT_GRAPH_APP_ID,
    DEFAULT_OBO_SCOPES,
)


app = typer.Typer(
    name="agent-cli",
    help="CLI tool for managing Microsoft Entra Agent Identity Blueprints",
    no_args_is_help=True,
)
console = Console()


def require_tenant_id(tenant_id: Optional[str]) -> str:
    """Ensure tenant ID is available."""
    config = get_config()
    tid = tenant_id or config.tenant_id
    
    if not tid:
        console.print("[red]Error: Tenant ID is required.[/red]")
        console.print("Set TENANT_ID in .env file or pass --tenant-id")
        raise typer.Exit(1)
    
    return tid


def display_token_claims(token_name: str, claims: dict) -> None:
    """Display token claims in a formatted panel."""
    claims_json = json.dumps(claims, indent=2)
    syntax = Syntax(claims_json, "json", theme="monokai", line_numbers=False)
    console.print(Panel(syntax, title=f"[bold]{token_name} Claims[/bold]", border_style="blue"))


@app.command("list-blueprints")
def list_blueprints(
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    from_graph: bool = typer.Option(False, "--from-graph", "-g", help="Fetch from Graph API (requires auth)"),
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication (ignore cached token)"),
) -> None:
    """List all Agent Identity Blueprints.
    
    By default, lists blueprints stored in local config.
    Use --from-graph to fetch from Microsoft Graph API.
    """
    config = get_config()
    
    if from_graph:
        # Fetch from Graph API
        tid = require_tenant_id(tenant_id)
        console.print("[bold blue]Authenticating to fetch blueprints from Graph API...[/bold blue]")
        
        token = get_device_code_token(tid, scopes=READ_ONLY_SCOPES, force_refresh=force_refresh)
        if not token:
            raise typer.Exit(1)
        
        client = GraphClient(token.access_token)
        
        # Fetch both applications and principals
        console.print("[bold blue]Fetching blueprint applications...[/bold blue]")
        blueprints = client.list_blueprints()
        
        console.print("[bold blue]Fetching blueprint principals...[/bold blue]")
        principals = client.list_blueprint_principals()
        
        # Create a map of app_id to principal
        principal_map = {p.get("appId"): p for p in principals}
        
        if not blueprints:
            console.print("[yellow]No blueprints found in tenant.[/yellow]")
            return
        
        table = Table(title="Agent Identity Blueprints (from Graph API)")
        table.add_column("Display Name", style="cyan")
        table.add_column("App ID", style="green")
        table.add_column("Object ID", style="dim")
        table.add_column("Has Principal", style="yellow")
        
        for bp in blueprints:
            has_principal = "✓" if bp.get("appId") in principal_map else "✗"
            table.add_row(
                bp.get("displayName", "N/A"),
                bp.get("appId", "N/A"),
                bp.get("id", "N/A"),
                has_principal,
            )
        
        console.print(table)
    else:
        # List from local config
        stored_blueprints = config.list_blueprints()
        
        if not stored_blueprints:
            console.print("[yellow]No blueprints stored locally.[/yellow]")
            console.print("Use 'create-new-blueprint' to create one, or '--from-graph' to list from Azure.")
            return
        
        table = Table(title="Stored Blueprints (local config)")
        table.add_column("Name", style="cyan")
        table.add_column("App ID", style="green")
        table.add_column("Has Secret", style="yellow")
        
        for name, bp in stored_blueprints.items():
            has_secret = "✓" if bp.client_secret else "✗"
            table.add_row(name, bp.app_id, has_secret)
        
        console.print(table)


@app.command("create-new-blueprint")
def create_new_blueprint(
    name: str = typer.Argument(..., help="Display name for the blueprint"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    save: bool = typer.Option(True, "--save/--no-save", help="Save blueprint to local config"),
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication (ignore cached token)"),
) -> None:
    """Create a new Agent Identity Blueprint.
    
    This will:
    1. Authenticate using device code flow (or use cached token)
    2. Create the blueprint application
    3. Create the blueprint service principal
    4. Generate a client secret
    5. Optionally save to local config
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Check if blueprint already exists locally
    if config.get_blueprint(name):
        console.print(f"[yellow]Warning: Blueprint '{name}' already exists in local config.[/yellow]")
        if not typer.confirm("Overwrite?"):
            raise typer.Exit(0)
    
    console.print(f"\n[bold]Creating Agent Identity Blueprint: {name}[/bold]\n")
    
    # Authenticate
    console.print("[bold blue]Step 1: Authenticate with device code flow[/bold blue]")
    token = get_device_code_token(tid, force_refresh=force_refresh)
    if not token:
        raise typer.Exit(1)
    
    console.print("[green]✓ Authentication successful[/green]\n")
    
    # Create blueprint
    console.print("[bold blue]Step 2: Create blueprint and resources[/bold blue]")
    blueprint = create_full_blueprint(token.access_token, name)
    if not blueprint:
        console.print("[red]Failed to create blueprint.[/red]")
        raise typer.Exit(1)
    
    # Save to config
    if save:
        config.save_blueprint(name, blueprint)
        # Also save tenant ID if not already set
        if not config.tenant_id:
            config.tenant_id = tid
        console.print(f"\n[green]✓ Blueprint saved to config[/green]")
    
    console.print(f"\n[bold green]Blueprint '{name}' created successfully![/bold green]")
    console.print(f"\nApp ID: {blueprint.app_id}")
    console.print(f"Object ID: {blueprint.object_id}")
    console.print(f"Principal ID: {blueprint.principal_id}")
    console.print(f"\n[yellow]Client Secret: {blueprint.client_secret}[/yellow]")
    console.print("[dim](This secret is saved in your local config file)[/dim]")


@app.command("list-agent-identities")
def list_agent_identities(
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    from_graph: bool = typer.Option(False, "--from-graph", "-g", help="Fetch from Graph API (requires auth)"),
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication (ignore cached token)"),
) -> None:
    """List all Agent Identities.
    
    By default, lists agent identities stored in local config.
    Use --from-graph to fetch from Microsoft Graph API.
    """
    config = get_config()
    
    if from_graph:
        tid = require_tenant_id(tenant_id)
        console.print("[bold blue]Authenticating to fetch agent identities from Graph API...[/bold blue]")
        
        token = get_device_code_token(tid, scopes=READ_ONLY_SCOPES, force_refresh=force_refresh)
        if not token:
            raise typer.Exit(1)
        
        client = GraphClient(token.access_token)
        
        console.print("[bold blue]Fetching agent identities...[/bold blue]")
        agents = client.list_agent_identities()
        
        if not agents:
            console.print("[yellow]No agent identities found in tenant.[/yellow]")
            return
        
        table = Table(title="Agent Identities (from Graph API)")
        table.add_column("Display Name", style="cyan")
        table.add_column("App ID", style="green")
        table.add_column("ID", style="dim")
        
        for agent in agents:
            table.add_row(
                agent.get("displayName", "N/A"),
                agent.get("appId", "N/A"),
                agent.get("id", "N/A"),
            )
        
        console.print(table)
    else:
        stored_agents = config.list_agent_identities()
        
        if not stored_agents:
            console.print("[yellow]No agent identities stored locally.[/yellow]")
            console.print("Use 'create-new-agent-identity-from-blueprint' to create one.")
            return
        
        table = Table(title="Stored Agent Identities (local config)")
        table.add_column("Name", style="cyan")
        table.add_column("App ID", style="green")
        table.add_column("Blueprint App ID", style="dim")
        
        for name, agent in stored_agents.items():
            table.add_row(name, agent.app_id, agent.blueprint_app_id or "N/A")
        
        console.print(table)


@app.command("create-new-agent-identity-from-blueprint")
def create_new_agent_identity(
    name: str = typer.Argument(..., help="Display name for the agent identity"),
    blueprint_name: str = typer.Option(..., "--blueprint", "-b", help="Name of the blueprint to use"),
    sponsor_user_id: str = typer.Option(..., "--sponsor", "-s", help="User ID of the sponsor"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    save: bool = typer.Option(True, "--save/--no-save", help="Save agent identity to local config"),
    enable_obo: bool = typer.Option(True, "--enable-obo/--no-enable-obo", help="Grant admin consent for OBO flows (Graph API)"),
    obo_scopes: str = typer.Option(DEFAULT_OBO_SCOPES, "--obo-scopes", help="Scopes to grant for OBO (space-separated)"),
) -> None:
    """Create a new Agent Identity from a stored blueprint.
    
    Requires a blueprint to be created and stored first.
    The sponsor user ID must be provided (e.g., from 'az ad signed-in-user show --query id').
    
    By default, grants admin consent for Microsoft Graph OBO flows.
    Use --no-enable-obo to skip this step.
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Get the blueprint
    blueprint = config.get_blueprint(blueprint_name)
    if not blueprint:
        console.print(f"[red]Blueprint '{blueprint_name}' not found in local config.[/red]")
        console.print("Use 'list-blueprints' to see available blueprints.")
        raise typer.Exit(1)
    
    console.print(f"\n[bold]Creating Agent Identity: {name}[/bold]")
    console.print(f"Using blueprint: {blueprint_name} ({blueprint.app_id})")
    if enable_obo:
        console.print(f"OBO enabled: Will grant consent for scopes: {obo_scopes}")
    console.print()
    
    # Get blueprint token
    console.print("[bold blue]Getting blueprint access token...[/bold blue]")
    token = get_client_credentials_token(
        tenant_id=tid,
        client_id=blueprint.app_id,
        client_secret=blueprint.client_secret,
    )
    if not token:
        raise typer.Exit(1)
    
    console.print("[green]✓ Got blueprint token[/green]\n")
    
    # Create agent identity
    agent = create_agent_identity_from_blueprint(
        blueprint_token=token.access_token,
        display_name=name,
        blueprint_app_id=blueprint.app_id,
        sponsor_user_id=sponsor_user_id,
    )
    
    if not agent:
        console.print("[red]Failed to create agent identity.[/red]")
        raise typer.Exit(1)
    
    # Save to config
    if save:
        config.save_agent_identity(agent)
        console.print(f"\n[green]✓ Agent identity saved to config[/green]")
    
    # Grant admin consent for OBO if enabled
    if enable_obo:
        import time
        console.print(f"\n[bold blue]Waiting for Azure AD propagation (5 seconds)...[/bold blue]")
        time.sleep(5)
        
        console.print(f"[bold blue]Granting admin consent for OBO...[/bold blue]")
        console.print("[dim]This requires user authentication with admin permissions[/dim]")
        
        # Get user token for granting consent
        user_token = get_device_code_token(tid, scopes=["DelegatedPermissionGrant.ReadWrite.All", "Application.Read.All"])
        if user_token:
            if grant_agent_admin_consent(
                access_token=user_token.access_token,
                agent_identity_app_id=agent.app_id,
                scopes=obo_scopes,
            ):
                console.print(f"[green]✓ Admin consent granted for OBO![/green]")
            else:
                console.print("[yellow]Warning: Failed to grant admin consent.[/yellow]")
                console.print("[yellow]You can manually grant consent using 'grant-admin-consent' command.[/yellow]")
        else:
            console.print("[yellow]Warning: Could not authenticate to grant consent.[/yellow]")
            console.print("[yellow]Use 'grant-admin-consent' command to grant consent later.[/yellow]")
    
    console.print(f"\n[bold green]Agent Identity '{name}' created successfully![/bold green]")
    console.print(f"\nID: {agent.id}")
    console.print(f"App ID: {agent.app_id}")


@app.command("get-access-token-for-agent-identity")
def get_access_token(
    agent_name: str = typer.Argument(..., help="Name of the agent identity"),
    blueprint_name: Optional[str] = typer.Option(None, "--blueprint", "-b", help="Blueprint name (auto-detected if saved)"),
    scope: str = typer.Option("https://graph.microsoft.com/.default", "--scope", "-s", help="Token scope"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    show_claims: bool = typer.Option(True, "--show-claims/--hide-claims", help="Display decoded token claims"),
    output_token: bool = typer.Option(False, "--output-token", "-o", help="Output the final token value"),
) -> None:
    """Get an access token for an Agent Identity.
    
    This performs the two-step token exchange:
    1. Get T1: Blueprint token with fmi_path pointing to agent identity
    2. Get T2: Exchange T1 for the agent identity token
    
    All intermediate tokens are displayed for debugging purposes.
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Get agent identity
    agent = config.get_agent_identity(agent_name)
    if not agent:
        console.print(f"[red]Agent identity '{agent_name}' not found in local config.[/red]")
        console.print("Use 'list-agent-identities' to see available agent identities.")
        raise typer.Exit(1)
    
    # Determine blueprint to use
    bp_name = blueprint_name
    if not bp_name and agent.blueprint_app_id:
        # Find blueprint by app_id
        for name, bp in config.list_blueprints().items():
            if bp.app_id == agent.blueprint_app_id:
                bp_name = name
                break
    
    if not bp_name:
        console.print("[red]Could not determine blueprint to use.[/red]")
        console.print("Specify --blueprint or ensure the agent identity has a stored blueprint_app_id.")
        raise typer.Exit(1)
    
    blueprint = config.get_blueprint(bp_name)
    if not blueprint:
        console.print(f"[red]Blueprint '{bp_name}' not found in local config.[/red]")
        raise typer.Exit(1)
    
    console.print(f"\n[bold]Getting Access Token for Agent Identity: {agent_name}[/bold]")
    console.print(f"Using blueprint: {bp_name}")
    console.print(f"Scope: {scope}\n")
    
    # Get all tokens
    blueprint_token, t1_token, t2_token = get_agent_identity_token(
        tenant_id=tid,
        blueprint_app_id=blueprint.app_id,
        client_secret=blueprint.client_secret,
        agent_identity_app_id=agent.app_id,
        scope=scope,
        show_intermediate=True,
    )
    
    # Display tokens
    if show_claims:
        console.print("\n")
        
        if blueprint_token:
            display_token_claims("Blueprint Token", blueprint_token.decoded_claims())
        
        if t1_token:
            display_token_claims("T1 Token (Blueprint with fmi_path)", t1_token.decoded_claims())
        
        if t2_token:
            display_token_claims("T2 Token (Agent Identity)", t2_token.decoded_claims())
    
    if t2_token:
        console.print(f"\n[bold green]✓ Successfully obtained agent identity token![/bold green]")
        console.print(f"Token expires in: {t2_token.expires_in} seconds")
        
        if output_token:
            console.print(f"\n[bold]Access Token:[/bold]")
            console.print(t2_token.access_token)
    else:
        console.print("\n[red]Failed to obtain agent identity token.[/red]")
        raise typer.Exit(1)


@app.command("get-obo-token-for-agent-identity")
def get_obo_access_token(
    agent_name: str = typer.Argument(..., help="Name of the agent identity"),
    blueprint_name: Optional[str] = typer.Option(None, "--blueprint", "-b", help="Blueprint name (auto-detected if saved)"),
    scope: str = typer.Option("https://graph.microsoft.com/.default", "--scope", "-s", help="Target resource scope"),
    user_token: Optional[str] = typer.Option(None, "--user-token", "-u", help="Existing user token (Tc) with Blueprint audience"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    show_claims: bool = typer.Option(True, "--show-claims/--hide-claims", help="Display decoded token claims"),
    output_token: bool = typer.Option(False, "--output-token", "-o", help="Output the final token value"),
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication for user token"),
) -> None:
    """Get an OBO (On-Behalf-Of) token for an Agent Identity acting on behalf of a user.
    
    This performs the Agent Identity OBO flow:
    1. Get Tc: User token with Blueprint as audience (device code or --user-token)
    2. Get T1: Blueprint impersonation token with fmi_path
    3. Get T2: OBO exchange for resource token (agent acting for user)
    
    Prerequisites:
    - Blueprint must expose an API with 'access_as_user' scope
    - Admin consent must be granted for the Agent Identity
    
    See OBO-GUIDE.md for setup instructions.
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Get agent identity
    agent = config.get_agent_identity(agent_name)
    if not agent:
        console.print(f"[red]Agent identity '{agent_name}' not found in local config.[/red]")
        console.print("Use 'list-agent-identities' to see available agent identities.")
        raise typer.Exit(1)
    
    # Determine blueprint to use
    bp_name = blueprint_name
    if not bp_name and agent.blueprint_app_id:
        # Find blueprint by app_id
        for name, bp in config.list_blueprints().items():
            if bp.app_id == agent.blueprint_app_id:
                bp_name = name
                break
    
    if not bp_name:
        console.print("[red]Could not determine blueprint to use.[/red]")
        console.print("Specify --blueprint or ensure the agent identity has a stored blueprint_app_id.")
        raise typer.Exit(1)
    
    blueprint = config.get_blueprint(bp_name)
    if not blueprint:
        console.print(f"[red]Blueprint '{bp_name}' not found in local config.[/red]")
        raise typer.Exit(1)
    
    console.print(f"\n[bold]Getting OBO Token for Agent Identity: {agent_name}[/bold]")
    console.print(f"Using blueprint: {bp_name}")
    console.print(f"Target scope: {scope}\n")
    
    # Step 0: Get user token (Tc)
    tc_token = None
    if user_token:
        console.print("[bold blue]Step 0: Using provided user token (Tc)...[/bold blue]")
        from .models import TokenResult
        tc_token = TokenResult(access_token=user_token)
        console.print("[green]✓ User token provided[/green]")
    else:
        console.print("[bold blue]Step 0: Getting user token (Tc) via device code flow...[/bold blue]")
        console.print(f"[dim]Requesting scope: api://{blueprint.app_id}/access_as_user[/dim]")
        tc_token = get_user_token_for_blueprint(
            tenant_id=tid,
            blueprint_app_id=blueprint.app_id,
            force_refresh=force_refresh,
        )
        if not tc_token:
            console.print("[red]Failed to get user token.[/red]")
            console.print("[yellow]Hint: Ensure the Blueprint has an exposed API with 'access_as_user' scope.[/yellow]")
            raise typer.Exit(1)
        console.print("[green]✓ Got user token (Tc)[/green]")
    
    # Get OBO token (T1 and T2)
    t1_token, t2_token = get_obo_token(
        tenant_id=tid,
        blueprint_app_id=blueprint.app_id,
        client_secret=blueprint.client_secret,
        agent_identity_app_id=agent.app_id,
        user_token=tc_token.access_token,
        scope=scope,
    )
    
    # Display tokens
    if show_claims:
        console.print("\n")
        
        if tc_token:
            display_token_claims("Tc Token (User token, aud=Blueprint)", tc_token.decoded_claims())
        
        if t1_token:
            display_token_claims("T1 Token (Blueprint impersonation with fmi_path)", t1_token.decoded_claims())
        
        if t2_token:
            display_token_claims("T2 Token (OBO - Agent acting on behalf of User)", t2_token.decoded_claims())
    
    if t2_token:
        console.print(f"\n[bold green]✓ Successfully obtained OBO token![/bold green]")
        console.print(f"Token expires in: {t2_token.expires_in} seconds")
        
        # Show who the agent is acting on behalf of
        claims = t2_token.decoded_claims()
        if claims.get("name") or claims.get("upn"):
            console.print(f"Acting on behalf of: {claims.get('name', 'N/A')} ({claims.get('upn', 'N/A')})")
        
        if output_token:
            console.print(f"\n[bold]Access Token:[/bold]")
            console.print(t2_token.access_token)
    else:
        console.print("\n[red]Failed to obtain OBO token.[/red]")
        console.print("[yellow]Hints:[/yellow]")
        console.print("  - Ensure admin consent is granted for the Agent Identity")
        console.print("  - Check that the Blueprint exposes the 'access_as_user' scope")
        console.print("  - See OBO-GUIDE.md for detailed setup instructions")
        raise typer.Exit(1)


@app.command("grant-admin-consent")
def grant_consent(
    agent_name: str = typer.Argument(..., help="Name of the agent identity"),
    scopes: str = typer.Option(DEFAULT_OBO_SCOPES, "--scopes", "-s", help="Scopes to grant (space-separated)"),
    resource: str = typer.Option(MICROSOFT_GRAPH_APP_ID, "--resource", "-r", help="Resource app ID (default: Microsoft Graph)"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
) -> None:
    """Grant admin consent for an Agent Identity to access resources via OBO.
    
    This is required for OBO flows since Agent Identities cannot prompt users
    for consent. By default, grants consent for Microsoft Graph.
    
    Common resources:
    - Microsoft Graph: 00000003-0000-0000-c000-000000000000
    
    Common scopes for Graph OBO:
    - User.Read openid profile offline_access
    - Mail.Read Calendars.Read (for email/calendar access)
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Get agent identity
    agent = config.get_agent_identity(agent_name)
    if not agent:
        console.print(f"[red]Agent identity '{agent_name}' not found in local config.[/red]")
        console.print("Use 'list-agent-identities' to see available agent identities.")
        raise typer.Exit(1)
    
    console.print(f"\n[bold]Granting Admin Consent for Agent Identity: {agent_name}[/bold]")
    console.print(f"Agent App ID: {agent.app_id}")
    console.print(f"Resource: {resource}")
    console.print(f"Scopes: {scopes}\n")
    
    # Get user token with required permissions
    console.print("[bold blue]Authenticating with admin permissions...[/bold blue]")
    user_token = get_device_code_token(
        tid, 
        scopes=["DelegatedPermissionGrant.ReadWrite.All", "Application.Read.All"]
    )
    if not user_token:
        console.print("[red]Failed to authenticate.[/red]")
        raise typer.Exit(1)
    
    # Grant consent
    if grant_agent_admin_consent(
        access_token=user_token.access_token,
        agent_identity_app_id=agent.app_id,
        resource_app_id=resource,
        scopes=scopes,
    ):
        console.print(f"\n[bold green]✓ Admin consent granted successfully![/bold green]")
        console.print(f"The agent '{agent_name}' can now perform OBO flows to access the resource.")
    else:
        console.print("\n[red]Failed to grant admin consent.[/red]")
        raise typer.Exit(1)


@app.command("create-mcp-server-app")
def create_mcp_server_app_cmd(
    name: str = typer.Argument(..., help="Display name for the MCP Server app"),
    agent_name: Optional[str] = typer.Option(None, "--agent-name", "-a", help="Agent Identity name to grant access"),
    graph_permissions: str = typer.Option("User.Read", "--graph-permissions", "-g", help="Microsoft Graph permissions (comma-separated)"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication"),
) -> None:
    """Create an MCP Server app registration for OBO flows.
    
    This creates an application that can:
    1. Receive OBO tokens from AI Agents (via AI Gateway)
    2. Perform OBO exchange to call Microsoft Graph on behalf of users
    
    The created app will have:
    - Exposed API with 'access_as_user' scope
    - Client secret for OBO to Microsoft Graph
    - Delegated permissions for specified Graph scopes
    
    If --agent-name is provided, also grants that Agent Identity
    permission to call the MCP Server API.
    
    Example:
        python -m agent_cli.main create-mcp-server-app "MCP Tool Server" \\
            --agent-name "Interactive Agent" \\
            --graph-permissions "User.Read,Mail.Read"
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Parse graph permissions
    permissions_list = [p.strip() for p in graph_permissions.split(",") if p.strip()]
    
    console.print(f"\n[bold]Creating MCP Server App: {name}[/bold]")
    console.print(f"Graph permissions: {', '.join(permissions_list)}")
    if agent_name:
        console.print(f"Will grant access to Agent: {agent_name}")
    console.print()
    
    # Authenticate
    console.print("[bold blue]Step 1: Authenticate with device code flow[/bold blue]")
    required_scopes = [
        "Application.ReadWrite.All",
        "DelegatedPermissionGrant.ReadWrite.All",
    ]
    token = get_device_code_token(tid, scopes=required_scopes, force_refresh=force_refresh)
    if not token:
        raise typer.Exit(1)
    
    console.print("[green]✓ Authentication successful[/green]\n")
    
    # Create the MCP server app
    console.print("[bold blue]Step 2: Create MCP Server app registration[/bold blue]")
    mcp_app = create_mcp_server_app(
        access_token=token.access_token,
        display_name=name,
        graph_permissions=permissions_list,
    )
    
    if not mcp_app:
        console.print("[red]Failed to create MCP Server app.[/red]")
        raise typer.Exit(1)
    
    # Grant Agent Identity permission if specified
    if agent_name:
        console.print(f"\n[bold blue]Step 3: Grant Agent Identity permission[/bold blue]")
        
        agent = config.get_agent_identity(agent_name)
        if not agent:
            console.print(f"[yellow]Warning: Agent '{agent_name}' not found in local config.[/yellow]")
            console.print("[yellow]You can manually grant permission later using 'grant-agent-mcp-permission'.[/yellow]")
        else:
            if grant_agent_permission_to_mcp(
                access_token=token.access_token,
                agent_identity_app_id=agent.app_id,
                mcp_server_app_id=mcp_app.app_id,
            ):
                console.print(f"[green]✓ Agent '{agent_name}' can now call MCP Server API[/green]")
            else:
                console.print("[yellow]Warning: Failed to grant Agent permission.[/yellow]")
    
    # Display results
    console.print(f"\n[bold green]MCP Server App '{name}' created successfully![/bold green]\n")
    console.print("[bold]Configuration for your MCP Server:[/bold]")
    console.print(f"  MCP_CLIENT_ID={mcp_app.app_id}")
    console.print(f"  MCP_CLIENT_SECRET={mcp_app.client_secret}")
    console.print(f"  TENANT_ID={tid}")
    console.print()
    console.print("[bold]API Scope (for AI Agent to request tokens):[/bold]")
    console.print(f"  {mcp_app.api_scope}")
    console.print()
    console.print("[bold]Configuration for ai-agent-cli (.env):[/bold]")
    console.print(f"  MCP_SERVER_APP_ID={mcp_app.app_id}")


@app.command("grant-agent-mcp-permission")
def grant_agent_mcp_permission_cmd(
    agent_name: str = typer.Argument(..., help="Name of the Agent Identity"),
    mcp_app_id: str = typer.Argument(..., help="MCP Server application ID"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
) -> None:
    """Grant an Agent Identity permission to call an MCP Server API.
    
    This is needed so the Agent Identity can request OBO tokens
    with the MCP Server as the audience.
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Get agent identity
    agent = config.get_agent_identity(agent_name)
    if not agent:
        console.print(f"[red]Agent identity '{agent_name}' not found in local config.[/red]")
        raise typer.Exit(1)
    
    console.print(f"\n[bold]Granting MCP Permission[/bold]")
    console.print(f"Agent: {agent_name} ({agent.app_id})")
    console.print(f"MCP Server: {mcp_app_id}\n")
    
    # Authenticate
    token = get_device_code_token(
        tid,
        scopes=["DelegatedPermissionGrant.ReadWrite.All", "Application.Read.All"]
    )
    if not token:
        raise typer.Exit(1)
    
    # Grant permission
    if grant_agent_permission_to_mcp(
        access_token=token.access_token,
        agent_identity_app_id=agent.app_id,
        mcp_server_app_id=mcp_app_id,
    ):
        console.print(f"\n[bold green]✓ Permission granted successfully![/bold green]")
    else:
        console.print("\n[red]Failed to grant permission.[/red]")
        raise typer.Exit(1)


@app.command("configure-agent-claims")
def configure_agent_claims_cmd(
    app_id: str = typer.Argument(..., help="Application ID of the MCP Server or API app"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
) -> None:
    """Configure Agent Identity optional claims on an existing app registration.
    
    This adds the xms_* claims that identify tokens as coming from Agent Identities:
    - xms_act_fct: Actor facet (11 = AgentIdentity)
    - xms_sub_fct: Subject facet
    - xms_par_app_azp: Parent application (Blueprint)
    - xms_idrel: Identity relationship
    - xms_tnt_fct: Tenant facet
    
    Use this if you created an MCP Server app before this feature was added,
    or if you want to enable Agent Identity detection on any custom API.
    """
    tid = require_tenant_id(tenant_id)
    
    console.print(f"\n[bold]Configuring Agent Identity Claims[/bold]")
    console.print(f"App ID: {app_id}\n")
    
    # Authenticate
    token = get_device_code_token(
        tid,
        scopes=["Application.ReadWrite.All"]
    )
    if not token:
        raise typer.Exit(1)
    
    # Get the application object ID
    from .graph_client import GraphClient
    client = GraphClient(token.access_token)
    
    console.print("[bold blue]Looking up application...[/bold blue]")
    app = client.get_application_by_app_id(app_id)
    if not app:
        console.print(f"[red]Application not found for App ID: {app_id}[/red]")
        raise typer.Exit(1)
    
    object_id = app["id"]
    display_name = app.get("displayName", app_id)
    console.print(f"[green]✓ Found: {display_name}[/green]")
    console.print(f"  Object ID: {object_id}")
    
    # Configure optional claims
    console.print("\n[bold blue]Configuring optional claims...[/bold blue]")
    if client.configure_agent_identity_optional_claims(object_id):
        console.print("[green]✓ Agent Identity optional claims configured![/green]")
        console.print("\n[bold]Claims added to access tokens:[/bold]")
        console.print("  • xms_act_fct  - Actor facet (11 = AgentIdentity)")
        console.print("  • xms_sub_fct  - Subject facet")
        console.print("  • xms_par_app_azp - Parent application (Blueprint)")
        console.print("  • xms_idrel    - Identity relationship")
        console.print("  • xms_tnt_fct  - Tenant facet")
        console.print("\n[dim]Note: Existing tokens won't have these claims until they're refreshed.[/dim]")
    else:
        console.print("\n[red]Failed to configure optional claims.[/red]")
        raise typer.Exit(1)


@app.command("add-federated-credential")
def add_federated_credential(
    blueprint_name: Optional[str] = typer.Argument(None, help="Name of the locally stored blueprint"),
    issuer: str = typer.Option(..., "--issuer", "-i", help="OIDC Issuer URL (e.g., Kubernetes OIDC provider)"),
    subject: str = typer.Option(..., "--subject", "-s", help="Subject claim (e.g., system:serviceaccount:namespace:sa-name)"),
    name: Optional[str] = typer.Option(None, "--name", "-n", help="Credential name (default: auto-generated from subject)"),
    audience: str = typer.Option("api://AzureADTokenExchange", "--audience", "-a", help="Token audience"),
    description: str = typer.Option("", "--description", help="Optional description"),
    blueprint_id: Optional[str] = typer.Option(None, "--blueprint-id", help="Blueprint client ID (instead of stored name)"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication"),
) -> None:
    """Add a Federated Identity Credential to a Blueprint for workload identity.
    
    This enables Kubernetes workload identity authentication, allowing pods
    with a specific service account to authenticate as the Blueprint without
    needing a client secret.
    
    The subject claim format for Kubernetes service accounts is:
        system:serviceaccount:<namespace>:<service-account-name>
    
    Examples:
    
        # Using stored blueprint name
        python -m agent_cli.main add-federated-credential "My Blueprint" \\
            --issuer "https://oidc.example.com" \\
            --subject "system:serviceaccount:entra-demo:sidecar-sa"
        
        # Using blueprint client ID directly
        python -m agent_cli.main add-federated-credential \\
            --blueprint-id "abc123-..." \\
            --issuer "https://oidc.example.com" \\
            --subject "system:serviceaccount:entra-demo:sidecar-sa" \\
            --name "kind-workload-identity"
    
    See WORKLOAD-IDENTITY-GUIDE.md for detailed setup instructions.
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Determine blueprint client ID
    bp_client_id: Optional[str] = None
    bp_display_name: Optional[str] = None
    
    if blueprint_id:
        bp_client_id = blueprint_id
    elif blueprint_name:
        blueprint = config.get_blueprint(blueprint_name)
        if not blueprint:
            console.print(f"[red]Blueprint '{blueprint_name}' not found in local config.[/red]")
            console.print("Use 'list-blueprints' to see available blueprints, or use --blueprint-id.")
            raise typer.Exit(1)
        bp_client_id = blueprint.app_id
        bp_display_name = blueprint_name
    else:
        console.print("[red]Error: Either blueprint name or --blueprint-id is required.[/red]")
        raise typer.Exit(1)
    
    # Auto-generate credential name from subject if not provided
    cred_name = name
    if not cred_name:
        # Extract namespace and sa name from subject
        # subject format: system:serviceaccount:namespace:sa-name
        parts = subject.split(":")
        if len(parts) >= 4:
            namespace = parts[2]
            sa_name = parts[3]
            cred_name = f"{namespace}-{sa_name}-workload-id"
        else:
            cred_name = "workload-identity"
    
    # Sanitize name (only alphanumeric, hyphens, underscores allowed)
    import re
    cred_name = re.sub(r'[^a-zA-Z0-9_-]', '-', cred_name)
    
    console.print(f"\n[bold]Adding Federated Identity Credential[/bold]")
    if bp_display_name:
        console.print(f"Blueprint: {bp_display_name} ({bp_client_id})")
    else:
        console.print(f"Blueprint ID: {bp_client_id}")
    console.print(f"Credential Name: {cred_name}")
    console.print(f"Issuer: {issuer}")
    console.print(f"Subject: {subject}")
    console.print(f"Audience: {audience}")
    if description:
        console.print(f"Description: {description}")
    console.print()
    
    # Authenticate
    console.print("[bold blue]Step 1: Authenticate with device code flow[/bold blue]")
    token = get_device_code_token(
        tid, 
        scopes=["Application.ReadWrite.All"],
        force_refresh=force_refresh
    )
    if not token:
        raise typer.Exit(1)
    
    console.print("[green]✓ Authentication successful[/green]\n")
    
    # Get the Blueprint application object ID
    console.print("[bold blue]Step 2: Looking up Blueprint application...[/bold blue]")
    client = GraphClient(token.access_token)
    blueprint_app = client.get_blueprint_by_app_id(bp_client_id)
    
    if not blueprint_app:
        console.print(f"[red]Blueprint application not found with Client ID: {bp_client_id}[/red]")
        raise typer.Exit(1)
    
    object_id = blueprint_app["id"]
    display_name = blueprint_app.get("displayName", bp_client_id)
    console.print(f"[green]✓ Found Blueprint: {display_name}[/green]")
    console.print(f"  Object ID: {object_id}")
    
    # Add the federated identity credential
    console.print(f"\n[bold blue]Step 3: Adding Federated Identity Credential...[/bold blue]")
    success, result = client.add_federated_identity_credential(
        app_object_id=object_id,
        name=cred_name,
        issuer=issuer,
        subject=subject,
        audiences=[audience],
        description=description,
    )
    
    if success:
        console.print(f"\n[bold green]✓ Federated Identity Credential added successfully![/bold green]")
        console.print(f"\n[bold]Credential Details:[/bold]")
        console.print(f"  Name: {result.get('name')}")
        console.print(f"  Issuer: {result.get('issuer')}")
        console.print(f"  Subject: {result.get('subject')}")
        console.print(f"  Audiences: {', '.join(result.get('audiences', []))}")
        if result.get('description'):
            console.print(f"  Description: {result.get('description')}")
        console.print(f"\n[dim]The Blueprint can now authenticate using workload identity from the configured issuer.[/dim]")
    else:
        error = result.get("error", {})
        error_msg = error.get("message", str(result))
        
        if "already exists" in error_msg.lower() or "conflicting object" in error_msg.lower():
            console.print(f"[yellow]⚠️  Federated credential '{cred_name}' already exists on this Blueprint.[/yellow]")
            console.print("[dim]Use 'list-federated-credentials' to view existing credentials.[/dim]")
        else:
            console.print(f"[red]Failed to add federated identity credential.[/red]")
            console.print(f"[red]Error: {error_msg}[/red]")
            raise typer.Exit(1)


@app.command("list-federated-credentials")
def list_federated_credentials(
    blueprint_name: Optional[str] = typer.Argument(None, help="Name of the locally stored blueprint"),
    blueprint_id: Optional[str] = typer.Option(None, "--blueprint-id", help="Blueprint client ID (instead of stored name)"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication"),
) -> None:
    """List Federated Identity Credentials on a Blueprint.
    
    Shows all federated identity credentials configured on a Blueprint,
    including workload identity configurations for Kubernetes.
    
    Examples:
    
        # Using stored blueprint name
        python -m agent_cli.main list-federated-credentials "My Blueprint"
        
        # Using blueprint client ID directly
        python -m agent_cli.main list-federated-credentials --blueprint-id "abc123-..."
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Determine blueprint client ID
    bp_client_id: Optional[str] = None
    bp_display_name: Optional[str] = None
    
    if blueprint_id:
        bp_client_id = blueprint_id
    elif blueprint_name:
        blueprint = config.get_blueprint(blueprint_name)
        if not blueprint:
            console.print(f"[red]Blueprint '{blueprint_name}' not found in local config.[/red]")
            console.print("Use 'list-blueprints' to see available blueprints, or use --blueprint-id.")
            raise typer.Exit(1)
        bp_client_id = blueprint.app_id
        bp_display_name = blueprint_name
    else:
        console.print("[red]Error: Either blueprint name or --blueprint-id is required.[/red]")
        raise typer.Exit(1)
    
    console.print(f"\n[bold]Listing Federated Identity Credentials[/bold]")
    if bp_display_name:
        console.print(f"Blueprint: {bp_display_name} ({bp_client_id})")
    else:
        console.print(f"Blueprint ID: {bp_client_id}")
    console.print()
    
    # Authenticate
    console.print("[bold blue]Authenticating...[/bold blue]")
    token = get_device_code_token(
        tid, 
        scopes=["Application.Read.All"],
        force_refresh=force_refresh
    )
    if not token:
        raise typer.Exit(1)
    
    # Get the Blueprint application object ID
    console.print("[bold blue]Looking up Blueprint application...[/bold blue]")
    client = GraphClient(token.access_token)
    blueprint_app = client.get_blueprint_by_app_id(bp_client_id)
    
    if not blueprint_app:
        console.print(f"[red]Blueprint application not found with Client ID: {bp_client_id}[/red]")
        raise typer.Exit(1)
    
    object_id = blueprint_app["id"]
    display_name = blueprint_app.get("displayName", bp_client_id)
    console.print(f"[green]✓ Found Blueprint: {display_name}[/green]\n")
    
    # List federated identity credentials
    fics = client.list_federated_identity_credentials(object_id)
    
    if not fics:
        console.print("[yellow]No federated identity credentials found on this Blueprint.[/yellow]")
        console.print("[dim]Use 'add-federated-credential' to add one for workload identity.[/dim]")
        return
    
    # Display in a table
    table = Table(title=f"Federated Identity Credentials on '{display_name}'")
    table.add_column("Name", style="cyan")
    table.add_column("Subject", style="green")
    table.add_column("Issuer", style="dim", max_width=50)
    table.add_column("Audiences", style="yellow")
    
    for fic in fics:
        audiences = ", ".join(fic.get("audiences", []))
        # Truncate issuer if too long
        issuer_val = fic.get("issuer", "N/A")
        if len(issuer_val) > 50:
            issuer_val = issuer_val[:47] + "..."
        
        table.add_row(
            fic.get("name", "N/A"),
            fic.get("subject", "N/A"),
            issuer_val,
            audiences,
        )
    
    console.print(table)
    
    # Show detailed view
    console.print(f"\n[bold]Details ({len(fics)} credential(s)):[/bold]")
    for fic in fics:
        console.print(f"\n[cyan]• {fic.get('name')}[/cyan]")
        console.print(f"  ID: {fic.get('id')}")
        console.print(f"  Issuer: {fic.get('issuer')}")
        console.print(f"  Subject: {fic.get('subject')}")
        console.print(f"  Audiences: {', '.join(fic.get('audiences', []))}")
        if fic.get("description"):
            console.print(f"  Description: {fic.get('description')}")


@app.command("delete-federated-credential")
def delete_federated_credential(
    blueprint_name: Optional[str] = typer.Argument(None, help="Name of the locally stored blueprint"),
    credential_name: str = typer.Option(..., "--name", "-n", help="Name of the federated credential to delete"),
    blueprint_id: Optional[str] = typer.Option(None, "--blueprint-id", help="Blueprint client ID (instead of stored name)"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    force: bool = typer.Option(False, "--force", "-f", help="Skip confirmation prompt"),
) -> None:
    """Delete a Federated Identity Credential from a Blueprint.
    
    Examples:
    
        # Using stored blueprint name
        python -m agent_cli.main delete-federated-credential "My Blueprint" \\
            --name "namespace-sa-name-workload-id"
        
        # Using blueprint client ID directly
        python -m agent_cli.main delete-federated-credential \\
            --blueprint-id "abc123-client-id" \\
            --name "old-credential"
        
        # Skip confirmation
        python -m agent_cli.main delete-federated-credential "My Blueprint" \\
            --name "old-credential" --force
    """
    tid = require_tenant_id(tenant_id)
    config = get_config()
    
    # Determine blueprint client ID
    bp_client_id: Optional[str] = None
    bp_display_name: Optional[str] = None
    
    if blueprint_id:
        bp_client_id = blueprint_id
    elif blueprint_name:
        blueprint = config.get_blueprint(blueprint_name)
        if not blueprint:
            console.print(f"[red]Blueprint '{blueprint_name}' not found in local config.[/red]")
            console.print("Use 'list-blueprints' to see available blueprints, or use --blueprint-id.")
            raise typer.Exit(1)
        bp_client_id = blueprint.app_id
        bp_display_name = blueprint_name
    else:
        console.print("[red]Error: Either blueprint name or --blueprint-id is required.[/red]")
        raise typer.Exit(1)
    
    console.print(f"\n[bold]Deleting Federated Identity Credential[/bold]")
    if bp_display_name:
        console.print(f"Blueprint: {bp_display_name} ({bp_client_id})")
    else:
        console.print(f"Blueprint ID: {bp_client_id}")
    console.print(f"Credential Name: {credential_name}")
    console.print()
    
    # Authenticate
    console.print("[bold blue]Authenticating...[/bold blue]")
    token = get_device_code_token(
        tid, 
        scopes=["Application.ReadWrite.All"],
    )
    if not token:
        raise typer.Exit(1)
    
    # Get the Blueprint application object ID
    console.print("[bold blue]Looking up Blueprint application...[/bold blue]")
    client = GraphClient(token.access_token)
    blueprint_app = client.get_blueprint_by_app_id(bp_client_id)
    
    if not blueprint_app:
        console.print(f"[red]Blueprint application not found with Client ID: {bp_client_id}[/red]")
        raise typer.Exit(1)
    
    object_id = blueprint_app["id"]
    display_name = blueprint_app.get("displayName", bp_client_id)
    console.print(f"[green]✓ Found Blueprint: {display_name}[/green]")
    
    # Find the credential by name
    console.print("[bold blue]Looking up federated credential...[/bold blue]")
    fics = client.list_federated_identity_credentials(object_id)
    
    target_fic = None
    for fic in fics:
        if fic.get("name") == credential_name:
            target_fic = fic
            break
    
    if not target_fic:
        console.print(f"[red]Federated credential '{credential_name}' not found on this Blueprint.[/red]")
        console.print("[dim]Use 'list-federated-credentials' to see available credentials.[/dim]")
        raise typer.Exit(1)
    
    # Show what we're about to delete
    console.print(f"\n[yellow]About to delete:[/yellow]")
    console.print(f"  Name: {target_fic.get('name')}")
    console.print(f"  Subject: {target_fic.get('subject')}")
    console.print(f"  Issuer: {target_fic.get('issuer')}")
    console.print()
    
    # Confirm deletion
    if not force:
        if not typer.confirm("Are you sure you want to delete this credential?"):
            console.print("[yellow]Aborted.[/yellow]")
            raise typer.Exit(0)
    
    # Delete the credential
    console.print("[bold blue]Deleting federated credential...[/bold blue]")
    credential_id = target_fic.get("id")
    
    if client.delete_federated_identity_credential(object_id, credential_id):
        console.print(f"\n[bold green]✓ Federated credential '{credential_name}' deleted successfully![/bold green]")
    else:
        console.print("\n[red]Failed to delete federated credential.[/red]")
        raise typer.Exit(1)


@app.command("list-applications")
def list_applications_cmd(
    name_filter: Optional[str] = typer.Option(None, "--filter", "-f", help="Filter by display name (substring match)"),
    starts_with: bool = typer.Option(False, "--starts-with", "-s", help="Use startsWith filter instead of search"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    force_refresh: bool = typer.Option(False, "--force-refresh", help="Force re-authentication"),
) -> None:
    """List application registrations, optionally filtering by name.
    
    Examples:
    
        # List all applications (up to 100)
        python -m agent_cli.main list-applications
        
        # Filter by name containing "mcp"
        python -m agent_cli.main list-applications --filter mcp
        
        # Filter by name starting with "MCP"
        python -m agent_cli.main list-applications --filter MCP --starts-with
    """
    tid = require_tenant_id(tenant_id)
    
    console.print("[bold blue]Authenticating...[/bold blue]")
    token = get_device_code_token(tid, scopes=READ_ONLY_SCOPES, force_refresh=force_refresh)
    if not token:
        raise typer.Exit(1)
    
    client = GraphClient(token.access_token)
    
    if name_filter:
        console.print(f"[bold blue]Searching applications with name containing '{name_filter}'...[/bold blue]")
    else:
        console.print("[bold blue]Listing applications...[/bold blue]")
    
    apps = client.list_applications(name_filter=name_filter, use_search=not starts_with)
    
    if not apps:
        if name_filter:
            console.print(f"[yellow]No applications found matching '{name_filter}'.[/yellow]")
        else:
            console.print("[yellow]No applications found.[/yellow]")
        return
    
    table = Table(title=f"Applications{f' (filter: {name_filter})' if name_filter else ''}", show_lines=False)
    table.add_column("Display Name", style="cyan", no_wrap=True)
    table.add_column("App ID (Client ID)", style="green", no_wrap=True)
    table.add_column("Object ID", style="dim", no_wrap=True)
    table.add_column("Created", style="yellow", no_wrap=True)
    
    for app in apps:
        # Format created date
        created = app.get("createdDateTime", "N/A")
        if created != "N/A":
            # Truncate to just the date part
            created = created[:10] if len(created) >= 10 else created
        
        table.add_row(
            app.get("displayName", "N/A"),
            app.get("appId", "N/A"),
            app.get("id", "N/A"),
            created,
        )
    
    console.print(table)
    console.print(f"\n[dim]Found {len(apps)} application(s)[/dim]")


@app.command("config")
def show_config(
    path: bool = typer.Option(False, "--path", "-p", help="Show config file path only"),
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID (for showing cached accounts)"),
) -> None:
    """Show current configuration."""
    config = get_config()
    
    if path:
        console.print(str(config.config_path))
        return
    
    console.print(f"[bold]Config file:[/bold] {config.config_path}")
    console.print(f"[bold]Token cache:[/bold] {TOKEN_CACHE_PATH}")
    console.print(f"[bold]Tenant ID:[/bold] {config.tenant_id or '[dim]Not set[/dim]'}")
    console.print(f"[bold]Default Blueprint:[/bold] {config.default_blueprint_name or '[dim]Not set[/dim]'}")
    console.print(f"\n[bold]Stored Blueprints:[/bold] {len(config.list_blueprints())}")
    console.print(f"[bold]Stored Agent Identities:[/bold] {len(config.list_agent_identities())}")
    
    # Show cached accounts if tenant ID is available
    tid = tenant_id or config.tenant_id
    if tid:
        accounts = get_cached_accounts(tid)
        if accounts:
            console.print(f"\n[bold]Cached Accounts ({len(accounts)}):[/bold]")
            for account in accounts:
                console.print(f"  - {account.get('username', 'unknown')}")
        else:
            console.print(f"\n[bold]Cached Accounts:[/bold] [dim]None[/dim]")


@app.command("logout")
def logout() -> None:
    """Clear cached authentication tokens.
    
    This removes all cached tokens, forcing re-authentication
    on the next command that requires it.
    """
    console.print("[bold blue]Clearing token cache...[/bold blue]")
    clear_token_cache()
    console.print("[green]✓ Logged out successfully[/green]")


@app.command("login")
def login(
    tenant_id: Optional[str] = typer.Option(None, "--tenant-id", "-t", help="Azure AD tenant ID"),
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication (ignore cached token)"),
) -> None:
    """Authenticate and cache tokens for future use.
    
    This pre-authenticates so subsequent commands don't require login.
    """
    tid = require_tenant_id(tenant_id)
    
    console.print("[bold blue]Authenticating...[/bold blue]")
    token = get_device_code_token(tid, force_refresh=force_refresh)
    
    if token:
        console.print("[green]✓ Authentication successful, token cached for future use[/green]")
    else:
        console.print("[red]Authentication failed[/red]")
        raise typer.Exit(1)


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    main()
