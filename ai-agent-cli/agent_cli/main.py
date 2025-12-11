"""AI Agent CLI - Main entry point with interactive menu."""

from typing import Optional

import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.markdown import Markdown

from .auth import (
    get_device_code_token,
    clear_token_cache,
    get_current_username,
    AZURE_OPENAI_SCOPES,
)
from .config import get_config
from .models import MCPServer, TokenResult
from .mcp_client import MCPManager
from .agent import Agent, create_agent_with_entra_token, create_agent_with_api_key


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
        console.print("Set AZURE_OPENAI_ENDPOINT in .env file or configure via CLI")
        raise typer.Exit(1)
    
    if not config.azure_openai_deployment:
        console.print("[red]Error: Azure OpenAI deployment not configured.[/red]")
        console.print("Set AZURE_OPENAI_DEPLOYMENT in .env file or configure via CLI")
        raise typer.Exit(1)
    
    return (
        config.azure_openai_endpoint,
        config.azure_openai_deployment,
        config.azure_openai_api_version,
    )


def authenticate() -> Optional[TokenResult]:
    """Authenticate using device code flow.
    
    Returns:
        TokenResult if successful, None otherwise
    """
    config = get_config()
    
    if config.azure_openai_auth_mode == "api_key":
        # No Entra auth needed for API key mode
        return None
    
    if not config.tenant_id:
        console.print("[red]Error: Tenant ID not configured.[/red]")
        console.print("Set TENANT_ID in .env file")
        raise typer.Exit(1)
    
    return get_device_code_token(
        tenant_id=config.tenant_id,
        scopes=AZURE_OPENAI_SCOPES,
    )


def create_agent(token: Optional[TokenResult], mcp_manager: Optional[MCPManager] = None) -> Agent:
    """Create an agent with the current configuration.
    
    Args:
        token: Entra token (for Entra auth mode)
        mcp_manager: Optional MCP manager
        
    Returns:
        Configured Agent
    """
    config = get_config()
    endpoint, deployment, api_version = require_azure_openai_config()
    
    if config.azure_openai_auth_mode == "api_key":
        if not config.azure_openai_api_key:
            console.print("[red]Error: API key not configured.[/red]")
            console.print("Set AZURE_OPENAI_API_KEY in .env file")
            raise typer.Exit(1)
        
        return create_agent_with_api_key(
            endpoint=endpoint,
            deployment=deployment,
            api_key=config.azure_openai_api_key,
            api_version=api_version,
            mcp_manager=mcp_manager,
        )
    else:
        if not token:
            console.print("[red]Error: No token available for Entra auth.[/red]")
            raise typer.Exit(1)
        
        return create_agent_with_entra_token(
            endpoint=endpoint,
            deployment=deployment,
            token=token,
            api_version=api_version,
            mcp_manager=mcp_manager,
        )


def display_menu(username: Optional[str] = None) -> None:
    """Display the main menu.
    
    Args:
        username: Logged in username to display
    """
    login_status = f"Logged in as: [green]{username}[/green]" if username else "[yellow]Not logged in (API key mode)[/yellow]"
    
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
        console.print("[red]Error: Azure OpenAI is not configured.[/red]")
        console.print("\nPlease set the following in your .env file:")
        console.print("  - TENANT_ID (for Entra auth)")
        console.print("  - AZURE_OPENAI_ENDPOINT")
        console.print("  - AZURE_OPENAI_DEPLOYMENT")
        console.print("  - AZURE_OPENAI_AUTH_MODE (entra or api_key)")
        console.print("  - AZURE_OPENAI_API_KEY (if using api_key mode)")
        raise typer.Exit(1)
    
    # Authenticate if using Entra
    token: Optional[TokenResult] = None
    username: Optional[str] = None
    
    if config.azure_openai_auth_mode == "entra":
        console.print("[bold blue]Authenticating with Microsoft Entra...[/bold blue]")
        token = get_device_code_token(
            tenant_id=config.tenant_id,
            scopes=AZURE_OPENAI_SCOPES,
            force_refresh=force_refresh,
        )
        
        if not token:
            console.print("[red]Authentication failed.[/red]")
            raise typer.Exit(1)
        
        username = get_current_username(config.tenant_id)
    else:
        console.print("[dim]Using API key authentication[/dim]")
    
    # Initialize MCP manager and connect to saved servers
    mcp_manager = MCPManager()
    connect_saved_mcp_servers(mcp_manager)
    
    # Create agent
    agent = create_agent(token, mcp_manager)
    
    # Main menu loop
    while True:
        display_menu(username)
        
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
    mcp_manager.disconnect_all()


@app.command()
def config_show() -> None:
    """Show current configuration."""
    config = get_config()
    
    console.print("\n[bold]Current Configuration[/bold]\n")
    
    table = Table(show_header=False)
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="white")
    
    table.add_row("Config file", str(config.config_path))
    table.add_row("Tenant ID", config.tenant_id or "[dim]Not set[/dim]")
    table.add_row("Auth mode", config.azure_openai_auth_mode)
    table.add_row("Azure OpenAI Endpoint", config.azure_openai_endpoint or "[dim]Not set[/dim]")
    table.add_row("Azure OpenAI Deployment", config.azure_openai_deployment or "[dim]Not set[/dim]")
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

