# Testing User OBO Flows with Entra Agent ID SDK on Kubernetes

This guide walks through testing On-Behalf-Of (OBO) flows with the Microsoft Entra Agent ID SDK. You'll create a test user, implement a device code flow client, and exchange user tokens for downstream API access via agent identities.


## Step 2: Expose an API on Your Blueprint

Using Beta Graph API:

```bash
# Install the beta module if not already installed
Install-Module Microsoft.Graph.Beta -Scope CurrentUser

# Import the beta module
Import-Module Microsoft.Graph.Beta.Applications

# Make sure to connect with these perms
Connect-MgGraph -Scopes @(
    "AgentIdentityBlueprint.ReadWrite.All",
    "Application.ReadWrite.All"
)
```

The Blueprint must expose an API so users can request tokens for it. This is **required** for OBO flows.

### Using Microsoft Graph PowerShell

```powershell
# Your Blueprint's Client ID
$blueprintClientId = "<your-blueprint-client-id>"


# Get the Blueprint application object
$blueprintApp = Get-MgApplication -Filter "appId eq '$blueprintClientId'"
$blueprintAppObjectId = $blueprintApp.Id

Write-Host "Blueprint Object ID: $blueprintAppObjectId"

# Step 2a: Set the Application ID URI
$appIdUri = "api://$blueprintClientId"


# Use the beta cmdlet
Update-MgBetaApplication -ApplicationId $blueprintAppObjectId -IdentifierUris @($appIdUri)

Write-Host "✅ Set App ID URI to: $appIdUri"

# Step 2b: Add the 'access_as_user' scope
$newScopeId = (New-Guid).Guid

$apiSettings = @{
    Oauth2PermissionScopes = @(
        @{
            Id = $newScopeId
            AdminConsentDescription = "Allow the application to access the agent on behalf of the signed-in user"
            AdminConsentDisplayName = "Access agent as user"
            IsEnabled = $true
            Type = "User"
            UserConsentDescription = "Allow the application to access the agent on your behalf"
            UserConsentDisplayName = "Access agent as user"
            Value = "access_as_user"
        }
    )
}

Update-MgBetaApplication -ApplicationId $blueprintAppObjectId -Api $apiSettings

Write-Host "✅ Added 'access_as_user' scope"
Write-Host "Full scope: api://$blueprintClientId/access_as_user"
```



### Test OBO with Agent Identity Impersonation

> **Note**: The sidecar does NOT perform the Agent OBO flow automatically. You must implement this manually using the OAuth 2.0 token exchange protocol as documented in [Agent OAuth flows: On behalf of flow](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/agent-on-behalf-of-oauth-flow).

The Agent OBO flow requires three tokens:
- **Tc**: User access token (audience = Blueprint)
- **T1**: Blueprint impersonation token (obtained via `fmi_path` pointing to agent identity)
- **T2**: Final resource token (obtained via OBO exchange using both Tc and T1)

#### Step 1: Set Your Variables

```powershell

# Or import from a variable file
. "$PWD/variables.ps1"

# The resource you want to access (e.g., Microsoft Graph)
$targetScope = "https://graph.microsoft.com/.default"
```

#### Step 2: Get User Token (Tc)

Get a user token with the Blueprint as the audience:

```powershell
# Option A: Using Azure CLI (interactive)
az logout
az login --tenant $tenantId --scope "api://$blueprintClientId/access_as_user"

$userToken = az account get-access-token --resource "api://$blueprintClientId" --query accessToken -o tsv

Write-Host "✅ Got user token (Tc) - length: $($userToken.Length)"
```

#### Step 3: Get Blueprint Impersonation Token (T1)

Request a token from the Blueprint with `fmi_path` pointing to the agent identity:

```powershell
# Step 3: Get blueprint token with fmi_path pointing to agent identity
$t1Body = @{
    client_id     = $blueprintClientId
    scope         = "api://AzureADTokenExchange/.default"
    grant_type    = "client_credentials"
    client_secret = $blueprintClientSecret
    fmi_path      = $agentIdentityAppId
}

$t1Response = Invoke-RestMethod -Method POST `
    -Uri "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token" `
    -ContentType "application/x-www-form-urlencoded" `
    -Body $t1Body

