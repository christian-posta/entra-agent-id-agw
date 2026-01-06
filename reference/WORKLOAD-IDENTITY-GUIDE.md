# Workload Identity Federation for Agent Blueprints on Kind

This guide walks through configuring workload identity federation to eliminate client secrets when using the Entra SDK sidecar with Agent Blueprints on a local Kind Kubernetes cluster.

## Overview

Instead of storing a client secret in Kubernetes, workload identity federation allows the sidecar to authenticate using a Kubernetes service account token. Entra ID trusts tokens signed by your cluster's service account issuer.

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

---

## Prerequisites

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

---

## Part 1: Set Up Self-Hosted OIDC for Kind

### Step 1.1: Set Your Variables

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

### Step 1.2: Generate Service Account Signing Keys

Generate an RSA key pair that Kind will use to sign service account tokens:

```bash
# Generate RSA private key (for Kind to sign tokens)
openssl genrsa -out sa-signer.key 2048

# Extract public key (for JWKS)
openssl rsa -in sa-signer.key -pubout -out sa-signer.pub

echo "✅ Generated signing keys"
ls -la sa-signer.*
```

### Step 1.3: Create Azure Blob Storage for OIDC Endpoints

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

### Step 1.4: Create OIDC Discovery Document

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

### Step 1.5: Upload OIDC Discovery Document to Azure Blob

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

### Step 1.6: Create Kind Cluster with Custom OIDC Issuer

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

### Step 1.7: Extract JWKS from Kind and Upload to Azure Blob

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

### Step 1.8: Create the Namespace

```bash
kubectl create namespace "$SERVICE_ACCOUNT_NAMESPACE"
echo "✅ Created namespace: $SERVICE_ACCOUNT_NAMESPACE"
```

---

## Part 2: Configure Federated Credential on Agent Blueprint

### Step 2.1: Set Your Blueprint Variables

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

### Step 2.2: Connect to Microsoft Graph

```powershell
# Connect with required permissions
Connect-MgGraph -Scopes @(
    "Application.ReadWrite.All"
) -TenantId $tenantId

Get-MgContext
```

### Step 2.3: Get the Blueprint Application Object ID

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

### Step 2.4: Add Federated Identity Credential

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
            
            # Optionally update it
            # $updateBody = @{
            #     issuer = $oidcIssuerUrl
            #     subject = $subject
            #     audiences = @("api://AzureADTokenExchange")
            # } | ConvertTo-Json
            # 
            # Invoke-MgGraphRequest -Method PATCH `
            #     -Uri "https://graph.microsoft.com/beta/applications/$blueprintObjectId/federatedIdentityCredentials/$($existingFic.id)" `
            #     -Body $updateBody `
            #     -ContentType "application/json"
        }
    } else {
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
        throw $_
    }
}
```

### Step 2.5: Verify the Federated Credential

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

## Part 3: Update Kubernetes Configuration

```bash
cd ./kubernetes
./deploy.sh
```

## Part 4: Verify the Setup

### Step 4.1: Check Pod Status

```bash
kubectl get pods -n entra-demo
kubectl describe pod -l app=demo-app -n entra-demo
```

### Step 4.2: Verify Token is Projected

```bash
# Check that the token file exists
kubectl exec -n entra-demo deployment/demo-app -c sidecar -- \
  ls -la /var/run/secrets/tokens/

# View the token (it's a JWT)
kubectl exec -n entra-demo deployment/demo-app -c sidecar -- \
  cat /var/run/secrets/tokens/azure-identity-token
```

### Step 4.3: Decode and Inspect the Token

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

### Step 4.4: Check Sidecar Logs

```bash
kubectl logs -n entra-demo deployment/demo-app -c sidecar
```

### Step 4.5: Test Token Acquisition

```bash
# Call the sidecar's health endpoint
kubectl exec -n entra-demo deployment/demo-app -c app -- \
  curl -s http://localhost:5000/healthz -H "Host: localhost"

# Try to get an authorization header for Graph API
kubectl exec -n entra-demo deployment/demo-app -c app -- \
  curl -s http://localhost:5000/AuthorizationHeaderUnauthenticated/graph -H "Host: localhost"
