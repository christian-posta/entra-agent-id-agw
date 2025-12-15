"""AI Agent CLI - Main entry point with interactive menu."""

from typing import Optional

import json

import typer
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown
from rich.panel import Panel
from rich.syntax import Syntax

from .auth import (
    get_user_token_for_blueprint,
    clear_token_cache,
    get_current_username,
    OBOTokenManager,
    AZURE_COGNITIVE_SERVICES_SCOPE,
)
from .config import get_config
from .models import MCPServer, TokenResult
from .mcp_client import MCPManager
from .agent import Agent, create_agent_with_api_key, create_agent_with_obo_token


app = typer.Typer(
    name="ai-agent-cli",
    help="Interactive AI Agent CLI with Microsoft Entra authentication and MCP tools",
    no_args_is_help=False,
)
console = Console()


def require_azure_openai_config() -> tuple[str, str, str]:
    """Ensure Azure OpenAI is configured.
    
    Returns:
        Tuple of (endpoint, deployment, api_version)
    """
    config = get_config()
    
    if not config.azure_openai_endpoint:
        console.print("[red]Error: Azure OpenAI endpoint not configured.[/red]")
        console.print("Set AZURE_OPENAI_ENDPOINT in .env file")
        raise typer.Exit(1)
    
    if not config.azure_openai_deployment:
        console.print("[red]Error: Azure OpenAI deployment not configured.[/red]")
        console.print("Set AZURE_OPENAI_DEPLOYMENT in .env file")
        raise typer.Exit(1)
    
    return (
        config.azure_openai_endpoint,
        config.azure_openai_deployment,
        config.azure_openai_api_version,
    )


def display_menu(username: Optional[str] = None, auth_mode: str = "api_key") -> None:
    """Display the main menu.
    
    Args:
        username: Logged in username to display
        auth_mode: Authentication mode (entra or api_key)
    """
    if auth_mode == "api_key":
        login_status = "[yellow]Test Mode (API Key)[/yellow]"
    elif username:
        login_status = f"Logged in as: [green]{username}[/green]"
    else:
        login_status = "[yellow]Entra Mode (OBO)[/yellow]"
    
    menu_text = f"""
[bold cyan]═══════════════════════════════════════[/bold cyan]
[bold white]           AI Agent CLI[/bold white]
           {login_status}
[bold cyan]═══════════════════════════════════════[/bold cyan]

[bold]1.[/bold] Prompt agent
[bold]2.[/bold] List MCP tools
[bold]3.[/bold] Add MCP tool server
[bold]4.[/bold] Remove MCP tool server
[bold]5.[/bold] Clear conversation history
[bold]6.[/bold] Exit
"""
    console.print(menu_text)


def prompt_agent_loop(agent: Agent) -> None:
    """Run the interactive chat loop.
    
    Args:
        agent: Configured agent
    """
    console.print("\n[bold cyan]Chat with AI Agent[/bold cyan]")
    console.print("[dim]Type 'exit' or 'quit' to return to menu, 'clear' to reset history[/dim]\n")
    
    while True:
        try:
            user_input = Prompt.ask("[bold green]You[/bold green]")
        except (KeyboardInterrupt, EOFError):
            console.print("\n")
            break
        
        if not user_input.strip():
            continue
        
        if user_input.lower() in ("exit", "quit"):
            break
        
        if user_input.lower() == "clear":
            agent.clear_history()
            console.print("[dim]Conversation history cleared.[/dim]\n")
            continue
        
        # Get response from agent
        console.print("\n[bold blue]Assistant[/bold blue]:")
        
        try:
            response = agent.chat(user_input)
            # Render response as markdown for better formatting
            console.print(Markdown(response))
            console.print()
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]\n")


