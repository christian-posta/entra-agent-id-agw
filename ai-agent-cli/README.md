# AI Agent CLI

An interactive CLI AI agent that uses Azure OpenAI with Microsoft Entra authentication (OBO flows) and MCP (Model Context Protocol) tool support.

## Features

- **Two Authentication Modes**:
  - **Test Mode (API Key)**: Quick testing with Azure OpenAI API key
  - **Production Mode (Entra OBO)**: Full OBO flow with Agent Identity
- **Azure OpenAI Integration**: Chat with GPT models deployed on Azure
- **MCP Tool Support**: Connect to remote MCP servers via SSE with Bearer token auth
- **Agent Identity**: OBO tokens carry both agent and user identity for gateway authorization

## Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                        AUTH MODES                             │
├───────────────────────────────────────────────────────────────┤
│  TEST MODE (api_key)         │  PRODUCTION MODE (entra)       │
│  • Azure OpenAI: API Key     │  • User login → Blueprint      │
│  • MCP: No auth              │  • Azure OpenAI: OBO token     │
│  • Quick testing             │  • MCP/Gateway: OBO token      │
│                              │  • Full audit trail            │
└───────────────────────────────────────────────────────────────┘
```

### Production Mode Token Flow

```
1. User login → Tc (aud=Blueprint, scope=access_as_user)
2. Get T1: Blueprint + fmi_path → T1 (impersonation token)
3. OBO for Azure OpenAI: Tc + T1 → T2 (aud=cognitiveservices)
4. OBO for MCP Server:   Tc + T1 → T2 (aud=MCP_SERVER_APP_ID)
5. Agent uses Azure OpenAI T2 for LLM calls
6. MCP client passes MCP Server T2 to Gateway as Bearer token
7. Gateway validates T2 (checks appid, user claims)
8. MCP Server can do chained OBO to call Graph API

T2 Token contains:
  • aud   = Target resource (cognitiveservices or MCP Server)
  • appid = Agent Identity (which agent is calling)
  • sub   = User's ID
  • upn   = User's email (christian.posta@solo.io)
  • name  = User's display name
```

┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 1: User Login (Device Code Flow)                                       │
│ ─────────────────────────────────────                                       │
│ Client: Microsoft Graph PowerShell (14d82eec-...)                           │
│ Scope:  api://{blueprint_app_id}/access_as_user                             │
│                     ↓                                                       │
│ Result: Tc (User Token with Blueprint as audience)                          │
│         - aud: api://{blueprint}                                            │
│         - sub: christian.posta@solo.io                                      │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 2: Get T1 (Blueprint Impersonation Token with fmi_path)                │
│ ───────────────────────────────────────────────────────────                 │
│ Client:       Blueprint App ID                                              │
│ Scope:        api://AzureADTokenExchange/.default                           │
│ Grant Type:   client_credentials                                            │
│ fmi_path:     {agent_identity_app_id}  ← THIS MAKES IT AGENT IDENTITY OBO   │
│                     ↓                                                       │
│ Result: T1 (Blueprint can impersonate Agent Identity)                       │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STEP 3: OBO Exchange (Tc + T1 → T2)                                         │
│ ───────────────────────────────────                                         │
│ Client:            Agent Identity App ID                                    │
│ client_assertion:  T1 (proves blueprint can speak for agent)                │
│ assertion:         Tc (user token - on behalf of THIS user)                 │
│ Scope:             https://cognitiveservices.azure.com/.default             │
│ Grant Type:        urn:ietf:params:oauth:grant-type:jwt-bearer              │
│                     ↓                                                       │
│ Result: T2 (OBO Token)                                                      │
│         - aud: https://cognitiveservices.azure.com                          │
│         - sub: christian.posta@solo.io (USER's identity)                    │
│         - appid: {agent_identity_app_id} (AGENT's identity)                 │
│         - Contains BOTH user and agent claims                               │
└─────────────────────────────────────────────────────────────────────────────┘

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

### Test Mode (API Key)

For quick testing without Entra authentication:

```bash
# .env
AUTH_MODE=api_key

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_API_KEY=your-api-key
```

### Production Mode (Entra OBO)

You may need to give the agent identity the OpenAI User Role:

```bash
# Get the Agent Identity's Object ID (Service Principal ID)
AGENT_SP_ID="65027832-f56f-4d8e-93aa-a09113ba2d47"
RESOURCE_GROUP="your-resource-group"
AOAI_RESOURCE_NAME="your-openai-resource"
SUBSCRIPTION_ID="your-subscription-id"

