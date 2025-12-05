

Use powershell graph client to create a blueprint

```bash
$tenantId = "<tenant-id-here>"
$blueprintName = "My Agent Identity Blueprint"

Connect-MgGraph -Scopes "AgentIdentityBlueprint.AddRemoveCreds.All","AgentIdentityBlueprint.Create","DelegatedPermissionGrant.ReadWrite.All","Application.Read.All","AgentIdentityBlueprintPrincipal.Create","User.Read" -TenantId $tenantId

Get-MgContext

$me = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/me"
$myUserId = $me.id
Write-Host "Your User ID: $myUserId"

# Create the blueprint
$body = @{
    "@odata.type" = "Microsoft.Graph.AgentIdentityBlueprint"
    displayName = $blueprintName
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

List all blueprints:

```bash
# List all blueprint APPLICATIONS
$blueprints = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/beta/applications/graph.agentIdentityBlueprint"

$blueprints.value | Select-Object displayName, appId, id | Format-Table
```

List all blueprint principals:

```bash
# List all blueprint principals
$principals = Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/beta/servicePrincipals/graph.agentIdentityBlueprintPrincipal"

# Display them
$principals.value | Select-Object displayName, appId, id | Format-Table
```

Create a client secret for the blueprint we just created:

```bash
# Find the blueprint application
$blueprintApp = (Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/beta/applications?`$filter=appId eq '$blueprintAppId'").value[0]

# Add a client secret (for testing only - use certificates/FIC in production!)
$secretBody = @{
    passwordCredential = @{
        displayName = "Agent Identity Creation Secret"
    }
}

$secret = Invoke-MgGraphRequest -Method POST `
    -Uri "https://graph.microsoft.com/beta/applications/$($blueprintApp.id)/addPassword" `
    -Body ($secretBody | ConvertTo-Json)

Write-Host "✅ Client secret created!"
Write-Host "Secret Value: $($secret.secretText)"  # Save this! You won't see it again
```

Creating blueprints only needs to be done once to create agent identities from the blueprint. 
If you want a different blueprint, you'll need to create a new blueprint. 

Save the secret and you can use it to get a blueprint access token which allows to create agent identities. 

Once we create agent identities, we still need this client secret to get the T1 token. 

```bash
# Your blueprint details
$tenantId = "<tenant-id-here>"
$blueprintAppId = $blueprint.appId    # From when you created the blueprint
$clientSecret = $secret.secretText     # From the password you just added

# Your user ID (for sponsor/owner)
$myUserId = $me.id

# Display to verify
Write-Host "Tenant ID: $tenantId"
Write-Host "Blueprint App ID: $blueprintAppId"
Write-Host "User ID: $myUserId"
```

Now get the blueprint access token. This is for the blueprint client to create agent identities. 

```bash
$tokenBody = @{
    client_id     = $blueprintAppId
    scope         = "https://graph.microsoft.com/.default"
    grant_type    = "client_credentials"
    client_secret = $clientSecret
}

$tokenResponse = Invoke-RestMethod -Method POST `
    -Uri "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token" `
    -ContentType "application/x-www-form-urlencoded" `
    -Body $tokenBody

$blueprintToken = $tokenResponse.access_token
Write-Host "✅ Got blueprint access token (length: $($blueprintToken.Length))"
```

Here's what the token looks like:

```json
{
  "aud": "https://graph.microsoft.com",
  "iss": "https://sts.windows.net/<tenant-id-here>/",
  "iat": 1764881919,
  "nbf": 1764881919,
  "exp": 1764885819,
  "aio": "k2JgYNiYOzvStP+9vMX5knMPWjnLAA==",
  "app_displayname": "My Agent Identity Blueprint",
  "appid": "<blueprint-client-id-here>",
  "appidacr": "1",
  "idp": "https://sts.windows.net/<tenant-id-here>/",
  "idtyp": "app",
  "oid": "241316bd-a01d-411a-b8bc-39ff7a9ef8da",
  "rh": "1.AXgAZoF9XnZ4VUehpLR21KNE9gMAAAAAAAAAwAAAAAAAAAB4AAB4AA.",
  "roles": [
    "AgentIdentity.CreateAsManager"
  ],
  "sub": "241316bd-a01d-411a-b8bc-39ff7a9ef8da",
  "tenant_region_scope": "NA",
  "tid": "<tenant-id-here>",
  "uti": "8hpd54jqCEueln0eWkgWAA",
  "ver": "1.0",
  "wids": [
    "0997a1d0-0d1d-4acb-b408-d5ca73121e90"
  ],
  "xms_acd": 1764880353,
  "xms_act_fct": "9 3",
  "xms_ftd": "vvWYl9xd63PnrWG1YtjLvClWg1IYRfP7c5Jt96Xu6SIBdXNlYXN0LWRzbXM",
  "xms_idrel": "7 6",
  "xms_rd": "0.42LlYBJirBAS4WAXEtgpkil0m2md96SyRUYa3-PvAUU5hQTOextEiVqcc1m_tM_Y8bGfClCUQ0iAmQECDkBpAA",
  "xms_sub_fct": "9 3",
  "xms_tcdt": 1657299251,
  "xms_tnt_fct": "2 3"
}
```

Create the agent identity:

```bash
$agentIdentityBody = @{
    displayName = "My Test Agent"
    agentIdentityBlueprintId = $blueprintAppId
    "sponsors@odata.bind" = @(
        "https://graph.microsoft.com/v1.0/users/$myUserId"
    )
}

$agentIdentity = Invoke-RestMethod -Method POST `
    -Uri "https://graph.microsoft.com/beta/serviceprincipals/Microsoft.Graph.AgentIdentity" `
    -Headers @{
        "Authorization" = "Bearer $blueprintToken"
        "OData-Version" = "4.0"
        "Content-Type"  = "application/json"
    } `
    -Body ($agentIdentityBody | ConvertTo-Json)

Write-Host "✅ Agent Identity created!"
Write-Host "Agent Identity ID: $($agentIdentity.id)"
Write-Host "Agent Identity AppId: $($agentIdentity.appId)"
```

Verify the agent identity was created:

```bash
# List all agent identities using the dedicated endpoint
$agentIdentities = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/beta/servicePrincipals/graph.agentIdentity"

$agentIdentities.value | Select-Object displayName, appId, id | Format-Table
$agentIdentityAppId = $agentIdentity.appId   # Agent Identity's App ID
```

Now, to get the agent identity's token, we need to do the special impersonation dance, first getting Token T1

```bash
# Step 1: Get blueprint token with fmi_path pointing to agent identity
$t1Body = @{
    client_id     = $blueprintAppId
    scope         = "api://AzureADTokenExchange/.default"
    grant_type    = "client_credentials"
    client_secret = $clientSecret
    fmi_path      = $agentIdentityAppId
}

$t1Response = Invoke-RestMethod -Method POST `
    -Uri "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token" `
    -ContentType "application/x-www-form-urlencoded" `
    -Body $t1Body

$blueprintToken = $t1Response.access_token
Write-Host "✅ Got blueprint token (T1) - length: $($blueprintToken.Length)"
```

Now we have T1.

```json
{
  "aud": "fb60f99c-7a34-4190-8149-302f77469936",
  "iss": "https://login.microsoftonline.com/<tenant-id-here>/v2.0",
  "iat": 1764882202,
  "nbf": 1764882202,
  "exp": 1764886102,
  "aio": "k2JgYLhuuvqxunqsRcXNXBH5xPpnJrsNgydx1t67nvQqIun3/C0A",
  "azp": "<blueprint-client-id-here>",
  "azpacr": "1",
  "idtyp": "app",
  "oid": "241316bd-a01d-411a-b8bc-39ff7a9ef8da",
  "rh": "1.AXgAZoF9XnZ4VUehpLR21KNE9pz5YPs0epBBgUkwL3dGmTZ4AAB4AA.",
  "sub": "/eid1/c/pub/t/ZoF9XnZ4VUehpLR21KNE9g/a/gXbsYAjY9EiYcfq4d6lVXQ/58326923-8cbc-4ef2-a30b-9c2a9684dbb1",
  "tid": "<tenant-id-here>",
  "uti": "FnxYV08LCU2Y3sALWaoJAA",
  "ver": "2.0",
  "xms_act_fct": "3 9",
  "xms_ficinfo": "CAAQABgAIAAoAjAA",
  "xms_ftd": "IbqC0S9UqVh-pRjI9iSZRkR2FiC6whGwbdnFZMUtL3oBdXNlYXN0LWRzbXM",
  "xms_idrel": "7 24",
  "xms_sub_fct": "3 9"
}
```

Now we can exchange that for the Agent's token:

```bash
# Step 2: Exchange T1 for agent identity token (T2)
$t2Body = @{
    client_id              = $agentIdentityAppId
    scope                  = "https://graph.microsoft.com/.default"
    grant_type             = "client_credentials"
    client_assertion_type  = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
    client_assertion       = $blueprintToken
}

$t2Response = Invoke-RestMethod -Method POST `
    -Uri "https://login.microsoftonline.com/$tenantId/oauth2/v2.0/token" `
    -ContentType "application/x-www-form-urlencoded" `
    -Body $t2Body

$agentToken = $t2Response.access_token
Write-Host "✅ Got agent identity token (T2) - length: $($agentToken.Length)"
```

Now we have the token (T2).

```bash
Write-Host $agentToken  
```


```json
{
  "aud": "https://graph.microsoft.com",
  "iss": "https://sts.windows.net/<tenant-id-here>/",
  "iat": 1764882257,
  "nbf": 1764882257,
  "exp": 1764886157,
  "aio": "ASQA2/8aAAAAg3+p9I3XdggaOE/Y+1CJSedUqbrC1xHbMjc9pVm5m6M=",
  "app_displayname": "My Test Agent",
  "appid": "58326923-8cbc-4ef2-a30b-9c2a9684dbb1",
  "appidacr": "2",
  "idp": "https://sts.windows.net/<tenant-id-here>/",
  "idtyp": "app",
  "oid": "58326923-8cbc-4ef2-a30b-9c2a9684dbb1",
  "rh": "1.AXgAZoF9XnZ4VUehpLR21KNE9gMAAAAAAAAAwAAAAAAAAAB4AAB4AA.",
  "sub": "58326923-8cbc-4ef2-a30b-9c2a9684dbb1",
  "tenant_region_scope": "NA",
  "tid": "<tenant-id-here>",
  "uti": "86th2zBy30WF_ImYQCUxAA",
  "ver": "1.0",
  "wids": [
    "0997a1d0-0d1d-4acb-b408-d5ca73121e90"
  ],
  "xms_act_fct": "3 11 9",
  "xms_ftd": "hT4aI0eAZTDOyxTVHCSlvIAXiTZtrt4bRxCx0z_IaLQBdXNub3J0aC1kc21z",
  "xms_idrel": "7 8",
  "xms_par_app_azp": "<blueprint-client-id-here>",
  "xms_rd": "0.42LlYBJirBAS4WAXEkgX5EufwfPbZ9Wm6rzMugtvgKKcQgLnvQ2iRC3Ouaxf2mfs-NhPBSjKISTAzAABB6C0FB8HlxCXobmZiYWFkZGBEQA",
  "xms_sub_fct": "3 11 9",
  "xms_tcdt": 1657299251,
  "xms_tnt_fct": "6 3"
}
```