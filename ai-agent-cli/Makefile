# AI Agent CLI - Makefile
# Build and manage Docker container for Kubernetes deployment

# Configuration
IMAGE_NAME ?= ai-agent-cli
IMAGE_TAG ?= latest
REGISTRY ?= 
FULL_IMAGE := $(if $(REGISTRY),$(REGISTRY)/$(IMAGE_NAME),$(IMAGE_NAME))

# Build Configuration
DOCKER_BUILD_ARGS ?= 
DOCKER_PLATFORM ?= linux/amd64

# Kubernetes Configuration
NAMESPACE ?= default
KIND_CLUSTER ?= kind

# Colors for output
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m  # No Color

.PHONY: help build build-no-cache push run run-interactive shell test clean version tag

#------------------------------------------------------------------------------
# Help
#------------------------------------------------------------------------------
help: ## Show this help message
	@echo "AI Agent CLI - Docker Build Targets"
	@echo ""
	@echo "Usage: make [target] [VARIABLE=value]"
	@echo ""
	@echo "Variables:"
	@echo "  IMAGE_NAME     Docker image name (default: ai-agent-cli)"
	@echo "  IMAGE_TAG      Docker image tag (default: latest)"
	@echo "  REGISTRY       Container registry (default: none, local only)"
	@echo "  DOCKER_PLATFORM Target platform (default: linux/amd64)"
	@echo "  KIND_CLUSTER   Kind cluster name (default: kind)"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'

#------------------------------------------------------------------------------
# Build Targets
#------------------------------------------------------------------------------
build: ## Build Docker image
	@echo "$(GREEN)Building $(FULL_IMAGE):$(IMAGE_TAG)...$(NC)"
	docker build \
		--platform $(DOCKER_PLATFORM) \
		$(DOCKER_BUILD_ARGS) \
		-t $(FULL_IMAGE):$(IMAGE_TAG) \
		.
	@echo "$(GREEN)✓ Build complete: $(FULL_IMAGE):$(IMAGE_TAG)$(NC)"

build-no-cache: ## Build Docker image without cache
	@echo "$(GREEN)Building $(FULL_IMAGE):$(IMAGE_TAG) (no cache)...$(NC)"
	docker build \
		--platform $(DOCKER_PLATFORM) \
		--no-cache \
		$(DOCKER_BUILD_ARGS) \
		-t $(FULL_IMAGE):$(IMAGE_TAG) \
		.
	@echo "$(GREEN)✓ Build complete: $(FULL_IMAGE):$(IMAGE_TAG)$(NC)"

build-multi-arch: ## Build multi-architecture image (amd64 and arm64)
	@echo "$(GREEN)Building multi-arch $(FULL_IMAGE):$(IMAGE_TAG)...$(NC)"
	docker buildx build \
		--platform linux/amd64,linux/arm64 \
		$(DOCKER_BUILD_ARGS) \
		-t $(FULL_IMAGE):$(IMAGE_TAG) \
		--push \
		.
	@echo "$(GREEN)✓ Multi-arch build complete: $(FULL_IMAGE):$(IMAGE_TAG)$(NC)"

#------------------------------------------------------------------------------
# Registry Targets
#------------------------------------------------------------------------------
push: ## Push image to registry
ifndef REGISTRY
	$(error REGISTRY is not set. Use: make push REGISTRY=your-registry.io)
endif
	@echo "$(GREEN)Pushing $(FULL_IMAGE):$(IMAGE_TAG) to registry...$(NC)"
	docker push $(FULL_IMAGE):$(IMAGE_TAG)
	@echo "$(GREEN)✓ Push complete$(NC)"

tag: ## Tag image for registry
ifndef REGISTRY
	$(error REGISTRY is not set. Use: make tag REGISTRY=your-registry.io)
endif
	@echo "$(GREEN)Tagging $(IMAGE_NAME):$(IMAGE_TAG) as $(FULL_IMAGE):$(IMAGE_TAG)...$(NC)"
	docker tag $(IMAGE_NAME):$(IMAGE_TAG) $(FULL_IMAGE):$(IMAGE_TAG)
	@echo "$(GREEN)✓ Tagged$(NC)"

#------------------------------------------------------------------------------
# Run Targets
#------------------------------------------------------------------------------
run: ## Run container with env file (non-interactive)
	@echo "$(GREEN)Running $(FULL_IMAGE):$(IMAGE_TAG)...$(NC)"
	@if [ -f .env ]; then \
		docker run --rm \
			--env-file .env \
			$(FULL_IMAGE):$(IMAGE_TAG); \
	else \
		echo "$(YELLOW)Warning: No .env file found. Running without environment variables.$(NC)"; \
		docker run --rm $(FULL_IMAGE):$(IMAGE_TAG); \
	fi

run-interactive: ## Run container interactively with TTY
	@echo "$(GREEN)Running $(FULL_IMAGE):$(IMAGE_TAG) (interactive)...$(NC)"
	@if [ -f .env ]; then \
		docker run --rm -it \
			--env-file .env \
			$(FULL_IMAGE):$(IMAGE_TAG); \
	else \
		echo "$(YELLOW)Warning: No .env file found. Running without environment variables.$(NC)"; \
		docker run --rm -it $(FULL_IMAGE):$(IMAGE_TAG); \
	fi

