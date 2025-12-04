# Setting Up Microsoft Entra SDK for AgentID Sidecar with Kind

> **⚠️ IMPORTANT**: The Microsoft Entra SDK for AgentID is currently in **preview**. 
> This guide is based on the source code in this repository and official documentation.
> Always check [the official documentation](https://learn.microsoft.com/en-us/entra/msidweb/agent-id-sdk/overview) for the latest information.

## Overview

This guide walks you through deploying the Microsoft Entra SDK for AgentID sidecar in a local Kubernetes cluster using [kind](https://kind.sigs.k8s.io/). The sidecar handles token acquisition, validation, and downstream API calls for your application.

**References:**
- [Microsoft Entra SDK for AgentID Overview](https://learn.microsoft.com/en-us/entra/msidweb/agent-id-sdk/overview)
- [Microsoft Agent Identity Platform](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/)

---

## Prerequisites

### Tools Required

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **kind**: [Install kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- **kubectl**: [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- **.NET SDK 9.0**: Required to build the sidecar from source (see Step 2)

### Azure/Entra Requirements

- Access to [Microsoft Entra admin center](https://entra.microsoft.com/)
- An Azure subscription with permissions to register applications

---

## Step 1: Understand the Architecture

Before deploying, understand what you're setting up:

**Key Points:**
- The sidecar only listens on **localhost** in production (enforced in code)
- You must explicitly call the sidecar's HTTP endpoints - it's not transparent
- One Blueprint per service for proper security isolation (recommended)

---

## Step 2: Build the Sidecar Container Image

> **Note**: As of this writing, the SDK is in preview. Check [GitHub releases](https://github.com/AzureAD/microsoft-identity-web/releases) 
> for official container images. If no official image is available, build from source:

### Option A: Build from Source (Recommended for Testing)

# Clone the repository (if you haven't already)
cd /path/to/microsoft-identity-web

# Navigate to the sidecar project
cd src/Microsoft.Identity.Web.Sidecar

# Build the container image
docker build -t entra-sidecar:local -f Dockerfile .### Option B: Use Official Image (When Available)

Check [the official documentation](https://learn.microsoft.com/en-us/entra/msidweb/agent-id-sdk/overview) 
for the latest container image location. The docs mention checking GitHub releases for available tags.

---

## Step 3: Set Up Microsoft Entra ID

### 3.1 Create the Agent Identity Blueprint

The Blueprint is an app registration that can create and impersonate Agent Identities.

> **📖 Official Documentation**: For complete instructions, see:
> - [Create an agent identity blueprint](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/create-blueprint)
> - [Agent service principals](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/agent-service-principals)

**High-level steps:**

1. Go to [Microsoft Entra admin center](https://entra.microsoft.com/)
2. Navigate to **App registrations** → **New registration**
3. Name it (e.g., `my-service-blueprint`)
4. Set **Supported account types** to "Accounts in this organizational directory only"
5. Click **Register**
6. Note the **Application (client) ID** and **Directory (tenant) ID**

### 3.2 Add Credentials to the Blueprint

For **local development/testing** (not recommended for production):

1. In your app registration, go to **Certificates & secrets**
2. Click **New client secret**
3. Note the secret value (you won't see it again)

For **production**, use certificates or Federated Identity Credentials (FIC) with Kubernetes OIDC.

### 3.3 Create an Agent Identity

> **📖 Official Documentation**: See [Agent service principals](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/agent-service-principals)

Agent Identities are created via Microsoft Graph API using the Blueprint's credentials. 
This is done **before** deploying the sidecar.

**The general process is:**
1. Use the Blueprint to authenticate to Microsoft Graph
2. Create a Service Principal that represents the Agent Identity
3. Configure Federated Identity Credentials (FIC) to establish trust between Blueprint and Agent Identity
4. Grant permissions to the Agent Identity (e.g., `User.Read` for Graph)
5. Admin consent for the permissions

---

## Step 4: Create the Kind Cluster

# Create a kind cluster
kind create cluster --name entra-sidecar-test

# Verify the cluster is running
kubectl cluster-info --context kind-entra-sidecar-test

# Load your locally built image into kind
kind load docker-image entra-sidecar:local --name entra-sidecar-test---

## Step 5: Create Kubernetes Configuration

### 5.1 Create Namespace

kubectl create namespace entra-demo### 5.2 Create ConfigMap (Non-Sensitive Config)

Create `sidecar-config.yaml`:

apiVersion: v1
kind: ConfigMap
metadata:
  name: sidecar-config
  namespace: entra-demo
data:
  # Azure AD / Entra configuration
  AzureAd__Instance: "https://login.microsoftonline.com/"
  AzureAd__TenantId: "<YOUR-TENANT-ID>"
  AzureAd__ClientId: "<YOUR-BLUEPRINT-CLIENT-ID>"
  
  # Credential source type
  AzureAd__ClientCredentials__0__SourceType: "ClientSecret"
  
  # Downstream API configuration (example: Microsoft Graph)
  DownstreamApis__graph__BaseUrl: "https://graph.microsoft.com/v1.0/"
  DownstreamApis__graph__Scopes__0: "https://graph.microsoft.com/.default"
  
  # ASP.NET Core settings
  ASPNETCORE_ENVIRONMENT: "Production"
  ASPNETCORE_URLS: "http://+:5000"Apply it:
kubectl apply -f sidecar-config.yaml### 5.3 Create Secret (Sensitive Config)

Create `sidecar-secret.yaml`:

apiVersion: v1
kind: Secret
metadata:
  name: sidecar-secret
  namespace: entra-demo
type: Opaque
stringData:
  AzureAd__ClientCredentials__0__ClientSecret: "<YOUR-BLUEPRINT-CLIENT-SECRET>"Apply it:
kubectl apply -f sidecar-secret.yaml> **⚠️ Security Note**: Using client secrets is only for development/testing. 
> For production, use certificates or Federated Identity Credentials.

---

## Step 6: Deploy the Sidecar with a Test Application

Create `deployment.yaml`:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-app
  namespace: entra-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: demo-app
  template:
    metadata:
      labels:
        app: demo-app
    spec:
      containers:
      # Your application container
      - name: app
        image: curlimages/curl:latest
        command: ["sleep", "infinity"]  # Keep container running for testing
        env:
        - name: SIDECAR_URL
          value: "http://localhost:5000"
      
      # Entra SDK Sidecar
      - name: sidecar
        image: entra-sidecar:local  # Use your built image
        ports:
        - containerPort: 5000
        envFrom:
        - configMapRef:
            name: sidecar-config
        - secretRef:
            name: sidecar-secret
        readinessProbe:
          httpGet:
            path: /healthz
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /healthz
            port: 5000
          initialDelaySeconds: 10
          periodSeconds: 30Apply it:
kubectl apply -f deployment.yaml---

## Step 7: Verify the Deployment

### Check Pod Status

kubectl get pods -n entra-demoWait until the pod shows `2/2` containers running.

### Check Sidecar Logs

kubectl logs -n entra-demo deployment/demo-app -c sidecar### Test the Sidecar from Inside the Pod

# Get a shell in the app container
kubectl exec -it -n entra-demo deployment/demo-app -c app -- sh

# Test health endpoint
curl http://localhost:5000/healthz

# Test getting an authorization header (requires valid token from Blueprint)
# For app-only token using Blueprint's credentials:
curl "http://localhost:5000/AuthorizationHeaderUnauthenticated/graph"

# For Agent Identity token (replace <agent-identity-id> with your Agent Identity's client ID):
curl "http://localhost:5000/AuthorizationHeaderUnauthenticated/graph?AgentIdentity=<agent-identity-id>"---

## Step 8: Using the Sidecar from Your Application

### Available Endpoints

| Endpoint | Method | Auth Required | Description |
|----------|--------|---------------|-------------|
| `/healthz` | GET | No | Health check |
| `/Validate` | GET | Yes (Bearer) | Validates incoming token, returns claims |
| `/AuthorizationHeader/{apiName}` | GET | Yes (Bearer) | Gets token using caller's identity (OBO) |
| `/AuthorizationHeaderUnauthenticated/{apiName}` | GET | No | Gets token using Blueprint's app identity |
| `/DownstreamApi/{apiName}` | POST | Yes (Bearer) | Proxies API call with caller's identity |
| `/DownstreamApiUnauthenticated/{apiName}` | POST | No | Proxies API call with Blueprint's identity |

### Agent Identity Parameters

Add these query parameters to impersonate an Agent Identity:
