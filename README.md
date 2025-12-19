# Creating Agent Identity for Kubernetes

Before we do anything, we need to configure a client that can create an Agent Identity Blueprint. Once we have that, we can create as many Blueprints as we want.  

See [creating a blueprint](./BLUEPRINT-CREATION-POWERSHELL.md)



## Set up powershell
```bash
brew install powershell/tap/powershell
```
```bash
pwsh
```

```bash
# Install the Microsoft Graph module (this may take a few minutes)
Install-Module Microsoft.Graph -Scope CurrentUser -Repository PSGallery -Force
```

```bash
# Connect with more priv
Connect-MgGraph -Scopes "RoleManagement.ReadWrite.Directory","Directory.ReadWrite.All","AgentIdentityBlueprint.ReadWrite.All"


# Check that you're connected and have the right permissions
Get-MgContext

# Get your user ID
$me = Get-MgUser -UserId "christian.posta@solo.io"
$myUserId = $me.Id
Write-Host "Your User ID: $myUserId"

```

# Deploy to Kubernetes

Copy env.example to .env (and fill in proper variables)
Then go deploy to k8s with envsub:

```bash
cp env.example .env
cd kubernetes
./deploy.sh
```

## Quick Scripts

Get my user token with scopes for blueprint:

```bash
BLUEPRINT_CLIENT_ID=<id-here>
az logout
az login --tenant "5e7d8166-7876-4755-a1a4-b476d4a344f6" --scope "api://$BLUEPRINT_CLIENT_ID/access_as_user"
TOKEN=$(az account get-access-token --resource "api://$BLUEPRINT_CLIENT_ID" --query accessToken -o tsv)
echo $TOKEN
```


## Digging into Roles

List all Azure RBAC Providers:

```bash
# List all Azure providers
az provider list --output table


# List all "operations" on a specific provider / show data operations:
az provider operation list \
  --query "[?name=='Microsoft.Storage'].resourceTypes[].operations[].{Name:name, IsDataAction:isDataAction, Description:description}" \
  --output table


# List all "app roles" for Graph
az rest --method GET \
  --url "https://graph.microsoft.com/v1.0/servicePrincipals?\$filter=appId eq '00000003-0000-0000-c000-000000000000'" \
  --query "value[0].appRoles[].{Value:value, DisplayName:displayName}" \
  --output table
```