def list_mcp_tools(mcp_manager: MCPManager) -> None:
    """Display all available MCP tools.
    
    Args:
        mcp_manager: MCP manager
    """
    tools = mcp_manager.list_all_tools()
    
    if not tools:
        console.print("\n[yellow]No MCP tools available.[/yellow]")
        console.print("[dim]Add an MCP server using option 3.[/dim]\n")
        return
    
    table = Table(title="Available MCP Tools")
    table.add_column("Tool Name", style="cyan")
    table.add_column("Server", style="green")
    table.add_column("Description", style="white")
    
    for tool in tools:
        table.add_row(
            tool.name,
            tool.server_name,
            tool.description[:60] + "..." if len(tool.description) > 60 else tool.description,
        )
    
    console.print()
    console.print(table)
    console.print()


def add_mcp_server(mcp_manager: MCPManager) -> None:
    """Prompt user to add an MCP server.
    
    Args:
        mcp_manager: MCP manager
    """
    config = get_config()
    
    console.print("\n[bold cyan]Add MCP Tool Server[/bold cyan]\n")
    
    try:
        name = Prompt.ask("Server name")
        if not name.strip():
            console.print("[red]Server name cannot be empty.[/red]\n")
            return
        
        url = Prompt.ask("SSE URL (e.g., http://localhost:3000/sse)")
        if not url.strip():
            console.print("[red]URL cannot be empty.[/red]\n")
            return
        
        # Create server config
        server = MCPServer(name=name.strip(), url=url.strip())
        
        # Try to connect
        console.print(f"\n[dim]Connecting to {name}...[/dim]")
        
        if mcp_manager.add_server(server):
            # Save to config
            config.add_mcp_server(server)
            console.print(f"[green]✓ MCP server '{name}' added and connected![/green]")
            
            # Show available tools
            client = mcp_manager.get_client(name)
            if client and client.tools:
                console.print(f"[dim]Found {len(client.tools)} tool(s)[/dim]")
        else:
            console.print(f"[red]Failed to connect to MCP server.[/red]")
            if Confirm.ask("Save server configuration anyway?", default=False):
                config.add_mcp_server(server)
                console.print("[yellow]Server saved (not connected).[/yellow]")
    
    except (KeyboardInterrupt, EOFError):
        console.print("\n[dim]Cancelled.[/dim]")
    
    console.print()


def remove_mcp_server(mcp_manager: MCPManager) -> None:
    """Prompt user to remove an MCP server.
    
    Args:
        mcp_manager: MCP manager
    """
    config = get_config()
    servers = config.list_mcp_servers()
    
    if not servers:
        console.print("\n[yellow]No MCP servers configured.[/yellow]\n")
        return
    
    console.print("\n[bold cyan]Remove MCP Tool Server[/bold cyan]\n")
    
    # List servers
    for i, server in enumerate(servers, 1):
        connected = "✓" if server.name in mcp_manager.connected_servers else "✗"
        console.print(f"  {i}. {server.name} ({server.url}) [{connected}]")
    
    console.print()
    
    try:
        choice = Prompt.ask("Enter server number to remove (or 'cancel')")
        
        if choice.lower() == "cancel":
            console.print("[dim]Cancelled.[/dim]\n")
            return
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(servers):
                server = servers[idx]
                if Confirm.ask(f"Remove '{server.name}'?"):
                    mcp_manager.remove_server(server.name)
                    config.remove_mcp_server(server.name)
                    console.print(f"[green]✓ Server '{server.name}' removed.[/green]\n")
            else:
                console.print("[red]Invalid selection.[/red]\n")
        except ValueError:
            console.print("[red]Invalid input.[/red]\n")
    
    except (KeyboardInterrupt, EOFError):
        console.print("\n[dim]Cancelled.[/dim]\n")


def connect_saved_mcp_servers(mcp_manager: MCPManager) -> None:
    """Connect to all saved MCP servers.
    
    Args:
        mcp_manager: MCP manager
    """
    config = get_config()
    servers = config.list_mcp_servers()
    
    for server in servers:
        if server.enabled:
            console.print(f"[dim]Connecting to MCP server: {server.name}...[/dim]")
            mcp_manager.add_server(server)