run-api-key: ## Run container in API key mode for testing
	@echo "$(GREEN)Running in API key mode...$(NC)"
	@if [ -f .env ]; then \
		docker run --rm -it \
			--env-file .env \
			-e AUTH_MODE=api_key \
			$(FULL_IMAGE):$(IMAGE_TAG); \
	else \
		echo "$(RED)Error: .env file required with AZURE_OPENAI_API_KEY$(NC)"; \
		exit 1; \
	fi

shell: ## Open shell in container
	@echo "$(GREEN)Opening shell in $(FULL_IMAGE):$(IMAGE_TAG)...$(NC)"
	docker run --rm -it \
		--entrypoint /bin/bash \
		$(FULL_IMAGE):$(IMAGE_TAG)

#------------------------------------------------------------------------------
# Test Targets
#------------------------------------------------------------------------------
test: ## Test the built image
	@echo "$(GREEN)Testing $(FULL_IMAGE):$(IMAGE_TAG)...$(NC)"
	@docker run --rm $(FULL_IMAGE):$(IMAGE_TAG) --help > /dev/null 2>&1 && \
		echo "$(GREEN)✓ Image runs successfully$(NC)" || \
		(echo "$(RED)✗ Image test failed$(NC)" && exit 1)
	@docker run --rm $(FULL_IMAGE):$(IMAGE_TAG) config-show 2>/dev/null && \
		echo "$(GREEN)✓ CLI commands work$(NC)" || \
		echo "$(YELLOW)⚠ config-show requires environment variables$(NC)"

test-health: ## Test the healthcheck
	@echo "$(GREEN)Testing healthcheck...$(NC)"
	@docker run --rm $(FULL_IMAGE):$(IMAGE_TAG) \
		python -c "from agent_cli import __version__; print(f'Version: {__version__}')"

#------------------------------------------------------------------------------
# Utility Targets
#------------------------------------------------------------------------------
version: ## Show image version info
	@echo "Image: $(FULL_IMAGE):$(IMAGE_TAG)"
	@docker images $(FULL_IMAGE):$(IMAGE_TAG) --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedAt}}"

clean: ## Remove built images
	@echo "$(YELLOW)Removing $(FULL_IMAGE):$(IMAGE_TAG)...$(NC)"
	-docker rmi $(FULL_IMAGE):$(IMAGE_TAG) 2>/dev/null || true
	@echo "$(GREEN)✓ Clean complete$(NC)"

clean-all: ## Remove all ai-agent-cli images
	@echo "$(YELLOW)Removing all $(IMAGE_NAME) images...$(NC)"
	-docker images $(IMAGE_NAME) -q | xargs -r docker rmi -f 2>/dev/null || true
	@echo "$(GREEN)✓ Clean complete$(NC)"

prune: ## Prune Docker build cache
	@echo "$(YELLOW)Pruning Docker build cache...$(NC)"
	docker builder prune -f
	@echo "$(GREEN)✓ Prune complete$(NC)"

#------------------------------------------------------------------------------
# Development Targets
#------------------------------------------------------------------------------
dev-build: ## Build for local development (with verbose output)
	docker build \
		--progress=plain \
		-t $(IMAGE_NAME):dev \
		.

dev-run: ## Run development build
	docker run --rm -it \
		-v $(PWD)/agent_cli:/app/agent_cli:ro \
		--env-file .env \
		$(IMAGE_NAME):dev

#------------------------------------------------------------------------------
# Kubernetes Targets
#------------------------------------------------------------------------------
k8s-load-kind: ## Load image into kind cluster
	@echo "$(GREEN)Loading $(FULL_IMAGE):$(IMAGE_TAG) into kind cluster '$(KIND_CLUSTER)'...$(NC)"
	kind load docker-image $(FULL_IMAGE):$(IMAGE_TAG) --name $(KIND_CLUSTER)
	@echo "$(GREEN)✓ Image loaded into kind$(NC)"

k8s-load-minikube: ## Load image into minikube
	@echo "$(GREEN)Loading $(FULL_IMAGE):$(IMAGE_TAG) into minikube...$(NC)"
	minikube image load $(FULL_IMAGE):$(IMAGE_TAG)
	@echo "$(GREEN)✓ Image loaded into minikube$(NC)"

k8s-deploy: ## Deploy to Kubernetes (requires .env file)
	@echo "$(GREEN)Deploying to Kubernetes...$(NC)"
	./deploy.sh
	@echo "$(GREEN)✓ Deployment complete$(NC)"

k8s-delete: ## Delete Kubernetes resources
	@echo "$(YELLOW)Deleting ai-agent-cli resources...$(NC)"
	-kubectl delete -f deployment.yaml 2>/dev/null || true
	-kubectl delete -f app-config.yaml 2>/dev/null || true
	-kubectl delete -f sidecar-config.yaml 2>/dev/null || true
	-kubectl delete -f serviceaccount.yaml 2>/dev/null || true
	@echo "$(GREEN)✓ Resources deleted$(NC)"

k8s-logs: ## Tail logs from the app container
	kubectl logs -n entra-demo -l app=ai-agent-cli -c app -f

k8s-logs-sidecar: ## Tail logs from the sidecar container
	kubectl logs -n entra-demo -l app=ai-agent-cli -c sidecar -f

k8s-exec: ## Exec into the app container
	kubectl exec -it -n entra-demo deploy/ai-agent-cli -c app -- /bin/bash

k8s-status: ## Show Kubernetes deployment status
	@echo "$(GREEN)Deployment Status:$(NC)"
	@kubectl get pods -n entra-demo -l app=ai-agent-cli
	@echo ""
	@kubectl get deployment -n entra-demo ai-agent-cli

