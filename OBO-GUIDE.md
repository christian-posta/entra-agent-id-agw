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

### Getting User Access Token

You can login with the right scopes and get the token:

```bash
az logout
az login --tenant "5e7d8166-7876-4755-a1a4-b476d4a344f6" --scope "api://60ec7681-d808-48f4-9871-fab877a9555d/access_as_user"
TOKEN=$(az account get-access-token --resource "api://$BLUEPRINT_CLIENT_ID" --query accessToken -o tsv)
echo $TOKEN
```

### Test OBO with Agent Identity Impersonation

```bash
# Inside the client container
AGENT_IDENTITY_ID="<agent-identity-client-id>"

# Call Graph with OBO, impersonating the agent identity
# The sidecar will:
# 1. Validate your user token (aud=blueprint)
# 2. Use blueprint credentials to impersonate the agent identity
# 3. Do OBO exchange: user token + impersonation → Graph token
curl -s -X POST "http://localhost:5000/DownstreamApi/graph?AgentIdentity=$AGENT_IDENTITY_ID" \
  -H "Host: localhost" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json"

# Using the Python client
python main.py \
  --base-url http://localhost:5000 \
  --authorization-header "Bearer $TOKEN" \
  --agent-identity "$AGENT_IDENTITY_ID" \
  invoke-downstream graph
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

```
User → [Device Code] → User Token (aud=Blueprint, Tc)
                              ↓
                        Sidecar validates Tc
                              ↓
                        Blueprint gets impersonation token (T1)
                        (using FIC/certificate/secret)
                              ↓
                        OBO Exchange: Tc + T1
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

**Cause**: Missing consent for the scope.

**Solutions**:
1. User consent: The user will be prompted on first login
2. Admin consent: Grant via PowerShell or admin center
3. Check the public client app has the permission configured

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

```bash
# Get user token (device code flow)
TOKEN=$(python get_token_device.py \
  --client-id "$PUBLIC_CLIENT_ID" \
  --authority "https://login.microsoftonline.com/$TENANT_ID" \
  --scope "api://$BLUEPRINT_CLIENT_ID/access_as_user")

# Validate token
curl -s "http://localhost:5000/Validate" -H "Authorization: Bearer $TOKEN" -H "Host: localhost"

# OBO to Graph (as user)
curl -s -X POST "http://localhost:5000/DownstreamApi/graph" -H "Authorization: Bearer $TOKEN" -H "Host: localhost"

# OBO to Graph (as agent identity)
curl -s -X POST "http://localhost:5000/DownstreamApi/graph?AgentIdentity=$AGENT_ID" -H "Authorization: Bearer $TOKEN" -H "Host: localhost"

# App-only call (no user)
curl -s -X POST "http://localhost:5000/DownstreamApiUnauthenticated/graph" -H "Host: localhost"
```