# Assign "Cognitive Services OpenAI User" role to the Agent Identity
az role assignment create \
    --assignee "$AGENT_SP_ID" \
    --role "Cognitive Services OpenAI User" \
    --scope "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.CognitiveServices/accounts/$AOAI_RESOURCE_NAME"


# Assign role to myself
az role assignment create \
    --assignee "christian.posta@solo.io" \
    --role "Cognitive Services OpenAI User" \
    --scope "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.CognitiveServices/accounts/$AOAI_RESOURCE_NAME"
```

For full OBO flow with Agent Identity:

```bash
# .env
AUTH_MODE=entra

# Microsoft Entra ID
TENANT_ID=your-tenant-id

# Azure OpenAI
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o

# Blueprint (parent application for agent identity)
BLUEPRINT_APP_ID=your-blueprint-client-id
BLUEPRINT_CLIENT_SECRET=your-blueprint-secret

# Agent Identity (the identity the agent assumes)
AGENT_IDENTITY_APP_ID=your-agent-identity-client-id

# MCP Server (for OBO tokens to AI Gateway/MCP)
# Create with: entra-agent-cli create-mcp-server-app "MCP Tool Server"
MCP_SERVER_APP_ID=your-mcp-server-client-id
```

### Prerequisites for Production Mode

1. **Create a Blueprint** with exposed API scope `access_as_user`
2. **Create an Agent Identity** from the Blueprint
3. **Grant admin consent** for the Agent Identity to access downstream APIs
4. User must have permission to authenticate against the Blueprint

**For MCP Server OBO (optional but recommended):**

5. **Create an MCP Server App Registration** using `entra-agent-cli`:
   ```bash
   # Option A: Create and grant agent permission in one command
   python -m agent_cli.main create-mcp-server-app "MCP Tool Server" \
       --agent-name "Interactive Agent" \
       --graph-permissions "User.Read"
   
   # Option B: Create separately, then grant permission
   python -m agent_cli.main create-mcp-server-app "MCP Tool Server"
   
   # Then grant the Agent Identity permission to call the MCP Server
   python -m agent_cli.main grant-agent-mcp-permission "Interactive Agent" "<MCP_SERVER_APP_ID>"
   ```

6. Add the MCP Server App ID to your `.env` file:
   ```bash
   MCP_SERVER_APP_ID=<the-app-id-from-step-5>
   ```

7. **Verify tokens** using `show-tokens`:
   ```bash
   python -m agent_cli.main show-tokens
   ```
   All three tokens (Tc, T2 for OpenAI, T2 for MCP) should show ✓

See `OBO-GUIDE.md` in the parent directory for detailed setup instructions.

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

#### Test Mode Output

```
Starting AI Agent CLI...

Running in TEST MODE (API Key)
MCP calls will not have authentication.

═══════════════════════════════════════
           AI Agent CLI
           Test Mode (API Key)
═══════════════════════════════════════
```

#### Production Mode Output

```
Starting AI Agent CLI...

Running in PRODUCTION MODE (Entra OBO)

Step 1: User Authentication
To sign in, use a web browser to open https://microsoft.com/devicelogin
and enter the code XXXXXX to authenticate.

✓ Logged in as: user@example.com

Step 2: Initializing OBO Token Manager
Step 3: Getting OBO token for Azure OpenAI
✓ T1 token acquired
✓ OBO token acquired for cognitiveservices
✓ Azure OpenAI OBO token acquired

Step 4: Getting OBO token for MCP Server
MCP Server App ID: abc123-...
✓ MCP Server OBO token acquired

Step 5: Create MCP manager with OBO token provider
Step 6: Create agent with OBO token
✓ Agent initialized with OBO authentication

═══════════════════════════════════════
           AI Agent CLI
           Logged in as: user@example.com
═══════════════════════════════════════
```

### Interactive Menu

```
1. Prompt agent
2. List MCP tools
3. Add MCP tool server
4. Remove MCP tool server
5. Clear conversation history
6. Exit
```

### Other Commands

```bash
# Show current configuration
python -m agent_cli.main config-show

# Show all OBO tokens with decoded claims
python -m agent_cli.main show-tokens

# Show tokens with raw token strings
python -m agent_cli.main show-tokens --output-raw

# Clear cached tokens (logout)
python -m agent_cli.main logout

# Force re-authentication
python -m agent_cli.main run --force-refresh
```

### Show Tokens Command

The `show-tokens` command displays all tokens in the OBO flow with their decoded JWT claims:

```bash
python -m agent_cli.main show-tokens
```

Output:
```
OBO Token Flow - Token Display

Step 1: Getting user token (Tc)...
✓ Got Tc token

┌─────────────────────────────────────────┐
│ Tc Token (User token, aud=Blueprint)    │
├─────────────────────────────────────────┤
│ {                                       │
│   "aud": "api://blueprint-app-id",      │
│   "sub": "user-id...",                  │
│   "upn": "user@example.com",            │
│   ...                                   │
│ }                                       │
└─────────────────────────────────────────┘

Step 3: Getting T2 for Azure OpenAI...
✓ Got T2 for Azure OpenAI

┌─────────────────────────────────────────────────────┐
│ T2 Token (Azure OpenAI, aud=cognitiveservices)      │
├─────────────────────────────────────────────────────┤
│ {                                                   │
│   "aud": "https://cognitiveservices.azure.com",     │
│   "appid": "agent-identity-app-id",                 │
│   "upn": "user@example.com",                        │
│   ...                                               │
│ }                                                   │
└─────────────────────────────────────────────────────┘

Token Summary
┌──────────────────┬─────────────────────┬──────────────────┬─────────────┬────────┐
│ Token            │ Audience (aud)      │ Subject (sub)    │ App ID      │ Status │
├──────────────────┼─────────────────────┼──────────────────┼─────────────┼────────┤
│ Tc (User)        │ api://blueprint...  │ user@example.com │ graph-cli   │ ✓      │
│ T2 (Azure OpenAI)│ cognitiveservices   │ user@example.com │ agent-id    │ ✓      │
│ T2 (MCP Server)  │ api://mcp-server... │ user@example.com │ agent-id    │ ✓      │
└──────────────────┴─────────────────────┴──────────────────┴─────────────┴────────┘
```

This is useful for:
- **Debugging**: Verify tokens have correct audiences and claims
- **Understanding OBO**: See how user identity flows through the token chain
- **Verifying permissions**: Check that appid matches your Agent Identity

## MCP Tool Integration

### Without Authentication (Test Mode)

In test mode, MCP servers are connected without authentication. Use this for local MCP servers that don't require auth.

### With OBO Authentication (Production Mode)

In production mode, the MCP client automatically includes the OBO token as a Bearer token in all requests to MCP servers. This allows an AI Gateway to:

1. **Validate the Agent Identity** (`appid` claim in T2)
2. **Validate the User Identity** (`upn`, `name`, `oid` claims in T2)
3. **Check permissions and scopes** (`scp` claim)
4. **Maintain audit trail** of which agent did what for which user

### Adding an MCP Server

From the interactive menu, select option 3:

```
Server name: my-mcp-server
SSE URL: http://localhost:3000/sse

Connecting to my-mcp-server...
✓ MCP server 'my-mcp-server' added and connected!
Found 5 tool(s)
```

## Security Notes

- Authentication tokens are cached locally in `~/.ai-agent-cli-tokens.json`
- MCP server configurations are stored in `~/.ai-agent-cli.json`
- Blueprint client secrets should be protected (use environment variables, not config files)
- Use `logout` command to clear cached tokens
- In production, the OBO token provides a complete audit trail

## Module Structure

```
ai-agent-cli/
├── agent_cli/
│   ├── __init__.py
│   ├── main.py          # CLI entry point & interactive menu
│   ├── auth.py          # Device code flow & OBO token exchange
│   ├── config.py        # Configuration management
│   ├── models.py        # Data classes
│   ├── agent.py         # Azure OpenAI agent with tool calling
│   └── mcp_client.py    # MCP SSE client with Bearer auth
├── env.example
├── requirements.txt
└── README.md
```

## Troubleshooting

### "OBO exchange failed: AADSTS65001"

**Cause**: Admin consent not granted for the Agent Identity.

**Solution**: Grant admin consent for the Agent Identity to access the required resources. See `OBO-GUIDE.md` for instructions.

### "T1 token request failed"

**Cause**: Invalid Blueprint credentials or configuration.

**Solution**: Verify `BLUEPRINT_APP_ID` and `BLUEPRINT_CLIENT_SECRET` are correct.

### "OBO exchange failed: AADSTS65001" for MCP Server

**Cause**: The Agent Identity hasn't been granted permission to request tokens for the MCP Server.

**Solution**: Grant the Agent Identity permission to call the MCP Server API:

```bash
# In entra-agent-cli directory
python -m agent_cli.main grant-agent-mcp-permission "Interactive Agent" "<MCP_SERVER_APP_ID>"
```

This creates an admin consent grant allowing the Agent Identity to request OBO tokens with the MCP Server as the audience.

### "Failed to connect to MCP server: Unauthorized"

**Cause**: MCP server/gateway rejected the Bearer token.

**Solution**: Ensure the gateway is configured to accept tokens from the Agent Identity.
