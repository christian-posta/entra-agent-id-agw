#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load environment variables from .env file
if [[ -f "$SCRIPT_DIR/.env" ]]; then
    echo "Loading environment from $SCRIPT_DIR/.env"
    set -a
    source "$SCRIPT_DIR/.env"
    set +a
else
    echo "Error: .env file not found at $SCRIPT_DIR/.env"
    echo ""
    echo "Create a .env file with the following variables:"
    echo "  TENANT_ID=<your-tenant-id>"
    echo "  BLUEPRINT_APP_ID=<your-blueprint-app-id>"
    echo "  MCP_SERVER_APP_ID=<your-mcp-server-app-id>"
    echo "  AZURE_OPENAI_ENDPOINT=<your-azure-openai-endpoint>"
    echo "  AZURE_OPENAI_DEPLOYMENT=<your-deployment-name>"
    exit 1
fi

# Verify required variables are set
required_vars=(
    "TENANT_ID"
    "BLUEPRINT_APP_ID"
    "AGENT_IDENTITY_APP_ID"
    "MCP_SERVER_APP_ID"
    "AZURE_OPENAI_ENDPOINT"
    "AZURE_OPENAI_DEPLOYMENT"
)

echo "Checking required environment variables..."
missing_vars=()
for var in "${required_vars[@]}"; do
    if [[ -z "${!var:-}" ]]; then
        missing_vars+=("$var")
    fi
done

if [[ ${#missing_vars[@]} -gt 0 ]]; then
    echo "Error: Missing required variables:"
    for var in "${missing_vars[@]}"; do
        echo "  - $var"
    done
    exit 1
fi

echo "✓ All required variables set"
echo ""

# Set defaults for optional variables
export AZURE_OPENAI_API_VERSION="${AZURE_OPENAI_API_VERSION:-2024-02-15-preview}"

# Namespace
NAMESPACE="${NAMESPACE:-entra-demo}"

# Create namespace if it doesn't exist
if ! kubectl get namespace "$NAMESPACE" >/dev/null 2>&1; then
    echo "Creating namespace: $NAMESPACE"
    kubectl create namespace "$NAMESPACE"
else
    echo "Namespace '$NAMESPACE' already exists"
fi

echo "Deploying ai-agent-cli to namespace: $NAMESPACE"
echo ""

# Apply ServiceAccount with substitution
echo "Applying serviceaccount..."
envsubst < "$SCRIPT_DIR/serviceaccount.yaml" | kubectl apply -f -

# Apply ConfigMap with substitution
echo "Applying sidecar-config..."
envsubst < "$SCRIPT_DIR/sidecar-config.yaml" | kubectl apply -f -

# Apply app ConfigMap with substitution
echo "Applying app-config..."
envsubst < "$SCRIPT_DIR/app-config.yaml" | kubectl apply -f -

# Apply Deployment
echo "Applying deployment..."
kubectl apply -f "$SCRIPT_DIR/deployment.yaml"

echo ""
echo "✓ Deployment complete!"
echo ""
echo "To check status:"
echo "  kubectl get pods -n $NAMESPACE"
echo ""
echo "To view logs:"
echo "  kubectl logs -n $NAMESPACE -l app=ai-agent-cli -c app -f"
echo ""
echo "To exec into the pod:"
echo "  kubectl exec -it -n $NAMESPACE deploy/ai-agent-cli -c app -- /bin/bash"