@app.command()
def run(
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication"),
) -> None:
    """Start the interactive AI Agent CLI."""
    config = get_config()
    
    console.print("\n[bold]Starting AI Agent CLI...[/bold]\n")
    
    # Check configuration
    if not config.is_configured():
        console.print("[red]Error: Configuration incomplete.[/red]")
        console.print("\nFor API Key mode (testing), set:")
        console.print("  - AUTH_MODE=api_key")
        console.print("  - AZURE_OPENAI_ENDPOINT")
        console.print("  - AZURE_OPENAI_DEPLOYMENT")
        console.print("  - AZURE_OPENAI_API_KEY")
        console.print("\nFor Entra mode (production with OBO), set:")
        console.print("  - AUTH_MODE=entra")
        console.print("  - TENANT_ID")
        console.print("  - AZURE_OPENAI_ENDPOINT")
        console.print("  - AZURE_OPENAI_DEPLOYMENT")
        console.print("  - BLUEPRINT_APP_ID")
        console.print("  - BLUEPRINT_CLIENT_SECRET")
        console.print("  - AGENT_IDENTITY_APP_ID")
        raise typer.Exit(1)
    
    endpoint, deployment, api_version = require_azure_openai_config()
    
    # Variables for session
    username: Optional[str] = None
    agent: Optional[Agent] = None
    mcp_manager: Optional[MCPManager] = None
    obo_manager: Optional[OBOTokenManager] = None
    
    if config.auth_mode == "api_key":
        # Test mode: API key authentication
        console.print("[bold yellow]Running in TEST MODE (API Key)[/bold yellow]")
        console.print("[dim]MCP calls will not have authentication.[/dim]\n")
        
        # Create MCP manager without auth
        mcp_manager = MCPManager()
        connect_saved_mcp_servers(mcp_manager)
        
        # Create agent with API key
        agent = create_agent_with_api_key(
            endpoint=endpoint,
            deployment=deployment,
            api_key=config.azure_openai_api_key,
            api_version=api_version,
            mcp_manager=mcp_manager,
        )
    
    else:
        # Production mode: Entra OBO authentication
        console.print("[bold blue]Running in PRODUCTION MODE (Entra OBO)[/bold blue]\n")
        
        # Step 1: User login with Blueprint scope
        console.print("[bold]Step 1: User Authentication[/bold]")
        console.print(f"[dim]Requesting token with Blueprint audience: api://{config.blueprint_app_id}[/dim]")
        
        user_token = get_user_token_for_blueprint(
            tenant_id=config.tenant_id,
            blueprint_app_id=config.blueprint_app_id,
            force_refresh=force_refresh,
        )
        
        if not user_token:
            console.print("[red]User authentication failed.[/red]")
            raise typer.Exit(1)
        
        username = get_current_username(config.tenant_id)
        console.print(f"[green]✓ Logged in as: {username}[/green]\n")
        
        # Step 2: Create OBO Token Manager
        console.print("[bold]Step 2: Initializing OBO Token Manager[/bold]")
        obo_manager = OBOTokenManager(
            tenant_id=config.tenant_id,
            blueprint_app_id=config.blueprint_app_id,
            blueprint_client_secret=config.blueprint_client_secret,
            agent_identity_app_id=config.agent_identity_app_id,
            user_token=user_token.access_token,
        )
        
        # Step 3: Get OBO token for Azure OpenAI
        console.print("[bold]Step 3: Getting OBO token for Azure OpenAI[/bold]")
        aoai_token = obo_manager.get_azure_openai_token()
        
        if not aoai_token:
            console.print("[red]Failed to get OBO token for Azure OpenAI.[/red]")
            console.print("[yellow]Hint: Ensure admin consent is granted for the Agent Identity.[/yellow]")
            raise typer.Exit(1)
        
        console.print("[green]✓ Azure OpenAI OBO token acquired[/green]\n")
        
        # Step 4: Get OBO token for MCP Server (if configured)
        mcp_token = None
        if config.mcp_server_app_id:
            console.print("[bold]Step 4: Getting OBO token for MCP Server[/bold]")
            console.print(f"[dim]MCP Server App ID: {config.mcp_server_app_id}[/dim]")
            
            mcp_scope = f"api://{config.mcp_server_app_id}/.default"
            mcp_token = obo_manager.get_token_for_scope(mcp_scope)
            
            if mcp_token:
                console.print("[green]✓ MCP Server OBO token acquired[/green]\n")
            else:
                console.print("[yellow]Warning: Could not get MCP Server OBO token.[/yellow]")
                console.print("[yellow]MCP calls will not have authentication.[/yellow]\n")
        else:
            console.print("[dim]Step 4: No MCP_SERVER_APP_ID configured, MCP calls will not have OBO tokens[/dim]\n")
        
        # Step 5: Create MCP manager with OBO token provider
        # The token provider returns the access token string for MCP gateway authentication
        def mcp_token_provider() -> Optional[str]:
            if not config.mcp_server_app_id:
                return None
            mcp_scope = f"api://{config.mcp_server_app_id}/.default"
            token = obo_manager.get_token_for_scope(mcp_scope)
            return token.access_token if token else None
        
        mcp_manager = MCPManager(token_provider=mcp_token_provider)
        connect_saved_mcp_servers(mcp_manager)
        
        # Step 6: Create agent with OBO token
        agent = create_agent_with_obo_token(
            endpoint=endpoint,
            deployment=deployment,
            token=aoai_token,
            api_version=api_version,
            mcp_manager=mcp_manager,
        )
        
        console.print("[bold green]✓ Agent initialized with OBO authentication[/bold green]\n")
    
    # Main menu loop
    while True:
        display_menu(username, config.auth_mode)
        
        try:
            choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6"])
        except (KeyboardInterrupt, EOFError):
            console.print("\n[bold]Goodbye![/bold]\n")
            break
        
        if choice == "1":
            prompt_agent_loop(agent)
        elif choice == "2":
            list_mcp_tools(mcp_manager)
        elif choice == "3":
            add_mcp_server(mcp_manager)
        elif choice == "4":
            remove_mcp_server(mcp_manager)
        elif choice == "5":
            agent.clear_history()
            console.print("\n[green]✓ Conversation history cleared.[/green]\n")
        elif choice == "6":
            console.print("\n[bold]Goodbye![/bold]\n")
            break
    
    # Cleanup
    if mcp_manager:
        mcp_manager.disconnect_all()
    if obo_manager:
        obo_manager.clear_cache()


