# Microsoft Entra Agent ID on Kubernetes

This is part of a multi-part series where we dig into how Microsoft Entra Agent ID gives an option for agent identity. This set of guides will specifically dive deeply into how it works (it's full token-exchange mechanism) with the goal of getting it working on Kubernetes for Agent and MCP workloads outside of Azure. Azure has managed identities but they work within the Azure ecosystem, but if we want to expand past that, we need to understand how Agent ID works. If you're interested in this, please follow me [/in/ceposta](https://www.linkedin.com/in/ceposta) for updates!

# Part Four: Workload Identity Federation

In the previous post, we saw how to use the [microsoft-web-identity](https://github.com/AzureAD/microsoft-identity-web) sidecar to shield the agent app from doing complex token exchanges and dealing with blueprint's sensitive tokens. But we still had to configure client credentials for the blueprint to get its access tokens. We should never use client credentials in a production environment ([or API keys](https://blog.christianposta.com/api-keys-are-a-bad-idea-for-enterprise-llm-agent-and-mcp-access/)!). Instead of client credentials, let's configure [Workload Identity Federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation). This allows us to use a trusted token already baked into the platform (ie, like a Kubrenetes service-account token) and have Entra trust that. That allows us to get rid of the client credential and seamlessly integrate the Kubernetes workloads / service accounts with an Agent Blueprint. This solves some of the problems from the previous post (Post Three) but not all. We will still need some automation to smooth over the other rough edges.

Let's see how to set up workload identity federation for our `microsoft-web-identity` sidecar. 

## Configuring Workload Identity Federation for Agent Blueprint

This post walks through configuring workload identity federation to eliminate client secrets when using the Entra SDK sidecar with Agent Blueprints on a local Kind Kubernetes cluster. Instead of storing a client secret in Kubernetes, workload identity federation allows the sidecar to authenticate using a Kubernetes service account token. Entra ID trusts tokens signed by your cluster's service account issuer.

### Architecture

```
Kind Cluster                              Entra ID
┌──────────────────────┐                 ┌───────────────────────────┐
│ Pod with Sidecar     │                 │ Agent Blueprint App       │
│ ┌──────────────────┐ │                 │ (Federated Credential)    │
│ │ ServiceAccount   │ │                 │                           │
│ │ Token (JWT)      │─┼──────────────►  │ Validates:                │
│ └──────────────────┘ │   Token         │ - issuer matches          │
└──────────────────────┘   Exchange      │ - subject matches         │
         │                               │ - audience matches        │
         │                               └───────────────────────────┘
         ▼                                          │
┌──────────────────────┐                           ▼
│ Azure Blob Storage   │ ◄─────────────  Fetches JWKS to verify
│ /.well-known/openid  │                 token signature
│ /openid/v1/jwks      │
└──────────────────────┘
```

### Why Self-Hosted OIDC?

Kind clusters don't expose their OIDC endpoints publicly by default. Entra ID needs to:
1. Fetch the OIDC discovery document to find the JWKS URL
2. Fetch the JWKS to verify the service account token's signature

We solve this by hosting the OIDC discovery document and JWKS on Azure Blob Storage.


### Prerequisites

```bash
# Required tools
az --version          # Azure CLI 2.64+
kind --version        # Kind for local Kubernetes
openssl version       # OpenSSL for key generation
pwsh --version        # PowerShell 7+ with Microsoft.Graph module
kubectl version       # Kubernetes CLI
```

Install PowerShell modules if needed:

```powershell
Install-Module Microsoft.Graph.Beta -Scope CurrentUser
Install-Module Microsoft.Graph.Applications -Scope CurrentUser
```

### Set Up Self-Hosted OIDC for Kind

Setting up some variables:

```bash
# Azure configuration
export AZURE_SUBSCRIPTION_ID="<your-subscription-id>"
export AZURE_RESOURCE_GROUP="ceposta-oidc-test"
export AZURE_LOCATION="eastus"
export STORAGE_ACCOUNT_NAME="oidc$(openssl rand -hex 4)"  # Must be globally unique

# Kubernetes configuration
export SERVICE_ACCOUNT_NAMESPACE="entra-demo"
export SERVICE_ACCOUNT_NAME="sidecar-sa"

# Create a working directory
mkdir -p ~/temp/workload-identity-setup
cd ~/temp/workload-identity-setup
```

#### Generate Service Account Signing Keys

Generate an RSA key pair that Kind will use to sign service account tokens:

```bash
# Generate RSA private key (for Kind to sign tokens)
openssl genrsa -out sa-signer.key 2048

# Extract public key (for JWKS)
openssl rsa -in sa-signer.key -pubout -out sa-signer.pub

echo "✅ Generated signing keys"
ls -la sa-signer.*
```

#### Create Azure Blob Storage for OIDC Endpoints

```bash
# Login to Azure
az login

# Set subscription
az account set --subscription "$AZURE_SUBSCRIPTION_ID"

# Create resource group
az group create \
  --name "$AZURE_RESOURCE_GROUP" \
  --location "$AZURE_LOCATION"

# Create storage account with anonymous blob access enabled
az storage account create \
  --name "$STORAGE_ACCOUNT_NAME" \
  --resource-group "$AZURE_RESOURCE_GROUP" \
  --location "$AZURE_LOCATION" \
  --sku Standard_LRS \
  --allow-blob-public-access true

# Create container with public access
az storage container create \
  --name "oidc" \
  --account-name "$STORAGE_ACCOUNT_NAME" \
  --public-access blob

# Get the blob endpoint URL
export OIDC_ISSUER_URL="https://${STORAGE_ACCOUNT_NAME}.blob.core.windows.net/oidc"
echo "OIDC Issuer URL: $OIDC_ISSUER_URL"
```

#### Create OIDC Discovery Document

```bash
# Create the openid-configuration document
cat > openid-configuration.json << EOF
{
  "issuer": "${OIDC_ISSUER_URL}",
  "jwks_uri": "${OIDC_ISSUER_URL}/openid/v1/jwks",
  "response_types_supported": ["id_token"],
  "subject_types_supported": ["public"],
  "id_token_signing_alg_values_supported": ["RS256"]
}
EOF

echo "✅ Created openid-configuration.json"
cat openid-configuration.json
```

#### Upload OIDC Discovery Document to Azure Blob

> **Important**: We only upload the discovery document now. The JWKS will be extracted from Kind after the cluster is created, because Kind generates its own key ID (`kid`) for the signing key.

```bash
# Upload openid-configuration to .well-known path
az storage blob upload \
  --account-name "$STORAGE_ACCOUNT_NAME" \
  --container-name "oidc" \
  --name ".well-known/openid-configuration" \
  --file openid-configuration.json \
  --content-type "application/json"

echo "✅ Uploaded openid-configuration"
echo "Discovery: ${OIDC_ISSUER_URL}/.well-known/openid-configuration"

# Verify it's accessible
curl -s "${OIDC_ISSUER_URL}/.well-known/openid-configuration" | jq .
```

#### Create Kind Cluster with Custom OIDC Issuer

```bash
# Delete existing cluster if present
kind delete cluster --name workload-identity 2>/dev/null || true

# Create Kind config
cat > kind-config.yaml << EOF
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraMounts:
  # Mount the signing key into the API server
  - hostPath: $(pwd)/sa-signer.key
    containerPath: /etc/kubernetes/pki/sa-signer.key
    readOnly: true
  kubeadmConfigPatches:
  - |
    kind: ClusterConfiguration
    apiServer:
      extraArgs:
        # Use our custom signing key
        service-account-signing-key-file: /etc/kubernetes/pki/sa-signer.key
        service-account-key-file: /etc/kubernetes/pki/sa-signer.key
        # Set the issuer to our Azure Blob URL
        service-account-issuer: ${OIDC_ISSUER_URL}
        # API audiences - include the Azure token exchange audience
        api-audiences: api://AzureADTokenExchange,https://kubernetes.default.svc
    controllerManager:
      extraArgs:
        service-account-private-key-file: /etc/kubernetes/pki/sa-signer.key
EOF

echo "✅ Created kind-config.yaml"
cat kind-config.yaml
```

Create the cluster:

```bash
kind create cluster --name workload-identity --config kind-config.yaml

echo "✅ Kind cluster created"
kubectl cluster-info --context kind-workload-identity
```

#### Extract JWKS from Kind and Upload to Azure Blob

> **Critical**: Kind generates its own key ID (`kid`) when using the signing key. We must extract the actual JWKS from Kind's API server and upload it to Azure Blob Storage. If you skip this step, Entra ID will fail to verify tokens with error `AADSTS7000272: The certificate with identifier ... could not be found`.

```bash
# Extract the actual JWKS from Kind's API server
kubectl get --raw /openid/v1/jwks > jwks.json

echo "✅ Extracted JWKS from Kind:"
cat jwks.json | jq .

# Upload the correct JWKS to Azure Blob Storage
az storage blob upload \
  --account-name "$STORAGE_ACCOUNT_NAME" \
  --container-name "oidc" \
  --name "openid/v1/jwks" \
  --file jwks.json \
  --content-type "application/json" \
  --overwrite

echo "✅ Uploaded JWKS to Azure Blob"
echo "JWKS URL: ${OIDC_ISSUER_URL}/openid/v1/jwks"

# Verify it matches
echo ""
echo "Verify the JWKS is accessible and matches:"
curl -s "${OIDC_ISSUER_URL}/openid/v1/jwks" | jq .
```

#### Create the Namespace

```bash
kubectl create namespace "$SERVICE_ACCOUNT_NAMESPACE"
echo "✅ Created namespace: $SERVICE_ACCOUNT_NAMESPACE"
```

---

## Configure Federated Credential on Agent Blueprint

So far we've set up our cluster to use a signing key and published OIDC discovery docs. The Kind cluster we created will sign service account tokens with our signing key and now that we have a public JWKS, we can configure the Agent Blueprint to trust this signing key. Let's configure the Blueprint with our OIDC discovery endpoint / JWKS. 

#### Set Your Blueprint Variables

```powershell
# PowerShell - Set your variables
$tenantId = "<your-tenant-id>"
$blueprintClientId = "<your-blueprint-client-id>"  # The CLIENT_ID from sidecar-config.yaml

# These should match your Kubernetes setup
$oidcIssuerUrl = "<your-oidc-issuer-url>"  # e.g., https://oidcXXXX.blob.core.windows.net/oidc
$serviceAccountNamespace = "entra-demo"
$serviceAccountName = "sidecar-sa"

# The subject claim format for Kubernetes service accounts
$subject = "system:serviceaccount:${serviceAccountNamespace}:${serviceAccountName}"

Write-Host "Tenant ID: $tenantId"
Write-Host "Blueprint Client ID: $blueprintClientId"
Write-Host "OIDC Issuer URL: $oidcIssuerUrl"
Write-Host "Subject: $subject"
```

#### Connect to Microsoft Graph

```powershell
# Connect with required permissions
Connect-MgGraph -Scopes @(
    "Application.ReadWrite.All"
) -TenantId $tenantId

Get-MgContext
```

#### Get the Blueprint Application Object ID

> **Important**: Agent Blueprints require the **Beta Graph API**. We use `Invoke-MgGraphRequest` to call the Beta endpoint directly.

```powershell
# Get the Blueprint application using Beta API
$blueprintApp = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/beta/applications?`$filter=appId eq '$blueprintClientId'"

if (-not $blueprintApp.value -or $blueprintApp.value.Count -eq 0) {
    Write-Error "Blueprint application not found with Client ID: $blueprintClientId"
    exit 1
}

$blueprintObjectId = $blueprintApp.value[0].id
$blueprintDisplayName = $blueprintApp.value[0].displayName

Write-Host "✅ Found Blueprint application"
Write-Host "Object ID: $blueprintObjectId"
Write-Host "Display Name: $blueprintDisplayName"
```

#### Add Federated Identity Credential

> **Note**: Agent Blueprints require the Beta API. The standard PowerShell cmdlets use v1.0 and will fail with "Agent Blueprints are not supported on the API version used in this request."

```powershell
# Create the federated identity credential using Beta API
$ficBody = @{
    name = "kind-workload-identity"
    issuer = $oidcIssuerUrl
    subject = $subject
    audiences = @("api://AzureADTokenExchange")
    description = "Workload identity for Kind cluster sidecar"
} | ConvertTo-Json

try {
    $fic = Invoke-MgGraphRequest -Method POST `
        -Uri "https://graph.microsoft.com/beta/applications/$blueprintObjectId/federatedIdentityCredentials" `
        -Body $ficBody `
        -ContentType "application/json"
    
    Write-Host "✅ Created Federated Identity Credential"
    Write-Host "Name: $($fic.name)"
    Write-Host "Issuer: $($fic.issuer)"
    Write-Host "Subject: $($fic.subject)"
    Write-Host "Audiences: $($fic.audiences -join ', ')"
} catch {
    if ($_.Exception.Message -like "*already exists*" -or $_.Exception.Message -like "*conflicting object*") {
        Write-Host "⚠️  Federated credential already exists"
        
        # Get existing credentials
        $existingFics = Invoke-MgGraphRequest -Method GET `
            -Uri "https://graph.microsoft.com/beta/applications/$blueprintObjectId/federatedIdentityCredentials"
        
        $existingFic = $existingFics.value | Where-Object { $_.name -eq "kind-workload-identity" }
        
        if ($existingFic) {
            Write-Host "Existing credential found with ID: $($existingFic.id)"
            Write-Host "Issuer: $($existingFic.issuer)"
            Write-Host "Subject: $($existingFic.subject)"
            
        }
    } else {
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
        throw $_
    }
}
```

#### Verify the Federated Credential

```powershell
# List all federated credentials on the Blueprint using Beta API
$fics = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/beta/applications/$blueprintObjectId/federatedIdentityCredentials"

Write-Host ""
Write-Host "Federated Identity Credentials on Blueprint:"
$fics.value | ForEach-Object {
    Write-Host "---"
    Write-Host "Name: $($_.name)"
    Write-Host "Issuer: $($_.issuer)"
    Write-Host "Subject: $($_.subject)"
    Write-Host "Audiences: $($_.audiences -join ', ')"
}
```

---

## Update Kubernetes Configuration

Now in our Kuberentes configmap, we update the config to use our signed token and not a client secret:

```yaml
  # Credential source type - Use workload identity (file-based token)
  AzureAd__ClientCredentials__0__SourceType: "SignedAssertionFilePath"
  # Path where the projected service account token will be mounted
  AzureAd__ClientCredentials__0__SignedAssertionFileDiskPath: "/var/run/secrets/tokens/azure-identity-token"
```

We can get rid of the `CLIENT_SECRET` from our env files now. Let's deploy to Kubernetes:

```bash
cd ./kubernetes
./deploy.sh
```

## Verify the Setup


```bash
kubectl get pods -n entra-demo
kubectl describe pod -l app=demo-app -n entra-demo
```

#### Verify Token is Projected

```bash
# Check that the token file exists
kubectl exec -n entra-demo deployment/demo-app -c sidecar -- \
  ls -la /var/run/secrets/tokens/

# View the token (it's a JWT)
kubectl exec -n entra-demo deployment/demo-app -c sidecar -- \
  cat /var/run/secrets/tokens/azure-identity-token
```

#### Decode and Inspect the Token

```bash
# Get the token
TOKEN=$(kubectl exec -n entra-demo deployment/demo-app -c sidecar -- \
  cat /var/run/secrets/tokens/azure-identity-token)

# Decode and display (requires jq)
echo $TOKEN | cut -d'.' -f2 | base64 -d 2>/dev/null | jq .
```

The token should contain:
- `iss`: Your OIDC issuer URL (Azure Blob Storage URL)
- `sub`: `system:serviceaccount:entra-demo:sidecar-sa`
- `aud`: `api://AzureADTokenExchange`

## Wrapping Up

At this point, we should be able to run all of the commands from the sidecar like we did in Post Three, but this time we are not exposed to any sensitive client secrets. Although we've taken steps to make this type of deployment more acceptable for production, we are still a ways off.

Additionally:

* An AI agent needs to make calls to an AI model. How do we get credentials to do that?
* An AI agent may need to call out to MCP tools. Those aren't agents. How do we enforce policy based on user/agent identity?
* How do we get any observability here? How do we know what's being called?

So far we've been exploring this through a very simplistic app (sleep/curl). But what if we have a more powerful AI agent deployed in the container? And we want to call out to MCP tools? Let's look at what a more realistic app looks like and then we can see how to alleviate the aforementioned problems. 