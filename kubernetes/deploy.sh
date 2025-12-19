#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Load environment variables from .env file
if [[ -f "$ROOT_DIR/.env" ]]; then
    set -a
    source "$ROOT_DIR/.env"
    set +a
else
    echo "Error: .env file not found at $ROOT_DIR/.env"
    exit 1
fi

# Verify required variables are set
# Note: CLIENT_SECRET is no longer required - using workload identity federation
required_vars=("TENANT_ID" "CLIENT_ID" "MCP_SERVER_APP_ID")
for var in "${required_vars[@]}"; do
    if [[ -z "${!var:-}" ]]; then
        echo "Error: Required variable $var is not set in .env"
        exit 1
    fi
done

if ! kubectl get namespace entra-demo >/dev/null 2>&1; then
    echo "Creating namespace: entra-demo"
    kubectl create namespace entra-demo
else
    echo "Namespace 'entra-demo' already exists"
fi

echo "Deploying to namespace: entra-demo"

# Apply ServiceAccount with substitution
echo "Applying serviceaccount..."
envsubst < "$SCRIPT_DIR/serviceaccount.yaml" | kubectl apply -f -

# Apply ConfigMap with substitution
echo "Applying sidecar-config..."
envsubst < "$SCRIPT_DIR/sidecar-config.yaml" | kubectl apply -f -

# Note: No secret needed - using workload identity federation

# Apply Deployment (no substitution needed)
echo "Applying deployment..."
kubectl apply -f "$SCRIPT_DIR/deployment.yaml"

echo "Deployment complete!"