@app.command()
def config_show() -> None:
    """Show current configuration."""
    config = get_config()
    
    console.print("\n[bold]Current Configuration[/bold]\n")
    
    table = Table(show_header=False)
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="white")
    
    table.add_row("Config file", str(config.config_path))
    table.add_row("Auth mode", config.auth_mode)
    table.add_row("", "")
    
    # Entra settings
    table.add_row("[bold]Entra ID[/bold]", "")
    table.add_row("Tenant ID", config.tenant_id or "[dim]Not set[/dim]")
    table.add_row("Blueprint App ID", config.blueprint_app_id or "[dim]Not set[/dim]")
    table.add_row("Blueprint Secret", "[green]Set[/green]" if config.blueprint_client_secret else "[dim]Not set[/dim]")
    table.add_row("Agent Identity App ID", config.agent_identity_app_id or "[dim]Not set[/dim]")
    table.add_row("MCP Server App ID", config.mcp_server_app_id or "[dim]Not set[/dim]")
    table.add_row("", "")
    
    # Azure OpenAI settings
    table.add_row("[bold]Azure OpenAI[/bold]", "")
    table.add_row("Endpoint", config.azure_openai_endpoint or "[dim]Not set[/dim]")
    table.add_row("Deployment", config.azure_openai_deployment or "[dim]Not set[/dim]")
    table.add_row("API Version", config.azure_openai_api_version)
    table.add_row("API Key", "[green]Set[/green]" if config.azure_openai_api_key else "[dim]Not set[/dim]")
    
    console.print(table)
    
    # MCP Servers
    servers = config.list_mcp_servers()
    if servers:
        console.print(f"\n[bold]MCP Servers ({len(servers)}):[/bold]")
        for server in servers:
            status = "[green]enabled[/green]" if server.enabled else "[dim]disabled[/dim]"
            console.print(f"  - {server.name}: {server.url} ({status})")
    else:
        console.print("\n[dim]No MCP servers configured.[/dim]")
    
    console.print()


