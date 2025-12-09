# Agent Identity Blueprint CLI

A Python CLI tool for managing Microsoft Entra Agent Identity Blueprints.

## Features

- Create and manage Agent Identity Blueprints
- Create Agent Identities from Blueprints
- Get access tokens for Agent Identities with full token exchange visibility
- Device code flow authentication with **persistent token caching**
- Local configuration file for storing blueprints and credentials

## Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Optional: Install as editable package
pip install -e .
```

## Configuration

### Environment Variables

Copy `env.example` to `.env` and configure:

```bash
cp env.example .env
```

Edit `.env`:
```
TENANT_ID=your-tenant-id-here
```

### Config Files

The CLI uses two config files in your home directory:

| File | Purpose |
|------|---------|
| `~/.agent-identity-cli.json` | Stores blueprints, agent identities, and secrets |
| `~/.agent-identity-cli-tokens.json` | Caches authentication tokens |

## Usage

Run the CLI:

```bash
python -m agent_cli.main --help
```

### Authentication & Token Caching

The CLI caches authentication tokens so you don't need to re-authenticate for every command.

```bash
# Pre-authenticate (optional - commands will prompt if needed)
python -m agent_cli.main login

# Clear cached tokens (logout)
python -m agent_cli.main logout

# Force re-authentication on any command
python -m agent_cli.main list-blueprints --from-graph --force-refresh
```

### Commands

#### List Blueprints

```bash
# List locally stored blueprints
python -m agent_cli.main list-blueprints

# List blueprints from Graph API (uses cached token or prompts for auth)
python -m agent_cli.main list-blueprints --from-graph
```

#### Create a New Blueprint

```bash
python -m agent_cli.main create-new-blueprint "My Agent Blueprint"

# With explicit tenant ID
python -m agent_cli.main create-new-blueprint "My Agent Blueprint" --tenant-id <tenant-id>
```

This will:
1. Authenticate using device code flow (or use cached token)
2. Create the blueprint application
3. Create the blueprint service principal
4. Generate and store a client secret

#### List Agent Identities

```bash
# List locally stored agent identities
python -m agent_cli.main list-agent-identities

# List from Graph API
python -m agent_cli.main list-agent-identities --from-graph
```

#### Create Agent Identity from Blueprint

First, get your user ID:
```bash
az ad signed-in-user show --query id -o tsv
```

Then create the agent identity:
```bash
python -m agent_cli.main create-new-agent-identity-from-blueprint "My Agent" \
    --blueprint "My Agent Blueprint" \
    --sponsor <your-user-id>
```

#### Get Access Token for Agent Identity

```bash
python -m agent_cli.main get-access-token-for-agent-identity "My Agent"

# With custom scope
python -m agent_cli.main get-access-token-for-agent-identity "My Agent" \
    --scope "https://graph.microsoft.com/.default"

# Output the token value
python -m agent_cli.main get-access-token-for-agent-identity "My Agent" --output-token
```

This displays all intermediate tokens:
- **Blueprint Token**: The blueprint's client credentials token
- **T1 Token**: Blueprint token with `fmi_path` pointing to the agent identity
- **T2 Token**: The final agent identity access token

#### Show Configuration

```bash
python -m agent_cli.main config

# Show config file path only
python -m agent_cli.main config --path
```

## Token Exchange Flow

When getting an agent identity token, the CLI performs the following steps:

1. **Blueprint Token** (optional, for display): Standard client credentials token for the blueprint
2. **T1 Token**: Client credentials with `fmi_path` parameter pointing to the agent identity's app ID
3. **T2 Token**: Exchange T1 using `client_assertion` to get the final agent identity token

This mirrors the PowerShell flow documented in `BLUEPRINT-CREATION-POWERSHELL.md`.

## Required Permissions

For creating blueprints, the following Graph API permissions are required:
- `AgentIdentityBlueprint.Create`
- `AgentIdentityBlueprint.AddRemoveCreds.All`
- `AgentIdentityBlueprintPrincipal.Create`
- `DelegatedPermissionGrant.ReadWrite.All`
- `Application.Read.All`
- `User.Read`

For read-only operations (listing), only `Application.Read.All` and `User.Read` are needed.

## Security Notes

- Client secrets are stored in the local config file (`~/.agent-identity-cli.json`)
- Authentication tokens are cached in `~/.agent-identity-cli-tokens.json`
- For production use, consider using certificates or Federated Identity Credentials (FIC) instead of client secrets
- Both config files contain sensitive data - protect them appropriately
- Use `logout` command to clear cached tokens when switching accounts