$blueprintToken = $t1Response.access_token
Write-Host "✅ Got blueprint impersonation token (T1) - length: $($blueprintToken.Length)"
```

> **Important**: In production, use managed identity or certificate instead of client secret:
> ```powershell
> # Using managed identity as FIC (recommended for production)
> $t1Body = @{
>     client_id        = $blueprintClientId
>     scope            = "api://AzureADTokenExchange/.default"
>     grant_type       = "client_credentials"
>     client_assertion_type = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
>     client_assertion = $managedIdentityToken  # TUAMI
>     fmi_path         = $agentIdentityAppId
> }
> ```

#### Mid Step: Grant Admin Consent for Agent Identity

Agent Identities can't prompt users for consent (no redirect URIs), so you must grant admin consent before the OBO exchange will work. Without this, you'll get error `AADSTS65001: consent_required`.

This is required only once. Don't need to do for each call.

```powershell
Connect-MgGraph -Scopes "Application.ReadWrite.All", "DelegatedPermissionGrant.ReadWrite.All"

# List all agent identities to find yours
$agentIdentities = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/beta/servicePrincipals/graph.agentIdentity"

# Show them (Agent Identities use 'id' not 'appId')
$agentIdentities.value | Select-Object displayName, id | Format-Table

# Set your Agent Identity's ID
$agentIdentityId = "58326923-8cbc-4ef2-a30b-9c2a9684dbb1"

# Get the Microsoft Graph service principal
$graphSp = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/servicePrincipals?`$filter=appId eq '00000003-0000-0000-c000-000000000000'"

$graphSpId = $graphSp.value[0].id
Write-Host "Graph Service Principal ID: $graphSpId"

# Grant admin consent for delegated permissions
# This creates an OAuth2PermissionGrant (admin consent for all users in tenant)
$consentBody = @{
    clientId    = $agentIdentityId       # The Agent Identity's ID
    consentType = "AllPrincipals"        # Admin consent for all users
    resourceId  = $graphSpId             # Microsoft Graph
    scope       = "User.Read openid profile offline_access"  # Scopes needed for OBO
} | ConvertTo-Json

Invoke-MgGraphRequest -Method POST `
    -Uri "https://graph.microsoft.com/v1.0/oauth2PermissionGrants" `
    -Body $consentBody `
    -ContentType "application/json"

Write-Host "✅ Admin consent granted for Agent Identity"
```

> **Note**: You only need to do this once per Agent Identity. Add more scopes to the `scope` field if your agent needs additional permissions (e.g., `Mail.Read`, `Calendars.Read`).

#### Step 4: OBO Exchange for Resource Token (T2)

Now perform the OBO exchange using both T1 (as client assertion) and Tc (as assertion):

```powershell
# Step 4: OBO exchange - Agent Identity requests resource token
$t2Body = @{
    client_id              = $agentIdentityAppId
    scope                  = $targetScope
    client_assertion_type  = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
    client_assertion       = $blueprintToken  # T1
    grant_type             = "urn:ietf:params:oauth:grant-type:jwt-bearer"
    assertion              = $userToken       # Tc
    requested_token_use    = "on_behalf_of"
}

$t2Response = Invoke-RestMethod -Method POST `
    -Uri "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token" `
    -ContentType "application/x-www-form-urlencoded" `
    -Body $t2Body

$resourceToken = $t2Response.access_token
$refreshToken = $t2Response.refresh_token  # Save for async/background scenarios

Write-Host "✅ Got resource token (T2) - length: $($resourceToken.Length)"
Write-Host "✅ Got refresh token - length: $($refreshToken.Length)"
```

#### Step 5: Use the Resource Token

```powershell
# Call Microsoft Graph with the agent identity token
$headers = @{
    "Authorization" = "Bearer $resourceToken"
    "Content-Type"  = "application/json"
}

# Example: Get current user info (the user whose identity we're acting on behalf of)
$graphResponse = Invoke-RestMethod -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/me" `
    -Headers $headers

Write-Host "Acting on behalf of: $($graphResponse.displayName) ($($graphResponse.userPrincipalName))"
```

#### Using Refresh Token (for Async/Background Scenarios)

```powershell
# Refresh the token when needed (no user interaction required)
$refreshBody = @{
    client_id              = $agentIdentityAppId
    scope                  = $targetScope
    client_assertion_type  = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
    client_assertion       = $blueprintToken  # T1 (may need to be refreshed first)
    grant_type             = "refresh_token"
    refresh_token          = $refreshToken
}

