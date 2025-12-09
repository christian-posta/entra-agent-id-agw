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