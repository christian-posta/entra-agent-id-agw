# Microsoft Entra Agent ID on Kubernetes

This repository contains comprehensive guides and examples for setting up [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/) on Kubernetes. Entra Agent ID is a new feature that adds first-class support for AI Agent workloads, providing strong agent identity and the ability for agents to act on behalf of users (delegation) with proper audit trails.

## 📚 Documentation

**👉 [Read the full documentation on GitHub Pages →](https://blog.christianposta.com/entra-agent-id-agw/)**

The documentation includes a comprehensive 5-part series covering:
- Understanding Entra Agent ID fundamentals
- Agent On-Behalf-Of (OBO) token exchange mechanisms
- Running Entra Agent ID on Kubernetes with the SDK sidecar
- Workload Identity Federation to eliminate client secrets
- Full working examples with LLMs, MCP servers, and AgentGateway

## What's Included

- **Multi-part guide series** - Deep dive into how Entra Agent ID works
- **Kubernetes deployment examples** - Ready-to-use configurations for deploying to Kubernetes
- **AI Agent CLI demo** - Full working example application with Azure OpenAI and MCP integration using [AgentGateway](https://agentgateway.dev)
- **Setup guides** - PowerShell and programmatic blueprint creation
- **Reference documentation** - Detailed technical references

## Quick Start

### Prerequisites

Before you begin, you'll need to create an Agent Identity Blueprint. See the [Blueprint Creation Guide](./BLUEPRINT-CREATION-POWERSHELL.md) for details.

### Deploy to Kubernetes

```bash
cp env.example .env
# Edit .env with your configuration
cd kubernetes
./deploy.sh
```

## Repository Structure

- `PART-*.md` - Multi-part guide series (also available on [GitHub Pages](https://blog.christianposta.com/entra-agent-id-agw/))
- `ai-agent-cli/` - Full working example application
- `kubernetes/` - Kubernetes deployment configurations
- `reference/` - Technical reference documentation
- `docs/` - GitHub Pages site configuration

## Related Projects

- **[AgentGateway](https://agentgateway.dev)** - LLM and MCP gateway used in the AI Agent CLI demo for network and policy control

## Stay Updated

For updates and more content on Entra Agent ID, Kubernetes, and AI agents, follow me on [LinkedIn](https://www.linkedin.com/in/ceposta).

## License

This repository contains guides and examples. Please refer to Microsoft's documentation for official Entra Agent ID licensing and terms.
