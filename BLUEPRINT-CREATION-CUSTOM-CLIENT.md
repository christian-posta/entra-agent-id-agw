# How to Create an Agent Identity Blueprint via Graph API

This guide documents the steps required to programmatically create a Microsoft Entra Agent Identity Blueprint using the Graph API and PowerShell.

## Prerequisites

- **Agent ID Administrator** or **Agent ID Developer** role assigned to your user
- PowerShell with Microsoft Graph module installed:
  ```powershell
  Install-Module Microsoft.Graph -Scope CurrentUser -Repository PSGallery -Force
  ```

---

## Step 1: Create a Custom App Registration

1. Go to **Microsoft Entra admin center** → **Identity** → **App registrations**
2. Click **New registration**
3. Name: `Agent Blueprint Client` (or similar)
4. Supported account types: **Accounts in this organizational directory only**
5. Click **Register**
6. Note the **Application (client) ID** and **Directory (tenant) ID**

---

## Step 2: Add Redirect URI

1. In your app → **Authentication** → **Add a platform**
2. Select **Mobile and desktop applications**
3. Check: `https://login.microsoftonline.com/common/oauth2/nativeclient`
4. Click **Save**

---

## Step 3: Grant Permissions Programmatically

The Agent ID permissions aren't visible in the Entra admin center UI, so you must grant them via PowerShell.

### Connect as Admin

```powershell
Connect-MgGraph -Scopes "DelegatedPermissionGrant.ReadWrite.All","AppRoleAssignment.ReadWrite.All","Application.Read.All" -TenantId "<your-tenant-id>"
```

### Get Service Principals

```powershell
$yourAppClientId = "<your-app-client-id>"
$yourAppSp = Get-MgServicePrincipal -Filter "appId eq '$yourAppClientId'"
$graphSp = Get-MgServicePrincipal -Filter "appId eq '00000003-0000-0000-c000-000000000000'"
```

### Grant Delegated Permissions (Required)

```powershell
# AgentIdentityBlueprint.Create - for creating blueprints
New-MgOauth2PermissionGrant -BodyParameter @{
    clientId    = $yourAppSp.Id
    consentType = "AllPrincipals"
    resourceId  = $graphSp.Id
    scope       = "AgentIdentityBlueprint.Create"
}
Write-Host "✅ AgentIdentityBlueprint.Create delegated permission granted"

# AgentIdentityBlueprintPrincipal.Create - for creating blueprint principals
New-MgOauth2PermissionGrant -BodyParameter @{
    clientId    = $yourAppSp.Id
    consentType = "AllPrincipals"
    resourceId  = $graphSp.Id
    scope       = "AgentIdentityBlueprintPrincipal.Create"
}
Write-Host "✅ AgentIdentityBlueprintPrincipal.Create delegated permission granted"
```

### Grant Application Permissions

```powershell
# User.Read.All - for reading user information
$userReadRole = $graphSp.AppRoles | Where-Object { $_.Value -eq "User.Read.All" }
New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $yourAppSp.Id -BodyParameter @{
    principalId = $yourAppSp.Id
    resourceId = $graphSp.Id
    appRoleId = $userReadRole.Id
}
Write-Host "✅ User.Read.All application permission granted"

# Application.ReadWrite.All - for creating/managing applications
$appWriteRole = $graphSp.AppRoles | Where-Object { $_.Value -eq "Application.ReadWrite.All" }
New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $yourAppSp.Id -BodyParameter @{
    principalId = $yourAppSp.Id
    resourceId = $graphSp.Id
    appRoleId = $appWriteRole.Id
}
Write-Host "✅ Application.ReadWrite.All application permission granted"
```

---

## Step 4: Connect Using Your App with Delegated Auth

```powershell
Disconnect-MgGraph

# Connect with DELEGATED auth using YOUR app (not the default Graph CLI)
Connect-MgGraph -ClientId "<your-app-client-id>" -TenantId "<your-tenant-id>" -Scopes "AgentIdentityBlueprint.Create","User.Read"

# Verify connection - should show YOUR app's ClientId and AuthType: Delegated
Get-MgContext
```

---

## Step 5: Create the Agent Identity Blueprint

```powershell
# Get your user ID
$me = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/me"
$myUserId = $me.id
Write-Host "Your User ID: $myUserId"

# Create the blueprint
$body = @{
    "@odata.type" = "Microsoft.Graph.AgentIdentityBlueprint"
    displayName = "My Agent Identity Blueprint"
    "sponsors@odata.bind" = @(
        "https://graph.microsoft.com/v1.0/users/$myUserId"
    )
    "owners@odata.bind" = @(
        "https://graph.microsoft.com/v1.0/users/$myUserId"
    )
}

$blueprint = Invoke-MgGraphRequest -Method POST `
    -Uri "https://graph.microsoft.com/beta/applications/" `
    -Headers @{ "OData-Version" = "4.0" } `
    -Body ($body | ConvertTo-Json)

Write-Host "✅ Blueprint created!"
Write-Host "App ID: $($blueprint.appId)"
Write-Host "Object ID: $($blueprint.id)"

# Save the appId for the next step
$blueprintAppId = $blueprint.appId
```

---

## Step 6: Create the Blueprint Principal

The blueprint principal is required for the blueprint to appear in the Entra admin center UI and to create agent identities from it.

> **Note:** There can be a timing delay after creating the blueprint. Wait a few seconds before creating the principal.

```powershell
# Reconnect with the BlueprintPrincipal.Create permission
Disconnect-MgGraph
Connect-MgGraph -ClientId "<your-app-client-id>" -TenantId "<your-tenant-id>" -Scopes "AgentIdentityBlueprintPrincipal.Create","User.Read"

# Wait a moment (docs mention timing issues between blueprint and principal creation)
Start-Sleep -Seconds 5

# Create the blueprint principal
$principalBody = @{
    appId = $blueprintAppId  # Use the appId from Step 5
}

$principal = Invoke-MgGraphRequest -Method POST `
    -Uri "https://graph.microsoft.com/beta/serviceprincipals/graph.agentIdentityBlueprintPrincipal" `
    -Headers @{ "OData-Version" = "4.0" } `
    -Body ($principalBody | ConvertTo-Json)

Write-Host "✅ Blueprint Principal created!"
Write-Host "Principal ID: $($principal.id)"
```

---

## Step 7: Verify in the UI

After creating both the blueprint and principal:

1. Go to **Microsoft Entra admin center** (https://entra.microsoft.com)
2. Navigate to **Entra ID** → **Agent ID (Preview)** → **Agent identity blueprints**
3. Your blueprint should now be visible

---

## Summary of Permissions

| Permission | Type | Purpose |
|------------|------|---------|
| `AgentIdentityBlueprint.Create` | Delegated | Create agent identity blueprints |
| `AgentIdentityBlueprintPrincipal.Create` | Delegated | Create blueprint principals |
| `User.Read.All` | Application | Read user information |
| `Application.ReadWrite.All` | Application | Create and manage applications |

---

## Complete Script (All Steps Combined)

```powershell
# ============================================
# CONFIGURATION - Update these values
# ============================================
$yourAppClientId = "<your-app-client-id>"
$tenantId = "<your-tenant-id>"
$blueprintName = "My Agent Identity Blueprint"

# ============================================
# STEP 1: Grant Permissions (Run once as admin)
# ============================================
Connect-MgGraph -Scopes "DelegatedPermissionGrant.ReadWrite.All","AppRoleAssignment.ReadWrite.All","Application.Read.All" -TenantId $tenantId

$yourAppSp = Get-MgServicePrincipal -Filter "appId eq '$yourAppClientId'"
$graphSp = Get-MgServicePrincipal -Filter "appId eq '00000003-0000-0000-c000-000000000000'"

# Grant delegated permissions
New-MgOauth2PermissionGrant -BodyParameter @{
    clientId = $yourAppSp.Id; consentType = "AllPrincipals"; resourceId = $graphSp.Id
    scope = "AgentIdentityBlueprint.Create"
}
New-MgOauth2PermissionGrant -BodyParameter @{
    clientId = $yourAppSp.Id; consentType = "AllPrincipals"; resourceId = $graphSp.Id
    scope = "AgentIdentityBlueprintPrincipal.Create"
}

# Grant application permissions
$userReadRole = $graphSp.AppRoles | Where-Object { $_.Value -eq "User.Read.All" }
$appWriteRole = $graphSp.AppRoles | Where-Object { $_.Value -eq "Application.ReadWrite.All" }
New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $yourAppSp.Id -BodyParameter @{
    principalId = $yourAppSp.Id; resourceId = $graphSp.Id; appRoleId = $userReadRole.Id
}
New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $yourAppSp.Id -BodyParameter @{
    principalId = $yourAppSp.Id; resourceId = $graphSp.Id; appRoleId = $appWriteRole.Id
}

Write-Host "✅ All permissions granted"

# ============================================
# STEP 2: Create Blueprint
# ============================================
Disconnect-MgGraph
Connect-MgGraph -ClientId $yourAppClientId -TenantId $tenantId -Scopes "AgentIdentityBlueprint.Create","User.Read"

$me = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/me"
$myUserId = $me.id

$body = @{
    "@odata.type" = "Microsoft.Graph.AgentIdentityBlueprint"
    displayName = $blueprintName
    "sponsors@odata.bind" = @("https://graph.microsoft.com/v1.0/users/$myUserId")
    "owners@odata.bind" = @("https://graph.microsoft.com/v1.0/users/$myUserId")
}

$blueprint = Invoke-MgGraphRequest -Method POST `
    -Uri "https://graph.microsoft.com/beta/applications/" `
    -Headers @{ "OData-Version" = "4.0" } `
    -Body ($body | ConvertTo-Json)

Write-Host "✅ Blueprint created: $($blueprint.appId)"

# ============================================
# STEP 3: Create Blueprint Principal
# ============================================
Start-Sleep -Seconds 5

Disconnect-MgGraph
Connect-MgGraph -ClientId $yourAppClientId -TenantId $tenantId -Scopes "AgentIdentityBlueprintPrincipal.Create","User.Read"

$principal = Invoke-MgGraphRequest -Method POST `
    -Uri "https://graph.microsoft.com/beta/serviceprincipals/graph.agentIdentityBlueprintPrincipal" `
    -Headers @{ "OData-Version" = "4.0" } `
    -Body (@{ appId = $blueprint.appId } | ConvertTo-Json)

Write-Host "✅ Blueprint Principal created: $($principal.id)"
Write-Host ""
Write-Host "🎉 Done! Check Entra admin center → Agent ID → Agent identity blueprints"
```

---

## Key Insights & Troubleshooting

### Why Use a Custom App?

The default "Microsoft Graph Command Line Tools" app accumulates permissions over time, which can cause conflicts. A dedicated app gives you clean, controlled permissions.

### Why Delegated Auth?

App-only (application) authentication does not work for creating Agent Identity Blueprints. You must use delegated authentication with a user context.

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `403: This operation cannot be performed for the specified calling identity type` | Using wrong auth type or missing permission | Use delegated auth, not app-only |
| `403: Authorization_RequestDenied` | Missing required permission | Grant permissions programmatically as shown above |
| `403: Forbidden` when creating principal | Wrong permission | Use `AgentIdentityBlueprintPrincipal.Create`, not `EnableDisable.All` |
| Permission blocked by `Directory.AccessAsUser.All` | Known issue in Agent ID | Remove this permission from your app/session |
| `400: Object with id {id} not found` | Timing issue after creating blueprint | Wait a few seconds before creating the principal |

### Permissions Not in UI

The `AgentIdentityBlueprint.*` and `AgentIdentityBlueprintPrincipal.*` permissions are not visible in the Microsoft Entra admin center permission picker. You must grant them programmatically using `New-MgOauth2PermissionGrant`.

---

## References

- [Create an agent identity blueprint - Microsoft Learn](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/create-blueprint)
- [Agent identity blueprints in Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/agent-blueprint)
- [Microsoft Graph Permissions Reference](https://graphpermissions.merill.net/)
