# AI Agent CLI

An interactive CLI AI agent that uses Azure OpenAI with Microsoft Entra authentication and MCP (Model Context Protocol) tool support.

## Features

- **Microsoft Entra Authentication**: Device code flow with persistent token caching
- **Azure OpenAI Integration**: Chat with GPT models deployed on Azure
- **MCP Tool Support**: Connect to remote MCP servers via SSE for tool calling
- **Interactive Menu**: Easy-to-use command-line interface

## Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Copy `env.example` to `.env` and configure:

```bash
cp env.example .env
```

Edit `.env`:

```bash
# Microsoft Entra ID Configuration
TENANT_ID=your-tenant-id-here

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_API_VERSION=2024-02-15-preview

# Authentication Mode: "entra" or "api_key"
AZURE_OPENAI_AUTH_MODE=entra

# API Key (only used if AUTH_MODE=api_key)
AZURE_OPENAI_API_KEY=
```

### Config Files

The CLI uses two config files in your home directory:

| File | Purpose |
|------|---------|
| `~/.ai-agent-cli.json` | Stores MCP server configurations |
| `~/.ai-agent-cli-tokens.json` | Caches authentication tokens |

## Usage

### Start the Interactive CLI

```bash
python -m agent_cli.main run
```

On first run with Entra authentication, you'll see:

```
To sign in, use a web browser to open the page https://microsoft.com/devicelogin 
and enter the code XXXXXX to authenticate.
```

### Interactive Menu

After login, you'll see:

```
═══════════════════════════════════════
           AI Agent CLI
           Logged in as: user@example.com
═══════════════════════════════════════

1. Prompt agent
2. List MCP tools
3. Add MCP tool server
4. Remove MCP tool server
5. Clear conversation history
6. Exit

Select an option:
```

### Menu Options

#### 1. Prompt Agent

Enter an interactive chat session with the AI agent. The agent can use any connected MCP tools to help answer your questions.

Type `exit` or `quit` to return to the menu, or `clear` to reset conversation history.

#### 2. List MCP Tools

Display all available tools from connected MCP servers in a formatted table.

#### 3. Add MCP Tool Server

Add a new MCP server by providing:
- **Server name**: A friendly name for the server
- **SSE URL**: The Server-Sent Events endpoint (e.g., `http://localhost:3000/sse`)

The server will be connected immediately and its tools will be available to the agent.

#### 4. Remove MCP Tool Server

Remove a previously configured MCP server.

#### 5. Clear Conversation History

Reset the agent's conversation history while staying in the session.

#### 6. Exit

Exit the CLI application.

### Other Commands

```bash
# Show current configuration
python -m agent_cli.main config-show

# Clear cached tokens (logout)
python -m agent_cli.main logout

# Force re-authentication
python -m agent_cli.main run --force-refresh
```

## Authentication Modes

### Entra ID Authentication (Recommended)

Uses Microsoft Entra ID (Azure AD) for secure authentication:
1. Set `AZURE_OPENAI_AUTH_MODE=entra`
2. Configure `TENANT_ID`
3. On first run, complete device code flow authentication
4. Token is cached for future use

### API Key Authentication

For simpler setups or testing:
1. Set `AZURE_OPENAI_AUTH_MODE=api_key`
2. Set `AZURE_OPENAI_API_KEY` to your Azure OpenAI API key

## MCP Tool Integration

The agent supports the Model Context Protocol (MCP) for tool calling. Connect to MCP servers that expose tools via SSE (Server-Sent Events).

When you chat with the agent, it will automatically use available tools when helpful. For example, if you have a filesystem MCP server connected, you can ask the agent to list files, read content, etc.

## Security Notes

- Authentication tokens are cached locally in `~/.ai-agent-cli-tokens.json`
- MCP server configurations are stored in `~/.ai-agent-cli.json`
- Use `logout` command to clear cached tokens
- Protect these files appropriately on shared systems

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                       AI Agent CLI                          │
├─────────────────────────────────────────────────────────────┤
│  main.py          - Interactive menu & CLI commands         │
│  auth.py          - Microsoft Entra device code flow        │
│  config.py        - Configuration management                │
│  agent.py         - Azure OpenAI chat & tool calling        │
│  mcp_client.py    - MCP SSE client for tools                │
│  models.py        - Data classes                            │
└─────────────────────────────────────────────────────────────┘
          │                    │                    │
          ▼                    ▼                    ▼
    ┌──────────┐        ┌───────────┐        ┌──────────┐
    │  Entra   │        │   Azure   │        │   MCP    │
    │   ID     │        │  OpenAI   │        │ Servers  │
    └──────────┘        └───────────┘        └──────────┘
```
