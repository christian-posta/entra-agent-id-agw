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
)
from .config import get_config
from .graph_client import (
    GraphClient,
    create_full_blueprint,
    create_agent_identity_from_blueprint,
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
        
        token = get_device_code_token(tid)
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
) -> None:
    """Create a new Agent Identity Blueprint.
    
    This will:
    1. Authenticate using device code flow
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
    token = get_device_code_token(tid)
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
) -> None:
    """List all Agent Identities.
    
    By default, lists agent identities stored in local config.
    Use --from-graph to fetch from Microsoft Graph API.
    """
    config = get_config()
    
    if from_graph:
        tid = require_tenant_id(tenant_id)
        console.print("[bold blue]Authenticating to fetch agent identities from Graph API...[/bold blue]")
        
        token = get_device_code_token(tid)
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
) -> None:
    """Create a new Agent Identity from a stored blueprint.
    
    Requires a blueprint to be created and stored first.
    The sponsor user ID must be provided (e.g., from 'az ad signed-in-user show --query id').
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
    console.print(f"Using blueprint: {blueprint_name} ({blueprint.app_id})\n")
    
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


@app.command("config")
def show_config(
    path: bool = typer.Option(False, "--path", "-p", help="Show config file path only"),
) -> None:
    """Show current configuration."""
    config = get_config()
    
    if path:
        console.print(str(config.config_path))
        return
    
    console.print(f"[bold]Config file:[/bold] {config.config_path}")
    console.print(f"[bold]Tenant ID:[/bold] {config.tenant_id or '[dim]Not set[/dim]'}")
    console.print(f"[bold]Default Blueprint:[/bold] {config.default_blueprint_name or '[dim]Not set[/dim]'}")
    console.print(f"\n[bold]Stored Blueprints:[/bold] {len(config.list_blueprints())}")
    console.print(f"[bold]Stored Agent Identities:[/bold] {len(config.list_agent_identities())}")


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    main()

