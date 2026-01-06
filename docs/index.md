---
layout: default
title: Microsoft Entra Agent ID on Kubernetes
---

# Microsoft Entra Agent ID on Kubernetes

Welcome to the comprehensive guide for setting up Microsoft Entra Agent ID on Kubernetes.

[Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/) is a new feature for [Microsoft Entra](https://learn.microsoft.com/en-us/entra) that adds support for "AI Agent" workloads. This set of guides will specifically dive deeply into how it works (its full token-exchange mechanism) with the goal of getting it working on Kubernetes (not necessarily AKS, but would apply there too) for Agent and MCP workloads.

## Multi-Part Series

This comprehensive series walks through Entra Agent ID from basics to production deployment:

1. [Part One: Understanding Entra Agent ID](PART-1.md) - Learn the fundamentals of Entra Agent ID, blueprints, and agent identities
2. [Part Two: Agent On-Behalf-Of User](PART-2.md) - Deep dive into OBO token exchange mechanisms
3. [Part Three: Running on Kubernetes](PART-3.md) - Deploy the Entra SDK sidecar on Kubernetes
4. [Part Four: Workload Identity Federation](PART-4.md) - Eliminate client secrets with workload identity federation
5. [Part Five: LLM and MCP with Entra Agent ID and AgentGateway](PART-5.md) - Full working example with AI agents, LLMs, and MCP servers

---

For additional guides, setup instructions, and reference documentation, visit the [GitHub repository](https://github.com/christian-posta/entra-agent-id-agw).

---

*If you're interested in updates on this topic, please follow [@ceposta](https://www.linkedin.com/in/ceposta) on LinkedIn.*