def display_token(title: str, token: TokenResult, color: str = "blue") -> None:
    """Display a token with its decoded claims.
    
    Args:
        title: Title for the token panel
        token: TokenResult to display
        color: Border color for the panel
    """
    claims = token.decoded_claims()
    claims_json = json.dumps(claims, indent=2)
    syntax = Syntax(claims_json, "json", theme="monokai", line_numbers=False)
    console.print(Panel(syntax, title=f"[bold]{title}[/bold]", border_style=color))


@app.command()
def show_tokens(
    force_refresh: bool = typer.Option(False, "--force-refresh", "-f", help="Force re-authentication"),
    output_raw: bool = typer.Option(False, "--output-raw", "-r", help="Also output raw token strings"),
) -> None:
    """Show all OBO tokens (Tc, T2 for OpenAI, T2 for MCP Server).
    
    This command authenticates and displays all the tokens in the OBO flow
    with their decoded claims. Useful for debugging and understanding the token flow.
    
    Tokens displayed:
    - Tc: User token with Blueprint as audience
    - T2 (Azure OpenAI): OBO token for Azure Cognitive Services
    - T2 (MCP Server): OBO token for MCP Server (if configured)
    """
    config = get_config()
    
    if config.auth_mode == "api_key":
        console.print("[yellow]Token display is only available in Entra mode (AUTH_MODE=entra).[/yellow]")
        console.print("[dim]In API key mode, no OBO tokens are used.[/dim]")
        raise typer.Exit(0)
    
    # Check configuration
    if not config.tenant_id or not config.blueprint_app_id:
        console.print("[red]Error: Entra configuration incomplete.[/red]")
        console.print("Required: TENANT_ID, BLUEPRINT_APP_ID, BLUEPRINT_CLIENT_SECRET, AGENT_IDENTITY_APP_ID")
        raise typer.Exit(1)
    
    console.print("\n[bold]OBO Token Flow - Token Display[/bold]\n")
    
    # Step 1: Get user token (Tc)
    console.print("[bold blue]Step 1: Getting user token (Tc)...[/bold blue]")
    console.print(f"[dim]Scope: api://{config.blueprint_app_id}/access_as_user[/dim]")
    
    tc_token = get_user_token_for_blueprint(
        tenant_id=config.tenant_id,
        blueprint_app_id=config.blueprint_app_id,
        force_refresh=force_refresh,
    )
    
    if not tc_token:
        console.print("[red]Failed to get user token (Tc).[/red]")
        raise typer.Exit(1)
    
    console.print("[green]✓ Got Tc token[/green]\n")
    
    # Display Tc token
    display_token("Tc Token (User token, aud=Blueprint)", tc_token, "cyan")
    
    if output_raw:
        console.print(f"\n[dim]Raw Tc token:[/dim]")
        console.print(f"[dim]{tc_token.access_token[:50]}...{tc_token.access_token[-20:]}[/dim]\n")
    
    # Step 2: Create OBO manager and get tokens
    console.print("[bold blue]Step 2: Creating OBO Token Manager...[/bold blue]")
    
    obo_manager = OBOTokenManager(
        tenant_id=config.tenant_id,
        blueprint_app_id=config.blueprint_app_id,
        blueprint_client_secret=config.blueprint_client_secret,
        agent_identity_app_id=config.agent_identity_app_id,
        user_token=tc_token.access_token,
    )
    
    # Step 3: Get T2 for Azure OpenAI
    console.print("\n[bold blue]Step 3: Getting T2 for Azure OpenAI...[/bold blue]")
    console.print(f"[dim]Scope: {AZURE_COGNITIVE_SERVICES_SCOPE}[/dim]")
    
    aoai_token = obo_manager.get_azure_openai_token()
    
    if aoai_token:
        console.print("[green]✓ Got T2 for Azure OpenAI[/green]\n")
        display_token("T2 Token (Azure OpenAI, aud=cognitiveservices)", aoai_token, "green")
        
        if output_raw:
            console.print(f"\n[dim]Raw Azure OpenAI T2 token:[/dim]")
            console.print(f"[dim]{aoai_token.access_token[:50]}...{aoai_token.access_token[-20:]}[/dim]\n")
    else:
        console.print("[red]✗ Failed to get T2 for Azure OpenAI[/red]")
        console.print("[yellow]Hint: Ensure admin consent is granted for the Agent Identity.[/yellow]\n")
    
    # Step 4: Get T2 for MCP Server (if configured)
    if config.mcp_server_app_id:
        console.print("[bold blue]Step 4: Getting T2 for MCP Server...[/bold blue]")
        mcp_scope = f"api://{config.mcp_server_app_id}/.default"
        console.print(f"[dim]Scope: {mcp_scope}[/dim]")
        
        mcp_token = obo_manager.get_token_for_scope(mcp_scope)
        
        if mcp_token:
            console.print("[green]✓ Got T2 for MCP Server[/green]\n")
            display_token("T2 Token (MCP Server, aud=MCP_SERVER_APP_ID)", mcp_token, "magenta")
            
            if output_raw:
                console.print(f"\n[dim]Raw MCP Server T2 token:[/dim]")
                console.print(f"[dim]{mcp_token.access_token[:50]}...{mcp_token.access_token[-20:]}[/dim]\n")
        else:
            console.print("[red]✗ Failed to get T2 for MCP Server[/red]")
            console.print("[yellow]Hint: Ensure the Agent Identity has permission to call the MCP Server.[/yellow]\n")
    else:
        console.print("[dim]Step 4: Skipped - MCP_SERVER_APP_ID not configured[/dim]\n")
    
    # Summary
    console.print("[bold]Token Summary[/bold]")
    table = Table(show_header=True)
    table.add_column("Token", style="cyan")
    table.add_column("Audience (aud)", style="white")
    table.add_column("Subject (sub)", style="white")
    table.add_column("App ID (appid)", style="white")
    table.add_column("Status", style="white")
    
    # Tc
    tc_claims = tc_token.decoded_claims()
    table.add_row(
        "Tc (User)",
        tc_claims.get("aud", "N/A")[:40] + "..." if len(str(tc_claims.get("aud", ""))) > 40 else tc_claims.get("aud", "N/A"),
        tc_claims.get("upn", tc_claims.get("sub", "N/A")),
        tc_claims.get("appid", tc_claims.get("azp", "N/A")),
        "[green]✓[/green]",
    )
    
    # T2 OpenAI
    if aoai_token:
        aoai_claims = aoai_token.decoded_claims()
        table.add_row(
            "T2 (Azure OpenAI)",
            aoai_claims.get("aud", "N/A")[:40] + "..." if len(str(aoai_claims.get("aud", ""))) > 40 else aoai_claims.get("aud", "N/A"),
            aoai_claims.get("upn", aoai_claims.get("sub", "N/A")),
            aoai_claims.get("appid", "N/A"),
            "[green]✓[/green]",
        )
    else:
        table.add_row("T2 (Azure OpenAI)", "-", "-", "-", "[red]✗[/red]")
    
    # T2 MCP
    if config.mcp_server_app_id:
        if mcp_token:
            mcp_claims = mcp_token.decoded_claims()
            table.add_row(
                "T2 (MCP Server)",
                mcp_claims.get("aud", "N/A")[:40] + "..." if len(str(mcp_claims.get("aud", ""))) > 40 else mcp_claims.get("aud", "N/A"),
                mcp_claims.get("upn", mcp_claims.get("sub", "N/A")),
                mcp_claims.get("appid", "N/A"),
                "[green]✓[/green]",
            )
        else:
            table.add_row("T2 (MCP Server)", "-", "-", "-", "[red]✗[/red]")
    else:
        table.add_row("T2 (MCP Server)", "[dim]Not configured[/dim]", "-", "-", "[dim]-[/dim]")
    
    console.print(table)
    console.print()


@app.command()
def logout() -> None:
    """Clear cached authentication tokens."""
    console.print("[bold blue]Clearing token cache...[/bold blue]")
    clear_token_cache()
    console.print("[green]✓ Logged out successfully[/green]")


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    main()