$refreshResponse = Invoke-RestMethod -Method POST `
    -Uri "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token" `
    -ContentType "application/x-www-form-urlencoded" `
    -Body $refreshBody

$newResourceToken = $refreshResponse.access_token
Write-Host "✅ Refreshed resource token - length: $($newResourceToken.Length)"
```

#### Complete Script

Here's a complete script you can save and run:

```powershell
# agent-obo-flow.ps1
param(
    [Parameter(Mandatory=$true)][string]$TenantId,
    [Parameter(Mandatory=$true)][string]$BlueprintClientId,
    [Parameter(Mandatory=$true)][string]$agentIdentityAppId,
    [Parameter(Mandatory=$true)][string]$BlueprintClientSecret,
    [string]$TargetScope = "https://graph.microsoft.com/.default"
)

Write-Host "=== Agent Identity OBO Flow ===" -ForegroundColor Cyan

# Step 1: Get user token via Azure CLI
Write-Host "`n[1/4] Getting user token (Tc)..." -ForegroundColor Yellow
$userToken = az account get-access-token --resource "api://$BlueprintClientId" --query accessToken -o tsv
if (-not $userToken) {
    Write-Host "❌ Failed to get user token. Run: az login --tenant $TenantId --scope api://$BlueprintClientId/access_as_user" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Got user token (Tc)" -ForegroundColor Green

# Step 2: Get blueprint impersonation token (T1)
Write-Host "`n[2/4] Getting blueprint impersonation token (T1)..." -ForegroundColor Yellow
$t1Body = @{
    client_id     = $BlueprintClientId
    scope         = "api://AzureADTokenExchange/.default"
    grant_type    = "client_credentials"
    client_secret = $BlueprintClientSecret
    fmi_path      = $agentIdentityAppId
}

try {
    $t1Response = Invoke-RestMethod -Method POST `
        -Uri "https://login.microsoftonline.com/$TenantId/oauth2/v2.0/token" `
        -ContentType "application/x-www-form-urlencoded" `
        -Body $t1Body
    $blueprintToken = $t1Response.access_token
    Write-Host "✅ Got blueprint token (T1)" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to get T1: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Step 3: OBO exchange for resource token (T2)
Write-Host "`n[3/4] Performing OBO exchange for resource token (T2)..." -ForegroundColor Yellow
$t2Body = @{
    client_id              = $agentIdentityAppId
    scope                  = $TargetScope
    client_assertion_type  = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
    client_assertion       = $blueprintToken
    grant_type             = "urn:ietf:params:oauth:grant-type:jwt-bearer"
    assertion              = $userToken
    requested_token_use    = "on_behalf_of"
}

try {
    $t2Response = Invoke-RestMethod -Method POST `
        -Uri "https://login.microsoftonline.com/$TenantId/oauth2/v2.0/token" `
        -ContentType "application/x-www-form-urlencoded" `
        -Body $t2Body
    $resourceToken = $t2Response.access_token
    Write-Host "✅ Got resource token (T2)" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed OBO exchange: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host $_.ErrorDetails.Message -ForegroundColor Red
    exit 1
}

# Step 4: Test the token
Write-Host "`n[4/4] Testing token against Microsoft Graph..." -ForegroundColor Yellow
$headers = @{ "Authorization" = "Bearer $resourceToken" }

try {
    $me = Invoke-RestMethod -Method GET -Uri "https://graph.microsoft.com/v1.0/me" -Headers $headers
    Write-Host "✅ Success! Acting on behalf of: $($me.displayName) ($($me.userPrincipalName))" -ForegroundColor Green
} catch {
    Write-Host "❌ Graph call failed: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host "`n=== Token Summary ===" -ForegroundColor Cyan
Write-Host "User Token (Tc): $($userToken.Substring(0,50))..."
Write-Host "Blueprint Token (T1): $($blueprintToken.Substring(0,50))..."
Write-Host "Resource Token (T2): $($resourceToken.Substring(0,50))..."
```

Run it with:
```powershell
.\agent-obo-flow.ps1 `
    -TenantId "your-tenant-id" `
    -BlueprintClientId "your-blueprint-client-id" `
    -agentIdentityAppId "your-agent-identity-client-id" `
    -BlueprintClientSecret "your-secret"
```

---

## Understanding the Token Flow

### Standard OBO (Without Agent Identity)

```
User → [Device Code] → User Token (aud=Blueprint)
                              ↓
                        Sidecar validates
                              ↓
                        OBO Exchange
                              ↓
                        Graph Token (user's identity)
```

### OBO with Agent Identity Impersonation

> **Note**: The sidecar does NOT perform Agent OBO automatically. You must implement the T1/T2 exchange yourself (see "Test OBO with Agent Identity Impersonation" section above).

```
User → [Device Code] → User Token (aud=Blueprint, Tc)
                              ↓
                        YOUR CODE gets T1 from Entra
                        (Blueprint + fmi_path → T1)
                              ↓
                        YOUR CODE does OBO exchange
                        (Tc + T1 → T2)
                              ↓
                        Graph Token (agent's identity, acting for user)
```

As documented in the [Agent OAuth flows](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/agent-on-behalf-of-oauth-flow):

> "The OBO protocol requires token audience to match the client ID:
> - T1 (aud) == Agent identity Parent app == Agent identity blueprint client ID
> - Tc (aud) == Agent identity blueprint client ID"

---

## Troubleshooting

### "Audience validation failed"

**Cause**: User token has wrong audience.

**Solution**: Ensure the scope requested includes your Blueprint's App ID URI:
```bash
--scope "api://<blueprint-client-id>/access_as_user"
```

### "AADSTS65001: The user or administrator has not consented"

**Cause**: Missing consent for the Agent Identity to access resources on behalf of users.

**Solution for Agent Identities**: Agent Identities can't prompt for user consent (no redirect URIs), so you must grant admin consent. See the "Mid Step: Grant Admin Consent for Agent Identity" section above.

**Solutions for other apps**:
1. User consent: The user will be prompted on first login
2. Admin consent: Grant via PowerShell or Azure Portal
3. Check the app has the required delegated permissions configured

### "AADSTS700016: Application not found"

**Cause**: Client ID is incorrect or app doesn't exist in the tenant.

**Solution**: Verify the PUBLIC_CLIENT_ID and that the app exists in your tenant.

### "Connection refused" to sidecar

**Cause**: Sidecar isn't running or isn't accessible.

**Solution**:
```bash
# Check sidecar logs
kubectl logs deployment/demo-app -c sidecar -n entra-demo

# Test health endpoint
kubectl exec -it deployment/demo-app -c client -n entra-demo -- \
  curl http://localhost:5000/healthz -H "Host: localhost"
```

### Token cache issues

**Cause**: Cached token expired or corrupted.

**Solution**:
```bash
# Clear the token cache
rm /app/cache/token_cache.bin
```

---

## References

- [Microsoft Entra SDK for AgentID - Python Quickstart](https://learn.microsoft.com/en-us/entra/msidweb/agent-id-sdk/quickstart-python)
- [Agent OAuth flows: On behalf of flow](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/agent-on-behalf-of-oauth-flow)
- [OAuth 2.0 On-Behalf-Of flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow)
- [Microsoft Identity Web Sidecar README](./src/Microsoft.Identity.Web.Sidecar/README.md)
- [Python Sidecar Client](./tests/DevApps/SidecarAdapter/python/README.md)

---

## Quick Reference Commands

### Sidecar Commands (Standard OBO - User Identity)

```bash
# Validate token
curl -s "http://localhost:5000/Validate" -H "Authorization: Bearer $TOKEN" -H "Host: localhost"

# OBO to Graph (as user) - sidecar handles OBO
curl -s -X POST "http://localhost:5000/DownstreamApi/graph" -H "Authorization: Bearer $TOKEN" -H "Host: localhost"

# App-only call (Blueprint identity, no user)
curl -s -X POST "http://localhost:5000/DownstreamApiUnauthenticated/graph" -H "Host: localhost"

# Get auth header for Blueprint's app identity
curl -s "http://localhost:5000/AuthorizationHeaderUnauthenticated/graph"
```

### Agent Identity OBO (Manual - Sidecar Does NOT Support This)

```powershell
# The sidecar AgentIdentity parameter does NOT perform the full Agent OBO flow.
# You must implement T1/T2 exchange manually. See "Test OBO with Agent Identity Impersonation" above.

# Quick summary:
# 1. Get Tc (user token with aud=Blueprint)
$userToken = az account get-access-token --resource "api://$BLUEPRINT_CLIENT_ID" --query accessToken -o tsv

# 2. Get T1 (Blueprint impersonation token)
# POST to /oauth2/v2.0/token with fmi_path=$AGENT_IDENTITY_CLIENT_ID

# 3. Get T2 (Resource token via OBO)
# POST to /oauth2/v2.0/token with grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer
```