```

---

## Troubleshooting

### "AADSTS70021: No matching federated identity record found"

**Cause**: The federated credential configuration doesn't match the token claims.

**Check**:
1. Issuer URL matches exactly (including trailing slashes)
2. Subject matches: `system:serviceaccount:<namespace>:<sa-name>`
3. Audience is `api://AzureADTokenExchange`

```powershell
# Verify your federated credential
Get-MgApplicationFederatedIdentityCredential -ApplicationId $blueprintObjectId | Format-List
```

### "AADSTS700024: Client assertion is not within its valid time range"

**Cause**: Token expiration issue or clock skew.

**Solution**: Check that the Kind node's time is synchronized:

```bash
docker exec workload-identity-control-plane date
date
```

### "AADSTS7000272: The certificate with identifier ... could not be found"

**Cause**: The JWKS in Azure Blob Storage has a different key ID (`kid`) than what Kind is using to sign tokens. This happens if you manually generated a JWKS instead of extracting it from Kind.

**Solution**: Extract the actual JWKS from Kind and upload it:

```bash
# Extract JWKS from Kind
kubectl get --raw /openid/v1/jwks > jwks.json
cat jwks.json | jq .

# Upload to Azure Blob Storage
az storage blob upload \
  --account-name "$STORAGE_ACCOUNT_NAME" \
  --container-name "oidc" \
  --name "openid/v1/jwks" \
  --file jwks.json \
  --content-type "application/json" \
  --overwrite

# Restart the pod to get a fresh token
kubectl rollout restart deployment/demo-app -n entra-demo
```

### "Failed to fetch JWKS" or "Unable to verify token signature"

**Cause**: Entra ID cannot reach your OIDC endpoints.

**Check**:
1. Blob storage has public access enabled
2. URLs are correct and accessible

```bash
curl -v "${OIDC_ISSUER_URL}/.well-known/openid-configuration"
curl -v "${OIDC_ISSUER_URL}/openid/v1/jwks"
```

### Token file not found

**Cause**: Projected volume not mounted correctly.

**Check**:
```bash
kubectl describe pod -l app=demo-app -n entra-demo | grep -A20 "Volumes:"
```

---

## Cleanup

### Remove Azure Resources

```bash
# Delete the resource group (includes storage account)
az group delete --name "$AZURE_RESOURCE_GROUP" --yes --no-wait
```

### Remove Kind Cluster

```bash
kind delete cluster --name workload-identity
```

### Remove Local Files

```bash
rm -rf ~/workload-identity-setup
```

### Remove Federated Credential (if keeping Blueprint)

```powershell
# Get the federated credential using Beta API
$fics = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/beta/applications/$blueprintObjectId/federatedIdentityCredentials"

$fic = $fics.value | Where-Object { $_.name -eq "kind-workload-identity" }

if ($fic) {
    Invoke-MgGraphRequest -Method DELETE `
        -Uri "https://graph.microsoft.com/beta/applications/$blueprintObjectId/federatedIdentityCredentials/$($fic.id)"
    
    Write-Host "✅ Removed federated credential"
} else {
    Write-Host "Federated credential 'kind-workload-identity' not found"
}
```

---

## Quick Reference

### Token Exchange Flow

```
1. Pod starts → Kubernetes projects SA token to /var/run/secrets/tokens/azure-identity-token
2. Sidecar reads token (SignedAssertionFilePath)
3. Sidecar sends token to Entra ID token endpoint
4. Entra ID:
   a. Fetches JWKS from ${OIDC_ISSUER_URL}/openid/v1/jwks
   b. Verifies token signature
   c. Checks issuer, subject, audience match federated credential
   d. Issues access token for the Blueprint
5. Sidecar uses Blueprint token for downstream API calls
```

### Key Configuration Values

| Setting | Value |
|---------|-------|
| Credential SourceType | `SignedAssertionFilePath` |
| Token File Path | `/var/run/secrets/tokens/azure-identity-token` |
| Token Audience | `api://AzureADTokenExchange` |
| Subject Format | `system:serviceaccount:<namespace>:<sa-name>` |

---

## References

- [Workload Identity Federation Concepts](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation)
- [Configure an app to trust an external IdP](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust)
- [Microsoft Entra Workload ID for Kubernetes](https://azure.github.io/azure-workload-identity/docs/)
- [Kubernetes Service Account Token Volume Projection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection)
- [Microsoft.Identity.Web Credential Configuration](https://aka.ms/idweb/client-credentials)
