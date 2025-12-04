**Tell us about your PDF experience.**

**Microsoft agent identity platform for**

**developers**

Learn how to build agents that can authenticate users, request permissions, and access

resources securely with Microsoft agent identity platform.

![](./assets/output_0_1.jpeg)![](./assets/output_0_2.jpeg)

**Microsoft agent identity platform for developers**

ｅ**OVERVIEW**

What is the Microsoft agent identity platform?

What is an agent identity?

What is the Agent Registry?

![](./assets/output_0_3.jpeg)![](./assets/output_0_4.jpeg)

**Agent development**

ｐ**CONCEPT**

Agent users

Agent identity blueprint

Agent registry collections

Tokens in agent IDs

Service principals and agents

ｃ**HOW-TO GUIDE**

Request agent user tokens for autonomous agents

Request agent tokens for autonomous agents

![](./assets/output_0_5.jpeg)![](./assets/output_0_6.jpeg)

**Access management**

ｃ**HOW-TO GUIDE**

Grant app permissions to an autonomous agent

![](./assets/output_1_1.jpeg)![](./assets/output_1_2.jpeg)

Request authorization from user

**What is Microsoft agent identity platform**

The Microsoft agent identity platform is an identity and authorization framework built to

address the unique authentication, authorization, and governance challenges posed by AI

agents operating in enterprise environments.

Unlike nonagentic application identities designed for web services or user identities designed

for humans, the Microsoft agent identity platform is purpose-built for AI agents. The platform

provides specialized components that enable AI agents to authenticate securely and access

resources appropriately. It also enables agents to discover other agents and operate within

enterprise-grade governance frameworks.

This overview introduces the core components of the Microsoft agent identity platform. It

focuses on the identity constructs, authentication mechanisms, token systems, and discovery

capabilities that form the foundation of agent identity management in enterprise

environments.

The Microsoft agent identity platform is built on several foundational technical components

that work together to provide a complete identity and authorization solution for AI agents:

**Authentication service**: An OAuth 2.0 and OpenID Connect (OIDC) standard-compliant

authentication service that enables secure, standards-based authentication for agents.

This service issues tokens that agents use to authenticate to resources and APIs,

supporting both application-only and delegated access scenarios. There are three objects

that form the core identity constructs in the platform: agent identity blueprint, agent

identity, and agent user.

**SDKs**: Software development kits that enable developers to integrate with the Microsoft

agent identity platform. SDKs abstract the complexity of token acquisition and protocol

handling, making it straightforward for platforms that build agents to incorporate identity

management into their applications. Microsoft agent identity platform includes two SDKs:

Microsoft Identity Web (.NET) and the Microsoft Entra SDK for agent ID.

） **Important**

**Microsoft Entra Agent ID**

is currently in PREVIEW. This information relates to a

prerelease product that may be substantially modified before it's released. Microsoft

makes no warranties, expressed or implied, with respect to the information provided here.

**Platform architecture overview**

**Agent management**: A comprehensive agent metadata store and administrative interface

within the Microsoft Entra admin center that enables administrators to discover, view,

configure, and manage agents. The platform provides the agent registry that is a

centralized repository for registering and managing agents across an organization.

These technical components work together with the identity constructs described in the

following section to provide complete platform functionality.

The Microsoft agent identity platform uses OAuth for authorization and OpenID Connect

(OIDC) for authentication.

**OpenID Connect (OIDC)** enables agents to authenticate and verify the identity of other

entities they communicate with, establishing secure trust relationships.

**OAuth 2.0** allows agents to request access tokens that authorize them to access resources

on behalf of themselves or users, supporting both application-only and delegated access

scenarios.

For more information, see Oauth protocols

Tokens are the fundamental security mechanism enabling secure communication and

authorization in the Microsoft agent identity platform. The platform supports multiple token

flow patterns designed for specific operational scenarios. For more information, see tokens in

Microsoft agent identity platform

The Microsoft agent identity platform is designed to work seamlessly across the Microsoft

ecosystem and beyond. It integrates with:

**Microsoft Entra ID**: The platform extends Microsoft Entra ID capabilities to support agent

scenarios, using existing identity infrastructure and policies

**Platforms / services that create agents**: Platforms that create and manage agents can

integrate with the Microsoft agent identity platform to secure agents. This includes both

Microsoft-owned platforms like Copilot Studio and third-party platforms.

**Extended Microsoft identity and security products**: Integration with conditional access,

identity protection, identity governance, global secure access, and other security services

enable comprehensive agent security

**Authentication and authorization**

**Integration and interoperability**

This interoperability ensures that organizations can build, deploy, and manage agent identities

consistently regardless of where agents are created or deployed.

**Last updated on 11/18/2025**

**What are agent identities**

Agent identities are identity accounts within Microsoft Entra ID that provide unique

identification and authentication capabilities for AI agents. As organizations increasingly deploy

autonomous AI systems, identity models designed for human users and applications prove

insufficient. Agent identities address this gap by providing a specialized identity construct built

specifically for the unique requirements of AI agents operating at enterprise scale.

In its most fundamental form, an agent is an application that attempts to achieve a goal by

understanding its environment / context, making decisions and acting on them autonomously

using available tools. Agents can act with or without human intervention when provided with

proper goals or objectives.

Key components of an agent include:

**Model**: Model based agents have language models that serve as the centralized decision

maker for agent processes. Models can be general purpose, multimodal, or fine-tuned

based on specific agent architecture needs.

**Orchestration Layer**: The cyclical process that governs how the agent takes in

information, performs internal reasoning, and uses that reasoning to inform its next

action. This loop continues until the agent reaches its goal or a stopping point.

Complexity varies from simple decision rules to chained logic.

**Memory**: Memory in agents provides agents with more dynamic and up-to-date

information, ensuring responses are accurate and relevant. This memory allows

developers to provide more data in its original format to an agent, without requiring data

transformations, model retraining, or fine-tuning. It differs from typical large language

models (LLMs) that remain static, retaining only the knowledge they were initially trained

on.

**Tools**: Tools enable agents to interact with their environment and extend their capabilities.

Tools can include web search, database access, APIs, file systems, or integrations with

other software. Each tool requires careful consideration of security, permissions, and error

） **Important**

**Microsoft Entra Agent ID**

is currently in PREVIEW. This information relates to a

prerelease product that may be substantially modified before it's released. Microsoft

makes no warranties, expressed or implied, with respect to the information provided here.

**What is an agent**

handling. By using tools, agents can perform complex tasks, access information, and

control external systems, making them more effective and adaptable.

Agent workflows are in whole or part planned and driven autonomously and independently of

a human user. There are many types of agent workflows, from the ones initiated directly by a

user, to the ones that operate autonomously. Subcomponents, skills, tools, or APIs used in

those workflows might or might not themselves be agents.

The emergence of AI agents as autonomous enterprise systems introduces security and

operational challenges that existing identity models can't adequately address. Agent identities

help to address certain security challenges posed by AI agents, such as:

The need to distinguish operations performed by AI agents from operations performed

by workforce, customer, or workload identities.

Enabling AI agents to gain right-sized access across systems.

Preventing AI agents from gaining access to the most critical security roles and systems.

Scaling identity management to large numbers of AI agents that might be quickly created

and destroyed.

Application identities, typically represented as service principals in Microsoft Entra ID, were

designed for services built and maintained by organizations. These identities carry the

expectation of long-term stability, known ownership, and managed lifecycle.

Agents are often created dynamically through automation, user actions in tools like Copilot

Studio, or API orchestration. An agent might exist for minutes during a specific task, or might

be created and destroyed thousands of times per day as part of an automated workflow.

Managing this level of dynamism with existing application identities creates operational

complexity and security challenges.

Agent identities embrace this dynamic nature while providing appropriate security controls.

Organizations can create agent identities in bulk, apply consistent policies to all agents, and

retire agents without leaving orphaned credentials or permission assignments behind. The

identity model is designed for scale and ephemerality rather than permanence.

**Why agent identities exist**

**Agent identities versus application identities**

**Agent identities versus human user identities**

Human user identities are tied to authentication mechanisms humans use daily, such as

passwords, multifactor authentication, and passkeys. Human users have data associated with

them like mailboxes, teams, and organizational hierarchy.

Agent identities represent software systems, not human beings. They don't use human

authentication mechanisms. However, certain scenarios require agents to appear and operate

as if they're human users. For these scenarios, agent identities can be paired with agent users -

special Microsoft Entra user accounts that maintain a one-to-one relationship with their paired

agent identity. This distinction allows organizations to provide agents with a user identity when

necessary for system compatibility, while still maintaining clear separation and appropriate

security policies for AI-driven operations.

Agent identities provide the foundation for secure, scalable AI agent deployment by enabling

several key capabilities. Like other accounts, agent identities are primarily a means to access

apps, web services, and other systems in your organization. An AI agent can use agent

identities to:

**Access web services**. Agents can request access tokens from Microsoft Entra, and use

those tokens to access web services. Services can include Microsoft services such as

Microsoft Graph, services built by your organization, and services purchased from third-

party vendors.

**Autonomous access**. Agents can act autonomously, using access rights given directly to

the agent identity. Access rights can include Microsoft Graph permissions, Azure RBAC

roles, Microsoft Entra directory roles, Microsoft Entra app roles, and more.

**Delegated access**. Agents can act on behalf of human users, using access rights given to

the user. The user has control over which rights are delegated to the agent identity.

**Authenticate incoming messages**: Agents can accept requests from other clients, users,

and agents. Those requests can be secured using access tokens issued by Microsoft Entra

ID, allowing the agent to reliably identify the caller and make authorization decisions.

Several Microsoft products already use agent identities for authenticating AI agents. Two

examples include:

**Entra conditional access optimization agent**: When this agent is enabled in your tenant,

it's given an agent identity. The Microsoft Entra conditional access optimization agent

**What agent identities enable**

**Agent identities in practice**

then uses its agent identity to query Microsoft Entra systems and inspect the tenant's

configuration. All queries made by the agent are recorded as having been performed by

an AI agent. The agent's activity is subject to any security policies enforced for agent

identities. You can view the agent's identity in the Microsoft Entra admin center in the

**Agent identities** tab.

**Agents built in Copilot Studio**: In organizations that use Copilot Studio, users can quickly

create AI agents using Copilot Studio's low-code tools. Each time an AI agent is created,

the agent gets an agent identity in the Microsoft Entra tenant. The user who created the

agent is recorded as its sponsor. The agent can then use its agent identity to send/receive

chat messages to users, and connect to various systems like SharePoint or Dataverse. Any

authentication performed by these agents is logged in Microsoft Entra ID as AI agents

and viewable through the Microsoft Entra admin center.

Agent identity technical architecture and authentication

**Last updated on 11/18/2025**

**Next steps**

**What is the Microsoft Entra Agent**

**Registry?**

AI agents are rapidly becoming part of enterprise workflows, such as handling data retrieval,

orchestration, and autonomous decisions. For this reason, organizations face growing security

and compliance risks without centralized visibility and control over these agents. The Agent

Registry, as part of the Microsoft Entra Agent ID system, solves this challenge by providing an

extensible metadata repository that delivers a unified view of all deployed agents across

Microsoft platforms and non-Microsoft ecosystems.

To learn more about Agent Registry, review the following articles:

Register agents with the registry

Agent Registry collections

Manage collections

Agent Registry metadata and discoverability

Agent communication

Agent Registry integrates with Microsoft Entra Agent ID and Core Directory to enforce identity

and discovery policies, supports flexible mappings between agent cards and multiple agent

instances, and acts as the single source of truth for agent-related data. By combining

comprehensive visibility, rich metadata management, and collection-based policies, the registry

helps organizations secure agent discovery, apply Zero Trust principles, and maintain

governance across diverse environments. The Agent Registry delivers following critical

capabilities and benefits to customers:

**Comprehensive inventory and visibility**: Maintains an inventory of all deployed agents

running in your environment, whether or not they have an agent identity and supporting

external agents and providers.

**Discovery before access and policy enforcement**: Introduces built-in and custom

controls with agent collections and policies to reduce exposure and align with Zero Trust

principles.

**Rich metadata for governance across ecosystems**: Captures detailed metadata for each

agent, using open standards for collaboration and a flexible schema, enabling customers

to apply policies that limit discoverability and enforce security.

） **Important**

**Microsoft Entra Agent ID**

is currently in PREVIEW. This information relates to a

prerelease product that may be substantially modified before it's released. Microsoft

makes no warranties, expressed or implied, with respect to the information provided here.

The Agent Registry acts as the central store for agent-related data, including agent identities,

agent users, agent identity blueprints, and other identity attributes. Each agent instance from

an authoritative agent store, such as Copilot Studio, is registered in the Registry and linked to

an agent card manifest, which can represent multiple agents (1:N relationship). These

components are the manifests that provide the agent's metadata.

The registry then connects to the Microsoft Entra Core Directory, which enforces identity and

entitlement policies. The agent identity blueprints define reusable identity templates that can

map to multiple agent instances, enabling flexible identity governance. Each agent instance

also has a direct 1:1 relationship with an agent identity and optionally an agent user, ensuring

policy enforcement and lifecycle management. This capability mirrors human identity principles

in Microsoft Entra, providing a single source of truth for agent identity, metadata, and

governance while supporting one-to-many mappings for scalability.

The registry enables organizations to map diverse agent data sources, identify systems of

authority, and route users to the correct endpoints. The following diagram explains the

relationship between various key attributes.

The following table summarizes the core components of the Agent Registry:

**Registry Architecture & Components**

![](./assets/output_10_1.png)



ﾉ

**Expand table**

**Component**

**Purpose**

**Key Features**

**Benefits**

**Metadata**

**store**

Centralized agent

metadata repository

NoSQL-based, agent card

manifest support, real-

time updates

Scalable storage for rich agent

information and agent

communication compliance

**Collections**

Secure agent

categorization and

discovery control

enforcement

Baseline discovery

controls, custom

collections

Secure-by-default discovery

boundaries and clearer

governance

**Discovery**

**service**

Agent and capability

discovery APIs

Multi-dimensional search,

collection-aware filtering,

skill-based discovery

Enables secure, intelligent

agent-to-agent coordination

**Integration**

**layer**

Coordinates with

Microsoft and non-

Microsoft ecosystems

Ecosystem-wide security

operations and custom

workflows

Registry acts as a central store

to map your data across

different stores

Security is embedded at every layer of the Agent Registry:

**Identity Assurance**: Microsoft platforms fully integrated with the Microsoft Entra Agent ID

Platform automatically receive an agent identity and are enrolled in the registry.

**Runtime Enforcement**: Discovery policies are enforced dynamically when agents attempt

discovery, preventing unauthorized actions. This enforcement works together with

Microsoft Entra Agent ID, which controls authentication as well as discovery of agents

within the registry. Only agents with agent identity are allowed to discover other agents

in the registry, but they can find other agents without agent ID.

Publish agents to registry

Agent Registry metadata and discoverability

Agent Registry collections

What is an agent ID?

**Last updated on 11/18/2025**

**How Agent Registry enables security for AI**

**Related content**

**Create an agent identity blueprint**

An agent identity blueprint is used to create agent identities and request tokens using those

agent identities. This guide walks you through creating an agent identity blueprint using

Microsoft Graph REST API and Microsoft Graph PowerShell.

Before creating your agent identity blueprint, ensure you have:

understand agent identity blueprints

Privileged Role Administrator required to grant permissions

One of the following roles required to create a blueprint: Agent ID Developer or Agent ID

Administrator. Prefer the Agent ID Administrator role.

In this article, you use Microsoft Graph PowerShell or another client to create your agent

identity blueprint. You must authorize this client to create an agent identity blueprint. The

client requires one of the following Microsoft Graph permissions:

`AgentIdentityBlueprint.Create` (delegated permission)

`AgentIdentityBlueprint.Create` (application permission)

Only a Global Administrator or Privileged Role Administrator is able to grant these permissions

to the client. To grant these permissions, an administrator can:

Use the `Connect-MgGraph` command.

Run a script to create an `oAuth2PermissionGrant` or `appRoleAssignment` in the tenant.

Creating a functional agent identity blueprint in your tenant requires two steps:

1\. Create an `AgentIdentityBlueprint` in the tenant.

2\. Create an `AgentIdentityBlueprintPrincipal` in the tenant.

The principal created in this case is different from the agent identity used by the agent.

**Prerequisites**

**Authorize a client to create agent identity**

**blueprints**

**Create an agent identity blueprint**

Microsoft Graph API

First obtain an access token with the permission `AgentIdentityBlueprint.Create` . Once you

have an access token, make the following request.

HTTP

After you create an agent identity blueprint, record its `appId` for upcoming steps in the guide.

Next, create a service principal for your agent identity blueprint:

To create the service principal, you first need to obtain an access token with the

permission `AgentIdentityBlueprint.Create` . Once you have an access token, make the

following request:

HTTP

 **Tip**

Always include the OData-Version header when using @odata.type.

`POST https://graph.microsoft.com/beta/applications/`

`OData-Version` `: 4.0`

`Content-Type` `: application/json`

`Authorization` `: Bearer <token>`

`{`

`  "@odata.type": "Microsoft.Graph.AgentIdentityBlueprint",`

`  "displayName": "My Agent Identity Blueprint",`

`  "sponsors@odata.bind": [`

`    "https:` `//graph.microsoft.com/v1.0/users/<id>",`

`  ],`

`"owners@odata.bind": [`

`  "https:` `//graph.microsoft.com/v1.0/users/<id>"`

`]`

`}`

Microsoft Graph API

 **Tip**

Always include the OData-Version header when using @odata.type.

`POST `

`https://graph.microsoft.com/beta/serviceprincipals/graph.agentIdentityBlueprintP`

`rincipal`

`OData-Version` `: 4.0`

To request access tokens using the agent identity blueprint, you must add a client credential.

We recommend using a managed identity as a federated identity credential for production

deployments. For local development and testing, use a client secret.

Add a managed identity as a credential using the following request:

To send this request, you first need to obtain an access token with the permission

`AgentIdentityBlueprint.AddRemoveCreds.All` .

HTTP

In some tenants, other kinds of app credentials including `keyCredentials` ,

`passwordCredentials` , and `trustedSubjectNameAndIssuers` are also supported. These kinds of

credentials aren't recommended for production, but can be convenient for local development

and testing. To add a password credential:

`Content-Type` `: application/json`

`Authorization` `: Bearer <token>`

`{`

`  "appId": "<agent-blueprint-app-id>"`

`}`

**Configure credentials for the agent identity**

**blueprint**

Microsoft Graph API

`POST https://graph.microsoft.com/beta/applications/<agent-blueprint-object-`

`id>/federatedIdentityCredentials`

`OData-Version` `: 4.0`

`Content-Type` `: application/json`

`Authorization` `: Bearer <token>`

`{`

`    "name": "my-msi",`

`    "issuer": "https:` `//login.microsoftonline.com/<my-test-tenant-id>/v2.0",`

`    "subject": "<msi-principal-id>",`

`    "audiences": [`

`        "api:` `//AzureADTokenExchange"`

`    ]`

`}`

Microsoft Graph API

To send this request, you first need to obtain an access token with the delegated

permission `AgentIdentityBlueprint.AddRemoveCreds.All`

HTTP

Be sure to securely store the `passwordCredential` value generated. It can't be viewed after

initial creation. You can also use client certificates as credentials; see Add a certificate

credential.

To receive incoming requests from users and other agents, you need to define an identifier URI

and OAuth scope for your agent identity blueprint:

To send this request, you first need to obtain an access token with the permission

`AgentIdentityBlueprint.ReadWrite.All` .

HTTP

`POST https://graph.microsoft.com/beta/applications/<agent-blueprint-object-`

`id>/addPassword`

`Content-Type` `: application/json`

`Authorization` `: Bearer <token>`

`{`

`  "passwordCredential": {`

`    "displayName": "My Secret",`

`    "endDateTime": "2026-08-05T23:59:59Z"`

`  }`

`}`

**Configure identifier URI and scope**

Microsoft Graph API

`PATCH https://graph.microsoft.com/beta/applications/<agent-blueprint-object-id>`

`OData-Version` `: 4.0`

`Content-Type` `: application/json`

`Authorization` `: Bearer <token>`

`{`

`    "identifierUris": ["api:` `//<agent-blueprint-id>"],`

`    "api": {`

`      "oauth2PermissionScopes": [`

`        {`

`          "adminConsentDescription": "Allow the application to access the agent `

`on behalf of the signed-`  `in` ` user.",`

`          "adminConsentDisplayName": "Access agent",`

Create and delete agent identities

**Last updated on 11/18/2025**

`          "id": "<generate-a-guid>",`

`          "isEnabled": ` `true` `,`

`          "type": "User",`

`          "value": "access_agent"`

`        }`

`      ]`

`  }`

`}`

**Related content**

**Create agent identities in agent identity**

**platform**

After you create an agent identity blueprint, the next step is to create one or more agent

identities that represent AI agents in your test tenant. Agent identity creation is typically

performed when provisioning a new AI agent.

This article guides you through the process of building a simple web service that creates agent

identities via Microsoft Graph APIs.

If you want to quickly create agent identities for testing purposes, consider using this

PowerShell module for creating and using agent identities

.

Before creating agent identities, ensure you have:

Understand agent identities

A configured agent identity blueprint (see Create an agent blueprint). Record the agent

identity blueprint app ID from the creation process

A web service or application (running locally or deployed to Azure) that host the agent

identity creation logic

You use the agent identity blueprint to create each agent identity. Request an access token

from Microsoft Entra using your agent identity blueprint:

When using a managed identity as a credential, you must first obtain an access token

using your managed identity. Managed identity tokens can be requested from an IP

address locally exposed in the compute environment. Refer to the managed identity

documentation for details.

**Prerequisites**

**Get an access token using agent identity blueprint**

Microsoft Graph API

`GET http://169.254.169.254/metadata/identity/oauth2/token?api-version=2019-08-`

`01&resource=api://AzureADTokenExchange/.default`

`Metadata: True`

After you obtain a token for the managed identity, request a token for the agent identity

blueprint:

A `client_secret` parameter can also be used instead of `client_assertion` and

`client_assertion_type` , when a client secret is being used in local development.

Using the access token acquired in the previous step, you can now create agent identities in

your test tenant. Agent identity creation might occur in response to many different events or

triggers, such as a user selecting a button to create a new agent.

We recommend you create one agent identity for each agent, but you might choose a different

approach based on your needs.

Always include the OData-Version header when using @odata.type.

`POST https://login.microsoftonline.com/<my-test-tenant>/oauth2/v2.0/token`

`Content-Type: application/x-www-form-urlencoded`

`client_id=<agent-blueprint-id>`

`scope=https://graph.microsoft.com/.default`

`client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`client_assertion=<msi-token>`

`grant_type=client_credentials`

**Create an agent identity**

Microsoft Graph API

`POST `

`https://graph.microsoft.com/beta/serviceprincipals/Microsoft.Graph.AgentIdentity`

`OData-Version: 4.0`

`Content-Type: application/json`

`Authorization: Bearer <token>`

`{`

`    "displayName": "My Agent Identity",`

`    "agentIdentityBlueprintId": "<my-agent-blueprint-id>",`

`    "sponsors@odata.bind": [`

`        "https://graph.microsoft.com/v1.0/users/<id>",`

`        "https://graph.microsoft.com/v1.0/groups/<id>"`

`    ],`

`}`

When an agent is deallocated or destroyed, your service should also delete the associated

agent identity:

HTTP

**Last updated on 11/18/2025**

**Delete an agent identity**

Microsoft Graph API

`DELETE https://graph.microsoft.com/beta/serviceprincipals/<agent-identity-id>`

`OData-Version` `: 4.0`

`Content-Type` `: application/json`

`Authorization` `: Bearer <token>`

**Request agent tokens for autonomous**

**agents**

When agents perform operations using their own identity, rather than acting as a delegate of a

user, they're called _autonomous agents_. To perform operations, agents must first authenticate

with Microsoft Entra ID and obtain an access token using their agent identity (agent ID). This

article walks you through the process of requesting an access token for an agent identity in

Microsoft Entra ID using a two-step process. You'll:

Obtain a token for an agent identity blueprint.

Exchange the agent identity blueprint token for an agent ID token.

Before implementing agent token authentication, ensure you have:

An agent identity. You'll need the agent identity client ID.

Understand oauth protocols in Microsoft Entra Agent ID

An agent identity blueprint.

Get your client credential details. This could be your client secret, a certificate or a managed

identity that you are using as a federated identity credential.

Proceed to the next step

**Prerequisites**

**Configure your client credentials**

２ **Warning**

Client secrets shouldn't be used as client credentials in production environments for agent

identity blueprints due to security risks. Instead, use more secure authentication methods

such as **federated identity credentials (FIC) with managed identities** or client certificates.

These methods provide enhanced security by eliminating the need to store sensitive

secrets directly within your application configuration.

Microsoft Graph API

**Request a token for the agent identity blueprint**

When requesting the token for the agent identity blueprint, provide the agent ID's client ID in

the `fmi_path` parameter. Provide the `client_secret` parameter instead of `client_assertion`

and `client_assertion_type` when using a client secret as a credential during local

development. For certificates and managed identities, use `client_assertion` and

`client_assertion_type` .

HTTP

Once you have the agent identity blueprint token (T1), use it to request for the agent

identity token.

HTTP

Agent identity access token claims

Acquire token using Microsoft Entra SDK for agent ID

Microsoft Graph API

`POST https://login.microsoftonline.com/<my-test-tenant>/oauth2/v2.0/token`

`Content-Type` `: application/x-www-form-urlencoded`

`client_id=<agent-blueprint-client-id>`

`&scope=api:` `//AzureADTokenExchange/.default`

`&grant_type=client_credentials`

`&client_secret=<client-secret>`

`&fmi_path=<agent-identity-client-id>`

**Request an agent identity token**

Microsoft Graph API

`POST https://login.microsoftonline.com/<my-test-tenant>/oauth2/v2.0/token`

`Content-Type` `: application/x-www-form-urlencoded`

`client_id=<agent-identity-client-id>`

`&scope=https:` `//graph.microsoft.com/.default`

`&grant_type=client_credentials`

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion=<agent-blueprint-token-T1>`

**Related content**

**Last updated on 11/18/2025**

**Grant application permissions to an**

**autonomous agent**

Agents often need to take actions in Microsoft Graph and other web services that require a

Microsoft Entra ID application permission (represented as app roles). Autonomous agents need

to request these permissions from a Microsoft Entra ID administrator. This article walks through

the process of requesting application permissions from an admin using the agent identity

created in previous steps.

There are two ways to grant application permissions to an autonomous agent:

An admin can create an _appRoleAssignment_ by using Microsoft Graph APIs or PowerShell.

The agent can direct the admin to a consent page using an admin consent URL.

Before granting permissions to agent identities, ensure you have:

A created agent identity (see Create and delete agent identities)

Administrator privileges in your Microsoft Entra ID tenant

Understanding of the specific permissions your agent requires

Use the following steps to get an app role assignment.

1\. Obtain an access token with the delegated permissions `Application.Read.All` and

`AppRoleAssignment.ReadWrite.All` .

2\. Get the object ID of the resource service principal that you're trying to access. For

example, to find the Microsoft Graph service principal object ID:

a. Go to the Microsoft Entra admin center

.

b. Navigate to **Entra ID** --\> **Enterprise Applications**

c. Filter by Application type == Microsoft Applications

d. Search for **Microsoft Graph**.

3\. Get the unique ID of the app role you want to assign.

4\. Create the app role assignment:

**Prerequisites**

**Create an app role assignment via APIs**

Microsoft Graph API

HTTP

To grant delegated permissions, construct the authorization URL that is used to prompt the

administrator. The role parameter is used to specify the requested application permissions.

Be sure to use the agent identity client ID in the following request.

Bash

Agent implementations might redirect the admin to this URL in various ways, such as including

it in a message sent to the admin in a chat window. When the admin is redirected to this URL,

they're asked to sign in and grant consent to the permissions specified in the scope parameter.

At the moment you must use the redirect URI listed, which directs the admin to a blank page

after granting consent.

After you grant your application the required permissions, request a new agent access token

for the permissions to take effect.

Microsoft Graph permissions reference

Permissions and consent in the Microsoft identity platform

`POST https://graph.microsoft.com/v1.0/servicePrincipals/<agent-identity-`

`id>/appRoleAssignments`

`Authorization` `: Bearer <token>`

`Content-Type` `: application/json`

`{`

`  "principalId": "<agent-identity-id>",`

`  "resourceId": "<microsoft-graph-sp-object-id>",`

`  "appRoleId": "<app-role-id>"`

`}`

**Request authorization from a tenant administrator**

`https://login.microsoftonline.com/contoso.onmicrosoft.com/v2.0/adminconsent`

`?client_id=<agent-identity-client-id>`

`&role=User.Read.All`

`&redirect_uri=https://entra.microsoft.com/TokenAuthorize`

`&state=xyz123`

**Related content**

**Last updated on 11/18/2025**

**Request agent user tokens for autonomous**

**agents**

In addition to requesting tokens using an agent identity, autonomous agents can also

authenticate using an agent user. Agent users are a special type of user account in Microsoft

Entra purpose-built for use by agents. They're most commonly used when an agent needs to

connect to systems that require the existence of a user account. For instance, mailbox, teams

channel, or other user-specific resources.

This guide walks you through creating an agent user in a tenant and requesting tokens as the

agent user. Each agent identity can only have a single associated agent user, and each agent

user can only be associated with a single agent identity.

Understand agent users in Microsoft Entra Agent ID

A created agent identity blueprint and at least one agent identity as described in Create

and delete agent identities

To create agent users, your agent identity blueprint must be granted the application

permission `AgentIdUser.ReadWrite.IdentityParentedBy` in the tenant. You can obtain

authorization in one of two ways:

Request agent authorization. Be sure to use your agent identity blueprint as the

`client_id` , not the agent identity.

Manually create an appRoleAssignment in the tenant. Be sure to use the object ID of the

agent identity blueprint principal as the `principalId` value. Don't use the ID of your agent

identity blueprint.

If you wish to use a different client, not the agent identity blueprint, to create agent users, that

client needs to obtain the `AgentIdUser.ReadWrite.All` delegated or application permission

instead.

This section covers creating an agent user using your agent identity blueprint or other

approved client. The recommended way to create an agent user is using your agent identity

blueprint. You require an access token to create an agent user.

**Prerequisites**

**Get authorization**

**Create an agent user**

Once you have an access token with the necessary permission, make the following request:

HTTP

Once you have your agent user created, you don't need to configure anything else. These users

don't have any credentials and can only be authenticated using the protocol described in the

next sections.

Agent users behave like any other user account. Before you can request tokens using your

agent user, you need to authorize the agent identity to act on its behalf. You can authorize the

agent identity using admin authorization as described in Request authorization from Microsoft

Entra admin or manually create an `oAuth2PermissionGrant` using Microsoft Graph or Microsoft

Graph PowerShell.

For Microsoft Graph, your request is as shown in the following snippet:

HTTP

REST

`POST https://graph.microsoft.com/beta/users`

`OData-Version` `: 4.0`

`Content-Type` `: application/json`

`Authorization` `: Bearer <token>`

`{`

`  "@odata.type": "microsoft.graph.agentUser",`

`  "displayName": "New Agent User",`

`  "userPrincipalName": "agentuserupn@tenant.onmicrosoft.com",`

`  "identityParentId": "{agent-identity-id}",`

`  "mailNickname": "agentuserupn",`

`  "accountEnabled": ` `true`

`}`

**Grant consent to agent identity**

`POST https://graph.microsoft.com/v1.0/oauth2PermissionGrants`

`Authorization` `: Bearer {token}`

`Content-Type` `: application/json`

`{`

`  "clientId": "{agent-identity-id}",`

`  "consentType": "Principal",`

`  "principalId": "{agent-id-user-object-id}",`

`  "resourceId": "{ms-graph-service-principal-object-id}",`

For Microsoft Graph PowerShell, use the following script:

PowerShell

To authenticate an agent user, you need to follow a three-step process:

Get a token as the agent identity blueprint

Use that token to get another token as the agent identity

Use both previous tokens to get another token as the agent user.

First, request a token as the agent identity blueprint, as described in Request agent tokens.

Once you have your agent app token, use it to request a Federated Identity Credential

(FIC) for your agent identity:

HTTP

`  "scope": "Mail.Read"`

`}`

`Connect-MgGraph` ` -Scopes` ` ` `"DelegatedPermissionGrant.ReadWrite.All"` ` -TenantId` ` <`  `your-`

`test` `-tenant>`

`# Get the service principal for Microsoft Graph`

`$graphSp = ` `Get-MgServicePrincipal` ` -Filter` ` ` `"appId eq '00000003-0000-0000-c000-`

`000000000000'"`

`# Get the service principal for your client app`

`$clientSp = ` `Get-MgServicePrincipal` ` -Filter` ` ` `"appId eq '{agent-identity-id}'"`

`# Create the delegated permission grant`

`New-MgOauth2PermissionGrant` ` -BodyParameter` ` @{`

`    clientId    = $clientSp.Id`

`    consentType = ``"Principal"`

`    principalId = ``"{agent-id-user-object-id}"`

`    resourceId  = $graphSp.Id`

`    scope       = ``"Mail.Read"`

`}`

**Request agent user token**

REST

`POST https://login.microsoftonline.com/<my-test-tenant>/oauth2/v2.0/token`

`Content-Type` `: application/x-www-form-urlencoded`

`client_id=<agent-identity-id>`

`&scope=api:` `//AzureADTokenExchange/.default`

`&grant_type=client_credentials`

This example gives you an access token you can use to authenticate your agent user. To

use it, make a request like:

HTTP

This gives you a delegated access token you can use to call Microsoft Graph as your agent

user. You can use `user_id=<user-object-id>` instead of `username=<UPN>` for the user

identifier.

Request agent tokens

Request authorization from Microsoft Entra admin

Create and delete agent identities

Acquire token using Microsoft Entra SDK for agent ID

**Last updated on 11/18/2025**

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion=<agent-blueprint-token>`

`POST https://login.microsoftonline.com/<my-test-tenant>/oauth2/v2.0/token`

`Content-Type` `: application/x-www-form-urlencoded`

`client_id=<agent-identity-id>`

`&scope=https:` `//graph.microsoft.com/.default`

`&grant_type=user_fic`

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion=<agent-blueprint-token>`

`&user_id=<agent-user-object-id>`

`&user_federated_identity_credential=<agent-identity-token>`

**Related content**

**Authenticate users in interactive agents**

Agents often need take actions on behalf of users that use the agent. The first step to building

an interactive agent is to authenticate the user. This article walks through the process of

building a simple web service that authenticates a user. The agent identity blueprint is used to

secure the web service. Steps include:

1\. A client obtains an access token scoped for the agent identity blueprint.

2\. Validate that token in the agent's API.

3\. Extract claims about the user that can be used for authorization.

Agent identity blueprints. Record the agent identity blueprint app ID (client ID).

To authenticate a user, the client app (such as a frontend or mobile app) should initiate an

OAuth 2.0 authorization request to obtain a token where the audience is the agent identity

blueprint.

1\. Redirect the user to the Microsoft Entra ID authorization endpoint with the following

parameters:

HTTP

2\. Once the user signs in, your app receives an authorization code at the redirect URI. You

exchange it for an access token:

HTTP

**Prerequisites**

**Request a token for the agent identity blueprint**

`GET https://login.microsoftonline.com/<my-test-tenant>/oauth2/v2.0/authorize?`

`client_id=<client-id>`

`&response_type=code`

`&redirect_uri=<redirect_uri>`

`&response_mode=query`

`&scope=api://<agent-blueprint-id>/access_agent`

`&state=abc123`

`POST https://login.microsoftonline.com/<my-test-tenant>/oauth2/v2.0/token`

`Content-Type` `: application/x-www-form-urlencoded`

`client_id`  `=<client-id>`

`grant_type`  `=authorization_code`

`code`  `=<authorization_code>`

The JSON response contains an access token that can be used to access the agent's API.

The agent, typically exposed via a web API, must validate the access token. Always use an

approved library to perform token validation and should never implement your own token

validation code.

1\. Install the `Microsoft.Identity.Web` NuGet package:

HTTP

2\. In your ASP.NET Core web API project, implement Microsoft Entra ID authentication:

C#

3\. Configure authentication credentials in _appsettings.json_ file:

`redirect_uri`  `=<redirect_uri>`

`scope`  `=api://<agent-blueprint-id>/access_agent`

`client_secret`  `=<client-secret>  # Only ` `if` ` using a confidential` ` client`

**Validate the token in the agent's API**

`dotnet add package Microsoft.Identity.Web`

`// Program.cs`

`using` ` Microsoft.Identity.Web;`

`var` ` builder = WebApplication.CreateBuilder(args);`

`builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)`

`    .AddMicrosoftIdentityWebApi(builder.Configuration.GetSection(` `"AzureAd"` `));`

`var` ` app = builder.Build();`

`app.UseAuthentication();`

`app.UseAuthorization();`

２ **Warning**

Client secrets shouldn't be used as client credentials in production environments for agent

identity blueprints due to security risks. Instead, use more secure authentication methods

such as **federated identity credentials (FIC) with managed identities** or client certificates.

These methods provide enhanced security by eliminating the need to store sensitive

secrets directly within your application configuration.

JSON

For more information on Microsoft.Identity.Web, see official docs.

After you validate the access token, the agent can now identify the user and perform

authorization checks. This example API route extracts user claims from the access token and

returns them in the API response:

C#

Token claims

**Last updated on 11/18/2025**

`"AzureAd"` `: {`

`"Instance"` `: ``"https://login.microsoftonline.com/"` `,`

`"TenantId"` `: ``"<my-test-tenant>"` `,`

`"ClientId"` `: ``"<agent-blueprint-id>"` `,`

`"Audience"` `: ``"<agent-blueprint-id>"` `,`

`"ClientCredentials"` `: [`

`    {`

`    ``"SourceType"` `: ``"ClientSecret"` `,`

`    ``"ClientSecret"` `: ``"your-client-secret"`

`    }`

`]`

`}`

**Validate user claims**

`app.MapGet(` `"/hello-agent"` `, (HttpContext httpContext) =>`

`{   `

`    ` `var` ` claims = httpContext.User.Claims.Select(c => ` `new`

`    {`

`        Type = c.Type,`

`        Value = c.Value`

`    });`

`    ` `return` ` Results.Ok(claims);`

`})`

`.RequireAuthorization();`

**Related content**

**Configure user authorization for interactive**

**agents**

Agents often need to take actions on behalf of users that use the agent. To do so, interactive

agents need to request delegated authorization from the user using the OAuth protocol. This

article walks you through the process of requesting consent from a user using the agent

identity. Steps include:

Updating the agent identity blueprint with a redirect URI.

Constructing an authorization request and redirecting the user to Microsoft Entra ID.

Before requesting user authorization, ensure you have:

An agent identity(create-delete-agent-identities.md)

OAuth 2.0 authorization code flow

In order to support delegated permissions, your agent identity blueprint must be configured

with a valid redirect URI. This URI is where Microsoft Entra ID sends users after they grant or

deny consent to your agent.

To send this request, you first need to obtain an access token with the delegated

permission `AgentIdentityBlueprint.ReadWrite.All` .

HTTP

**Prerequisites**

**Register a redirect URI**

Microsoft Graph API

`PATCH https://graph.microsoft.com/beta/applications/<agent-blueprint-id>`

`OData-Version` `: 4.0`

`Content-Type` `: application/json`

`Authorization` `: Bearer <token>`

`{`

`  ``"web"` `: {`

`    ``"redirectUris"` `: [`

`      ``"https://myagentapp.com/authorize"`

`    ]`

Now that your agent identity blueprint has a valid redirect URI, you can construct the

authorization URL that is used to prompt the user to grant delegated permissions. The

authorization URL follows the OAuth 2.0 authorization code flow standard.

Be sure to use the agent identity client ID in the following request, not the ID of the agent

identity blueprint. Agent implementations might redirect the user to this URL in various ways,

such as including it in a message sent to the user in a chat window.

HTTP

When the user is redirected to this URL, they're asked to sign in and grant consent to the

permissions specified in the scope parameter. After you grant consent, the user is returned to

the specified redirect URI.

The key parameters in the authorization URL are:

`client_id` : Use the agent identity client ID (not the agent identity blueprint client ID)

`response_type` : Set to `none` for authorization code flow

`redirect_uri` : Must match exactly what you configured in the previous step

`scope` : Specify the delegated permissions you need (for example, `User.Read` )

`state` : Optional parameter for maintaining state between the request and callback

Sign-in users for basic interactive agent authentication

Request user tokens for implementing the On-Behalf-Of flow

Permissions and consent in the Microsoft identity platform for detailed OAuth concepts

`  }`

`}`

**Construct the authorization request URL**

`https://login.microsoftonline.com/contoso.onmicrosoft.com/oauth2/v2.0/authorize?`

`  client_id=<agent-identity-id>`

`  &response_type=none`

`  &redirect_uri=https%3A%2F%2Fmyagentapp.com%2Fauthorize`

`  &response_mode=query`

`  &scope=User.Read`

`  &state=xyz123`

**Related content**

**Last updated on 11/18/2025**

**Configure admin authorization for**

**interactive agents**

Agents often need to take actions on behalf of users that use the agent. To do so, interactive

agents need to request delegated authorization from the user using the OAuth protocol.

Agents can also request authorization from a Microsoft Entra ID administrator, who can grant

authorization to the agent for all users in their tenant.

This article walks through the process of requesting consent from an administrator using the

agent identity.

Before requesting admin authorization, ensure you have:

An agent identity

An agent application configured for your agent identity

Access token with `Application.ReadWrite.OwnedBy` delegated permission. Understand the

difference between delegated and application permissions

Administrator access to grant consent for application permissions

To grant delegated permissions, construct the authorization URL that is used to prompt the

administrator. Be sure to use the agent identity ID in the following request.

HTTP

Request agent tokens for implementing client credentials flow after consent

Configure user authorization for requesting delegated permissions

**Last updated on 11/18/2025**

**Prerequisites**

**Construct the authorization request URL**

`https://login.microsoftonline.com/contoso.onmicrosoft.com/v2.0/adminconsent`

`?client_id=<agent-identity-id>`

`&scope=User.Read`

`&redirect_uri=https://entra.microsoft.com/TokenAuthorize`

`&state=xyz123`

**Related content**

**Acquire user tokens for interactive agents**

After an interactive agent obtains user authorization, it needs to request access tokens that can

be used to call APIs on behalf of the user. This article walks you through implementing the On-

Behalf-Of (OBO) flow to obtain delegated access tokens for your interactive agent.

The OBO flow allows a web API to:

Receive an access token from a client.

Exchange it for a new access token for a downstream API like Microsoft Graph.

Use that new token to access protected resources on behalf of the original user.

Before requesting user tokens, ensure you have:

An agent identity

Completed user authorization as described in Configure user authorization

Access token with appropriate permissions for your agent identity

Whereas you could implement the OBO flow manually by following the protocol, we

recommend using the `Microsoft.Identity.Web` library, which simplifies the implementation.

1\. Install the required NuGet package:

Bash

2\. In your ASP.NET core web API project, update the Microsoft Entra ID authentication

implementation.

C#

**Prerequisites**

**Request user tokens**

`dotnet add package Microsoft.Identity.Web`

`dotnet add package Microsoft.Identity.Web.AgentIdentities`

`// Program.cs`

`using` ` Microsoft.AspNetCore.Authorization;`

`using` ` Microsoft.Identity.Abstractions;`

`using` ` Microsoft.Identity.Web;`

`using` ` Microsoft.Identity.Web.Resource;`

`using` ` Microsoft.Identity.Web.TokenCacheProviders.InMemory;`

`var` ` builder = WebApplication.CreateBuilder(args);`

3\. In the agent API, exchange the incoming access token for a new access token for the

agent identity. _Microsoft.Identity.Web_ takes care of validation of the incoming access

token, but is currently not updated to handle the on-behalf-of token exchange.

C#

If you're using the Microsoft Graph SDK, you can authenticate to Microsoft Graph using the

`GraphServiceClient` .

1\. Install the \*Microsoft.Identity.Web.GraphServiceClient that handles authentication for the

Graph SDK

`// With Microsoft.Identity.Web`

`builder.Services.AddMicrosoftIdentityWebApiAuthentication(builder.Configuration`

`)`

`    .EnableTokenAcquisitionToCallDownstreamApi();`

`builder.Services.AddAgentIdentities();`

`builder.Services.AddInMemoryTokenCaches();`

`var` ` app = builder.Build();`

`app.UseAuthentication();`

`app.UseAuthorization();`

`app.Run();`

`app.MapGet(` `"/agent-obo-user"` `, ` `async` ` (HttpContext httpContext) =>`

`{`

`   ` `string` ` agentid = ``"<your-agent-identity>"` `;`

`    ``// Get the service to call the downstream API (preconfigured in the `

`appsettings.json file)`

`    IAuthorizationHeaderProvider authorizationHeaderProvider = `

`httpContext.RequestServices.GetService<IAuthorizationHeaderProvider>()!;`

`    AuthorizationHeaderProviderOptions options = ` `new` ` `

`AuthorizationHeaderProviderOptions().WithAgentIdentity(agentid);`

`    ``// Request user token for the agent identity`

`    ` `string` ` authorizationHeaderWithUserToken = ` `await` ` `

`authorizationHeaderProvider.CreateAuthorizationHeaderForUserAsync([` `"https://gra`

`ph.microsoft.com/.default"` `], options);`

`    ` `var` ` response = ` `new` ` { header = authorizationHeaderWithUserToken };`

`    ` `return` ` Results.Json(response);`

`})`

`.RequireAuthorization();`

**Use Microsoft Graph SDK**

Bash

2\. In your ASP.NET core web API project, add the support for Microsoft Graph in your

service collection.

Bash

3\. Get a `GraphServiceClient` from the service provider and call Microsoft Graph APIs with

the agent identity

C#

Sign-in users

Request agent tokens

Microsoft identity platform and OAuth 2.0 On-Behalf-Of flow

**Last updated on 11/18/2025**

`dotnet add package Microsoft.Identity.Web.GraphServiceClient`

`services.AddMicrosoftGraph();`

`app.MapGet(` `"/agent-obo-user"` `, ` `async` ` (HttpContext httpContext) =>`

`{`

`    ` `string` ` agentIdentity = ``"<your-agent-identity>"` `;`

`    builder.Services.AddMicrosoftGraph();`

`    GraphServiceClient graphServiceClient = `

`httpContext.RequestServices.GetService<GraphServiceClient>()!;`

`    ` `var` ` me = ` `await` ` graphServiceClient.Me.GetAsync(r => `

`r.Options.WithAuthenticationOptions(`

`        o =>`

`        {`

`            o.WithAgentIdentity(agentIdentity);`

`        }));`

`    ` `return` ` me.UserPrincipalName;`

`})`

**Related content**

**Call a Microsoft Graph API from an agent**

**using .NET**

This article explains how to call a Microsoft Graph API from an agent using agent identities or

agent user.

To call an API from an agent, you need to obtain an access token that the agent can use to

authenticate itself to the API. We recommend using the _Microsoft.Identity.Web_ SDK for .NET to

call your web APIs. This SDK simplifies the process of acquiring and validating tokens. For other

languages, use the Microsoft Entra agent SDK for agent ID.

An agent identity with appropriate permissions to call the target API. You need a user for

the on-behalf-of flow.

An agent user with appropriate permissions to call the target API.

1\. Install the _Microsoft.Identity.Web.GraphServiceClient_ that handles authentication for the

Graph SDK and the _Microsoft.Identity.Web.AgentIdentities_ package to add support for

agent identities.

Bash

2\. Add the support for Microsoft Graph and agent identities in your service collection.

C#

**Prerequisites**

**Call a Microsoft Graph API**

`dotnet add package Microsoft.Identity.Web.GraphServiceClient`

`dotnet add package Microsoft.Identity.Web.AgentIdentities`

`using` ` Microsoft.Identity.Web;`

`var` ` builder = WebApplication.CreateBuilder(args);`

`// Add authentication (web app or web API)`

`builder.Services.AddAuthentication(OpenIdConnectDefaults.AuthenticationScheme)`

`    .AddMicrosoftIdentityWebApp(builder.Configuration.GetSection(` `"AzureAd"` `))`

`    .EnableTokenAcquisitionToCallDownstreamApi()`

`    .AddInMemoryTokenCaches();`

`// Add Microsoft Graph support`

`builder.Services.AddMicrosoftGraph();`

3\. Configure Graph and agent identity options in _appsettings.json_.

JSON

4\. You can now get the `GraphServiceClient` injecting it in your service or from the service

provider and call Microsoft Graph.

For agent identities, you can acquire either an app only token (autonomous agents) or an

on-behalf of user token (interactive agents) by using the `WithAgentIdentity` method. For

`// Add Agent Identities support`

`builder.Services.AddAgentIdentities();`

`var` ` app = builder.Build();`

`app.UseAuthentication();`

`app.UseAuthorization();`

`app.Run();`

２ **Warning**

Client secrets shouldn't be used as client credentials in production environments for

agent identity blueprints due to security risks. Instead, use more secure

authentication methods such as **federated identity credentials (FIC) with managed**

**identities** or client certificates. These methods provide enhanced security by

eliminating the need to store sensitive secrets directly within your application

configuration.

`{`

`  ``"AzureAd"` `: {`

`    ``"Instance"` `: ``"https://login.microsoftonline.com/"` `,`

`    ``"TenantId"` `: ``"<my-test-tenant>"` `,`

`    ``"ClientId"` `: ``"<agent-blueprint-client-id>"` `,`

`    ``"ClientCredentials"` `: [`

`      {`

`        ``"SourceType"` `: ``"ClientSecret"` `,`

`        ``"ClientSecret"` `: ``"your-client-secret"`

`      }`

`    ]`

`  },`

`  ``"DownstreamApis"` `: {`

`    ``"MicrosoftGraph"` `: {`

`      ``"BaseUrl"` `: ``"https://graph.microsoft.com/v1.0"` `,`

`      ``"Scopes"` `: [` `"User.Read"` `, ``"User.ReadBasic.All"` `]`

`    }`

`  }`

`}`

app only tokens, set the `RequestAppToken` property to `true` . For delegated on-behalf of

user tokens, don't set the `RequestAppToken` property or explicitly set it to `false` .

C#

For agent user identities, you can specify either User Principal Name (UPN) or Object

Identity (OID) to identify the agent user by using the `WithAgentUserIdentity` method.

C#

`// Get the GraphServiceClient`

`GraphServiceClient graphServiceClient = `

`serviceProvider.GetRequiredService<GraphServiceClient>();`

`string` ` agentIdentity = ``"agent-identity-guid"` `;`

`// Call Microsoft Graph APIs with the agent identity for app only scenario`

`var` ` applications = ` `await` ` graphServiceClient.Applications`

`    .GetAsync(r => r.Options.WithAuthenticationOptions(options =>`

`    {`

`        options.WithAgentIdentity(agentIdentity);`

`        options.RequestAppToken = ` `true` `; ``// Set to true for app only`

`    }));`

`// Call Microsoft Graph APIs with the agent identity for on-behalf of user `

`scenario`

`var` ` applications = ` `await` ` graphServiceClient.Applications`

`    .GetAsync(r => r.Options.WithAuthenticationOptions(options =>`

`    {`

`        options.WithAgentIdentity(agentIdentity);`

`        options.RequestAppToken = ` `false` `; ``// False to show it's on-behalf of `

`user`

`    }));`

`// Get the GraphServiceClient`

`GraphServiceClient graphServiceClient = `

`serviceProvider.GetRequiredService<GraphServiceClient>();`

`string` ` agentIdentity = ``"agent-identity-guid"` `;`

`// Call Microsoft Graph APIs with the agent user identity using UPN`

`string` ` userUpn = ``"user-upn"` `;`

`var` ` me = ` `await` ` graphServiceClient.Me`

`    .GetAsync(r => r.Options.WithAuthenticationOptions(options =>`

`        options.WithAgentUserIdentity(agentIdentity, userUpn)));`

`// Or using OID`

`string` ` userOid = ``"user-object-id"` `;`

`var` ` me = ` `await` ` graphServiceClient.Me`

`    .GetAsync(r => r.Options.WithAuthenticationOptions(options =>`

`        options.WithAgentUserIdentity(agentIdentity, userOid)));`

Call custom APIs

Call Azure SDKs

**Last updated on 11/18/2025**

**Related content**

**Call custom APIs from an agent using .NET**

There are multiple ways to call custom APIs from an agent. Depending on your scenario, you

can use either `IDownstreamApi` , `MicrosoftIdentityMessageHandler` , or

`IAuthorizationHeaderProvider` . This guide explains the different approaches for calling your

own protected APIs all the three ways.

To call an API from an agent, you need to obtain an access token that the agent can use to

authenticate itself to the API. We recommend using the _Microsoft.Identity.Web_ SDK for .NET to

call your web APIs. This SDK simplifies the process of acquiring and validating tokens. For other

languages, use the Microsoft Entra agent SDK for agent ID.

An agent identity with appropriate permissions to call the target API. You need a user for

the on-behalf-of flow.

An agent user with appropriate permissions to call the target API.

The following table helps you decide which approach to use. For most scenarios, we

recommend using `IDownstreamApi` .

**Approach**

**Complexity**

**Flexibility**

**Use Case**

`IDownstreamApi`

Low

Medium

Standard REST APIs with configuration

`MicrosoftIdentityMessageHandler`

Medium

High

HttpClient with Direct Injection (DI) and

composable pipeline

`IAuthorizationHeaderProvider`

High

Very High

Complete control over HTTP requests

`IDownstreamApi` is the preferred way to call a protected API among the three options. It's

highly configurable and requires minimal code changes. It also offers automatic token

acquisition.

Use `IDownstreamApi` when you need the following listed items:

**Prerequisites**

**Decide which approach to use based on your**

**scenario**

ﾉ

**Expand table**

Use IDownstreamApi

You're calling standard REST APIs

You want a configuration-driven approach

You need automatic serialization/deserialization

You want to write minimal code

After determining what works for you, proceed to call your custom web API.

1\. Install the required NuGet package:

Bash

2\. Configure token credential options and your APIs in _appsettings.json_.

JSON

**Call your API**

２ **Warning**

Client secrets shouldn't be used as client credentials in production environments for agent

identity blueprints due to security risks. Instead, use more secure authentication methods

such as **federated identity credentials (FIC) with managed identities** or client certificates.

These methods provide enhanced security by eliminating the need to store sensitive

secrets directly within your application configuration.

Use IDownstreamApi

`dotnet add package Microsoft.Identity.Web.DownstreamApi`

`dotnet add package Microsoft.Identity.Web.AgentIdentities`

`{`

`  ``"AzureAd"` `: {`

`    ``"Instance"` `: ``"https://login.microsoftonline.com/"` `,`

`    ``"TenantId"` `: ``"your-tenant-id"` `,`

`    ``"ClientId"` `: ``"your-blueprint-id"` `,`

`    ``"ClientCredentials"` `: [`

`      {`

`        ``"SourceType"` `: ``"ClientSecret"` `,`

`        ``"ClientSecret"` `: ``"your-client-secret"`

`      }`

`    ]`

`  },`

`  ``"DownstreamApis"` `: {`

3\. Configure your services to add downstream API support:

C#

4\. Call your protected API using `IDownstreamApi` . When calling the API, you can specify

the agent identity or agent user identity using the `WithAgentIdentity` or

`WithAgentUserIdentity` methods. `IDownstreamApi` automatically handles token

acquisition and attaches the access token to the request.

For `WithAgentIdentity` , you either call the API using an app only token

(autonomous agent) or on-behalf of a user (interactive agent).

C#

`    ``"MyApi"` `: {`

`      ``"BaseUrl"` `: ``"https://api.example.com"` `,`

`      ``"Scopes"` `: [` `"api://my-api-client-id/read"` `, ``"api://my-api-client-`

`id/write"` `],`

`      ``"RelativePath"` `: ``"/api/v1"` `,`

`      ``"RequestAppToken"` `: ` `false`

`    }`

`  }`

`}`

`using` ` Microsoft.Identity.Web;`

`var` ` builder = WebApplication.CreateBuilder(args);`

`// Add authentication`

`builder.Services.AddAuthentication(OpenIdConnectDefaults.AuthenticationSche`

`me)`

`    `

`.AddMicrosoftIdentityWebApp(builder.Configuration.GetSection(` `"AzureAd"` `))`

`    .EnableTokenAcquisitionToCallDownstreamApi()`

`    .AddInMemoryTokenCaches();`

`// Register downstream APIs`

`builder.Services.AddDownstreamApis(`

`    builder.Configuration.GetSection(` `"DownstreamApis"` `));`

`// Add Agent Identities support`

`builder.Services.AddAgentIdentities();`

`builder.Services.AddControllersWithViews();`

`var` ` app = builder.Build();`

`app.UseAuthentication();`

`app.UseAuthorization();`

`app.MapControllers();`

`app.Run();`

For `WithAgentUserIdentity` , you can specify either User Principal Name (UPN) or

Object Identity (OID) to identify the agent user.

C#

`using` ` Microsoft.Identity.Abstractions;`

`using` ` Microsoft.AspNetCore.Authorization;`

`using` ` Microsoft.AspNetCore.Mvc;`

`[`  `Authorize` `]`

`public`  ` `  `class`  ` `  `ProductsController` ` : ` `Controller`

`{`

`    ` `private`  ` `  `readonly` ` IDownstreamApi _api;`

`    ` `public`  ` `  `ProductsController` `(IDownstreamApi api)`

`    {`

`        _api = api;`

`    }`

`    ``// GET request for app only token scenario for agent identity`

`    ` `public`  ` `  `async` ` Task<IActionResult> ` `Index` `()`

`    {`

`        ` `string` ` agentIdentity = ``"<your-agent-identity>"` `;`

`        ` `var` ` products = ` `await` ` _api.GetForAppAsync<List<Product>>(`

`            ``"MyApi"` `,`

`            ``"products"` `,`

`            options => options.WithAgentIdentity(agentIdentity));`

`        ` `return` ` View(products);`

`    }`

`    ``// GET request for on-behalf of user token scenario for agent `

`identity`

`    ` `public`  ` `  `async` ` Task<IActionResult> ` `UserProducts` `()`

`    {`

`        ` `string` ` agentIdentity = ``"<your-agent-identity>"` `;`

`        ` `var` ` products = ` `await` ` _api.GetForUserAsync<List<Product>>(`

`            ``"MyApi"` `,`

`            ``"products"` `,`

`            options => options.WithAgentIdentity(agentIdentity));`

`        ` `return` ` View(products);`

`    }`

`}`

`using` ` Microsoft.Identity.Abstractions;`

`using` ` Microsoft.AspNetCore.Authorization;`

`using` ` Microsoft.AspNetCore.Mvc;`

`[`  `Authorize` `]`

`public`  ` `  `class`  ` `  `ProductsController` ` : ` `Controller`

Microsoft identity web

Call Microsoft Graph APIs

Call Azure SDKs

**Last updated on 11/18/2025**

`{`

`    ` `private`  ` `  `readonly` ` IDownstreamApi _api;`

`    ` `public`  ` `  `ProductsController` `(IDownstreamApi api)`

`    {`

`        _api = api;`

`    }`

`    ``// GET request for agent user identity using UPN`

`    ` `public`  ` `  `async` ` Task<IActionResult> ` `Index` `()`

`    {`

`        ` `string` ` agentIdentity = ``"<your-agent-identity>"` `;`

`        ` `string` ` userUpn = ``"user@contoso.com"` `;`

`        ` `var` ` products = ` `await` ` _api.GetForUserAsync<List<Product>>(`

`            ``"MyApi"` `,`

`            ``"products"` `,`

`            options => options.WithAgentUserIdentity(agentIdentity, `

`userUpn));`

`        ` `return` ` View(products);`

`    }`

`    ``// GET request for agent user identity using OID`

`    ` `public`  ` `  `async` ` Task<IActionResult> ` `UserProducts` `()`

`    {`

`        ` `string` ` agentIdentity = ``"<your-agent-identity>"` `;`

`        ` `string` ` userOid = ``"user-object-id"` `;`

`        ` `var` ` products = ` `await` ` _api.GetForUserAsync<List<Product>>(`

`            ``"MyApi"` `,`

`            ``"products"` `,`

`            options => options.WithAgentUserIdentity(agentIdentity, `

`userOid));`

`        ` `return` ` View(products);`

`    }`

`}`

**Related content**

**Call Azure services from your agent using**

**.NET Azure SDK**

This article guides you on how to call Azure services from your agent. To authenticate to Azure

services such as Azure Storage or Azure Key Vault using agent identities, use the

`MicrosoftIdentityTokenCredential` class from _Microsoft.Identity.Web.Azure_. The

`MicrosoftIdentityTokenCredential` class implements Azure SDK's `TokenCredential` interface,

enabling seamless integration between _Microsoft.Identity.Web_ and Azure SDK clients.

To call an API from an agent, you need to obtain an access token that the agent can use to

authenticate itself to the API. We recommend using the _Microsoft.Identity.Web_ SDK for .NET to

call your web APIs. This SDK simplifies the process of acquiring and validating tokens. For other

languages, use the Microsoft Entra agent SDK for agent ID.

An agent identity with appropriate permissions to call the target API. You need a user for

the on-behalf-of flow.

An agent user with appropriate permissions to call the target API.

1\. Install the Azure integration package and the _Microsoft.Identity.Web.AgentIdentities_

package to add support for agent identities.

Bash

2\. Install the Azure SDK package you want to use, for example, Azure Storage:

Bash

3\. Configure your services to add Azure token credential support:

C#

**Prerequisites**

**Implementation steps**

`dotnet add package Microsoft.Identity.Web.Azure`

`dotnet add package Microsoft.Identity.Web.AgentIdentities`

`dotnet add package Azure.Storage.Blobs`

`using` ` Microsoft.Identity.Web;`

4\. Configure Azure token credential options in _appsettings.json_

JSON

5\. Acquire a token credential from the service provider and use it with Azure SDK clients.

`var` ` builder = WebApplication.CreateBuilder(args);`

`// Add authentication`

`builder.Services.AddAuthentication(OpenIdConnectDefaults.AuthenticationScheme)`

`    .AddMicrosoftIdentityWebApp(builder.Configuration.GetSection(` `"AzureAd"` `))`

`    .EnableTokenAcquisitionToCallDownstreamApi()`

`    .AddInMemoryTokenCaches();`

`// Add Azure token credential support`

`builder.Services.AddMicrosoftIdentityAzureTokenCredential();`

`builder.Services.AddControllersWithViews();`

`var` ` app = builder.Build();`

`app.UseAuthentication();`

`app.UseAuthorization();`

`app.MapControllers();`

`app.Run();`

２ **Warning**

Client secrets shouldn't be used as client credentials in production environments for

agent identity blueprints due to security risks. Instead, use more secure

authentication methods such as **federated identity credentials (FIC) with managed**

**identities** or client certificates. These methods provide enhanced security by

eliminating the need to store sensitive secrets directly within your application

configuration.

`{`

`  ``"AzureAd"` `: {`

`    ``"Instance"` `: ``"https://login.microsoftonline.com/"` `,`

`    ``"TenantId"` `: ``"<your-tenant>"` `,`

`    ``"ClientId"` `: ``"<agent-blueprint-id>"` `,`

`   // Other client creedentials available. See <https://aka.ms/ms-id-`

`web/client-credentials>`

`    ``"ClientCredentials"` `: [`

`      {`

`        ``"SourceType"` `: ``"ClientSecret"` `,`

`        ``"ClientSecret"` `: ``"your-client-secret"`

`      }`

`    ]   `

`  }`

`}`

a. For agent identities, you can acquire either an app only token (autonomous agents) or

an on-behalf of user token (interactive agents) by using the `WithAgentIdentity`

method. For app only tokens, set the `RequestAppToken` property to `true` . For delegated

on-behalf of user tokens, don't set the `RequestAppToken` property or explicitly set it to

`false` .

C#

`using` ` Microsoft.Identity.Web;`

`public`  ` `  `class`  ` `  `AgentService`

`{`

`    ` `private`  ` `  `readonly` ` MicrosoftIdentityTokenCredential _credential;`

`    ` `public`  ` `  `AgentService` `(MicrosoftIdentityTokenCredential credential)`

`    {`

`        _credential = credential;`

`    }`

`    ``// Call Azure service with the agent identity for app only scenario`

`    ` `public`  ` `  `async` ` Task<List<`  `string`  `>> ListBlobsForAgentAsync(`  `string` ` `

`agentIdentity)`

`    {`

`        ``// Configure for agent identity`

`        ` `string` ` agentIdentity = ``"agent-identity-guid"` `;`

`        _credential.Options.WithAgentIdentity(agentIdentity);`

`        _credential.Options.RequestAppToken = ` `true` `;`

`        ` `var` ` blobClient = ` `new` ` BlobServiceClient(`

`            ` `new` ` Uri(` `"https://myaccount.blob.core.windows.net"` `),`

`            _credential);`

`        ` `var` ` container = blobClient.GetBlobContainerClient(` `"agent-data"` `);`

`        ` `var` ` blobs = ` `new` ` List<`  `string`  `>();`

`        ` `await`  ` `  `foreach` ` (`  `var` ` blob ` `in` ` container.GetBlobsAsync())`

`        {`

`            blobs.Add(blob.Name);`

`        }`

`        ` `return` ` blobs;`

`    }`

`    ``// Call Azure service with the agent identity for on-behalf of user `

`scenario`

`    ` `public`  ` `  `async` ` Task<List<`  `string`  `>> ListBlobsForAgentAsync(`  `string` ` `

`agentIdentity)`

`    {`

`        ``// Configure for agent identity`

`        ` `var` ` blobClient = ` `new` ` BlobServiceClient(`

`            ` `new` ` Uri(` `"https://myaccount.blob.core.windows.net"` `));`

b. You can also acquire a token for an agent user. To do this, you can use either User

Principal Name (UPN) or Object Identity (OID) to identify the agent user.

For object ID:

C#

`        ` `var` ` container = blobClient.GetBlobContainerClient(` `"agent-data"` `);`

`        ` `var` ` blobs = ` `new` ` List<`  `string`  `>();`

`        ` `await`  ` `  `foreach` ` (`  `var` ` blob ` `in` ` container.GetBlobsAsync())`

`        {`

`            blobs.Add(blob.Name);`

`        }`

`        ` `return` ` blobs;`

`    }`

`}`

`using` ` Microsoft.Identity.Web;`

`public`  ` `  `class`  ` `  `AgentService`

`{`

`    ` `private`  ` `  `readonly` ` MicrosoftIdentityTokenCredential _credential;`

`    ` `public`  ` `  `AgentService` `(MicrosoftIdentityTokenCredential credential)`

`    {`

`        _credential = credential;`

`    }`

`    ``// Use object ID to identify the agent user`

`    ` `public`  ` `  `async` ` Task<List<`  `string`  `>> ListBlobsForAgentAsync(`  `string` ` `

`agentIdentity)`

`    {`

`        ``// Configure for agent identity`

`        ` `string` ` agentIdentity = ``"agent-identity-guid"` `;`

`        ` `string` ` userOid = ``"user-object-id"` `;`

`        _credential.Options.WithAgentUserIdentity(agentIdentity, userOid);`

`        ` `var` ` blobClient = ` `new` ` BlobServiceClient(`

`            ` `new` ` Uri(` `"https://myaccount.blob.core.windows.net"` `),`

`            _credential);`

`        ` `var` ` container = blobClient.GetBlobContainerClient(` `"agent-data"` `);`

`        ` `var` ` blobs = ` `new` ` List<`  `string`  `>();`

`        ` `await`  ` `  `foreach` ` (`  `var` ` blob ` `in` ` container.GetBlobsAsync())`

`        {`

`            blobs.Add(blob.Name);`

`        }`

`        ` `return` ` blobs;`

`    }`

Call custom APIs

Call Microsoft Graph

**Last updated on 11/18/2025**

`    ``// Use UPN to identify the agent user\`

`    ` `public`  ` `  `async` ` Task<List<`  `string`  `>> ListBlobsForAgentAsync(`  `string` ` `

`agentIdentity)`

`    {`

`        ``// Configure for agent identity`

`        ` `string` ` agentIdentity = ``"agent-identity-guid"` `;`

`        ` `string` ` userUpn = ``"user@contoso.com"` `;`

`        _credential.Options.WithAgentUserIdentity(agentIdentity, userUpn);`

`        ` `var` ` blobClient = ` `new` ` BlobServiceClient(`

`            ` `new` ` Uri(` `"https://myaccount.blob.core.windows.net"` `),`

`            _credential);`

`        ` `var` ` container = blobClient.GetBlobContainerClient(` `"agent-data"` `);`

`        ` `var` ` blobs = ` `new` ` List<`  `string`  `>();`

`        ` `await`  ` `  `foreach` ` (`  `var` ` blob ` `in` ` container.GetBlobsAsync())`

`        {`

`            blobs.Add(blob.Name);`

`        }`

`        ` `return` ` blobs;`

`    }`

`}`

**Related content**

**Acquire tokens and call downstream APIs**

**with Microsoft Entra SDK for Agent ID**

The Microsoft Entra SDK for Agent ID is a containerized web service that handles token

acquisition, validation, and downstream API calls for agents. This SDK communicates with your

application through HTTP APIs, providing consistent integration patterns regardless of your

technology stack. Instead of embedding identity logic directly in your application code, the

Microsoft Entra SDK for Agent ID manages token acquisition, validation, and API calls through

standard HTTP requests.

Before you begin, ensure you have:

Set up the Microsoft Entra SDK for Agent ID

An agent identity. Record the agent identity client ID.

An agent identity blueprint. Record the agent identity blueprint client ID.

Necessary permissions configured in Microsoft Entra ID

Deploy the Microsoft Entra SDK for Agent ID as a containerized service in your environment.

Follow the instructions in the Set up the Microsoft Entra SDK for Agent ID guide to configure

the service with your agent identity details.

Follow these steps to configure your Microsoft Entra SDK for Agent ID settings:

**Prerequisites**

**Deploy your containerized service**

**Configure your Microsoft Entra SDK for Agent ID**

**settings**

２ **Warning**

Client secrets shouldn't be used as client credentials in production environments for agent

identity blueprints due to security risks. Instead, use more secure authentication methods

such as **federated identity credentials (FIC) with managed identities** or client certificates.

These methods provide enhanced security by eliminating the need to store sensitive

secrets directly within your application configuration.

1\. Set up the necessary components in Microsoft Entra ID. Ensure you register your

application in the Microsoft Entra ID tenant.

2\. Configure your client credentials. This credential can be a client secret, a certificate, or a

managed identity that you're using as a federated identity credential.

3\. If you're calling a downstream API, ensure that the necessary permissions are granted.

Calling a custom web API requires you to provide the API registration details in the SDK

configuration.

For more information, see Configure your Microsoft Entra SDK for AgentID settings

These are the steps to acquire tokens using the Microsoft Entra SDK for Agent ID:

1\. Acquire token using the Microsoft Entra SDK for Agent ID. This varies based on whether

the agent is operating autonomously or on behalf of a user. There are three scenarios to

consider:

Autonomous agents: Agents operating on their own behalf using service principals

created for agents (autonomous).

Autonomous agent user: Agents operating on their own behalf using user principals

created specifically for agents (for instance agents having their own mailbox).

Interactive agents: Agents operating on behalf of human users.

Specify the downstream API by including its name in the request URL based on your

agent ID SDK configuration. The authorization header endpoint takes the format

`/AuthorizationHeader/{serviceName}` where `serviceName` is the name of the downstream

API configured in the SDK settings.

2\. To acquire an app only token for an autonomous agent, you provide the agent identity

client ID in the request.

Bash

3\. To acquire token for an autonomous agent user, provide either the user object ID or User

Principal Name but not both. This means providing either `AgentUsername` or `AgentUserId` .

Providing both causes a validation error. You must also provide the `AgentIdentity` to

**Acquire tokens using the Microsoft Entra SDK for**

**Agent ID**

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-id-client-ID>`

`Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

specify which agent identity to use for token acquisition. If the agent identity parameter is

missing, the request fails with a validation error.

Bash

Bash

4\. For interactive agents, use the on-behalf of flow. The agent first validates the user token

granted to it before acquiring the resource token to call the downstream API.

Agent web API receives user token from the calling application and validates the token

via the agent ID SDK `/Validate` endpoint Acquire token for downstream APIs by calling

`/AuthorizationHeader` with only the `AgentIdentity` and the incoming authorization

header

Bash

When obtaining the authorization header for calling a downstream API, the Microsoft Entra

SDK for Agent ID returns the `Authorization` header value that can be used directly in your API

calls.

You can use this header to call the downstream API. The web API should validate the token by

calling the `/Validate` endpoint of the Microsoft Entra SDK for Agent ID. This endpoint returns

token claims for further authorization decisions.

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-id-client-id>&AgentUserId=`

`<agent-user-object-id>`

`Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-id-client-`

`id>&AgentUsername=<agent-user-principal-name>`

`Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

`# Step 1: Validate incoming user token`

`GET /Validate`

`Authorization: Bearer <user-token>`

`# Step 2: Get authorization header on behalf of the user`

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-client-id>`

`Authorization: Bearer <user-token>`

**Call an API**

**Related content**

Python implementation of Microsoft Entra SDK for Agent ID

TypeScript implementation of Microsoft Entra SDK for Agent ID

Call a downstream API - Microsoft Entra SDK for agent ID docs

**Last updated on 11/18/2025**

**View and manage agent identities in your**

**tenant**

Microsoft Entra admin center provides you with a centralized interface to view and manage

your agent identities. This comes with the ability to perform various actions like searching,

filtering, sorting, and selecting multiple agent identities to disable.

To view and manage your agent identity blueprint principals, see View and manage agent

identity blueprints using Microsoft Entra admin center.

To view and manage agents registered in the Agent Registry without an identity, see

manage agent identity blueprints with no identities.

To view agent identities in your Microsoft Entra tenant, you need:

A Microsoft Entra user account. If you don't already have one, you can Create an account

for free

.

To manage agent identities in your Microsoft Entra tenant, you need:

Agent ID Administrator or Cloud Application Administrator role

You can also manage your agent identity if you're the owner of that agent identity, with

or without the above roles.

To view agent identities in your tenant:

1\. Sign in to the Microsoft Entra admin center

2\. Browse to **Entra ID** \> **Agent ID** \> **All agent identities**.

3\. Select any agent identity you'd like to manage.

This page contains a list of all agent identities in your organization. This includes both agent

identity objects and agents using a service principal.

To search for an agent identity, enter either the **name** or **object ID** of the agent identity

you want to find in the search box.

**Prerequisites**

**View a list of agent identities**

**Search for an agent identity**

To look up an agent identity by its **Agent Blueprint ID**, add the **Agent Blueprint ID** filter.

You can further refine the list using filters based on various criteria.

You can select an agent identity from this list to see information like:

An overview of the agent identity, including:

The name, description, and logo for your agent identity

The status of that agent identity, and the ability to enable/disable a given agent

identity

The link to the parent agent identity blueprint

The list of owners and sponsors for that agent identity

The agent's access via this agent identity's granted permissions and Microsoft Entra roles

Audit logs and sign-in logs for that agent identity

To customize your view of agent identities, you can change filters or select which columns are

shown for each agent identity. Not all columns are shown by default. To see all available

columns and edit shown columns, select the **Choose columns** button. The table columns and

their filter options are as follows:

**Column**

**Name**

**Description**

**Sortable**

**Filterable**

**Special notes**

**Name**

Display name of the agent

identity

✓

✓

Primary search field; clickable to

view details of the agent identity

**Created On**

Date when the agent was

created

✓

✓

Filter by "Last N days"

**Status**

Current operational state

(Active, or Disabled)

✓

✓

**Object ID**

Unique identifier for agent

identity

✗

✓

**View**

**Access**

Direct link to agent identity's

permissions

✗

✗

Navigates to the Agent's Access

pane, on Permissions tab

**Agent**

**Blueprint**

**ID**

Unique identifier for the agent

identity blueprint of this agent

identity

✗

✓

Will be blank for agents using

service principals

**Owners**

Direct link to the owners and

sponsors for a given agent

✗

✗

**Select viewing options**

ﾉ

**Expand table**

**Column**

**Name**

**Description**

**Sortable**

**Filterable**

**Special notes**

identity

**Uses agent**

**identity**

Represents whether or not this

agent has an agent identity

object, or utilizes a service

principal

✗

✗

If the answer is "yes," then it

uses an agent identity object. If

"no" this agent utilizes a service

principal

To disable an agent identity while in this page:

1\. Select one or more agents from the list by checking the box next to their logo.

2\. Select the **Disable** button in the toolbar.

You might also navigate into a single agent identity, and disable it there.

**Last updated on 11/18/2025**

**Disable an agent identity**

**View and manage agent identity blueprints**

**in your tenant**

Microsoft Entra Admin Center allows you to view all agent identity blueprint principals in your

tenant. You can perform various actions like searching, filtering, sorting, and selecting multiple

agent identity blueprint principals to disable.

To view your agent identity blueprint principals, follow these steps:

1\. Sign in to the Microsoft Entra admin center

.

2\. In the left-hand navigation pane, select **Entra ID** \> **Agent identities** \> **All agent identities**.

3\. Select **View agent blueprint** in the upper right of the command bar.

4\. Select any agent identity blueprint principal you want to manage.

1\. Enter either the **name** or **object ID** of the agent identity blueprint principal you want to

find in the search box.

2\. To look up an agent identity by its **Agent Blueprint ID**, add the **Agent Blueprint ID** filter.

3\. You can further refine the list using filters based on various criteria.

To customize your view of agent identity blueprint principals, you can change filters or select

which columns are shown for each agent identity. To see all available columns and edit shown

columns, select the **Choose columns** button. The table columns and their filter options are as

follows:

**Column**

**Name**

**Description**

**Sortable**

**Filterable**

**Special notes**

**Name**

Display name of the agent

identity blueprint principal

✓

✓

Primary search field; clickable

to view details of the agent

identity blueprint principal

**Navigate to your agent identity blueprint principal**

**list**

**Search for an agent identity blueprint principal**

**Select viewing options**

ﾉ

**Expand table**

**Column**

**Name**

**Description**

**Sortable**

**Filterable**

**Special notes**

**Agent**

**identities**

The number of child agent

identities created by the agent

blueprint principal

✗

✗

Select this to see a list of linked

child agent identities for that

agent identity blueprint

principal

**Status**

Current operational state

(Active, or Disabled)

✓

✓

**Agent**

**Blueprint**

**ID**

Unique identifier for the agent

identity blueprint of this agent

identity blueprint principal

✗

✓

**Object ID**

Unique identifier for agent

identity

✗

✓

Use the following steps to manage an agent identity blueprint principal in your tenant:

1\. Select the agent identity blueprint principal you want to manage. It opens the agent

identity blueprint principal's management page.

2\. View your agent identity blueprint principal details. The page provides you with

information about your app pulled from the agent registry. This information includes:

Your agent identity blueprint principal name and logo

Your agent description

Your agent status. It indicates whether your agent is active or disabled

Your agent blueprint ID and object ID

3\. To manage this agent identity blueprint principal, this page provides you with several tabs

to manage different aspects of your agent identity blueprint principal. These tabs include:

**Linked agent identities**: View and manage the agent identities associated with the

agent identity blueprint principal.

**Blueprint's access**: View, manage, and revoke the permissions assigned to the agent

identity blueprint principal.

**Owners and sponsors**: View and manage the owners and sponsors of the agent

identity blueprint principal. Owners are technical administrators responsible for

operational management, while sponsors are business owners accountable for the

agent's purpose and lifecycle decisions. For more information, see owners, sponsors,

and managers.

**Manage agent identity blueprint principals**

**Audit logs**: View the audit logs related to the agent identity blueprint principal. It

includes actions taken on the agent, such as changes to permissions, access reviews,

and other administrative activities. It helps you monitor and track changes for

security and compliance purposes. For more information, see view audit logs for

agents.

**Sign-in logs**. View the sign-in logs for the agent identity blueprint principal. For

more information, see view sign-in logs for agents.

4\. To disable an agent identity blueprint principal, select the **Disable** button in the top

command bar.

**Last updated on 11/18/2025**

**Manage Agents in end user experience**

**(Preview)**

The Manage agents feature in Microsoft Entra lets you view, and control, agent identities you

own or sponsor. Agents identities are special identities, such as bots or automated processes,

that act on behalf of users or teams. With the manage agents feature, you can easily see which

agents you’re responsible for, review their details, and take action to enable, disable, or request

access for them.

1\. Sign in to the My Account end user portal

as either an owner or sponsor of at least one

agent identity.

2\. In the left menu, select **Manage agents (Preview)**.

７ **Note**

This feature is in public preview. Functionality might change before general availability.

**License requirements**

） **Important**

Microsoft Entra Agent ID is part of Microsoft Agent 365, available now in Frontier, the

Microsoft early access program for the latest AI innovations. For more information, see

**Microsoft Entra Agent ID**

.

**Manage agents as an agent identity owner or**

**sponsor**

７ **Note**

This will only appear if you're an owner or sponsor of at least one agent identity.

3\. Choose either the **Agents you sponsor** or **Agents you own tab** to view your agents.

![](./assets/output_65_1.png)

4\. Select an agent to view details about it.

![](./assets/output_65_2.png)

1\. To disable an agent, select it from the list and choose **Disable agent**. This blocks users

from being able to access it and prevents it from being issued tokens.

2\. To re-enable, select the agent that is disabled and choose **Enable agent**. This allows users

to access it, and allows it to be issued tokens.

**Enable or Disable an agent**

If an agent needs other access packages, Request an access package on behalf of an

agent identity (Preview)

**Last updated on 11/18/2025**

**Next Steps**

**Register agents to the Agent Registry**

Registering agents in Microsoft Entra Agent Registry enables centralized visibility and

management across your organization. It provides a unified view of all agents, including those

from non-Microsoft builder platforms and identity providers. The registration process varies

based on how the agent is created.

The registry stores two key types of information for each agent:

**Agent Instance**: Operational details for execution and management.

**Agent Card Manifest**: Discovery metadata for collaboration.

Understanding this distinction ensures accurate registration.

If your agent was built on one of the following Microsoft products, you don't need to register

your agent with Agent Registry. Agents built on these products are automatically integrated for

both agent instances and agent card manifests and contain information on the agent ID.

Currently, Microsoft products integrated with Microsoft Entra Agent Registry include:

Microsoft Copilot Studio

Microsoft Agent 365

Azure AI Foundry

Before registering agents with the registry, ensure you have the following requirements:

The Agent Registry Administrator role

A valid Microsoft Entra access token with the `https://graph.microsoft.com/.default`

scope

Either app-only permissions or delegated permissions

For non-Microsoft agents, you need your agent's operational endpoint and metadata

information

**Microsoft product integrations**

**Prerequisites**

） **Important**

Microsoft Entra Agent ID is part of Microsoft Agent 365, available now in Frontier, the

Microsoft early access program for the latest AI innovations. For more information, see

**Microsoft Entra Agent ID**

.

Registering an agent in the registry involves the creation of an agent instance and an agent

card.

The agent instance is the registration of your agent in the registry that contains

operational details such as the agent's endpoint URL, agent identity, originating store,

and owner information.

The agent card contains metadata that describes the agent's capabilities, skills, and other

discovery-related information. Without the agent card, your agent isn't discoverable.

When creating the agent instance, you don't need to create an agent card at the same time.

You can create the agent card later using the agent instance ID. Agent cards can only be

created via agent instances. Agent instances can share an agent card.

Agents created on Microsoft platforms not listed above and non-Microsoft platforms require

self-serve registration using the Microsoft Graph API. This process involves:

Registering the agent instance for inventory and operational management.

Registering the agent card manifest for discovery and collaboration.

The agent instance contains operational information needed for agent execution and

management.

1\. Ensure you have the necessary permissions:

For delegated flows: `AgentInstance.ReadWrite.All`

For app-only flows: `AgentInstance.ReadWrite.All` ,

`AgentInstance.ReadWrite.ManagedBy`

2\. Make a POST request to register the agent.

HTTP

**Agent instance and agent cards**

**Self-serve registration**

**Register an agent instance**

`POST /beta/agentRegistry/agentInstances`

`Authorization` `: Bearer {token}`

`Content-Type` `: application/json`

`{`

`    "displayName": "My Agent Instance",`

The response includes the created agent instance with timestamps and confirms successful

registration. The `sourceAgentId` links your agent to its original platform identifier, while

`originatingStore` indicates the platform where the agent was created.

The agent card manifest provides discovery metadata that enables other agents and

applications to find and interact with your agent. Using the same authentication token, register

the agent card using the following API call:

HTTP

`    "ownerIds": [`

`        "11112222-bbbb-3333-cccc-4444dddd5555"`

`    ],`

`    "sourceAgentId": "a0a0a0a0-bbbb-cccc-dddd-e1e1e1e1e1e1",`

`    "originatingStore": "Copilot Studio",`

`    "agentIdentityBlueprintId": "aaaabbbb-0000-cccc-1111-dddd2222eeee",`

`    "agentIdentityId": "aaaabbbb-6666-cccc-7777-dddd8888eeee",`

`    "agentUserId": "22cc22cc-dd33-ee44-ff55-66aa66aa66aa",`

`    "url": "https:` `//conditional-access-agent.example.com/a2a/v1",`

`    "preferredTransport": "JSONRPC",`

`    "additionalInterfaces": [`

`        {`

`            "url": "https:` `//conditional-access-agent.example.com/a2a/v1",`

`            "transport": "JSONRPC"`

`        },`

`        {`

`            "url": "https:` `//conditional-access-agent.example.com/a2a/grpc",`

`            "transport": "GRPC"`

`        },`

`        {`

`            "url": "https:` `//conditional-access-agent.example.com/a2a/json",`

`            "transport": "HTTP+JSON"`

`        }`

`    ],`

`    "signatures": [`

`        {`

`            "protected": "A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0u",`

`            "signature": "BB88CC99DD00EE11FF22AA33BB44CC55DD66EE77",`

`            "header": {`

`                "kidHint": "contoso-key-1",`

`                "nonce": "mN7oP8qR9sT0uV1wX2-yZ3aB4dE="`

`            }`

`        }`

`    ]`

`}`

**Register agent card**

`    ` `POST /beta/agentRegistry/agentInstances`

`    Authorization` `: Bearer {token}`

`    ` `Content-Type` `: application/json`

The skills array defines specific capabilities your agent provides, enabling precise discovery

based on required functionality. The capabilities object specifies technical features your agent

supports for integration protocols.

Successful registration returns `HTTP 201` , created with the complete agent information

including system-generated timestamps. If registration fails, the response includes error details

to help resolve issues:

`    `

`    {`

`      "`  `displayName"` `: "",`

`      "`  `ownerIds"` `: [],`

`      "`  `sourceAgentId"` `: "",`

`      "`  `originatingStore"` `: "",`

`      "`  `url"` `: "",`

`      "`  `preferredTransport"` `: "",`

`      "`  `agentIdentityBlueprintId"` `: "",`

`      "`  `agentIdentityId"` `: "",`

`      "`  `agentUserId"` `: "",`

`      "`  `additionalInterfaces"` `: [],`

`      "`  `signatures"` `: [],`

`      "`  `agentCardManifest"` `: {`

`        "`  `ownerIds"` `: [],`

`        "`  `originatingStore"` `: "",`

`        "`  `displayName"` `: "",`

`        "`  `description"` `: "",`

`        "`  `iconUrl"` `: "",`

`        "`  `provider"` `: {},`

`        "`  `protocolVersion"` `: "",`

`        "`  `version"` `: "",`

`        "`  `documentationUrl"` `: "",`

`        "`  `capabilities"` `: {},`

`        "`  `securitySchemes"` `: {`

`          "`  `apiKeyAuth"` `: {},`

`          "`  `entraAuth"` `: {}`

`        },`

`        "`  `security"` `: [],`

`        "`  `signatures"` `: [],`

`        "`  `defaultInputModes"` `: ["application/json"],`

`        "`  `defaultOutputModes"` `: ["application/json", "text/html"],`

`        "`  `supportsAuthenticatedExtendedCard"` `: true,`

`        "`  `skills"` `: []`

`      }`

`    }`

**Handle registration responses**

ﾉ

**Expand table**

**Error Code**

**Description**

**Resolution**

`ValidationError`

Required fields missing or

invalid

Review request payload against schema

requirements

`Unauthorized`

Authentication token invalid

Refresh token and retry request

`AgentAlreadyExists`

Agent ID already registered

Use different ID or update existing agent

Common validation errors include missing required fields like `id` and `isBlocked` for agent

instances, or `name` and `skills` for agent cards.

After registration, confirm your agent appears correctly in the registry. You can verify

registration through the Microsoft Entra Admin Center or using the Microsoft Graph API.

1\. Navigate to **Agent identities**

2\. Select **Agent Registry**. Your agent won't have an agent ID but you're able to view its

associated metadata if you provided the information during registration.

**Last updated on 11/18/2025**

**Verify agent registration**

Microsoft Entra admin center

**Manage collections in Microsoft Entra**

**Agent Registry**

Agent collections provide a way to organize your agent identities. Collections allow

administrators to group agents based on various criteria such as function, security

requirements, or business context, and then apply consistent policies across those groups. This

article explains how to navigate, create, and manage agent collections, including adding agents

to both predefined and custom collections.

To get to your agent ID blueprint page, follow these steps:

1\. Sign in to the Microsoft Entra admin center

as an Agent Registry Administrator.

2\. Browse to **Entra ID** \> **Agent ID** \> **Agent Collections (Preview)**.

3\. In the **Agent collections** view, you see a tabbed section containing two options:

Select **Predefined** tab to view agents added to the **Global** collection.

Select **Custom** tab to view agents added to custom collections. This tab displays any

custom collections that you created in your tenant. Selecting a custom collection

shows the agents that are part of that collection.

To create a custom collection, follow these steps:

1\. In the **Agent collections** view, select the **Custom** tab.

2\. Select **\+ Create collection**.

3\. Provide a descriptive and meaningful **Name** and **Description** of the collection.

Use the following steps to add an agent to a predefined collection.

1\. Select the **Predefined** tab to view the predefined collections.

2\. Select the predefined collection you want to add the agent to. It opens a view listing all

the agents in that collection and their source (builder platform).

3\. To add an agent to the collection, select **\+ Add**, then choose the agents you want to add.

**Navigate to agent collections**

**Create a custom collection**

**Add an agent to predefined collections**

**Add an agent to custom collections**

Use the following steps to add an agent to a custom collection.

1\. Select the **Custom** tab to view the custom collections.

2\. Select the custom collection you want to add the agent to. A list of all agents and their

source (builder platform) appears.

3\. To add an agent to the collection, select **\+ Add**, then choose the agents you want to add.

The Microsoft Entra Agent Registry follows Zero Trust principles. For collections, Zero Trust

principles are applied by configuring access and discovery policies.

**Access policies** determine whether an agent can access Microsoft Entra-protected resources,

such as other agents, authentication endpoints, or APIs protected by conditional access.

1\. Ensure the agent can obtain a Microsoft Entra access token and complies with all access

policy requirements.

2\. Apply conditional access policies for agents to enforce access controls based on the

agent's context.

3\. Use identity protection for agents to monitor and respond to risky agent behaviors.

**Discovery policies** define which agents can be discovered through the registry. You can use

system-defined policies provided by Microsoft or create admin-defined policies to suit your

organization's needs.

**Last updated on 11/18/2025**

**Configure Zero Trust Policies for agents**

**Enable secure agent communication with**

**the Agent Registry API**

Agent Communication enables secure interactions between AI agents through the Microsoft

Entra Agent Registry API. Agent communication through Agent Registry provides a common

language and standardized approach for agent communication to boost interoperability and

break organizational silos. This capability enables agents from different developers, built on

different frameworks, and owned by different owners to work together.

There are three major components in agent communication:

**Agent manifest**: The agent manifest is a JSON document that serves as a business card

for the agents. Each agent manifest contains essential metadata about an agent's identity,

capabilities, endpoint, skills, and authentication requirements. The Registry parses this

information to determine if an agent is suitable for a given task, how to structure requests,

and how to communicate securely. You can't use agent communication without an agent

manifest.

**Client agent**: The client agent initiates communication and orchestrates interactions with

other agents to accomplish tasks. Clients parse the information contained in an agent

manifest to determine if an agent is suitable for a given task, how to structure requests,

and how to communicate securely.

**Remote agent**: The remote agent is an autonomous agent or system that exposes an

HTTP endpoint, implementing the agent communication. The remote agent receives

requests and processes tasks to accomplish the requests. The inner workings of the

remote agent aren't exposed to the client agent.

To test agent communication using Agent Registry, you need to validate that your client agent

has an agent ID.

1\. Sign in to the Microsoft Entra admin center

as an Agent Registry Administrator.

2\. Browse to **Agent ID** \> **Agent Registry** and validate that your client agent has an agent ID.

Only agents with an agent ID can query the Agent Registry.

In the returned payload, check whether the `agentIdentityId` field has a value.

You can also use the following API call:

**Understanding agent communication**

**Test agent communication**

HTTP

3\. Validate that your remote (target) agent, exists in the Agent Registry.

Agent discovery isn't possible if the agent doesn't exist in the registry. In several

scenarios, you might be able to skip to the following step if you're looking for

agents with a specific attribute but you need the registry ID.

You can also use the following API call:

HTTP

4\. Query the Agent Registry using attributes like `skills` , `agentName` , `capabilities` ,

`collection` , `id` , and so on. This step retrieves all the agent cards for all the agents that

match the query.

In the following example, we query by the `displayName` property and only retrieve

specific agent manifest attributes.

The response from this call contains the agent cards and baseUrl for the agent

communication endpoint of the matching agents. It's important to retrieve the

agent manifest, because it's a JSON document that serves as a digital business card

for initial discovery and interaction setup.

HTTP

5\. Agent Registry validates discovery policies (secure by default and custom, if applicable) by

confirming from the agent manifest JSON document that the remote (target) agent is in

the global or custom collection and that communication is allowed based on the set

policies. If validation fails, the registry denies the call with one of the following error

codes:

`GET `

`https://graph.microsoft.com/beta/agentRegistry/agentInstances/{agentInstance-`

`id}`

`GET `

`https://graph.microsoft.com/beta/agentRegistry/agentInstances/{agentInstance-`

`id}`

`GET https://graph.microsoft.com/beta/agentRegistry/agentCardManifests?`

`$filter=displayName eq 'Sample Agent Card'&$select=id,displayName,skills`

`Authorization` `: Bearer {token}`

ﾉ

**Expand table**

**HTTP Status**

**Error Code**

**Description**

400

ValidationError

Request validation failed

401

Unauthorized

Authentication required

403

Forbidden

Insufficient permissions

404

AgentNotFound

Agent not found

404

AgentCardNotFound

Agent card not found

500

InternalServerError

Server error

6\. Send the collaboration message to the remote (target) agent using JSON-RPC

specification

from the client (source) agent to the remote (target) agent. The payload

should include the following:

`method` : Action to invoke

`params` : Input data

`traceId` : For audit

`caller` : Registry-issued token

**Last updated on 11/18/2025**

**Agent identity and blueprint concepts in**

**Microsoft Entra ID**

The Microsoft agent identity platform provides specialized identity constructs designed

specifically for AI agents operating in enterprise environments. These identity constructs enable

secure authentication and authorization patterns that differ from traditional user and

application identities, addressing the unique requirements of autonomous AI systems.

This article explains the core concepts that form the foundation of agent identity management:

agent identities, agent identity blueprints, and their supporting components. Understanding

these concepts is essential for developers who need to implement secure, scalable

authentication patterns for AI agents.

The agent identity architecture follows a hierarchical model where agent identity blueprints

serve as templates for creating multiple agent instances, each with distinct identities and

capabilities. This approach enables centralized management while providing the flexibility

needed for diverse AI agent deployment scenarios.

The following concepts form the foundation of the agent identity system in Microsoft Entra ID.

Agent identity is the primary account used by an AI agent to authenticate to various systems. It

has unique identifiers - the object ID and the app ID, which always have the same value - which

can be reliably used for authentication and authorization decisions. Agent identities don't have

a password or any other credential. Instead, agent identities can only authenticate by

presenting an access token issued to the service or platform on which the agent runs. For more

information, see what is an agent ID

Agent identity blueprints provide the template and management structure for creating and

managing multiple agent identities. Agent identity blueprint serves as the parent of an agent

identity.

For more information, see What is an agent identity blueprint?

**Core identity concepts**

**Agent identity**

**Agent identity blueprint**

**Agent identity blueprint principal**

When blueprints are added to tenants, they create a corresponding principal object that

manages the blueprint's presence within that specific tenant. Agent identity blueprint principal

is the Microsoft Entra object is the record of a blueprint's addition to a tenant. For more

information, see agent identity blueprint principals

For scenarios where agents need to interact with systems that specifically require user objects,

the platform provides agent users as an alternative identity type. An agent user is a secondary

account that an AI agent uses to authenticate to various systems. These accounts are user

objects in a tenant and have most properties of other users, like a manager, UPN, and photo. It

makes them compatible with systems that have a hard dependency on user objects, and enable

AI agents to connect to these systems. For more information, see agent users

The agent registry is a centralized repository that maintains metadata about all registered

agents within an organization. It serves as a discovery mechanism, allowing systems and

services to locate and interact with agents based on their capabilities, roles, and other

attributes. For more information, see agent registry

The agent identity platform supports two primary patterns for how agents operate and

authenticate, each serving different use cases and security requirements.

Interactive agents are agents that sign-in a user and taken action in response to user

prompts, often via a chat interface. These agents act on behalf of the signed-in user,

utilizing that user's authorization to perform actions in various systems. Interactive agents

are granted Microsoft Entra delegated permissions that allow them to act on behalf of

users. Tokens issued to interactive agents are often called user tokens.

Autonomous agents are agents that perform actions using their own identity; not a

human user's identity. These agents often run in the background and make autonomous

decisions about what actions to take. Tokens issued to autonomous agents are often

called agent tokens when an agent identity is authenticated. They can also be called

agent user tokens when an agent user is authenticated.

**Agent user**

**Agent registry**

**Agent operation patterns**

**Agent owners, sponsors, and managers**

The agent identity platform introduces an administrative model that separates technical

administration from business accountability, ensuring operational control and compliance

oversight without excessive permissions. The agent administrative roles include owners,

managers, and sponsors.

Owners serve as technical administrators for agents, handling operational and

configuration aspects.

Sponsors provide business accountability for agents, making lifecycle decisions without

technical administrative access.

A manager is a human user who is designated as the hiring manager or operational

owner for an agent user.

For more information, see Administrative relationships for agent identities (Owners, sponsors,

and managers)

The Microsoft Entra SDK for AgentID is a containerized web service that handles token

acquisition, validation, and secure downstream API calls for agents registered in the Microsoft

identity platform. It runs as a companion container alongside your application, allowing you to

offload identity logic to a dedicated service. For more information, see Microsoft Entra SDK for

agent ID

What is an agent ID?

What is the agent identity platform?

Microsoft Entra Agent ID oauth protocols

Create an agent identity blueprint

**Last updated on 11/18/2025**

**Microsoft Entra SDK for agent ID**

**Related content**

**Agent identity blueprints in Microsoft Entra**

**Agent ID**

An agent identity blueprint is an object in Microsoft Entra ID that serves as a template for

creating agent identities. It establishes the foundation for how agents are created,

authenticated, and managed within an organization.

![](./assets/output_80_1.png)

All agent identities in a Microsoft Entra ID tenant are created from an agent identity blueprint.

The agent identity blueprint is a key component of the Microsoft agent identity platform that

enables secure development and administration of AI agents at scale. An agent identity

blueprint serves four purposes.

**Blueprints are a template for agent identities.**

Organizations can deploy many instances of an AI agent. Each instance pursues a

different goal and requires a different level of access. Each instance uses a distinct agent

identity for authentication and access. However, the many agent identities used share

certain characteristics. The agent identity blueprint records these common characteristics,

so that all agent identities created using the blueprint have a consistent configuration.

An agent identity blueprint has the following properties that are shared across all its

agent identities:

**Defining an agent identity blueprint**

`description` : A brief summary of the agent's purpose and functions.

`appRoles` : Define the roles that can be given to users and other principals when using

the agent.

`verifiedPublisher` : The organization that built the agent.

Settings for authentication protocols, such as `optionalClaims` : Configure which

information is included in access tokens issued to the agent.

These settings are configured on a blueprint so that they're consistent across all agent

identities created using the blueprint.

The full schema is available in the Microsoft Graph API reference documentation.

**Blueprints create agent identities.**

Blueprints don't just hold information. They're also a special identity type in a Microsoft

Entra ID tenant. A blueprint can perform exactly one operation in the tenant: provision or

deprovision agent identities. To create an agent identity, a blueprint has:

An OAuth client ID: a unique ID used to request access tokens from Microsoft Entra ID.

Credentials: used to request access tokens from Microsoft Entra ID.

`AgentIdentity.CreateAsManager` : a special Microsoft Graph permission that enables the

blueprint to create agent identities in the tenant.

A service uses the blueprint's client ID, credentials, and permissions to send agent identity

creation requests via Microsoft Graph APIs. The agent identities created by a blueprint

share common characteristics.

For more information, see create agent identities.

**Blueprints hold credentials for agent identities.**

Each agent identity doesn't have its own credentials. Instead, the credentials used to

authenticate an agent identity are configured on the blueprint. When an AI agent wants

to perform an operation, the credentials configured on the blueprint are used to request

an access token from Microsoft Entra ID.

For auth protocols, see Agent ID authentication protocols

**Blueprints are a container for agent identities.**

Identity administrators can apply policies and settings to agent identity blueprints that

take effect for all agent identities created using the blueprint. Examples include:

Conditional access policies applied to a blueprint take effect for all its agent identities.

OAuth permissions granted to a blueprint are granted to all its agent identities.

Disabling blueprints prevents all its agent identities from authenticating.

The blueprint provides a logical container for agent identities on which many different

identity administration operations can be performed. This helps administrators scale their

security efforts to large numbers of AI agents.

An agent identity blueprint principal is an object in Microsoft Entra Agent ID that represents

the presence of an agent identity blueprint within a specific tenant. When an agent identity

blueprint application is added to a tenant, Microsoft Entra creates a corresponding principal

object, which is the agent identity blueprint principal.

![](./assets/output_82_1.png)

This principal serves several important roles:

**Token Issuance**: When the agent identity blueprint is used to acquire tokens within a

tenant, the resulting token's `oid` (object ID) claim references the agent identity blueprint

principal. It ensures that any authentication or authorization performed by the agent

identity blueprint is traceable to its principal object in the tenant.

**Audit Logging**: Actions performed by the agent identity blueprint, such as creating agent

identities, are recorded in audit logs as being executed by the agent identity blueprint

principal. It provides clear accountability and traceability for operations initiated by the

agent identity blueprint.

**Agent identity blueprint principals**

Agent identity blueprints are always created in a Microsoft Entra tenant. An agent identity

blueprint is often used to create agent identities in that same tenant. These agent identity

blueprints are called "single-tenant." Agent identity blueprints can also be configured as

"multitenant" and published to potential customers via Microsoft catalogs. Customers can then

add these blueprints to their tenant, so that they can be used to create agent identities.

In either case, an agent identity blueprint principal is always created when a blueprint is added

to a tenant. The presence of this principal indicates that a blueprint exists in a tenant and can

be used to create agent identities. Customers can remove a blueprint from their tenant by

deleting the agent identity blueprint principal.

There are multiple ways to create an agent identity blueprint in Microsoft Entra Agent ID. For

more information, see agent identity blueprint.

There are several credentials types that can be used for agent identities. For more information

on these, see credentials for agent identities.

Agent identity blueprint creation channels

Create an agent identity blueprint

**Last updated on 11/18/2025**

**Create an agent identity blueprint**

**Credentials for agent identities**

**Related content**

**Agent identities in Microsoft Entra Agent**

**ID**

An agent identity is a special service principal in Microsoft Entra ID. It represents an identity

that the agent identity blueprint created and is authorized to impersonate. It doesn't have

credentials on its own. The agent identity blueprint can acquire tokens on behalf of the agent

identity provided the user or tenant admin consented for the agent identity to the

corresponding scopes. Autonomous agents acquire app tokens on behalf of the agent identity.

Interactive agents called with a user token acquire user tokens on behalf of the agent identity.

Agent identities can be used to:

Request agent tokens from Microsoft Entra ID. The subject of the access token is the

agent identity.

Receive incoming access tokens issued by Microsoft Entra ID. The audience of the access

token is the agent identity.

Request user tokens from Microsoft Entra ID for an authenticated user. The subject of the

token is a user, while the actor is the agent identity.

Agent identity blueprints

An account used by an AI agent is referred to as an **agent identity**. Much like your typical user

account, an agent identity has a few key components:

**Prerequisites**

**Anatomy of an agent identity**

![](./assets/output_85_1.png)

**Identifier**. Each agent identity has an `id` (also known as object ID), such as `aaaaaaaa-`

`1111-2222-3333-bbbbbbbbbb` . Microsoft Entra generates the `id` and uniquely identifies the

account within a Microsoft Entra tenant.

**Credentials**. Agent identities don't have passwords, but have other forms of credentials

they can use to authenticate.

**Display name**. An agent identity's display name is surfaced in many experiences such as

the Microsoft Entra admin center, Azure portal, Teams, Outlook, and more. It's the

human-friendly name of an agent and can be changed.

**Sponsor**. Agent identities can have a sponsor, which records the human user or group

that's accountable for an agent. This sponsor is used for various purposes, such as

contacting a human in case a security incident happens.

**Blueprint**. All agent identities are created from a reusable template called an agent

identity blueprint. The agent identity blueprint establishes the kind of agent and records

metadata shared across all agent identities of a common kind.

**Agent user (optional)**. Some agents need access to systems that strictly require a

Microsoft Entra user account be used for authentication. In these cases, an agent can be

given a second account, called an **agent user**. This second account is a user account in

the Microsoft Entra tenant that is decorated as an AI agent. It has a different `id` than the

agent identity, but a 1:1 relationship is always established between an agent identity and

its agent user.

These are the basic components of an agent identity that enable secure authentication and

authorization. The full object schema of an agent identity is available in Microsoft Graph

reference documentation.

Agent identity is the primary account used by an AI agent to authenticate to various systems. It

has unique identifiers - the object ID and the app ID, which always have the same value - which

can be reliably used for authentication and authorization decisions.

Unlike human users, AI agents don't use passwords, Short Message Service (SMS), passkeys, or

authenticator apps for authentication. Instead, agent identities use credentials types that are

usable by software systems. These credential types include:

Managed identities, for AI agents that run on Azure (most secure).

Federated identity credentials, for AI agents that run on Kubernetes or other cloud

providers.

Certificates / cryptographic keys.

Client secrets.

Agent identities can only be issued tokens in the Microsoft Entra tenant where they're created.

They can't access resources or APIs in other tenants.

A key characteristic of agent identities is that all agent identities are created from a reusable

template called an agent identity blueprint. The blueprint establishes the "kind" of agent and

records metadata shared across all agent identities of a common kind.

**Credentials for agent identities**

**Blueprints: Consistent security for agent identities**

![](./assets/output_87_1.png)

Imagine that an organization uses an AI agent called a "Sales Assistant Agent." Whether the

agent is purchased or built in-house, an agent identity blueprint would be added to the

organization's Microsoft Entra tenant. The blueprint captures the following information:

The name of the blueprint, such as "Sales Assistant Agent"

The organization who published the blueprint, such as "Contoso"

Any roles the agent might offer, such as "sales manager" or "sales rep"

Any Microsoft Graph permissions that its agents are granted, such as "read the signed in

user's calendar"

Many sales teams within the organization deploy the AI agent. An agent is deployed for North

America sales. Another is deployed for South America sales. One for enterprise sales, one for

small/medium businesses, and another for startups. Upon creation, each of these agents is

given an agent identity. Each agent begins running and performing tasks using its agent

identity for authentication.

Because each agent identity is created using the same agent identity blueprint, all agents

appear as "Sales Assistant Agents" in the Microsoft Entra admin center. This feature allows the

Microsoft Entra administrator to take actions like:

Apply a conditional access policy to all Sales Assistant Agents.

Disable all Sales Assistant agents.

Revoke a permission grant for all Sales Assistant agents.

Agent identity blueprints give the Microsoft Entra administrator the ability to secure agent

identities at scale by setting rules and performing operations based on the kind of agent. This

feature ensures consistent security for each AI agent that is deployed in the organization.

Create an agent identity

Microsoft Entra Agent ID authentication protocol

**Last updated on 11/18/2025**

**Related content**

**Agent users in Microsoft Entra Agent ID**

Agent users are a specialized identity type designed to bridge the gap between agents and

human user capabilities. Agent users enable AI-powered applications to interact with systems

and services that require user identities, while maintaining appropriate security boundaries and

management controls. It allows organizations to manage those agent's access using similar

capabilities as they do for human users.

Sometimes it's not enough for an agent to perform tasks on behalf of a user or operate as an

autonomous application. In certain scenarios, an agent needs to act as a user, functioning

essentially as a digital worker. The following are example scenarios where the agent user would

be applicable:

The organization needs long-term digital employees that function as team members with

mailboxes, chat access, and inclusion in HR systems.

The agent needs to access APIs or resources that are only available to user identities

The agent needs to participate in collaborative workflows as a team member

For these reasons, agent users are created. Agent users are optional and should only be

created for interactions where the agent needs to act as a user or access resources restricted to

user accounts.

Agent users represent a subtype of user identity within Microsoft Entra. These identities are

designed to enable agent applications to perform actions in contexts where a user identity is

required. Unlike nonagentic service principals or application identities, agent users receive

tokens with claim `idtyp=user` , allowing them to access APIs and services that specifically

require user identities. It also maintains security constraints necessary for nonhuman identities.

An agent user isn't created automatically. It requires an explicit creation process that connects

it to its parent agent identity. This parent-child relationship is fundamental to understanding

how agent users function and are secured in Microsoft Entra. Once established, this

relationship is immutable and serves as a cornerstone of the security model for agent users.

The relationship is a one-to-one (1:1) mapping. Each agent identity can have at most one

associated agent user, and each agent user is linked to exactly one parent agent identity, itself

linked to exactly one agent identity blueprint application.

Agent users:

**Example of agent user scenarios**

**Agent users**

Are also created using an agent identity blueprint.

Are always associated to a specific agent identity, specified upon creation.

Have distinct unique identifiers, separate from the agent identity.

Can only authenticate by presenting a token issued to the associated agent identity.

![](./assets/output_90_1.png)

The agent identity blueprint doesn't have the permission by default to create agent users

because this capability is optional and not always needed. It's a permission that must be

explicitly granted to the agent identity blueprint.

Agent users are created using agent identity blueprint. When granted proper permissions, the

agent identity blueprint can create an agent user and establish a parent relationship with a

specific agent identity. Agent identity is considered as the parent of the agent user.

Admins manage the lifecycle of an agent user. An admin user can delete the agent user once

agent user functionalities aren't needed anymore.

The authentication model for agent users differs significantly from human-user accounts:

**Agent user and agent ID relationship**

**Authentication and security model**

**Federated identity credentials**: Authentication happens through credentials assigned to

the agent user. In production systems, use Federated Identity Credentials (FIC). These

credentials are used for authenticating both the agent identity blueprint and the agent

identity. The credential assigned to the user is used for authenticating across the agent

ecosystem.

**Restricted credential model**: Agent users don't have regular credentials like passwords.

Instead, they're restricted to using the credentials provided through their parent

relationship. This restriction on credentials, along with restrictions on interactive sign-in,

ensures that agent users can't be used like standard user accounts.

**Impersonation mechanism**: The associated agent identity can impersonate its child agent

user. It allows the parent's business logic to obtain tokens and act as the agent user when

needed.

Agent users possess capabilities that allow them to function effectively within Microsoft 365

and other environments:

Agent users can be added to Microsoft Entra groups, including dynamic groups, enabling

them to inherit permissions granted to those groups. They can't, however, be added to

role-assignable groups.

Agent users can access resources and utilize other collaborative features typically

reserved for human users.

Agent users can be added to administrative units, similar to human users.

Agent users can be assigned licenses, which is often necessary for provisioning Microsoft

365 resources.

Agent users operate under specific security constraints to ensure appropriate use:

Credential limitations: Agent users can't have credentials like passwords or passkeys. The

only credential type they support is the agent identity reference to their parent. So even if

agent users behave as users, their credentials are confidential client credentials.

Administrative role restrictions: Agent users can't be assigned privileged administrator

roles. This limitation provides an important security boundary, preventing potential

elevation of privileges.

**Capabilities of agent users**

**Security constraints**

Permission model: Agent users typically have permissions similar to guest users, with

more capabilities for enumerating users and groups. Agent users can’t be assigned

privileged admin roles. Custom role assignment and role-assignable groups aren't

available to agent users. For more information, see Microsoft Graph permissions

reference

**Last updated on 11/18/2025**

**Agent identities, service principals, and**

**applications**

The agent app model introduces specific service principal types with distinct roles and

characteristics compared to nonagent application service principals. This article explains service

principals in the agent application model, how they relate to agent identity blueprint and differ

from nonagent application service principals.

Agent identity blueprint principals are created automatically when an agent identity blueprint

is instantiated in a tenant. These service principals provide the runtime representation of the

agent identity blueprint within the tenant's directory and enable the agent identity blueprint to

perform operations like creating instances and managing lifecycle operations.

The creation process involves consent operations that require permissions like

`AgentIdentity.Create` and `ServicePrincipal.Manage.OwnedBy` . The agent identity blueprint

principal enables the agent identity blueprint to obtain app-only tokens for Microsoft Graph

calls necessary to create and manage agent identities. This process is essential because agent

blueprints themselves can't directly obtain tokens for Microsoft Graph operations.

Agent identities are modeled as single-tenant service principals with a new "agent" subtype

classification. This design uses existing Microsoft Entra ID service principal infrastructure while

adding agent-specific behaviors and constraints.

Agent identities inherit their protocol properties from their parent agent identity blueprint

through the ParentID relationship. Unlike nonagentic service principals that operate

independently, agent identities require their parent agent identity blueprint for impersonation

and token exchange operations.

Agent identities can be granted permissions directly and appear in sign-in logs when tokens

are issued for agent operations. They serve as the primary identity that customers reason about

when managing agent permissions and access.

Agent identity blueprint principal creates agent identity service principals using Microsoft

Graph calls with app-only tokens and appropriate roles. The creation process establishes the

parent-child relationship and configures the necessary Federated Identity Credential (FIC)

relationships for impersonation.

**Agent identity blueprint principal**

**Agent identity as service principal**

Before the introduction of the Microsoft agent identity platform, some Microsoft applications

such as Microsoft Copilot Studio and Azure AI Foundry used application agent service

principals to ensure their agents were secured with identities. These are shown alongside agent

identity objects in your tenant in the **All agent identities** list.

They can be differentiated in this list by filtering to get those that use agent identities. With the

filter, you can show either or both of agent identity objects and agents using application

service principals. See the list of columns in the **All agent identities** list.

These agents using service principal behaves the same as application service principals, and

don't have the same differences from application service principals as agent identities or agent

identity blueprint principals.

The following sections describe the key differences between agent service principals and

nonagentic application service principals.

Nonagentic service principals operate using their own credentials and identity. Agent service

principals use an impersonation model where the agent identity blueprint impersonates the

agent identity to perform operations on the instance's behalf.

This impersonation model enables the agent identity blueprint to obtain tokens where the

agent identity appears as the client, even though the agent identity blueprint is performing the

actual token exchange. The resulting tokens maintain the agent identity's identity in audit logs

while enabling the agent identity blueprint to orchestrate complex token flows.

Nonagentic applications typically have a one-to-one relationship between application and

service principal. The agent app model introduces a one-to-many relationship where a single

agent identity blueprint can have multiple agent identity service principals across tenants and

within tenants.

This multi-instance model enables scenarios like creating multiple agent identities per Teams

channel, per project, or per organizational unit, all sourcing their protocol properties from the

same parent agent identity blueprint.

**Agents built using application service principals**

**Key Differences from nonagent service principals**

**Impersonation model**

**Multi-instance relationship**

Nonagentic service principals manage their own credentials (certificates, secrets, and managed

identities). The service principal presents these credentials to obtain tokens for itself or to

perform On-Behalf-Of operations for users. Agent identities rely on credentials from the parent

agent identity blueprint and can't manage credentials independently. Agent identity service

principals don't perform direct authentication.

Nonagentic service principals receive permissions through direct assignment or admin consent.

Agent service principals support both direct permission assignment and inheritance from

parent applications.

When inherit delegated permissions is enabled, an agent identity can inherit delegated

permissions from their parent agent identity blueprint, reducing consent complexity for multi-

instance scenarios. This inheritance applies when impersonation is used and enables efficient

permission management across multiple instances.

Agent service principals support both application permissions (for app-only operations) and

delegated permissions (for user-delegated operations). Permission assignment can be direct or

inherited depending on the scenario requirements.

**Direct assignment**: Permissions can be assigned directly to an agent identity for instance-

specific access requirements.

**Inherited assignment**: When `InheritDelegatedPermissions` is enabled on the service principal,

agent identities inherit delegated permissions from their parent agent identity blueprint,

simplifying permission management in multi-instance scenarios.

**Role assignment**: Agent identities can be assigned Azure Role Based Access Control (RBAC)

roles and directory roles like nonagentic service principals, enabling resource access and

administrative operations. Agent identity blueprints can't be assigned Azure RBAC roles

Agent service principals maintain distinct identities in audit logs and sign-in reports. When an

agent identity performs operations, the logs show the agent identity as the acting client while

indicating the relationship to the parent agent identity blueprint.

**Runtime credential management**

**Consent and permission model**

**Permission and role assignment**

**Audit and logging**

Sign-in logs differentiate between agent identity blueprints, agent identities, and agent users.

This differentiation enables clear role identification (client, credential, subject) depending on

the specific operation being performed. This enables audit trails for agent operations.

**Last updated on 11/18/2025**

**Agent Registry collections**

Collections in the Microsoft Entra Agent Registry define how agents are logically organized and

discovered during agent-to-agent collaboration. When an agent queries the registry, the

system evaluates its metadata and returns only agents permitted for discovery based on their

collection membership. Collections help organizations establish clear boundaries for

discoverability and collaboration, defining how agents can be discovered within the Agent

Registry.

Agents with or without an agent identity can be assigned as members of a collection.

Agents _with_ an agent identity can query the registry and discover other agents.

Agents _without_ an agent identity can be part of a collection and be discovered by other

agents, but they can't perform discovery themselves.

In other words, agents without an agent identity can act only as target agents in collaboration

scenarios. To function as a client agent and query the registry, an agent identity is required.

To help administrators manage agent discoverability, Microsoft Entra Agent Registry offers

predefined and custom collections.

**Global Collection**: Makes agents discoverable across the entire organization.

For example, an agent responsible for travel booking within the Global Collection can

be discovered and invoked by other agents that have an agent identity and the

appropriate Agent Registry role.

**Custom collection**: Created by administrators to apply discovery boundaries that align

with business or policy needs.

For example, if human resources agents should only interact with payroll agents, an

admin can create a "human resources department" collection so that only agents

within that collection can discover and collaborate with each other.

The Microsoft Entra Agent Registry follows the same Zero Trust principles as the rest of

Microsoft Entra: verify explicitly, use least privilege access, and assume breach. Every agent

interaction is governed by multiple policy enforcement layers to ensure secure and compliant

communication. To learn how to apply these principles, see Configure Zero Trust for agents.

**Access policies**: Determine whether an agent can access Microsoft Entra-protected

resources, such as other agents, authentication endpoints, or APIs protected by

**Collections types**

**Agent collaboration policies**

conditional access.

**Discovery policies**: Define which agents can be discovered through the registry, using

system and admin defined policies to determine how agents are discovered during

collaboration.

Discovery policies define how agents are discovered within the registry. You can use system-

defined policies provided by Microsoft or create admin-defined policies to suit your

organization’s needs.

**System-defined discovery policies**: System-defined policies apply automatically to Global

Collection.

Agents in the Global Collection inherit the _Discoverable by All_ policy.

This policy allows other agents with an agent identity to discover and collaborate with

agents in the Global Collection.

**Admin-defined discovery policies**: Admin-defined discovery policies let you control

agent discoverability based on your business or departmental boundaries.

For example, you can restrict discovery to a specific department such as HR.

Yes, In the initial preview release, moving agents into collections is a manual process. When

you create a collection; however, you can add multiple agents at one time.

No. There is no limit on the number of custom collections you can create.

Yes. During the preview, each collection supports up to 100 agents.

**Agent discovery policies**

**FAQs**

**Q: Do I need to manually move an agent into a collection?**

**Can I do it in bulk?**

**Q: Is there a limit on the number of custom collections I can**

**create?**

**Q: Is there a limit on the number of agents in a collection?**

Microsoft Entra Groups and Agent Registry collections serve different purposes in managing

agents and users. The table below summarizes the key distinctions:

**Aspect**

**Microsoft Entra Groups**

**Agent Registry collections**

Purpose

Manage access control

Manage discovery and collaboration

Used

for

People, devices, and agents

Agents

Scope

Applies across Microsoft 365 and Entra

services

Applies within the Microsoft Entra Agent

Registry

Analogy

“Who can enter the room”

“Who can be seen and communicated”

No. Collections _complement_ Microsoft Entra Groups. They serve different purposes and work

together to enforce Zero Trust principles.

Microsoft Entra Groups manage access control, defining who can sign in and what

resources they can access across Microsoft 365 and Entra services.

Collections in the Microsoft Entra Agent Registry manage discovery and collaboration

among agents.

Groups answer, _Who can access what?_.

Collections answer, _Which agents can be discovered and collaborate with each other?_, ensuring

secure, policy-driven visibility for agent interactions.

**If you want to control…**

**Use…**

Who can sign in or access data

Groups

Which agents can be discovered for collaboration

Collections

**Q: What’s the difference between Microsoft Entra Groups and**

**Agent Registry collections?**

ﾉ

**Expand table**

**Q: Are collections a replacement for Microsoft Entra Groups?**

**Q: When should I use Collections vs. Groups?**

ﾉ

**Expand table**

Quarantined collections are a predefined collection in Microsoft Entra, created to limit

discovery for agents. Agents in this collection can't discover other users or agents.

What is the Microsoft Entra Agent Registry?

Manage agent collections

**Last updated on 11/18/2025**

**Q: What are quarantined collections?**

**Related content**

**Agent metadata and discoverability**

**patterns**

Agent metadata serves as the foundation for agent discoverability within Microsoft Entra Agent

Registry. The metadata you provide determines how other agents, applications, and users can

find and interact with your agent. Understanding the metadata schema and its relationship to

the collections model ensures your agents are discoverable by the intended audience while

maintaining appropriate security boundaries.

The agent metadata schema defines the information structure required for agent

discoverability and interaction. This schema allows for agent collaboration through standard

protocols while extending it with Microsoft Entra-specific capabilities for enhanced security.

The foundational metadata includes essential identification and contact information for your

agent.

**Field**

**Description**

`id`

Unique identifier for the agent manifest. Required for all agent registrations.

`displayName`

Human-readable identifier that appears in discovery results. Should clearly indicate

the agent's purpose, such as "Customer Support Assistant" or "Invoice Processing

Agent."

`description`

Comprehensive details about the agent's purpose and capabilities. Include relevant

keywords that your target audience would naturally use when searching for this type

of agent, directly impacting discoverability.

`iconUrl`

URL to the agent's icon image, providing visual identification in discovery results and

user interfaces.

`version`

Version of the agent implementation, enabling tracking of agent updates and

compatibility considerations for integration scenarios.

`documentationUrl`

URL to the agent's documentation. Include links to detailed API documentation,

usage examples, and troubleshooting guides to support successful agent adoption.

`protocolVersion`

Protocol version supported by the agent, ensuring compatibility with clients and

**Agent metadata schema**

**Basic agent information**

ﾉ

**Expand table**

**Field**

**Description**

other agents during communication.

`provider`

Information about the organization providing the agent, including organization name

and contact URL. Helps identify the source of agents during discovery and provides

verification points for agent authenticity.

`managedBy`

Application identifier managing this manifest, establishing clear ownership and

responsibility for the agent's lifecycle and configuration.

`originatingStore`

Name of the store or system where the agent originated, helping track agent sources

and lineage within the registry.

The core functionality and interaction capabilities your agent provides.

**Field**

**Description**

`skills`

Core functionality your agent provides. Each skill requires a unique identifier,

descriptive name, and detailed description that explains what the skill

accomplishes. Directly determines discoverability in capability-based searches.

`defaultInputModes`

Default input modes supported by the agent. Use consistent MIME type

specifications such as "text/plain," "application/json," or "image/png" to

ensure proper matching with client applications.

`defaultOutputModes`

Default output modes supported by the agent. Specify the data formats your

agent produces, enabling automatic compatibility checking during agent

discovery.

`capabilities`

Technical features your agent supports for integration protocols.

`capabilities.extensions`

Extension capabilities containing properties including URI, description,

required status, and parameters. Affects how other agents and applications

interact with your agent during federation scenarios.

Security and authentication requirements that affect discoverability, trust, and access policies.

Security and provider information directly affect how Microsoft Entra Agent Registry applies

collection assignment and discovery policies to your agent, making these fields critical for

proper management and compliance.

**Skills and capabilities metadata**

ﾉ

**Expand table**

**Security and provider information**

**Field**

**Description**

`securitySchemes`

Dictionary of security scheme definitions keyed by scheme name,

specifying the authentication methods your agent supports.

Ensures your agent appears in discovery results only for clients that

can meet the authentication requirements.

`security`

Array of security scheme references that apply to different

operations. Defines security requirements that prevent failed

integration attempts and improve user experience by filtering

incompatible matches during discovery.

`signatures`

Digital signatures for the manifest, including protected content,

signature values, and header information for verifying manifest

integrity and authenticity.

`supportsAuthenticatedExtendedCard`

Indicates whether your agent provides more metadata for

authenticated callers. Enables progressive disclosure of information,

where basic capabilities are publicly discoverable while detailed

operational information requires authentication.

`ownerIds`

List of owner identifiers who have authority over the agent

manifest.

Collections determine which agents can discover each other and establish communication

channels. Agents must be explicitly assigned to collections by administrators or through

defined organizational policies. There are no automatic assignments based on metadata tags

or agent characteristics. This explicit assignment model ensures proper governance and

security controls over agent discoverability and interaction patterns.

For comprehensive information about collection types, assignment rules, and discovery

policies, see Agent registry collections.

Publish agents to registry

Agent registry collections

What is the agent registry?

**Last updated on 11/18/2025**

ﾉ

**Expand table**

**Collections and discoverability**

**Related content**

**Administrative relationships in Microsoft**

**Entra Agent ID (Owners, sponsors, and**

**managers)**

The Microsoft agent identity platform introduces an administrative model that separates

technical administration from business accountability, ensuring operational control and

compliance oversight without excessive permissions. This document explains the administrative

relationships for Microsoft Entra Agent ID identity types. This guidance applies to agent

identities, agent identity blueprints, agent blueprint principals, and agent users. The article

covers owners, sponsors, and managers and their importance in maintaining secure operations.

The administrative relationships available in Agent ID include:

**Owners**: Technical administrators responsible for operational management of agent

blueprints and agent identities, including setup, configuration, and credential

management.

**Sponsors**: Business representatives accountable for the agent's purpose and lifecycle

decisions, including access reviews and incident response, without technical

administrative access.

**Managers**: User responsible for the agent within the organization's hierarchy, able to

request access packages for their reporting agents.

These administrative relationships must be configured for each Agent ID object and are

separate from the administrative rights granted by Microsoft Entra Role Based Access Control

(RBAC) roles, like Agent Admin.

Owners usually serve as technical administrators for agents, handling operational and

configuration aspects. Service principals can also be set as owners, enabling automated

management of agent identities.

Owners can modify properties that the sponsor can't, like authentication properties. Owners

can also add or update other owners and sponsors for the agent identities. Like sponsors, they

can disable and delete agent identities that are no longer needed. Unlike sponsors, owners can

re-enable an agent identity that is disabled and restore soft deleted identities.

**Owners**

**Owner responsibilities**

Owners have administrative privileges scoped to their assigned applications. They can edit

settings, manage credentials, change configurations, and assign more owners.

Owners are typically developers or IT professionals with technical knowledge to manage

application identities. They might be agent creators, technical application owners, or IT

administrators for critical agents. Multiple owners can be assigned for backup coverage.

Service principals can also be set as owners when some other managing service needs the

ability to modify or delete specific agent identities without user intervention.

Sponsors provide business accountability for agents, making lifecycle decisions without

technical administrative access. They understand the business purpose of the agent, and they

can determine whether an agent is still needed or requires access.

Sponsorship should be maintained ensuring succession when an employee who's a sponsor

moves or leaves. Both users and groups can be assigned as sponsors. When a group is

assigned, all users who are direct members of the group have sponsor rights over the Agent ID

object.

Sponsors make decisions about the agent lifecycle, including renewal, extension, or removal

based on business need. They request access packages on behalf of agents, and they provide

business justification for access requests. During security incidents, sponsors might determine

whether agent behavior is expected and authorize appropriate responses including suspension

or permission adjustments.

Sponsors operate under least-privilege with limited administrative permissions. They can't

modify application settings. Access is limited to nondestructive lifecycle operations: enabling

and disabling agents.

**Owner access and permissions**

**Owner typical personas**

**Sponsors**

**Sponsor responsibilities**

**Sponsor access and permissions**

**Sponsor typical personas**

Sponsors are usually business owners, product managers, team leads, or stakeholders who

understand the agent's purpose. For unpublished agents, creators often serve as sponsors. For

published agents, sponsors typically come from teams using the agent.

Managers are individual users responsible for an agent within the organizational hierarchy. For

agents that are active in user scenarios, consider setting a manager. Managers can request

access packages and will see agents designated as reporting to them in the Microsoft Entra

admin center. Managers don't have authorization to modify or delete agents. Owners,

sponsors, or administrators are required to take those actions.

The administrative model enforces specific requirements and constraints to ensure effective

oversight and accountability.

A sponsor is required when creating an agent identity or agent blueprint. Agent blueprint

principals are exempt from the sponsor requirement during creation. Owners and managers

are always optional.

For delegated creation requests where both an application and user context exist, the calling

user automatically becomes the sponsor if no sponsors are explicitly specified. However, if one

or more other sponsors are designated during creation, the calling user isn't automatically

added. Users with Agent ID admin roles aren't made sponsor automatically during creation.

This avoids unintentionally overburdening admins with direct responsibility for individual

agents.

For app-only create requests, the creating service must set one or more users or groups as the

sponsor.

**Last updated on 11/18/2025**

**Manager**

**Requirements and constraints**

**Creation requirements**

**Assignment policies**

**Tokens in Microsoft agent identity platform**

Tokens are the fundamental security mechanism that enables secure communication and

authorization in the Microsoft agent identity platform. This article explains how tokens work in

agent app scenarios.

In agent app scenarios, tokens carry enhanced claims to support the unique requirements.

Unlike nonagentic application tokens, tokens used by agents include specialized claims that

identify entity types, delegation relationships, and authorization contexts specific to agent

operations.

These tokens enable secure communication between:

Agent identity blueprints and their agent identities

Agent identities and resource APIs

Agent users and the services they interact with

Complex delegation chains involving multiple agent entities

Agent tokens include specialized claims that identify the type and role of entities participating

in authentication flows:

Actor facet claims ( ` xms_act_fct` ): Identify the entity performing actions within the token

flow. These claims enable systems to understand who is actually requesting access or

performing operations.

Subject facet claims ( ` xms_sub_fct` ): Identify the ultimate subject for whom operations are

being performed. It enables proper attribution even in complex delegation scenarios.

Identity type claims ( ` idtyp` ): Distinguish between user and application contexts, enabling

appropriate policy application and security enforcement.

Identity relationship claims ( ` xms_idrel` ): Describe the relationship between the token

subject and the resource tenant, supporting multi-tenancy and guest access scenarios.

Agents participate in several distinct token flow patterns, each designed for specific operational

scenarios. For more information, see auth protocols in Microsoft agent identity platform.

**Token claims entity identifiers**

**Token flow patterns**

**Tokens in user delegation scenarios**

User delegation scenarios enable agent applications to operate on behalf of users. In this

scenario, tokens preserve user identity while identifying the agent identity blueprint as the

acting entity. The OBO protocol requires token audience to match the client ID. However, for

agent identity (agent ID), the incoming token has the audience of the agent identity blueprint.

In this scenario, tokens have the following key characteristics:

Maintain user identity context throughout operations

Include delegated permissions granted to the agent identity blueprint

Enable policy evaluation at both user and application levels

Support both interactive and background operations

The agent identity receives delegated permissions that can be directly assigned or inherited

from the parent agent identity blueprint when impersonation is used.

Application-only scenarios represent autonomous operations where agent identity blueprints

act on their own behalf without user context.

In this scenario, tokens have the following key characteristics:

Represent the agent identity blueprint's own identity

Include application-level permissions directly assigned by the tenant administrator

Enable unscoped access within granted permission boundaries. Delegated permissions

aren't applied.

Support fully autonomous background operations

Agent user impersonation scenarios enable agent users to operate like human users. These

tokens support scenarios where agents need user-like context but with controlled, predefined

identities.

In this scenario, tokens have the following key characteristics:

Use specialized agent user identities

Maintain user-context behavior patterns

Include scoped delegated permissions

Require explicit assignment to agent identities

In this scenario, the agent identity blueprint impersonates the agent identity, which then

impersonates the assigned agent user. Access is scoped to delegated permissions assigned to

the agent identity, ensuring the agent can't exceed its granted permissions even when

**Tokens in application-only scenarios**

**Tokens in agent user impersonation scenarios**

operating with user context. Agent users can only be used when assigned to an agent identity

and can't authenticate independently.

Both agents and nonagentic OBO clients carry forward subject facets. It enables resource

servers to apply appropriate policies and logging for agent subjects. It also enables proper

attribution even when tokens pass through nonagentic intermediaries.

Platforms that create agents and integrate with Microsoft Entra Agent ID don't receive special

token claims. These platforms use standard token claims appropriate for their authentication

method and don't participate in the specialized agent claim structure.

All tokens contain a tenant ID ( ` tid` ) representing the organization's tenant. Tokens are

bounded within the tenant of the agent identity. Each agent identity receives tokens scoped to

its operational tenant. Agent identities can't access resources outside their assigned customer

tenant. Permission inheritance flows directly from parent to child entities.

Clients using agent identities are expected to treat the access tokens issued to them to use at

resource servers as opaque, and not try to parse them. However, resource servers that receive

access tokens issued to agents need to parse the tokens to validate them and extract claims for

authorization purposes.

Resource servers should validate agent tokens by:

Verifying standard OAuth claims (aud, exp, iss)

Checking agent facet claims for proper entity identification

Validating permissions based on token type (delegated vs app-only)

Ensuring tenant boundary compliance

Token claims enable policy engines to:

Identify agents vs nonagentic clients

Distinguish between different agent scenarios

Apply appropriate conditional access policies

**Nonagentic API integration**

**Builder application claims**

**Tenancy models and token behavior**

**Token validation**

Generate accurate audit logs

Example of the validation process would be to do the following actions:

Check if a token was issued for an agent identity and for which agent blueprint.

C#

Check if a token was issued for an agent user identity.

C#

These two extensions methods, apply to both `ClaimsIdentity` and `ClaimsPrincipal` .

Token claims provide the foundation for comprehensive audit trails:

`azp` identifies the requesting agent identity for client attribution

`oid` identifies the subject for resource access attribution

`xms_act_fct` and `xms_sub_fct` enable detailed flow analysis

`tid` ensures proper tenant context in logs

Agent token claims

**Last updated on 11/18/2025**

`HttpContext.User.GetParentAgentBlueprint()`

`HttpContext.User.IsAgentUserIdentity()`

**Audit and logging integration**

**Related content**

**Authentication protocols in agents**

Agents use OAuth 2.0 protocols with specialized token exchange patterns enabled by

Federated Identity Credentials (FIC). All agent auth flows involve multi-stage token exchanges

where the agent identity blueprint impersonates the agent identity to perform operations. This

article explains the authentication protocols and token flows used by agents. It covers

delegation scenarios, autonomous operations, and federated identity credential patterns.

Microsoft recommends that you use our SDKs like Microsoft Entra SDK for Agent ID

since

implementing these protocol steps isn't easy.

All agent entities are confidential clients that can also serve as APIs for On-Behalf-Of scenarios.

Interactive flows aren't supported for any agent entity type, ensuring that all authentication

occurs through programmatic token exchanges rather than user interaction flows.

If you aren't familiar already, go through the following protocol docs.

Microsoft identity platform and OAuth 2.0 On-Behalf-Of flow

Microsoft identity platform and the OAuth 2.0 client credentials flow

The following are the supported grant types for agent applications.

Agent identity blueprints support `client_credentials` enabling secure token acquisition for

impersonation scenarios. The `jwt-bearer` grant type facilitates token exchanges in On-Behalf

Of scenarios, allowing for delegation patterns. `refresh_token` grants enable background

operations with user context, supporting long-running processes that maintain user

authorization.

２ **Warning**

Microsoft recommends using the approved SDKs like Microsoft.Identity.Web and

Microsoft Agent ID SDK libraries to implement these protocols. Manual implementation of

these protocols is complex and error-prone, and using the SDKs helps ensure security and

compliance with best practices.

**Prerequisites**

**Supported grant types**

**Agent identity blueprint**

Agent identities use `client_credentials` for app-only autonomous operations, enabling

independent functionality without user context, and impersonation for a user agent identity.

The `jwt-bearer` grant type supports both client credential flow and On-Behalf Of (OBO) flow

providing flexibility in delegation patterns. ` refresh_token` grants facilitate background user-

delegated operations, allowing agent identities to maintain user context across extended

operations.

The agent application model explicitly excludes certain authentication patterns to maintain

security boundaries. OBO flows using the `/authorize` endpoint aren't supported for any agent

entity, ensuring all authentication occurs programmatically.

Public client capabilities aren't available, requiring all agents to operate as confidential clients.

Redirect URLs aren't supported.

Agents can operate in three primary modes:

Agents operating on behalf of regular users in Microsoft Entra ID (interactive agents). This

is a regular on-behalf-of flow.

Agents operating on their own behalf using service principals created for agents

(autonomous).

Agents operating on their own behalf using user principals created specifically for that

agent (for instance agents having their own mailbox).

Managed identities are the preferred credential type. In this configuration, the managed

identity token serves as the credential for the parent agent identity blueprint, while standard

MSI protocols apply for credential acquisition. This integration allows the agent ID to receive

the full benefits of MSI security and management, including automatic credential rotation and

secure storage.

**Agent identity**

**Unsupported flows**

**Core protocol patterns**

**Managed identities integration**

２ **Warning**

There are three agent oauth flows:

Agent on-behalf of flow: Agents operating on behalf of regular users (interactive agents).

Autonomous app flow: App-only operations enable agent identities to act autonomously

without user context.

Agent user flow: Agents operating on their own behalf using user principals created

specifically for agents.

**Last updated on 11/18/2025**

Client secrets shouldn't be used as client credentials in production environments for agent

identity blueprints due to security risks. Instead, use more secure authentication methods

such as **federated identity credentials (FIC) with managed identities** or client certificates.

These methods provide enhanced security by eliminating the need to store sensitive

secrets directly within your application configuration.

**Oauth protocols**

![](./assets/output_113_1.png)



**Agent autonomous app OAuth flow - App-**

**only protocol**

App-only operations enable agent identities to act autonomously without user context, using

client credentials flows. The agent identity (actor) is used to obtain a token for itself (subject).

To obtain this token, the agent identity blueprint impersonates the agent identity. Subjects use

app-only access but are supposed to be only assigned the permissions necessary. Tenant

administrators grant all permissions.

Agent identity blueprints can only impersonate their child agent identities. Only a single agent

identity blueprint can impersonate an agent identity. An agent identity blueprint can

impersonate many agent identities, but no agent identity can be owned by multiple blueprints.

Agent identities are always single-tenant regardless of their parent Agent identity blueprint's

tenancy model. Each agent identity operates within one tenant's security and policy

boundaries.

Managed identities are the preferred credential type. In this configuration, the managed

identity token serves as the credential for the parent agent identity blueprint, while standard

MSI protocols apply for credential acquisition. This integration allows the agent ID to receive

the full benefits of MSI security and management, including automatic credential rotation and

secure storage.

The following are the protocol steps.

２ **Warning**

Microsoft recommends using the approved SDKs like Microsoft.Identity.Web and

Microsoft Agent ID SDK libraries to implement these protocols. Manual implementation of

these protocols is complex and error-prone, and using the SDKs helps ensure security and

compliance with best practices.

**Managed identities integration**

**Protocol steps**

![](./assets/output_115_1.png)

1\. Agent identity blueprint requests an exchange token T1. The agent identity blueprint

presents its credentials that could be a secret, a certificate, or a managed identity token.

Microsoft Entra ID returns the T1 to the agent identity blueprint. In this example we use a

managed identity as Federated Identity Credential (FIC).

Where TUAMI is the managed identity token for user assigned managed identity (UAMI).

This step returns T1. Where T1 is the token-exchange token for FIC.

2\. Agent identity sends a token exchange request to Microsoft Entra ID. The request

includes the token T1.

２ **Warning**

Client secrets shouldn't be used as client credentials in production environments for

agent identity blueprints due to security risks. Instead, use more secure

authentication methods such as **federated identity credentials (FIC) with managed**

**identities** or client certificates. These methods provide enhanced security by

eliminating the need to store sensitive secrets directly within your application

configuration.

`POST /oauth2/v2.0/token`

`Content-Type: application/x-www-form-urlencoded`

`client_id=AgentBlueprint`

`&scope=api://AzureADTokenExchange/.default`

`&fmi_path=AgentIdentity`

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion=TUAMI`

`&grant_type=client_credentials`

3\. Microsoft Entra ID issues an app-only resource access token (TR) to the agent identity

after validating T1. Microsoft Entra ID validates that T1 (aud) == Agent identity parent

app == Agent identity blueprint

The following is a sequence diagram for the app-only flow:

![](./assets/output_116_1.png)

Oauth2.0 flows for agents

On-behalf-of flow in agents

Agent user flow in agents

`POST /oauth2/v2.0/token`

`Content-Type: application/x-www-form-urlencoded`

`client_id=AgentIdentity`

`&scope=https://resource.example.com/.default`

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion={T1}`

`&grant_type=client_credentials`

**Sequence diagram**

**Related content**

**Last updated on 11/18/2025**

**Agent OAuth flows: On behalf of flow**

Agents (agent identity blueprints) operating on behalf of regular, signed-in users use the

standard OAuth 2.0 protocol with all its capabilities. User delegation enables agent identities to

operate on behalf of signed-in users using standard OAuth 2.0 On-Behalf-Of flows with agent-

specific impersonation. The agent identity is assigned the necessary delegated permissions

needed for OBO access. It requires consent from users to access their data.

Agents have the capabilities of Microsoft Entra ID resource (API) applications and support the

API attributes required for the (OAuth2Permissions, AppURI). Agents can’t use any OBO flows.

Redirect URIs aren't supported.

Managed identities are the preferred credential type. In this configuration, the managed

identity token serves as the credential for the parent agent identity blueprint, while standard

MSI protocols apply for credential acquisition. This integration allows the agent ID to receive

the full benefits of MSI security and management, including automatic credential rotation and

secure storage.

Agents aren't supported for OBO ( ` /authorize` ) flows. Supported grant types are

`client_credential` , `jwt_bearer` , and `refresh_token` . The flow involves the agent identity

blueprint, agent identity, and a client credential. The client credential can be a client secret, a

client certificate, or a managed identity used as Federated Identity Credential (FIC).

２ **Warning**

Microsoft recommends using the approved SDKs like Microsoft.Identity.Web and

Microsoft Agent ID SDK libraries to implement these protocols. Manual implementation of

these protocols is complex and error-prone, and using the SDKs helps ensure security and

compliance with best practices.

**Managed identities integration**

**Protocol steps**

![](./assets/output_119_1.png)

1\. The user authenticates with the client and obtains a user access token (client token, Tc).

2\. Client sends the user access token (Tc) to the agent identity blueprint to act on behalf of

the user. It's the token that is used for the OBO exchange for the agent identity blueprint.

3\. The agent identity blueprint requests an exchange token by presenting its client

credential (secret, certificate, or managed identity token (TUAMI)). In this example, we use

a managed identity as FIC. Microsoft Entra ID returns token T1 to the agent.

Where TUAMI is the managed identity token for user assigned managed identity (UAMI).

This step returns T1.

4\. The agent identity, a child of the agent identity blueprint, sends an OBO token exchange

request. This request includes both T1 and the user access token Tc.

２ **Warning**

Client secrets shouldn't be used as client credentials in production environments for

agent identity blueprints due to security risks. Instead, use more secure

authentication methods such as **federated identity credentials (FIC) with managed**

**identities** or client certificates. These methods provide enhanced security by

eliminating the need to store sensitive secrets directly within your application

configuration.

`POST /oauth2/v2.0/token`

`Content-Type: application/x-www-form-urlencoded`

`client_id=AgentBlueprint`

`&scope=api://AzureADTokenExchange/.default`

`&fmi_path=AgentIdentity`

`&client_assertion=TUAMI`

`&grant_type=client_credentials`

5\. Microsoft Entra ID returns the resource token after validating both the T1 and Tc. The

OBO protocol requires token audience to match the client ID:

T1 (aud) == Agent identity Parent app == Agent identity blueprint client ID

Tc (aud) == Agent identity blueprint client ID

The following sequence diagram shows the OBO flow

![](./assets/output_120_1.png)

Refresh token can be used for asynchronous scenarios and background processes:

`POST /oauth2/v2.0/token`

`Content-Type: application/x-www-form-urlencoded`

`client_id=AgentIdentity`

`&scope=https://resource.example.com/scope1`

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion={T1}`

`&grant_type=urn:ietf:params:oauth:grant-type:jwt_bearer`

`&assertion={Tc(aud=AgentIdentity Blueprint, oid=User)}`

`&requested_token_use=on_behalf_of`

**Sequence diagram**

**Refresh token support**

`POST /oauth2/v2.0/token`

`Content-Type: application/x-www-form-urlencoded`

Agent identities can inherit delegated permissions from their parent agent identity blueprint

when the `InheritDelegatedPermissions` property is enabled. This inheritance mechanism

reduces consent complexity for multi-instance scenarios by allowing agent identities to use

permissions already granted to their parent application. The inheritance functionality applies

specifically when FIC impersonation is used and enables efficient permission management

across multiple instances. However, inheritance works only within tenant boundaries, ensuring

that permission scope remains contained within appropriate organizational limits.

Oauth2.0 flows for agents

Autonomous app flow in agents

Agent user flow in agents

**Last updated on 11/18/2025**

`client_id=AgentIdentity`

`&scope=https://resource.example.com/scope1`

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion={T1}`

`&grant_type=refresh_token`

`&refresh_token={AgentIdentityRefreshToken}`

**Permission inheritance**

**Related content**

**Agent user impersonation protocol**

Agent user impersonation enables agent identities to operate with user context through agent

users, combining user permissions with autonomous operation. In this scenario, an agent

identity blueprint (actor 1) impersonates an agent identity (actor 2) that impersonates an agent

user (subject) using FIC. Access is scoped to delegations assigned to the agent identity. Agent

user can be impersonated only by a single agent identity.

Managed identities are the preferred credential type. In this configuration, the managed

identity token serves as the credential for the parent agent identity blueprint, while standard

MSI protocols apply for credential acquisition. This integration allows the agent ID to receive

the full benefits of MSI security and management, including automatic credential rotation and

secure storage.

Then following are the protocol steps.

![](./assets/output_122_1.png)

1\. The agent identity blueprint requests an exchange token (T1) that it uses for agent

identity impersonation. The agent identity blueprint presents client credentials that could

be a secret, a certificate, or a managed identity token used as an FIC.

２ **Warning**

Microsoft recommends using the approved SDKs like Microsoft.Identity.Web and

Microsoft Agent ID SDK libraries to implement these protocols. Manual implementation of

these protocols is complex and error-prone, and using the SDKs helps ensure security and

compliance with best practices.

**Managed identities integration**

**Protocol steps**

Where TUAMI is the MSI token for user assigned managed identity (UAMI). This returns

token T1.

2\. The agent identity requests a token (T2) that it uses for agent user impersonation. The

agent identity presents T1 as its client assertion. Microsoft Entra ID returns T2 to the

agent identity after validating that T1 (aud) == Agent identity parent app == Agent

identity blueprint.

This returns token T2.

3\. The agent identity then sends an OBO token exchange request to Microsoft Entra ID,

including both T1 and T2. Microsoft Entra ID validates that T2 (aud) == agent identity.

２ **Warning**

Client secrets shouldn't be used as client credentials in production environments for

agent identity blueprints due to security risks. Instead, use more secure

authentication methods such as **federated identity credentials (FIC) with managed**

**identities** or client certificates. These methods provide enhanced security by

eliminating the need to store sensitive secrets directly within your application

configuration.

`POST /oauth2/v2.0/token`

`Content-Type: application/x-www-form-urlencoded`

`client_id=AgentBlueprint`

`&scope=api://AzureADTokenExchange/.default`

`&fmi_path=AgentIdentity`

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion=TUAMI`

`&grant_type=client_credentials`

`POST /oauth2/v2.0/token`

`Content-Type: application/x-www-form-urlencoded`

`client_id=AgentIdentity`

`&scope=api://AzureADTokenExchange/.default`

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion={T1}`

`&grant_type=client_credentials`

4\. Microsoft Entra ID then issues the resource token.

The following sequence diagram shows the agent user impersonation flow

![](./assets/output_124_1.png)

Agent user impersonation requires credential chaining that follows the pattern agent identity

blueprint → Agent identity → Agent user. Each step in this chain uses the token from the

previous step as a credential, creating a secure delegation pathway. The same client ID must be

used for both phases to prevent privilege escalation attacks.

**Last updated on 11/18/2025**

`POST /oauth2/v2.0/token`

`Content-Type: application/x-www-form-urlencoded`

`client_id=AgentIdentity`

`&scope=https://resource.example.com/scope1`

`&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`

`&client_assertion={T1}`

`&assertion={T2}`

`&username=agentuser@contoso.com`

`&grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer`

`&requested_token_use=on_behalf_of`

**Sequence diagram**

**Token claims reference for agents**

Agents use specialized token claims to identify different entity types and their relationships

during authentication and authorization flows. These claims enable proper attribution, policy

evaluation, and audit trails for agent operations. This article outlines the token claims for agent

applications, detailing how tokens identify agent entities and their roles in authentication flows.

Clients using agent identities are expected to treat the access tokens issued to them to use at

resource servers as opaque, and not try to parse them. However, resource servers that receive

access tokens issued to agents need to parse the tokens to validate them and extract claims for

authorization purposes.

Tokens issued for identities used for resource access include claims that you'd normally expect

to see in access tokens that Microsoft Entra issues. For more information, see access token

claim reference. The following example shows a sample access token issued to an agent acting

autonomously.

JSON

**Core token claim types**

`{`

`  ``"aud"` `: ``"f2510d34-8dca-4ab8-a0bc-aaec4d3a3e36"` `,`

`  ``"iss"` `: ``"https://sts.windows.net/00000001-0000-0ff1-ce00-000000000000/"` `,`

`  ``"iat"` `: 1753392285,`

`  ``"nbf"` `: 1753392285,`

`  ``"exp"` `: 1753421385,`

`  ``"aio"` `: ``"Y2JgYGhn1nzmErKqi0vc4Fr6H22/C5/4FP+xZbZYpik8nRkp+gEA"` `,`

`  ``"appid"` `: ``"aaaaaaaa-1111-2222-3333-444444444444"` `,`

`  ``"appidacr"` `: ``"2"` `,`

`  ``"idp"` `: ``"https://sts.windows.net/00000001-0000-0ff1-ce00-000000000000/"` `,`

`  ``"idtyp"` `: ``"app"` `,`

`  ``"oid"` `: ``"bbbbbbbb-1111-2222-3333-444444444444"` `,`

`  ``"rh"` `: ``"1.AAAAAQAAAAAA8Q_OAAAAAAAAADQNUfLKjbhKoLyq7E06PjYAAAAAAA."` `,`

`  ``"sub"` `: ``"cccccccc-1111-2222-3333-444444444444"` `,`

`  ``"tid"` `: ``"00000001-0000-0ff1-ce00-000000000000"` `,`

`  ``"uti"` `: ``"m5RaaRnoFUyp2TbSCAAAAA"` `,`

`  ``"ver"` `: ``"1.0"` `,`

`  ``"xms_act_fct"` `: ``"3 9 11"` `,`

`  ``"xms_ftd"` `: ``"Z5DrW4HFOkR_Lz0M5qETa260d2-fO6seMZJ_tOwRNuc"` `,`

`  ``"xms_idrel"` `: ``"7 10"` `,`

`  ``"xms_sub_fct"` `: ``"9 3 11"` `,`

`  ``"xms_tnt_fct"` `: ``"3 9"` `,`

`  ``"xms_par_app_azp"` `: ``"30cf4c22-9985-4ef7-8756-91cc888176bd"`

`}`

In v2 tokens, you see `azp` instead of `appid` . They both refer to the application ID of the agent

identity.

You'd notice that the token includes a few claims that aren't previously seen in access tokens

issued to applications. The following optional claims are also supported to identify that the

tokens are for agent identities. They also provide more context in which the agent identity is

acting.

`xms_tnt_fct`

`xms_sub_fct`

`xms_act_fct`

`xms_par_app_azp`

**Claim Name**

**Description**

`tid`

Tenant ID of the customer tenant where the agent identity is registered. It's the tenant

where the token is valid.

`sub`

Subject (the user, service principal, or agent identity being authenticated)

`oid`

Object ID of the subject. User object ID for user delegation scenarios. Agent ID service

principal OID for app-only scenarios. Agent user OID for user impersonation scenarios.

`idtyp`

Type of entity the subject is. Values are `user` , `app` .

`tid`

Tenant ID of the customer tenant where the agent identity is registered.

`xms_idrel`

Relationship between the subject and the resource tenant. Learn more.

`aud`

Audience (the API that the agent is trying to access)

`azp` or `appid`

Authorized party / actor. The application ID of the agent identity. Enables proper client

attribution in audit logs.

`scp`

Scope. Delegated permissions for user-context tokens. Only present in user delegation

and agent user scenarios. Empty or `/` for app-only scenarios

`xms_act_fct`

Actor facets claim. Learn more.

`xms_sub_fct`

Subject facets claim. Learn more .

`xms_tnt_fct`

Tenant facets claim. Learn more .

`xms_par_app_azp`

Parent application of the authorized party. Learn more .

ﾉ

**Expand table**

The `xms_idrel` claim indicates the identity relationship between the entity for which the token

is issued and the resource tenant.

Here are the possible values for the `xms_idrel` claim. It's a multivalued claim, meaning it can

have multiple values, separated by spaces. The values are represented as integers. The valid

values are always odd numbers starting from 1.

**Claim Value**

**Description**

`1`

Member user

`3`

MSA member user

`5`

Guest user

`7`

Service principal

`9`

Device principal

`11`

GDAP user

`13`

SPLess application

`15`

Passthrough

`17`

Native identity user with profile

`19`

Native identity user

`21`

Native identity Teams meeting participant

`23`

Passthrough authenticated Teams meeting participant

`25`

Native identity content sharing user

`27`

Fully synced MTO member

`29`

Weak MTO user

`31`

DAP user

`33`

Federated managed identity

**xms\_idrel**

ﾉ

**Expand table**

**xms\_tnt\_fct, xms\_sub\_fct, and xms\_act\_fct claims**

The `xms_tnt_fct` claim describes the tenant (identified by the `tid` claim). The `xms_sub_fct` and

`xms_act_fct` claims are used to describe facts about the subject ( ` sub` ) and the actor ( ` azp` or

`appid` ) of the token, respectively. These claims provide more context about the agent's identity

and the actions it's performing.

Here are the relevant values for these claims. These claims are multivalued, meaning they can

have multiple values, separated by spaces. The valid values are always odd numbers starting

from 1.

**Claim Value**

**Description**

`11`

AgentIdentity

`13`

AgentIDUser

You should ignore any values that aren't relevant to your scenario or validation logic. Ignore

the values that aren't relevant to your application. Don't assume any order of the values in

these claims.

The `xms_par_app_azp` claim is used to identify the parent application of the authorized party

( ` azp` or `appid` ). It's a GUID, when included. You can use the claim to determine the parent

Log the parent application ID for auditing purposes. Microsoft Entra ID sign-in logs always

includes the parent ID if available, so resource server should do the same. It isn't recommended

to use the parent application ID for authorization decisions, as it would result in widespread

access by many agents.

The following section outlines some auth scenarios and the relevant claims for each one of

them.

In this scenario, the agent identity is acting on behalf of a human user. The access token

includes the following claims:

ﾉ

**Expand table**

**xms\_par\_app\_azp**

**Scenario-wise examples**

**Agent identity acting on behalf of a human user**

**Claim Name**

**Description**

`tid`

Tenant ID of the customer tenant

`idtyp`

`user` (indicating the subject is a user)

`xms_idrel`

`1` (indicating a member user; others possible too)

`azp` / `appid`

Application ID of the agent identity

`scp`

Delegated permissions granted to the agent identity

`oid`

Object ID of the user

`aud`

Resource audience for the token

`xms_act_fct`

`11` (AgentIdentity)

In this scenario, the agent identity acts using its own identity. The access token includes the

following claims:

**Claim Name**

**Description**

`tid`

Tenant ID of the customer tenant

`idtyp`

`app` (indicating the subject is an application)

`xms_idrel`

`7` (indicating a service principal)

`azp` / `appid`

Application ID of the agent identity

`roles`

Permissions granted to the agent identity

`oid`

Object ID of the agent identity

`xms_act_fct`

`11` (AgentIdentity)

`xms_sub_fct`

`11` (AgentIdentity)

`aud`

Resource audience for the token

`scp`

Empty or `/` (unscoped).

ﾉ

**Expand table**

**Agent identity acting autonomously**

ﾉ

**Expand table**

In this scenario, the agent obtains a token using the agent user associated with its agent

identity. The access token includes the following claims:

**Claim Name**

**Description**

`tid`

Tenant ID of the customer tenant

`idtyp`

`user` (indicating the subject is a user)

`xms_idrel`

`1` (indicating a member user; others possible too)

`azp` / `appid`

Application ID of the agent identity

`scp`

Delegated permissions granted to the agent identity

`oid`

Object ID of the agent user

`xms_act_fct`

`11` (Agent identity)

`xms_sub_fct`

`13` (Agent user)

`aud`

Resource audience for the token

**Last updated on 11/18/2025**

**Agent identity acts autonomously via agent user**

ﾉ

**Expand table**

**Microsoft Graph permissions reference**

For an app to access data in Microsoft Graph, the user or administrator must grant it the

permissions it needs. This article lists the delegated and application permissions exposed by

Microsoft Graph. For guidance about how to use the permissions, see the Overview of

Microsoft Graph permissions.

To read information about all Microsoft Graph permissions programmatically, sign in to an API

client such as Graph Explorer using an account that has at least the _Application.Read.All_

permission and run the following request.

msgraph

**Category**

**Application**

**Delegated**

Identifier

d07a8cc0-3d51-4b77-b3b0-

32704d1f69fa

ebfcd32b-babb-40f4-a14b-

42706e83bd28

DisplayText

Read all access reviews

Read all access reviews that user can

access

Description

Allows the app to read access

reviews, reviewers, decisions and

settings in the organization, without

a signed-in user.

Allows the app to read access reviews,

reviewers, decisions and settings that

the signed-in user has access to in the

organization.

`GET https://graph.microsoft.com/v1.0/servicePrincipals(appId='00000003-0000-0000-`

`c000-000000000000')?`

`$select=id,appId,displayName,appRoles,oauth2PermissionScopes,resourceSpecificApplica`

`tionPermissions`

７ **Note**

As a best practice, request the least privileged permissions that your app needs in order to

access data and function correctly. Requesting permissions with more than the necessary

privileges is poor security practice, which may cause users to refrain from consenting and

affect your app's usage.

**All permissions**

**AccessReview.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ef5f7d5c-338f-44b0-86c3-

351f46c8bb5f

e4aa47b9-9a69-4109-82ed-

36ec70d85ff1

DisplayText

Manage all access reviews

Manage all access reviews that user

can access

Description

Allows the app to read, update,

delete and perform actions on access

reviews, reviewers, decisions and

settings in the organization, without

a signed-in user.

Allows the app to read, update, delete

and perform actions on access reviews,

reviewers, decisions and settings that

the signed-in user has access to in the

organization.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

18228521-a591-40f1-b215-

5fad4488c117

5af8c3f5-baca-439a-97b0-

ea58a435e269

DisplayText

Manage access reviews for group

and app memberships

Manage access reviews for group and

app memberships

Description

Allows the app to read, update,

delete and perform actions on access

reviews, reviewers, decisions and

settings in the organization for group

and app memberships, without a

signed-in user.

Allows the app to read, update, delete

and perform actions on access reviews,

reviewers, decisions and settings for

group and app memberships that the

signed-in user has access to in the

organization.

AdminConsentRequired

Yes

Yes

**AccessReview.ReadWrite.All**

ﾉ

**Expand table**

**AccessReview.ReadWrite.Membership**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

8c0aed2c-0c61-433d-b63c-

6370ddc73248

9084c10f-a2d6-4713-8732-

348def50fe02

DisplayText

Read all acronyms

Read all acronyms that the user can

access

Description

Allows an app to read all acronyms

without a signed-in user.

Allows an app to read all acronyms that

the signed-in user can access.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

134fd756-38ce-4afd-ba33-

e9623dbe66c2

3361d15d-be43-4de6-b441-

3c746d05163d

DisplayText

Read all administrative units

Read administrative units

Description

Allows the app to read administrative

units and administrative unit

membership without a signed-in

user.

Allows the app to read administrative

units and administrative unit

membership on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

5eb59dd3-1da2-4329-8733-

7b8a2d34-6b3f-4542-a343-

**Acronym.Read.All**

ﾉ

**Expand table**

**AdministrativeUnit.Read.All**

ﾉ

**Expand table**

**AdministrativeUnit.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

9dabdc435916

54651608ad81

DisplayText

Read and write all administrative

units

Read and write administrative units

Description

Allows the app to create, read,

update, and delete administrative

units and manage administrative unit

membership without a signed-in user.

Allows the app to create, read, update,

and delete administrative units and

manage administrative unit

membership on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

aec9e0a0-6f46-4150-a9f7-

05e9e3e87399

73ea6732-992c-4292-98f7-

9feff18d3ade

DisplayText

Read all agent cards in Agent Registry

Read agent cards in Agent Registry

Description

Allows the app to read all agent cards

and their skills in your organization's

Agent Registry without a signed-in

user.

Allows the app to read agent cards

and their skills in your organization's

Agent Registry on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ef566853-42d6-45a5-bed9-

5ccb82c98b4f

b0f726a8-0fa2-4ce2-937b-

fd17a446261f

DisplayText

Read and write all agent cards in

Agent Registry

Read and write agent cards in Agent

Registry

**AgentCard.Read.All**

ﾉ

**Expand table**

**AgentCard.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to create, read,

update, and delete all agent cards

and manage their skills in your

organization's Agent Registry without

a signed-in user.

Allows the app to create, read, update,

and delete agent cards and manage

their skills in your organization's Agent

Registry on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

9c4a07db-e0c1-4fb0-8e85-dfd8ae3b8201

-

DisplayText

Read and write managed-by agent cards in Agent Registry

-

Description

Allows the app to read and update agent cards that designate the

calling app as their manager and manage their skills in your

organization's Agent Registry without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

3ee18438-e6e5-4858-8f1c-

d7b723b45213

ada96a26-9579-4c29-a578-

c3482a765716

DisplayText

Read all agent card manifests in

Agent Registry

Read agent card manifests in Agent

Registry

Description

Allows the app to read all agent card

manifests in your organization's

Agent Registry without a signed-in

user.

Allows the app to read agent card

manifests in your organization's Agent

Registry on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**AgentCard.ReadWrite.ManagedBy**

ﾉ

**Expand table**

**AgentCardManifest.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

228b1a03-f7ca-4348-b50d-

e8a547ab61af

80151b1a-1c31-4846-ae0d-

c79939ee13d1

DisplayText

Read and write all agent card

manifests in Agent Registry

Read and write agent card manifests

in Agent Registry

Description

Allows the app to read and write to all

agent card manifests in your

organization's Agent Registry without

a signed-in user.

Allows the app to read and write

agent card manifests in your

organization's Agent Registry on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

77f6034c-52f5-4526-9fa1-d55a67e72cc4

-

DisplayText

Read and write managed-by agent card manifests in Agent

Registry

-

Description

Allows the app to read and write agent card manifests that name

it as manager in your organization's Agent Registry without a

signed-in user.

-

AdminConsentRequired

Yes

-

**AgentCardManifest.ReadWrite.All**

ﾉ

**Expand table**

**AgentCardManifest.ReadWrite.ManagedBy**

ﾉ

**Expand table**

**AgentCollection.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

e65ee1da-d1d5-467b-bdd0-

3e9bb94e6e0c

fa50be38-fdff-469c-96dc-

ef5fce3c64bf

DisplayText

Read all collections in Agent Registry

Read collections in Agent Registry

Description

Allows the app to read all collections

and their membership in your

organization's Agent Registry without

a signed-in user.

Allows the app to read collections and

their membership in your

organization's Agent Registry on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

b14924c8-87f1-438a-81f2-dc370ba2f45d

DisplayText

-

Read global collection in Agent Registry

Description

-

Allows the app to read global collection and its membership in

your organization's Agent Registry on behalf of the signed-in

user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

43acfda3-daf3-4aa4-955d-b051d0024e82

DisplayText

-

Read quarantined collection in Agent Registry

Description

-

Allows the app to read quarantined collection and its

membership in your organization's Agent Registry on behalf of

the signed-in user.

AdminConsentRequired

-

Yes

**AgentCollection.Read.Global**

ﾉ

**Expand table**

**AgentCollection.Read.Quarantined**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

feb31d7d-a227-4487-898c-

e014840d07b3

6d8a7002-a05e-4b95-a768-

0e6f0badc6c8

DisplayText

Read and write all collections in Agent

Registry

Read and write collections in Agent

Registry

Description

Allows the app to create, read, update,

and delete all collections and manage

their membership in your

organization's Agent Registry without

a signed-in user.

Allows the app to create, read,

update, and delete collections and

manage their membership in your

organization's Agent Registry on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

c001dd65-8a6b-4349-ab0c-4e8a410d28d2

DisplayText

-

Read and write global collection in Agent Registry

Description

-

Allows the app to read and update global collection and

manage its membership in your organization's Agent Registry

on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**AgentCollection.ReadWrite.All**

ﾉ

**Expand table**

**AgentCollection.ReadWrite.Global**

ﾉ

**Expand table**

**AgentCollection.ReadWrite.ManagedBy**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

2e0fb698-9996-479f-926b-ce63f4397829

-

DisplayText

Read and write managed-by collections in Agent Registry

-

Description

Allows the app to create, read, update, and delete collections that

designate the calling app as their manager and manage their

membership in your organization's Agent Registry without a

signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

ae331cc9-9f51-484b-a90b-124f2e4a6398

DisplayText

-

Read and write quarantined collection in Agent Registry

Description

-

Allows the app to read and update quarantined collection and

manage its membership in your organization's Agent Registry

on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

799a4732-85b8-4c67-b048-

75f0e88a232b

4c3c738a-2df0-4877-bf4a-

f796950ff34c

DisplayText

Read all agent instances in Agent

Registry

Read agent instances in Agent

Registry

Description

Allows the app to read all agent

instances and their related collections

in your organization's Agent Registry

without a signed-in user.

Allows the app to read agent instances

and their related collections in your

organization's Agent Registry on

behalf of the signed-in user.

**AgentCollection.ReadWrite.Quarantined**

ﾉ

**Expand table**

**AgentInstance.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

07abdd95-78dc-4353-bd32-

09f880ea43d0

fc79e324-da24-497a-b5ec-

e7de08320375

DisplayText

Read and write all agent instances in

Agent Registry

Read and write agent instances in

Agent Registry

Description

Allows the app to create, read,

update, and delete all agent instances

in your organization's Agent Registry

without a signed-in user.

Allows the app to create, read, update,

and delete agent instances in your

organization's Agent Registry on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

782ab1bf-24f1-4c27-8bbc-2006d42792a6

-

DisplayText

Read and write managed-by agent instances in Agent Registry

-

Description

Allows the app to create, read, update, and delete agent instances

that designate the calling app as their manager in your

organization's Agent Registry without a signed-in user.

-

AdminConsentRequired

Yes

-

**AgentInstance.ReadWrite.All**

ﾉ

**Expand table**

**AgentInstance.ReadWrite.ManagedBy**

ﾉ

**Expand table**

**Agreement.Read.All**

**Category**

**Application**

**Delegated**

Identifier

2f3e6f8c-093b-4c57-a58b-

ba5ce494a169

af2819c9-df71-4dd3-ade7-

4d7c9dc653b7

DisplayText

Read all terms of use agreements

Read all terms of use agreements

Description

Allows the app to read terms of use

agreements, without a signed in

user.

Allows the app to read terms of use

agreements on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

c9090d00-6101-42f0-a729-

c41074260d47

ef4b5d93-3104-4664-9053-

a5c49ab44218

DisplayText

Read and write all terms of use

agreements

Read and write all terms of use

agreements

Description

Allows the app to read and write

terms of use agreements, without a

signed in user.

Allows the app to read and write terms

of use agreements on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

0b7643bb-5336-476f-80b5-18fbfbc91806

DisplayText

-

Read user terms of use acceptance statuses

Description

-

Allows the app to read terms of use acceptance statuses on

behalf of the signed-in user.

ﾉ

**Expand table**

**Agreement.ReadWrite.All**

ﾉ

**Expand table**

**AgreementAcceptance.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

d8e4ec18-f6c0-4620-8122-

c8b1f2bf400e

a66a5341-e66e-4897-9d52-

c2df58c2bfb9

DisplayText

Read all terms of use acceptance

statuses

Read terms of use acceptance statuses

that user can access

Description

Allows the app to read terms of use

acceptance statuses, without a

signed in user.

Allows the app to read terms of use

acceptance statuses on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

859cceb9-2ec2-4e48-bcd7-b8490b5248a5

DisplayText

-

Read user AI enterprise interactions.

Description

-

Allows the app to read user AI enterprise interactions, on behalf

of the signed-in user.

AdminConsentRequired

-

No

**AgreementAcceptance.Read.All**

ﾉ

**Expand table**

**AiEnterpriseInteraction.Read**

ﾉ

**Expand table**

**AiEnterpriseInteraction.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

839c90ab-5771-41ee-aef8-a562e8487c1e

-

DisplayText

Read all AI enterprise interactions.

-

Description

Allows the app to read all AI enterprise interactions.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

e03cf23f-8056-446a-8994-7d93dfc8b50e

DisplayText

-

Read user activity statistics

Description

-

Allows the app to read the signed-in user's activity statistics,

such as how much time the user has spent on emails, in

meetings, or in chat sessions.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

b86848a7-d5b1-41eb-a9b4-

54a4e6306e97

1b6ff35f-31df-4332-8571-

d31ea5a4893f

DisplayText

Read API connectors for

authentication flows

Read API connectors for authentication

flows

Description

Allows the app to read the API

connectors used in user

authentication flows, without a

signed-in user.

Allows the app to read the API

connectors used in user authentication

flows, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Analytics.Read**

ﾉ

**Expand table**

**APIConnectors.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

1dfe531a-24a6-4f1b-80f4-

7a0dc5a0a171

c67b52c5-7c69-48b6-9d48-

7b3af3ded914

DisplayText

Read and write API connectors for

authentication flows

Read and write API connectors for

authentication flows

Description

Allows the app to read, create and

manage the API connectors used in

user authentication flows, without a

signed-in user.

Allows the app to read, create and

manage the API connectors used in

user authentication flows, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e12dae10-5a57-4817-b79d-dfbec5348930

88e58d74-d3df-44f3-ad47-

e89edf4472e4

DisplayText

Read all app catalogs

Read all app catalogs

Description

Allows the app to read apps in the app

catalogs without a signed-in user.

Allows the app to read the apps

in the app catalogs.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

dc149144-f292-421e-b185-5953f2e98d7f

1ca167d5-1655-44a1-8adf-

1414072e1ef9

**APIConnectors.ReadWrite.All**

ﾉ

**Expand table**

**AppCatalog.Read.All**

ﾉ

**Expand table**

**AppCatalog.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write to all app catalogs

Read and write to all app catalogs

Description

Allows the app to create, read, update,

and delete apps in the app catalogs

without a signed-in user.

Allows the app to create, read,

update, and delete apps in the

app catalogs.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

3db89e36-7fa6-4012-b281-85f3d9d9fd2e

DisplayText

-

Submit application packages to the catalog and cancel pending

submissions

Description

-

Allows the app to submit application packages to the catalog

and cancel submissions that are pending review on behalf of the

signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

-

af281d3a-030d-4122-886e-146fb30a0413

DisplayText

-

Read the trusted certificate authority configuration for

applications

Description

-

Allows the app to read the trusted certificate authority

configuration which can be used to restrict application

certificates based on their issuing authority, on behalf of the

signed-in user.

AdminConsentRequired

-

Yes

**AppCatalog.Submit**

ﾉ

**Expand table**

**AppCertTrustConfiguration.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

4bae2ed4-473e-4841-a493-9829cfd51d48

DisplayText

-

Read and write the trusted certificate authority configuration for

applications

Description

-

Allows the app to create, read, update and delete the trusted

certificate authority configuration which can be used to restrict

application certificates based on their issuing authority, on

behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

3be0012a-cc4e-426b-895b-

f9c836bf6381

ffa91d43-2ad8-45cc-b592-

09caddeb24bb

DisplayText

Read and write the remote desktop

security configuration for all apps

Read and write the remote desktop

security configuration for apps

Description

Allows the app to read and write the

remote desktop security configuration

for all apps in your organization,

without a signed-in user.

Allows the app to read and write

other apps' remote desktop security

configuration, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**AppCertTrustConfiguration.ReadWrite.All**

ﾉ

**Expand table**

**Application-RemoteDesktopConfig.ReadWrite.All**

ﾉ

**Expand table**

**Application.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

9a5d68dd-52b0-4cc2-bd40-

abcf44ac3a30

c79f8feb-a9db-4090-85f9-

90d820caa0eb

DisplayText

Read all applications

Read applications

Description

Allows the app to read all

applications and service principals

without a signed-in user.

Allows the app to read applications

and service principals on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

![](./assets/output_147_1.png)![](./assets/output_147_2.png)

The _Application.Read.All_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

fc023787-fd04-4e44-9bc7-

d454f00c0f0a

0586a906-4d89-4de8-b3c8-

1aacdcc0c679

DisplayText

Read and update all apps

Read and update all apps

Description

Allows the app to read and update

all apps in your organization, without

a signed-in user.

Allows the app to read and update all

apps in your organization, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

1bfefb4e-e0b5-418b-a88f-

73c46d2cc8e9

bdfbf15f-ee85-4955-8675-

146e8e5296b5

DisplayText

Read and write all applications

Read and write all applications

**Application.ReadUpdate.All**

ﾉ

**Expand table**

**Application.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to create, read,

update and delete applications and

service principals without a signed-in

user. Does not allow management of

consent grants.

Allows the app to create, read, update

and delete applications and service

principals on behalf of the signed-in

user. Does not allow management of

consent grants.

AdminConsentRequired

Yes

Yes

![](./assets/output_148_1.png)![](./assets/output_148_2.png)

The _Application.ReadWrite.All_ delegated permission is available for consent in personal

Microsoft accounts.

Permissions that allow managing credentials, such as _Application.ReadWrite.All_, allow an

application to act as other entities, and use the privileges they were granted. Use caution when

granting any of these permissions.

**Category**

**Application**

**Delegated**

Identifier

18a4783c-866b-4cc7-a460-3d5e5662c884

-

DisplayText

Manage apps that this app creates or owns

-

Description

Allows the app to create other applications, and fully manage

those applications (read, update, update application secrets and

delete), without a signed-in user. It cannot update any apps that it

is not an owner of.

-

AdminConsentRequired

Yes

-

The _Application.ReadWrite.OwnedBy_ permission allows the same operations as

_Application.ReadWrite.All_ but only on applications and service principals that the calling app is

an owner of.

The _Application.ReadWrite.OwnedBy_ permission allows an app to call `GET /applications` and

`GET /servicePrincipals` endpoints to list all applications and service principals in the tenant.

This scope of access has been allowed for the permission.

**Application.ReadWrite.OwnedBy**

ﾉ

**Expand table**

**AppRoleAssignment.ReadWrite.All**

**Category**

**Application**

**Delegated**

Identifier

06b708a9-e830-4db3-a914-

8e69da51d44f

84bccea3-f856-4a8a-967b-

dbe0a3d53a64

DisplayText

Manage app permission grants and

app role assignments

Manage app permission grants and

app role assignments

Description

Allows the app to manage permission

grants for application permissions to

any API (including Microsoft Graph)

and application assignments for any

app, without a signed-in user.

Allows the app to manage permission

grants for application permissions to

any API (including Microsoft Graph)

and application assignments for any

app, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

b0df437d-d341-4df0-aa3e-89ca81a1207f

DisplayText

-

Read approvals

Description

-

Allows the app to read approvals on behalf of the signed-in

user.

AdminConsentRequired

-

Yes

ﾉ

**Expand table**

Ｕ **Caution**

Permissions that allow granting authorization, such as _AppRoleAssignment.ReadWrite.All_,

allow an application to grant additional privileges to itself, other applications, or any user.

Use caution when granting any of these permissions.

**ApprovalSolution.Read**

ﾉ

**Expand table**

**ApprovalSolution.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

9f265de7-8d5e-4e9a-a805-5e8bbc49656f

-

DisplayText

Read all approvals

-

Description

Allows the app to read all approvals and approval item

subscriptions, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

6768d3af-4562-48ff-82d2-c5e19eb21b9c

DisplayText

-

Read, create, and respond to approvals

Description

-

Allows the app to provision, read, create, and respond to

approvals on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

45583558-1113-4d06-8969-e79a28edc9ad

-

DisplayText

Read all approvals and manage approval subscriptions

-

Description

Allows the app to read all approvals and create, update, or

remove approval item subscriptions, without a signed-in user.

-

AdminConsentRequired

Yes

-

**ApprovalSolution.ReadWrite**

ﾉ

**Expand table**

**ApprovalSolution.ReadWrite.All**

ﾉ

**Expand table**

**ApprovalSolutionResponse.ReadWrite**

**Category**

**Application**

**Delegated**

Identifier

-

89d944f2-2011-44ad-830c-aa9bf5ef2319

DisplayText

-

Read and respond to approvals assigned to the current user

Description

-

Allows the app to read and respond to approvals on behalf of

the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

93283d0a-6322-4fa8-966b-

8c121624760d

104a7a4b-ca76-4677-b7e7-

2f4bc482f381

DisplayText

Read attack simulation data of an

organization

Read attack simulation data of an

organization

Description

Allows the app to read attack

simulation and training data for an

organization without a signed-in user.

Allows the app to read attack

simulation and training data for an

organization for the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e125258e-8c8a-42a8-8f55-

ab502afa52f3

27608d7c-2c66-4cad-a657-

951d575f5a60

DisplayText

Read, create, and update all attack

simulation data of an organization

Read, create, and update attack

simulation data of an organization

Description

Allows the app to read, create, and

update attack simulation and training

Allows the app to read, create, and

update attack simulation and training

ﾉ

**Expand table**

**AttackSimulation.Read.All**

ﾉ

**Expand table**

**AttackSimulation.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

data for an organization without a

signed-in user.

data for an organization for the

signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

99bc85fb-e857-4220-9f8c-

3a1c83148d2e

16786f81-40d2-4116-bb26-

d1a753bf0b20

DisplayText

Read activity audit log from the audit

store.

Read activity audit log from the audit

store.

Description

Read activity audit log from the audit

store.

Read activity audit log from the audit

store.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f6318678-2713-4bb6-b123-

233e7336c1bd

a78fd341-0672-4792-a8ae-

a5925b2546eb

DisplayText

Upload activity audit logs to the audit

store.

Upload activity audit logs to the audit

store.

Description

Allows the application to upload bulk

activity audit logs to the audit store.

Allows the application to upload bulk

activity audit logs to the audit store.

AdminConsentRequired

Yes

Yes

**AuditActivity.Read**

ﾉ

**Expand table**

**AuditActivity.Write**

ﾉ

**Expand table**

**AuditLog.Read.All**

**Category**

**Application**

**Delegated**

Identifier

b0afded3-3588-46d8-8b3d-

9842eff778da

e4c9e354-4dc5-45b8-9e7c-

e1393b0b1a20

DisplayText

Read all audit log data

Read audit log data

Description

Allows the app to read and query

your audit log activities, without a

signed-in user.

Allows the app to read and query your

audit log activities, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

20e6f8e4-ffac-4cf7-82f7-

70ddb7564318

ba78b16f-1e01-41b6-89ca-

73e0a32b304c

DisplayText

Read audit logs data from Dynamics

CRM workload

Read audit logs data from Dynamics

CRM workload

Description

Allows the app to read and query

audit logs from Dynamics CRM

workload, without a signed-in user

Allows the app to read and query audit

logs from Dynamics CRM workload, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

0bc85aed-7b0b-437a-bac8-

3b29a1b84c99

ee3409fe-617f-43cf-bd1e-

fc8b38049e69

DisplayText

Read audit logs data from Endpoint

Data Loss Prevention workload

Read audit logs data from Endpoint

Data Loss Prevention workload

ﾉ

**Expand table**

**AuditLogsQuery-CRM.Read.All**

ﾉ

**Expand table**

**AuditLogsQuery-Endpoint.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read and query

audit logs from Endpoint Data Loss

Prevention workload, without a

signed-in user

Allows the app to read and query audit

logs from Endpoint Data Loss

Prevention workload, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7276d950-48fc-4269-8348-

f22f2bb296d0

5ff2f415-e0f1-4d11-bfd0-

6d87c0f667fd

DisplayText

Read audit logs data from Entra

(Azure AD) workload

Read audit logs data from Entra (Azure

AD) workload

Description

Allows the app to read and query

audit logs from Entra (Azure AD)

workload, without a signed-in user

Allows the app to read and query audit

logs from Entra (Azure AD) workload,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

6b0d2622-d34e-4470-935b-

b96550e5ca8d

6c8c71d2-c7e1-45b0-ac6d-

1d2724fba6ae

DisplayText

Read audit logs data from Exchange

workload

Read audit logs data from Exchange

workload

Description

Allows the app to read and query

audit logs from Exchange workload,

without a signed-in user

Allows the app to read and query audit

logs from Exchange workload, on

behalf of a signed-in user.

AdminConsentRequired

Yes

Yes

**AuditLogsQuery-Entra.Read.All**

ﾉ

**Expand table**

**AuditLogsQuery-Exchange.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

8a169a81-841c-45fd-ad43-

96aede8801a0

4a72c235-a50d-4870-b598-

fd88fd1fa074

DisplayText

Read audit logs data from OneDrive

workload

Read audit logs data from OneDrive

workload

Description

Allows the app to read and query

audit logs from OneDrive workload,

without a signed-in user

Allows the app to read and query

audit logs from OneDrive workload,

on behalf of a signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

91c64a47-a524-4fce-9bf3-

3d569a344ecf

30630b65-ed12-4a81-9130-

e3a964109fae

DisplayText

Read audit logs data from SharePoint

workload

Read audit logs data from SharePoint

workload

Description

Allows the app to read and query

audit logs from SharePoint workload,

without a signed-in user

Allows the app to read and query audit

logs from SharePoint workload, on

behalf of a signed-in user.

AdminConsentRequired

Yes

Yes

**AuditLogsQuery-OneDrive.Read.All**

ﾉ

**Expand table**

**AuditLogsQuery-SharePoint.Read.All**

ﾉ

**Expand table**

**AuditLogsQuery.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

5e1e9171-754d-478c-812c-

f1755a9a4c2d

1d9e7ac3-0eca-442c-82f9-e92625af6e6d

DisplayText

Read audit logs data from all

services

Read audit logs data from all services

Description

Allows the app to read and

query audit logs from all

services.

Allows the app to read and query audit logs

from all services, on behalf of a signed-in

user

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

381f742f-e1f8-4309-b4ab-

e3d91ae4c5c1

57b030f1-8c35-469c-b0d9-

e4a077debe70

DisplayText

Read all authentication context

information

Read all authentication context

information

Description

Allows the app to read the

authentication context information in

your organization without a signed-

in user.

Allows the app to read all

authentication context information in

your organization on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

a88eef72-fed0-4bf7-a2a9-

f19df33f8b83

ba6d575a-1344-4516-b777-

1404f5593057

DisplayText

Read and write all authentication

context information

Read and write all authentication

context information

**AuthenticationContext.Read.All**

ﾉ

**Expand table**

**AuthenticationContext.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read and update

the authentication context

information in your organization

without a signed-in user.

Allows the app to read and update all

authentication context information in

your organization on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

5fbb5982-3230-4882-93c0-

2167523ce0c2

444ed4b6-0554-4dc6-8e9c-

3f9a34ee3ff6

DisplayText

Read all backup configuration policies

Read backup configuration policies

Description

Allows the app to read all backup

configurations, and lists of Microsoft

365 service resources to be backed-

up, without a signed-in user.

Allows the app to read the backup

configuration, and list of Microsoft

365 service resources to be backed-

up, on behalf of the signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

18133149-5489-40ac-80f0-

4b6fa85f6cdc

a0244d16-171c-4496-8ffb-

7b9b6954d339

DisplayText

Read and edit all backup

configuration policies

Read and edit backup configuration

policies

Description

Allows the app to read and update

the backup configuration, and list of

Microsoft 365 service resources to be

backed-up, without a signed-in user.

Allows the app to read and update the

backup configuration, and list of

Microsoft 365 service resources to be

backed-up, on behalf of the signed in

user.

**BackupRestore-Configuration.Read.All**

ﾉ

**Expand table**

**BackupRestore-Configuration.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

6fe20a79-0e15-45a1-b019-

834c125993a0

af598c63-4292-4437-b925-

e996354d3854

DisplayText

Read the status of the M365 backup

service

Read the status of the M365 backup

service

Description

Allows the app to read the status of

M365 backup service

(enable/disable), without signed in

user

Allows the app to read the status of

M365 backup service (enable/disable),

on behalf of the signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

fb240865-88f8-4a1d-923f-

98dbc7920860

96d46335-d92d-41b8-bc9f-

273a692381ea

DisplayText

Update or read the status of the

M365 backup service

Update or read the status of the M365

backup service

Description

Allows the app to update or read the

status of M365 backup service

(enable/disable), without signed in

user

Allows the app to update or read the

status of M365 backup service

(enable/disable), on behalf of the

signed in user.

AdminConsentRequired

Yes

Yes

**BackupRestore-Control.Read.All**

ﾉ

**Expand table**

**BackupRestore-Control.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

ecae8511-f2d7-4be4-bdbf-

91f244d45986

b4e98de1-4600-4e90-b5e1-

7c1dfef04e5c

DisplayText

Read all monitoring, quota and billing

information for the tenant

Read monitoring, quota and billing

information for the tenant

Description

Allows the app to monitor all backup

and restore jobs, view quota usage

and billing details, without a signed-in

user.

Allows the app to monitor backup and

restore jobs, view quota usage and

billing details, on behalf of the signed

in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

87853aa5-0372-4710-b34b-

cef27bb7156e

94b36f78-434f-4904-8c08-

421d9a9c1dc2

DisplayText

Read all restore sessions

Read restore sessions

Description

Allows the app to read all restore

sessions, without a signed-in user.

Allows the app to read restore

sessions, on behalf of the signed in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

bebd0841-a3d8-4313-a51d-

731112c8ee41

9f89e109-94b9-4c9b-b4fc-

98cdaa54f574

**BackupRestore-Monitor.Read.All**

ﾉ

**Expand table**

**BackupRestore-Restore.Read.All**

ﾉ

**Expand table**

**BackupRestore-Restore.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read restore all sessions and start

restore sessions from backups

Read restore sessions and start restore

sessions from backups

Description

Allows the app to search all backup

snapshots for Microsoft 365

resources, and restore Microsoft 365

resources from a backed-up

snapshot, without a signed-in user.

Allows the app to search the backup

snapshots for Microsoft 365 resources,

and restore Microsoft 365 resources

from a backed-up snapshot, on behalf

of the signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f6135c51-c766-4be1-9638-

ed90c2ed2443

2b24830f-f435-446f-ab5a-

b1e70d9a2eb5

DisplayText

Search for metadata properties in all

backup snapshots

Search for metadata properties in

backup snapshots

Description

Allows the app to search all backup

snapshots for Microsoft 365

resources, without a signed-in user.

Allows the app to search the backup

snapshots for Microsoft 365 resources,

on behalf of the signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

9e8be751-7eee-4c09-bcfd-

d64f6b087fd8

2bf6d319-dfca-4c22-9879-

f88dcfaee6be

DisplayText

Read and write application billing

configuration

Read and write application billing

configuration

Description

Allows the app to read and write the

billing configuration on all

Allows the app to read and write the

billing configuration on all applications

**BackupRestore-Search.Read.All**

ﾉ

**Expand table**

**BillingConfiguration.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

applications without a signed-in user.

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

57f1cf28-c0c4-4ec3-9a30-

19a2eaaf2f6e

b27a61ec-b99c-4d6a-b126-

c4375d08ae30

DisplayText

Read all BitLocker keys

Read BitLocker keys

Description

Allows an app to read BitLocker

keys for all devices, without a

signed-in user. Allows read of the

recovery key.

Allows the app to read BitLocker keys on

behalf of the signed-in user, for their

owned devices. Allows read of the

recovery key.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f690d423-6b29-4d04-98c6-

694c42282419

5a107bfc-4f00-4e1a-b67e-

66451267bc68

DisplayText

Read all BitLocker keys basic

information

Read BitLocker keys basic information

Description

Allows an app to read basic

BitLocker key properties for all

devices, without a signed-in user.

Does not allow read of the recovery

key.

Allows the app to read basic BitLocker

key properties on behalf of the signed-

in user, for their owned devices. Does

not allow read of the recovery key itself.

AdminConsentRequired

Yes

Yes

**BitlockerKey.Read.All**

ﾉ

**Expand table**

**BitlockerKey.ReadBasic.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

6b22000a-1228-42ec-88db-

b8c00399aecb

7f36b48e-542f-4d3b-9bcb-

8406f0ab9fdb

DisplayText

Manage bookings information

Manage bookings information

Description

Allows an app to read, write and

manage bookings appointments,

businesses, customers, services, and

staff on behalf of the signed-in user.

Allows an app to read, write and

manage bookings appointments,

businesses, customers, services, and

staff on behalf of the signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

6e98f277-b046-4193-a4f2-

6bf6a78cd491

33b1df99-4b29-4548-9339-

7a7b83eaeebc

DisplayText

Read all Bookings related resources.

Read bookings information

Description

Allows an app to read Bookings

appointments, businesses, customers,

services, and staff without a signed-in

user.

Allows an app to read bookings

appointments, businesses, customers,

services, and staff on behalf of the

signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

0c4b2d20-7919-468d-8668-

c54b09d4dee8

948eb538-f19d-4ec5-9ccc-

f059e1ea4c72

**Bookings.Manage.All**

ﾉ

**Expand table**

**Bookings.Read.All**

ﾉ

**Expand table**

**Bookings.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write bookings information

Read and write bookings information

Description

Allows an app to read and write

bookings appointments, businesses,

customers, services, and staff on

behalf of the signed-in user. Does not

allow create, delete and publish of

booking businesses.

Allows an app to read and write

bookings appointments, businesses,

customers, services, and staff on

behalf of the signed-in user. Does not

allow create, delete and publish of

booking businesses.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

9769393e-5a9f-4302-9e3d-

7e018ecb64a7

02a5a114-36a6-46ff-a102-

954d89d9ab02

DisplayText

Read and write all Bookings related

resources.

Read and write booking appointments

Description

Allows an app to read and write

Bookings appointments and

customers, and additionally allows

reading businesses, services, and

staff without a signed-in user.

Allows an app to read and write

bookings appointments and customers,

and additionally allows read businesses

information, services, and staff on

behalf of the signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

be95e614-8ef3-49eb-8464-

1c9503433b86

98b17b35-f3b1-4849-a85f-

9f13733002f0

DisplayText

Read all bookmarks

Read all bookmarks that the user can

access

**BookingsAppointment.ReadWrite.All**

ﾉ

**Expand table**

**Bookmark.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows an app to read all bookmarks

without a signed-in user.

Allows an app to read all bookmarks

that the signed-in user can access.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

c5ee1f21-fc7f-4937-9af0-

c91648ff9597

fb9be2b7-a7fc-4182-aec1-

eda4597c43d5

DisplayText

Read all browser site lists for your

organization

Read browser site lists for your

organization

Description

Allows an app to read all browser

site lists configured for your

organization, without a signed-in

user.

Allows an app to read the browser site

lists configured for your organization,

on behalf of the signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

8349ca94-3061-44d5-9bfb-

33774ea5e4f9

83b34c85-95bf-497b-a04e-

b58eca9d49d0

DisplayText

Read and write all browser site lists

for your organization

Read and write browser site lists for

your organization

Description

Allows an app to read and write all

browser site lists configured for your

organization, without a signed-in

user.

Allows an app to read and write the

browser site lists configured for your

organization, on behalf of the signed-in

user.

AdminConsentRequired

Yes

No

**BrowserSiteLists.Read.All**

ﾉ

**Expand table**

**BrowserSiteLists.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

d16480b2-e469-4118-846b-d3d177327bee

DisplayText

-

Read business scenario configurations

Description

-

Allows the app to read the configurations of your organization's

business scenarios, on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

acc0fc4d-2cd6-4194-8700-

1768d8423d86

c47e7b6e-d6f1-4be9-9ffd-

1e00f3e32892

DisplayText

Read all business scenario

configurations this app creates or

owns

Read business scenario configurations

this app creates or owns

Description

Allows the app to read the

configurations of business scenarios

it owns, without a signed-in user.

Allows the app to read the

configurations of business scenarios it

owns, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

755e785b-b658-446f-bb22-5a46abd029ea

DisplayText

-

Read and write business scenario configurations

**BusinessScenarioConfig.Read.All**

ﾉ

**Expand table**

**BusinessScenarioConfig.Read.OwnedBy**

ﾉ

**Expand table**

**BusinessScenarioConfig.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Allows the app to read and write the configurations of your

organization's business scenarios, on behalf of the signed-in

user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

bbea195a-4c47-4a4f-bff2-

cba399e11698

b3b7fcff-b4d4-4230-bf6f-

90bd91285395

DisplayText

Read and write all business scenario

configurations this app creates or

owns

Read and write business scenario

configurations this app creates or owns

Description

Allows the app to create new

business scenarios and fully manage

the configurations of scenarios it

owns, without a signed-in user.

Allows the app to create new business

scenarios and fully manage the

configurations of scenarios it owns, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

6c0257fd-cffe-415b-8239-

2d0d70fdaa9c

25b265c4-5d34-4e44-952d-

b567f6d3b96d

DisplayText

Read data for all business

scenarios this app creates or owns

Read all data for business scenarios this

app creates or owns

Description

Allows the app to read the data

associated with the business

scenarios it owns, without a

signed-in user.

Allows the app to read all data associated

with the business scenarios it owns. Data

access will be attributed to the signed-in

user.

**BusinessScenarioConfig.ReadWrite.OwnedBy**

ﾉ

**Expand table**

**BusinessScenarioData.Read.OwnedBy**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f2d21f22-5d80-499e-91cc-

0a8a4ce16f54

19932d57-2952-4c60-8634-3655c79fc527

DisplayText

Read and write data for all

business scenarios this app

creates or owns

Read and write all data for business

scenarios this app creates or owns

Description

Allows the app to fully manage

the data associated with the

business scenarios it owns,

without a signed-in user.

Allows the app to fully manage all data

associated with the business scenarios it

owns. Data access and changes will be

attributed to the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

798ee544-9d2d-430c-a058-570e29e34338

465a38f9-76ea-45b9-9f34-

9e8b0d4b0b42

DisplayText

Read calendars in all mailboxes

Read user calendars

Description

Allows the app to read events of all

calendars without a signed-in user.

Allows the app to read events in

user calendars.

AdminConsentRequired

Yes

No

![](./assets/output_167_1.png)![](./assets/output_167_2.png)

The _Calendars.Read_ delegated permission is available for consent in personal Microsoft

accounts.

**BusinessScenarioData.ReadWrite.OwnedBy**

ﾉ

**Expand table**

**Calendars.Read**

ﾉ

**Expand table**

Administrators can configure application access policy to limit app access to _specific_ mailboxes

and not to all the mailboxes in the organization, even if the app has been granted the

_Calendars.Read_ application permission.

**Category**

**Application**

**Delegated**

Identifier

-

2b9c4092-424d-4249-948d-b43879977640

DisplayText

-

Read user and shared calendars

Description

-

Allows the app to read events in all calendars that the user can

access, including delegate and shared calendars.

AdminConsentRequired

-

No

![](./assets/output_168_1.png)![](./assets/output_168_2.png)

The _Calendars.Read.Shared_ delegated permission is available for consent in personal

Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

-

662d75ba-a364-42ad-adee-f5f880ea4878

DisplayText

-

Read basic details of user calendars

Description

-

Allows the app to read events in user calendars, except for

properties such as body, attachments, and extensions.

AdminConsentRequired

-

No

![](./assets/output_168_3.png)![](./assets/output_168_4.png)

The _Calendars.ReadBasic_ delegated permission is available for consent in personal Microsoft

accounts.

**Calendars.Read.Shared**

ﾉ

**Expand table**

**Calendars.ReadBasic**

ﾉ

**Expand table**

**Calendars.ReadBasic.All**

**Category**

**Application**

**Delegated**

Identifier

8ba4a692-bc31-4128-9094-475872af8a53

-

DisplayText

Read basic details of calendars in all mailboxes

-

Description

Allows the app to read events of all calendars, except for

properties such as body, attachments, and extensions, without a

signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

ef54d2bf-783f-4e0f-bca1-3210c0444d99

1ec239c2-d7c9-4623-a91a-

a9775856bb36

DisplayText

Read and write calendars in all mailboxes

Have full access to user calendars

Description

Allows the app to create, read, update,

and delete events of all calendars without

a signed-in user.

Allows the app to create, read,

update, and delete events in user

calendars.

AdminConsentRequired

Yes

No

![](./assets/output_169_1.png)![](./assets/output_169_2.png)

The _Calendars.ReadWrite_ delegated permission is available for consent in personal Microsoft

accounts.

Administrators can configure application access policy to limit app access to specific mailboxes

and not to all the mailboxes in the organization, even if the app has been granted the

_Calendars.ReadWrite_ application permission.

ﾉ

**Expand table**

**Calendars.ReadWrite**

ﾉ

**Expand table**

**Calendars.ReadWrite.Shared**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

12466101-c9b8-439a-8589-dd09ee67e8e9

DisplayText

-

Read and write user and shared calendars

Description

-

Allows the app to create, read, update and delete events in all

calendars in the organization user has permissions to access.

This includes delegate and shared calendars.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

792b782b-7822-4b92-8103-

77e44f2f706c

e24bdaf9-83f8-468b-a144-

c681ccb6caf4

DisplayText

Read all AI Insights for calls.

Read all AI Insights for calls.

Description

Allows the app to read all AI Insights

for all calls, without a signed-in user.

Allows the app to read all AI Insights

for calls, on behalf of the signed-in

user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

-

305b375b-00fe-48bf-81bc-e8d78954c1b6

DisplayText

-

Read delegation settings

Description

-

Allows the app to read delegation settings of you

AdminConsentRequired

-

Yes

**CallAiInsights.Read.All**

ﾉ

**Expand table**

**CallDelegation.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

5aa33e77-b893-495e-bdc5-4bf6f27d42a0

-

DisplayText

Read delegation settings

-

Description

Allows the app to read delegation settings of you

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

599abf67-f72b-4b5f-98a3-cb38fe646118

DisplayText

-

Read and write delegation settings

Description

-

Allows the app to read and write delegation settings of you

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

8d06abce-e69b-4122-ba60-4f901bb1db2f

-

DisplayText

Read and write delegation settings

-

Description

Allows the app to read and write delegation settings of you

-

AdminConsentRequired

Yes

-

**CallDelegation.Read.All**

ﾉ

**Expand table**

**CallDelegation.ReadWrite**

ﾉ

**Expand table**

**CallDelegation.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

f0a35f91-2aa6-4a99-9d5a-5b6bcb66204e

-

DisplayText

Read all emergency call events

-

Description

Allows the app to read emergency call event information for all

users in your organization without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

43431c03-960e-400f-87c6-8f910321dca3

DisplayText

-

Read call event data

Description

-

Allows the app to read call event information for an organization

for the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

1abb026f-7572-49f6-9ddd-ad61cbba181e

-

DisplayText

Read all call events

-

Description

Allows the app to read call event information for all users in your

organization, without a signed-in user.

-

AdminConsentRequired

Yes

-

**CallEvents-Emergency.Read.All**

ﾉ

**Expand table**

**CallEvents.Read**

ﾉ

**Expand table**

**CallEvents.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

a2611786-80b3-417e-adaa-707d4261a5f0

-

DisplayText

Read PSTN and direct routing call log data

-

Description

Allows the app to read all PSTN and direct routing call log data

without a signed-in user.

-

AdminConsentRequired

Yes

-

The _CallRecord-PstnCalls.Read.All_ permission grants an application access to PSTN (calling

plans) and direct routing call logs. This includes potentially sensitive information about users as

well as calls to and from external phone numbers.

**Category**

**Application**

**Delegated**

Identifier

ce8fb1f1-5e1f-44a0-b102-

4ec28454d0dc

63d31bd6-bcf5-40ca-8283-

ba4130a66405

DisplayText

Read all call recordings

Read all recordings of calls.

**CallRecord-PstnCalls.Read.All**

ﾉ

**Expand table**

） **Important**

Discretion should be used when granting these permissions to applications. Call

records can provide insights into the operation of your business, and so can be a

target for malicious actors. Only grant these permissions to applications you trust to

meet your data protection requirements.

Make sure that you are compliant with the laws and regulations in your area

regarding data protection and confidentiality of communications. Please see the

**Terms of Use** and consult with your legal counsel for more information.

**CallRecordings.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read call recordings

for all calls without a signed-in user.

Allows the app to read all recordings

of calls, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

45bbb07e-7321-4fd7-a8f6-3ff27e6a81c8

-

DisplayText

Read all call records

-

Description

Allows the app to read call records for all calls and online

meetings without a signed-in user.

-

AdminConsentRequired

Yes

-

The _CallRecords.Read.All_ permission grants an application privileged access to callRecords for

every call and online meeting within your organization, including calls to and from external

phone numbers. This includes potentially sensitive details about who participated in the call, as

well as technical information pertaining to these calls and meetings that can be used for

network troubleshooting, such as IP addresses, device details, and other network information.

**CallRecords.Read.All**

ﾉ

**Expand table**

） **Important**

Discretion should be used when granting these permissions to applications. Call

records can provide insights into the operation of your business, and so can be a

target for malicious actors. Only grant these permissions to applications you trust to

meet your data protection requirements.

Make sure that you are compliant with the laws and regulations in your area

regarding data protection and confidentiality of communications. Please see the

**Terms of Use** and consult with your legal counsel for more information.

**Calls.AccessMedia.All**

**Category**

**Application**

**Delegated**

Identifier

a7a681dc-756e-4909-b988-f160edc6655f

-

DisplayText

Access media streams in a call as an app

-

Description

Allows the app to get direct access to media streams in a call,

without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

284383ee-7f6e-4e40-a2a8-e85dcb029101

-

DisplayText

Initiate outgoing 1 to 1 calls from the app

-

Description

Allows the app to place outbound calls to a single user and

transfer calls to users in your organization's directory, without a

signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

4c277553-8a09-487b-8023-29ee378d8324

-

DisplayText

Initiate outgoing group calls from the app

-

Description

Allows the app to place outbound calls to multiple users and add

participants to meetings in your organization, without a signed-in

user.

-

AdminConsentRequired

Yes

-

ﾉ

**Expand table**

**Calls.Initiate.All**

ﾉ

**Expand table**

**Calls.InitiateGroupCall.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

f6b49018-60ab-4f81-83bd-22caeabfed2d

-

DisplayText

Join group calls and meetings as an app

-

Description

Allows the app to join group calls and scheduled meetings in your

organization, without a signed-in user. The app will be joined with

the privileges of a directory user to meetings in your organization.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

fd7ccf6b-3d28-418b-9701-cd10f5cd2fd4

-

DisplayText

Join group calls and meetings as a guest

-

Description

Allows the app to anonymously join group calls and scheduled

meetings in your organization, without a signed-in user. The app

will be joined as a guest to meetings in your organization.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

4cd61b6d-8692-40bf-9d90-

7f38db5e5fce

fbace248-5d8e-441c-85ca-

cc19221a69a2

DisplayText

Read all call transcripts

Read all transcripts of calls.

**Calls.JoinGroupCall.All**

ﾉ

**Expand table**

**Calls.JoinGroupCallAsGuest.All**

ﾉ

**Expand table**

**CallTranscripts.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read call transcripts

for all calls without a signed-in user.

Allows the app to read all transcripts

of calls, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

418dae40-2b65-4819-900c-

519a04e4d278

4628dff5-c33e-4fde-b17a-

b64e7acb1bed

DisplayText

Read Change Management items

Read Change Management items

Description

Allows to read all Change

Management items.

Allows to read all Change

Management items.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

f3a65bd4-b703-46df-8f7e-

0174fea562aa

101147cf-4178-4455-9d58-

02b5c164e759

DisplayText

Create channels

Create channels

Description

Create channels in any team,

without a signed-in user.

Create channels in any team, on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**ChangeManagement.Read.All**

ﾉ

**Expand table**

**Channel.Create**

ﾉ

**Expand table**

**Channel.Delete.All**

**Category**

**Application**

**Delegated**

Identifier

6a118a39-1227-45d4-af0c-

ea7b40d210bc

cc83893a-e232-4723-b5af-

bd0b01bcfe65

DisplayText

Delete channels

Delete channels

Description

Delete channels in any team,

without a signed-in user.

Delete channels in any team, on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

59a6b24b-4225-4393-8165-

ebaec5f55d7a

9d8982ae-4365-4f57-95e9-

d6032a4c0b87

DisplayText

Read the names and descriptions of

all channels

Read the names and descriptions of

channels

Description

Read all channel names and channel

descriptions, without a signed-in

user.

Read channel names and channel

descriptions, on behalf of the signed-in

user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

3b55498e-47ec-484f-8136-

9013221c06a9

2eadaff8-0bce-4198-a6b9-

2cfc35a30075

DisplayText

Read the members of all channels

Read the members of channels

Description

Read the members of all channels,

without a signed-in user.

Read the members of channels, on

behalf of the signed-in user.

ﾉ

**Expand table**

**Channel.ReadBasic.All**

ﾉ

**Expand table**

**ChannelMember.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

35930dcf-aceb-4bd1-b99a-

8ffed403c974

0c3e411a-ce45-4cd1-8f30-

f99a3efa7b11

DisplayText

Add and remove members from all

channels

Add and remove members from

channels

Description

Add and remove members from all

channels, without a signed-in user.

Also allows changing a member's

role, for example from owner to non-

owner.

Add and remove members from

channels, on behalf of the signed-in

user. Also allows changing a member's

role, for example from owner to non-

owner.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

2b61aa8a-6d36-4b2f-ac7b-f29867937c53

DisplayText

-

Edit user's channel messages

Description

-

Allows an app to edit channel messages in Microsoft Teams, on

behalf of the signed-in user.

AdminConsentRequired

-

No

**ChannelMember.ReadWrite.All**

ﾉ

**Expand table**

**ChannelMessage.Edit**

ﾉ

**Expand table**

**ChannelMessage.Read.All**

**Category**

**Application**

**Delegated**

Identifier

7b2449af-6ccd-4f4d-9f78-

e550c193f0d1

767156cb-16ae-4d10-8f8b-41b657c8c8c8

DisplayText

Read all channel messages

Read user channel messages

Description

Allows the app to read all

channel messages in Microsoft

Teams

Allows an app to read a channel's messages

in Microsoft Teams, on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

5922d31f-46c8-4404-9eaf-2117e390a8a4

DisplayText

-

Read and write user channel messages

Description

-

Allows the app to read and write channel messages, on behalf of

the signed-in user. This doesn't allow the app to edit the

policyViolation of a channel message.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

ebf0f66e-9fb1-49e4-a278-222f76911cf4

DisplayText

-

Send channel messages

Description

-

Allows an app to send channel messages in Microsoft Teams, on

behalf of the signed-in user.

AdminConsentRequired

-

No

ﾉ

**Expand table**

**ChannelMessage.ReadWrite**

ﾉ

**Expand table**

**ChannelMessage.Send**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

4d02b0cc-d90b-441f-8d82-4fb55c34d6bb

-

DisplayText

Flag channel messages for violating policy

-

Description

Allows the app to update Microsoft Teams channel messages by

patching a set of Data Loss Prevention (DLP) policy violation

properties to handle the output of DLP processing.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

c97b873f-f59f-49aa-8a0e-

52b32d762124

233e0cf1-dd62-48bc-b65b-

b38fe87fcf8e

DisplayText

Read the names, descriptions, and

settings of all channels

Read the names, descriptions, and

settings of channels

Description

Read all channel names, channel

descriptions, and channel settings,

without a signed-in user.

Read all channel names, channel

descriptions, and channel settings, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

243cded2-bd16-4fd6-a953-

ff8177894c3d

d649fb7c-72b4-4eec-b2b4-

b15acf79e378

**ChannelMessage.UpdatePolicyViolation.All**

ﾉ

**Expand table**

**ChannelSettings.Read.All**

ﾉ

**Expand table**

**ChannelSettings.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write the names,

descriptions, and settings of all

channels

Read and write the names,

descriptions, and settings of channels

Description

Read and write the names,

descriptions, and settings of all

channels, without a signed-in user.

Read and write the names,

descriptions, and settings of all

channels, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

d9c48af6-9ad9-47ad-82c3-

63757137b9af

38826093-1258-4dea-98f0-

00003be2b8d0

DisplayText

Create chats

Create chats

Description

Allows the app to create chats

without a signed-in user.

Allows the app to create chats on behalf

of the signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

9c7abde0-eacd-4319-bf9e-

35994b1a1717

bb64e6fc-6b6d-4752-aea0-

dd922dbba588

DisplayText

Delete and recover deleted chats

Delete and recover deleted chats

Description

Allows the app to delete and recover

deleted chats, without a signed-in

user.

Allows the app to delete and recover

deleted chats, on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**Chat.Create**

ﾉ

**Expand table**

**Chat.ManageDeletion.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

f501c180-9344-439a-bca0-6cbf209fd270

DisplayText

-

Read user chat messages

Description

-

Allows an app to read 1 on 1 or group chats threads, on behalf

of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

6b7d71aa-70aa-4810-a8d9-5d9fb2830017

-

DisplayText

Read all chat messages

-

Description

Allows the app to read all 1-to-1 or group chat messages in

Microsoft Teams.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

1c1b4c8e-3cc7-4c58-8470-9b92c9d5848b

-

DisplayText

Read all chat messages for chats where the associated Teams

application is installed.

-

Description

Allows the app to read all one-to-one or group chat messages in

Microsoft Teams for chats where the associated Teams application

-

**Chat.Read**

ﾉ

**Expand table**

**Chat.Read.All**

ﾉ

**Expand table**

**Chat.Read.WhereInstalled**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

is installed, without a signed-in user.

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

9547fcb5-d03f-419d-9948-5928bbf71b0f

DisplayText

-

Read names and members of user chat threads

Description

-

Allows an app to read the members and descriptions of one-to-

one and group chat threads, on behalf of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

b2e060da-3baf-4687-9611-f4ebc0f0cbde

-

DisplayText

Read names and members of all chat threads

-

Description

Read names and members of all one-to-one and group chats in

Microsoft Teams, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Chat.ReadBasic**

ﾉ

**Expand table**

**Chat.ReadBasic.All**

ﾉ

**Expand table**

**Chat.ReadBasic.WhereInstalled**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

818ba5bd-5b3e-4fe0-bbe6-aa4686669073

-

DisplayText

Read names and members of all chat threads where the

associated Teams application is installed.

-

Description

Allows the app to read names and members of all one-to-one

and group chats in Microsoft Teams where the associated Teams

application is installed, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

9ff7295e-131b-4d94-90e1-69fde507ac11

DisplayText

-

Read and write user chat messages

Description

-

Allows an app to read and write 1 on 1 or group chats threads,

on behalf of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

294ce7c9-31ba-490a-ad7d-

97a7d075e4ed

7e9a077b-3711-42b9-b7cb-5fa5f3f7fea7

DisplayText

Read and write all chat messages

Read and write all chat messages

Description

Allows an app to read and write

all chat messages in Microsoft

Teams, without a signed-in user.

Allows an app to read and write all one-to-

one and group chats in Microsoft Teams,

without a signed-in user. Does not allow

sending messages.

AdminConsentRequired

Yes

Yes

**Chat.ReadWrite**

ﾉ

**Expand table**

**Chat.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

ad73ce80-f3cd-40ce-b325-df12c33df713

-

DisplayText

Read and write all chat messages for chats where the associated

Teams application is installed.

-

Description

Allows the app to read and write all chat messages in Microsoft

Teams for chats where the associated Teams application is

installed, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

7e847308-e030-4183-9899-5235d7270f58

-

DisplayText

Flag chat messages for violating policy

-

Description

Allows the app to update Microsoft Teams 1-to-1 or group chat

messages by patching a set of Data Loss Prevention (DLP) policy

violation properties to handle the output of DLP processing.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

c5a9e2b1-faf6-41d4-8875-d381aa549b24

DisplayText

-

Read the members of chats

**Chat.ReadWrite.WhereInstalled**

ﾉ

**Expand table**

**Chat.UpdatePolicyViolation.All**

ﾉ

**Expand table**

**ChatMember.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Read the members of chats, on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

a3410be2-8e48-4f32-8454-c29a7465209d

-

DisplayText

Read the members of all chats

-

Description

Read the members of all chats, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

93e7c9e4-54c5-4a41-b796-f2a5adaacda7

-

DisplayText

Read the members of all chats where the associated Teams

application is installed.

-

Description

Allows the app to read the members of all chats where the

associated Teams application is installed, without a signed-in user.

-

AdminConsentRequired

Yes

-

**ChatMember.Read.All**

ﾉ

**Expand table**

**ChatMember.Read.WhereInstalled**

ﾉ

**Expand table**

**ChatMember.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

dea13482-7ea6-488f-8b98-eb5bbecf033d

DisplayText

-

Add and remove members from chats

Description

-

Add and remove members from chats, on behalf of the signed-

in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

57257249-34ce-4810-a8a2-a03adf0c5693

-

DisplayText

Add and remove members from all chats

-

Description

Add and remove members from all chats, without a signed-in

user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

e32c2cd9-0124-4e44-88fc-772cd98afbdb

-

DisplayText

Add and remove members from all chats where the associated

Teams application is installed.

-

Description

Allows the app to add and remove members from all chats where

the associated Teams application is installed, without a signed-in

user.

-

AdminConsentRequired

Yes

-

**ChatMember.ReadWrite.All**

ﾉ

**Expand table**

**ChatMember.ReadWrite.WhereInstalled**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

cdcdac3a-fd45-410d-83ef-554db620e5c7

DisplayText

-

Read user chat messages

Description

-

Allows an app to read one-to-one and group chat messages, on

behalf of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

b9bb2381-47a4-46cd-aafb-00cb12f68504

-

DisplayText

Read all chat messages

-

Description

Allows the app to read all one-to-one and group chats messages

in Microsoft Teams, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

116b7235-7cc6-461e-b163-8e55691d839e

DisplayText

-

Send user chat messages

Description

-

Allows an app to send one-to-one and group chat messages in

Microsoft Teams, on behalf of the signed-in user.

AdminConsentRequired

-

No

**ChatMessage.Read**

ﾉ

**Expand table**

**ChatMessage.Read.All**

ﾉ

**Expand table**

**ChatMessage.Send**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

64a59178-dad3-4673-89db-

84fdcd622fec

ad46d60e-1027-4b75-af88-

7c14ccf43a19

DisplayText

Read all discovered cloud

applications data

Read discovered cloud applications

data

Description

Allows the app to read all details of

discovered cloud apps in the

organization, without a signed-in

user.

Allows the app to read details of

discovered cloud apps in the

organization, on behalf of the signed

in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

a9e09520-8ed4-4cde-838e-

4fdea192c227

5252ec4e-fd40-4d92-8c68-

89dd1d3c6110

DisplayText

Read Cloud PCs

Read Cloud PCs

Description

Allows the app to read the

properties of Cloud PCs, without a

signed-in user.

Allows the app to read the properties

of Cloud PCs on behalf of the signed-in

user.

AdminConsentRequired

Yes

No

**CloudApp-Discovery.Read.All**

ﾉ

**Expand table**

**CloudPC.Read.All**

ﾉ

**Expand table**

**CloudPC.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

3b4349e1-8cf5-45a3-95b7-

69d1751d3e6a

9d77138f-f0e2-47ba-ab33-

cd246c8b79d1

DisplayText

Read and write Cloud PCs

Read and write Cloud PCs

Description

Allows the app to read and write the

properties of Cloud PCs, without a

signed-in user.

Allows the app to read and write the

properties of Cloud PCs on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

407f0cce-3212-441f-9f55-

3bc91342cf86

12ae2e92-14b5-47b2-babb-

4e890bbedc0a

DisplayText

Read all Viva Engage communities

Read all Viva Engage communities

Description

Allows the app to list Viva Engage

communities, and to read their

properties without a signed-in user.

Allows the app to list Viva Engage

communities, and to read their

properties on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

35d59e32-eab5-4553-9345-abb62b4c703c

9e69467d-e0e2-402b-a926-

3d796990197f

DisplayText

Read and write all Viva Engage

communities

Read and write all Viva Engage

communities

Description

Allows the app to create Viva Engage

communities, read all community

Allows the app to create Viva

Engage communities and read all

**Community.Read.All**

ﾉ

**Expand table**

**Community.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

properties, update community properties,

and delete communities without a signed-

in user.

community properties on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

aca929ec-9830-44dc-bda1-

85cf938aaa95

c645bb69-adc4-4242-b620-

02e635f03bf6

DisplayText

Read all Configuration Monitoring

entities

Read all Configuration Monitoring

entities

Description

Allows the app to read all

Configuration Monitoring entities,

without a signed-in user.

Allows the app to read all

Configuration Monitoring entities on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

cfa85bfb-2ee8-4e13-8e7f-

489e57a015a1

54505ce9-e719-41f7-a7cc-

dbe114e1d811

DisplayText

Read and write all Configuration

Monitoring entities

Read and write all Configuration

Monitoring entities

Description

Allows the app to read and write all

Configuration Monitoring entities,

without a signed-in user.

Allows the app to read and write all

Configuration Monitoring entities on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**ConfigurationMonitoring.Read.All**

ﾉ

**Expand table**

**ConfigurationMonitoring.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

f2143d35-9b4b-480d-951c-d083e69eeb2c

DisplayText

-

Create consent requests

Description

-

Allows the app to read create consent requests on behalf of the

signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

5942b2f6-5a7b-40af-aa37-4b6ea5447506

DisplayText

-

Read consent requests created by the user

Description

-

Allows the app to read consent requests and approvals created

by the signed-in user, on behalf of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

1260ad83-98fb-4785-abbb-

d6cc1806fd41

f3bfad56-966e-4590-a536-

82ecf548ac1e

DisplayText

Read all consent requests

Read consent requests

Description

Allows the app to read consent

requests and approvals without a

signed-in user.

Allows the app to read consent

requests and approvals on behalf of

the signed-in user.

**ConsentRequest.Create**

ﾉ

**Expand table**

**ConsentRequest.Read**

ﾉ

**Expand table**

**ConsentRequest.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

e694a3a1-7878-46d8-8c29-3d195f6589f4

DisplayText

-

Read and approve consent requests

Description

-

Allows the app to read and approve consent requests on behalf

of the signed in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

9f1b81a7-0223-4428-bfa4-

0bcb5535f27d

497d9dfa-3bd1-481a-baab-

90895e54568c

DisplayText

Read and write all consent requests

Read and write consent requests

Description

Allows the app to read app consent

requests and approvals, and deny or

approve those requests without a

signed-in user.

Allows the app to read app consent

requests and approvals, and deny or

approve those requests on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**ConsentRequest.ReadApprove.All**

ﾉ

**Expand table**

**ConsentRequest.ReadWrite.All**

ﾉ

**Expand table**

**Contacts-OnPremisesSyncBehavior.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

c8948c23-e66b-42db-83fd-

770b71ab78d2

1e4c6c41-0803-4f52-85ef-0a5d63ad8670

DisplayText

Read and update the on-premises

sync behavior of contacts

Read and update the on-premises sync

behavior of contacts

Description

Allows the app to update the on-

premises sync behavior of all

contacts in all mailboxes without a

signed-in user.

Allows the app to read and update the

on-premises sync behavior of contacts a

user has permissions to, including their

own and shared contacts.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

089fe4d0-434a-44c5-8827-41ba8a0b17f5

ff74d97f-43af-4b68-9f2a-

b77ee6968c5d

DisplayText

Read contacts in all mailboxes

Read user contacts

Description

Allows the app to read all contacts in all

mailboxes without a signed-in user.

Allows the app to read user

contacts.

AdminConsentRequired

Yes

No

![](./assets/output_195_1.png)![](./assets/output_195_2.png)

The _Contacts.Read_ delegated permission is available for consent in personal Microsoft

accounts.

Administrators can configure application access policy to limit app access to _specific_ mailboxes

and not to all the mailboxes in the organization, even if the app has been granted the

_Contacts.Read_ application permission.

**Contacts.Read**

ﾉ

**Expand table**

**Contacts.Read.Shared**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

242b9d9e-ed24-4d09-9a52-f43769beb9d4

DisplayText

-

Read user and shared contacts

Description

-

Allows the app to read contacts a user has permissions to

access, including their own and shared contacts.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

6918b873-d17a-4dc1-b314-35f528134491

d56682ec-c09e-4743-aaf4-

1a3aac4caa21

DisplayText

Read and write contacts in all mailboxes

Have full access to user

contacts

Description

Allows the app to create, read, update, and

delete all contacts in all mailboxes without a

signed-in user.

Allows the app to create, read,

update, and delete user

contacts.

AdminConsentRequired

Yes

No

![](./assets/output_196_1.png)![](./assets/output_196_2.png)

The _Contacts.ReadWrite_ delegated permission is available for consent in personal Microsoft

accounts.

Administrators can configure application access policy to limit app access to specific mailboxes

and not to all the mailboxes in the organization, even if the app has been granted the

_Contacts.ReadWrite_ application permission.

**Category**

**Application**

**Delegated**

Identifier

-

afb6c84b-06be-49af-80bb-8f3f77004eab

**Contacts.ReadWrite**

ﾉ

**Expand table**

**Contacts.ReadWrite.Shared**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

-

Read and write user and shared contacts

Description

-

Allows the app to create, read, update, and delete contacts a

user has permissions to, including their own and shared

contacts.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

5ad511bf-571c-4ef6-8c3c-

85b94b85df98

7e2467d1-f874-46bb-828e-

24cb06b29d3f

DisplayText

Process content for data security,

governance and compliance

Process content for data security,

governance and compliance

Description

Allows the app to process and

evaluate content for data security,

governance and compliance

outcomes at tenant scope.

Allows the app to process and

evaluate content for data security,

governance and compliance

outcomes at tenant scope.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

24ceb246-ad29-4680-90b4-

3e91ffad15eb

1d787a13-f750-4ad6-875a-

fcbd2725596b

DisplayText

Process content for data security,

governance and compliance

Process content for data security,

governance and compliance

Description

Allows the app to process and

evaluate content for data security,

governance and compliance

outcomes for a user.

Allows the app to process and

evaluate content for data security,

governance and compliance outcomes

for a user.

**Content.Process.All**

ﾉ

**Expand table**

**Content.Process.User**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

368425e7-6954-4f5a-9d92-

90b75bd580c9

62c55b2f-a2b1-4312-8385-

be57afd901b4

DisplayText

Read contents activity audit log from

the audit store.

Read contents activity audit log from

the audit store.

Description

Read contents activity audit log from

the audit store.

Read contents activity audit log from

the audit store.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2932e07a-3c29-44e4-bb36-

6d0fc176387f

948caae6-152a-48cd-a746-

4844af30e8e9

DisplayText

Upload content activity audit logs to

the audit store.

Upload contents activity audit logs to

the audit store.

Description

Allows the application to upload bulk

contents activity audit logs to the

audit store.

Allows the application to upload bulk

contents activity audit logs to the

audit store.

AdminConsentRequired

Yes

Yes

**ContentActivity.Read**

ﾉ

**Expand table**

**ContentActivity.Write**

ﾉ

**Expand table**

**CopilotConversation.Delete**

**Category**

**Application**

**Delegated**

Identifier

-

ed510a02-ac32-45f9-93e6-04864f7f7e47

DisplayText

-

Delete Microsoft 365 Copilot conversations

Description

-

Allows the app to delete Microsoft 365 Copilot conversations on

behalf of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

-

aeb2982d-632d-4155-b533-18756ab6fdd8

DisplayText

-

Read organization-wide copilot limited mode setting

Description

-

Allows the app to read organization-wide copilot limited mode

setting on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

4704e5b2-0ada-4aa0-b18c-00ad7525bc06

DisplayText

-

Read and write organization-wide copilot limited mode setting

Description

-

Allows the app to read and write organization-wide copilot

limited mode setting on behalf of the signed-in user.

AdminConsentRequired

-

Yes

ﾉ

**Expand table**

**CopilotSettings-LimitedMode.Read**

ﾉ

**Expand table**

**CopilotSettings-LimitedMode.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

cac88765-0581-4025-9725-

5ebc13f729ee

81594d25-e88e-49cf-ac8c-

fecbff49f994

DisplayText

Read cross-tenant basic information

Read cross-tenant basic information

Description

Allows the application to obtain basic

tenant information about another

target tenant within the Azure AD

ecosystem without a signed-in user.

Allows the application to obtain basic

tenant information about another

target tenant within the Azure AD

ecosystem on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

cb1ba48f-d22b-4325-a07f-74135a62ee41

DisplayText

-

Read shared cross-tenant user profile and export data

Description

-

Allows the application to list and query user profile information

associated with the current tenant on behalf of the signed-in

user. It also permits the application to export external user data

(e.g. customer content or system-generated logs), associated

with the current tenant on behalf of the signed-in user.

AdminConsentRequired

-

Yes

![](./assets/output_200_1.png)![](./assets/output_200_2.png)

The _CrossTenantUserProfileSharing.Read_ delegated permission is available for consent in

personal Microsoft accounts.

**CrossTenantInformation.ReadBasic.All**

ﾉ

**Expand table**

**CrossTenantUserProfileSharing.Read**

ﾉ

**Expand table**

**CrossTenantUserProfileSharing.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

8b919d44-6192-4f3d-8a3b-

f86f8069ae3c

759dcd16-3c90-463c-937e-

abf89f991c18

DisplayText

Read all shared cross-tenant user

profiles and export their data

Read all shared cross-tenant user

profiles and export their data

Description

Allows the application to list and

query any shared user profile

information associated with the

current tenant without a signed-in

user. It also permits the application to

export external user data (e.g.

customer content or system-

generated logs), for any user

associated with the current tenant

without a signed-in user.

Allows the application to list and query

any shared user profile information

associated with the current tenant on

behalf of the signed-in user. It also

permits the application to export

external user data (e.g. customer

content or system-generated logs), for

any user associated with the current

tenant on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

![](./assets/output_201_1.png)![](./assets/output_201_2.png)

The _CrossTenantUserProfileSharing.Read.All_ delegated permission is available for consent in

personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

-

eed0129d-dc60-4f30-8641-daf337a39ffd

DisplayText

-

Read shared cross-tenant user profile and export or delete data

Description

-

Allows the application to list and query user profile information

associated with the current tenant on behalf of the signed-in

user. It also permits the application to export and remove

external user data (e.g. customer content or system-generated

logs), associated with the current tenant on behalf of the

signed-in user.

AdminConsentRequired

-

Yes

**CrossTenantUserProfileSharing.ReadWrite**

ﾉ

**Expand table**

**CrossTenantUserProfileSharing.ReadWrite.All**

**Category**

**Application**

**Delegated**

Identifier

306785c5-c09b-4ba0-a4ee-

023f3da165cb

64dfa325-cbf8-48e3-938d-

51224a0cac01

DisplayText

Read all shared cross-tenant user

profiles and export or delete their

data

Read all shared cross-tenant user

profiles and export or delete their data

Description

Allows the application to list and

query any shared user profile

information associated with the

current tenant without a signed-in

user. It also permits the application to

export and remove external user data

(e.g. customer content or system-

generated logs), for any user

associated with the current tenant

without a signed-in user.

Allows the application to list and query

any shared user profile information

associated with the current tenant on

behalf of the signed-in user. It also

permits the application to export and

remove external user data (e.g.

customer content or system-

generated logs), for any user

associated with the current tenant on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

88bb2658-5d9e-454f-aacd-

a3933e079526

b2052569-c98c-4f36-a5fb-

43e5c111e6d0

DisplayText

Read all custom authentication

extensions

Read your organization's custom

authentication extensions

Description

Allows the app to read your

organization's custom authentication

extensions without a signed-in user.

Allows the app to read your

organization's custom authentication

extensions on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

ﾉ

**Expand table**

**CustomAuthenticationExtension.Read.All**

ﾉ

**Expand table**

**CustomAuthenticationExtension.ReadWrite.All**

**Category**

**Application**

**Delegated**

Identifier

c2667967-7050-4e7e-b059-

4cbbb3811d03

8dfcf82f-15d0-43b3-bc78-

a958a13a5792

DisplayText

Read and write all custom

authentication extensions

Read and write your organization's

custom authentication extensions

Description

Allows the app to read or write your

organization's custom authentication

extensions without a signed-in user.

Allows the app to read or write your

organization's custom authentication

extensions on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

214e810f-fda8-4fd7-a475-29461495eb00

-

DisplayText

Receive custom authentication extension HTTP requests

-

Description

Allows custom authentication extensions associated with the app

to receive HTTP requests triggered by an authentication event.

The request can include information about a user, client and

resource service principals, and other information about the

authentication.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

673a007a-9e0f-4c97-b066-

3c0164486909

b13ff42e-f321-4d7d-a462-

141c46a1b832

DisplayText

Read all custom detection rules

Read custom detection rules

ﾉ

**Expand table**

**CustomAuthenticationExtension.Receive.Payload**

ﾉ

**Expand table**

**CustomDetection.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read custom

detection rules without a signed-in

user.

Allows the app to read custom

detection rules on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e0fd9c8d-a12e-4cc9-9827-

20c8c3cd6fb8

c34088fb-0649-4714-af0b-

bcbfec155897

DisplayText

Read and write all custom detection

rules

Read and write custom detection rules

Description

Allows the app to read and write

custom detection rules without a

signed-in user.

Allows the app to read and write

custom detection rules on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

3b37c5a4-1226-493d-bec3-

5d6c6b866f3f

b46ffa80-fe3d-4822-9a1a-

c200932d54d0

DisplayText

Read custom security attribute

assignments

Read custom security attribute

assignments

Description

Allows the app to read custom

security attribute assignments for all

principals in the tenant without a

signed in user.

Allows the app to read custom security

attribute assignments for all principals

in the tenant on behalf of a signed in

user.

AdminConsentRequired

Yes

Yes

**CustomDetection.ReadWrite.All**

ﾉ

**Expand table**

**CustomSecAttributeAssignment.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

de89b5e4-5b8f-48eb-8925-

29c2b33bd8bd

ca46335e-8453-47cd-a001-

8459884efeae

DisplayText

Read and write custom security

attribute assignments

Read and write custom security

attribute assignments

Description

Allows the app to read and write

custom security attribute assignments

for all principals in the tenant without

a signed in user.

Allows the app to read and write

custom security attribute assignments

for all principals in the tenant on

behalf of a signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2a4f026d-e829-4e84-bdbf-

d981a2703059

1fcdeaab-b519-44dd-bffc-

ed1fd15a24e0

DisplayText

Read all custom security attribute

audit logs

Read custom security attribute audit

logs

Description

Allows the app to read all audit logs

for events that contain information

about custom security attributes,

without a signed-in user.

Allows the app to read audit logs for

events that contain information about

custom security attributes, on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**CustomSecAttributeAssignment.ReadWrite.All**

ﾉ

**Expand table**

**CustomSecAttributeAuditLogs.Read.All**

ﾉ

**Expand table**

**CustomSecAttributeDefinition.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

b185aa14-d8d2-42c1-a685-

0f5596613624

ce026878-a0ff-4745-a728-

d4fedd086c07

DisplayText

Read custom security attribute

definitions

Read custom security attribute

definitions

Description

Allows the app to read custom

security attribute definitions for the

tenant without a signed in user.

Allows the app to read custom security

attribute definitions for the tenant on

behalf of a signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

12338004-21f4-4896-bf5e-

b75dfaf1016d

8b0160d4-5743-482b-bb27-

efc0a485ca4a

DisplayText

Read and write custom security

attribute definitions

Read and write custom security

attribute definitions

Description

Allows the app to read and write

custom security attribute definitions

for the tenant without a signed in

user.

Allows the app to read and write

custom security attribute definitions

for the tenant on behalf of a signed in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

9fd1f8bf-a443-4df6-bc2a-

5d00c5ec7828

9ddd870d-077c-49e7-b3e3-

6b3012a8a880

DisplayText

Read the provisioning configuration

of all active custom security attributes

Read the provisioning configuration of

all active custom security attributes

**CustomSecAttributeDefinition.ReadWrite.All**

ﾉ

**Expand table**

**CustomSecAttributeProvisioning.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read the

provisioning configuration of all

active custom security attributes

without a signed-in user.

Allows the app to read the

provisioning configuration of all active

custom security attributes on behalf of

a signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

1db69e9c-8d0a-498d-a5df-

11fd0b68ceab

1140d9e4-6776-433e-a9e4-

b9831adbb2e0

DisplayText

Read and edit the provisioning

configuration of all active custom

security attributes

Read and edit the provisioning

configuration of all active custom

security attributes

Description

Allows the app to read and edit the

provisioning configuration of all

active custom security attributes

without a signed-in user.

Allows the app to read and edit the

provisioning configuration of all active

custom security attributes on behalf of

a signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ab8a5872-7c88-47a6-8141-

7becce939190

de6ea87d-10bd-467c-8682-

d525a0c61b89

DisplayText

Read all custom tags data

Read all custom tags data

Description

Read custom tags data, without a

signed-in user

Read custom tags data on behalf of the

signed-in user

AdminConsentRequired

Yes

Yes

**CustomSecAttributeProvisioning.ReadWrite.All**

ﾉ

**Expand table**

**CustomTags.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

2f503208-e509-4e39-974c-

8cc16e5785c9

2f1bbe0a-f34b-4efb-9edb-

8db8dcb50eca

DisplayText

Read and write custom tags data

Read and write custom tags data

Description

Read and write custom tags data,

without a signed-in user

Read and write custom tags data on

behalf of the signed-in user

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f6e9e124-4586-492f-adc0-

c6f96e4823fd

0c0064ea-477b-4130-82a5-

4c2cc4ff68aa

DisplayText

Read Delegated Admin relationships

with customers

Read Delegated Admin relationships

with customers

Description

Allows the app to read details of

delegated admin relationships with

customers like access details (that

includes roles) and the duration as

well as specific role assignments to

security groups without a signed-in

user.

Allows the app to read details of

delegated admin relationships with

customers like access details (that

includes roles) and the duration as

well as specific role assignments to

security groups on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**CustomTags.ReadWrite.All**

ﾉ

**Expand table**

**DelegatedAdminRelationship.Read.All**

ﾉ

**Expand table**

**DelegatedAdminRelationship.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

cc13eba4-8cd8-44c6-b4d4-

f93237adce58

885f682f-a990-4bad-a642-

36736a74b0c7

DisplayText

Manage Delegated Admin

relationships with customers

Manage Delegated Admin

relationships with customers

Description

Allows the app to manage (create-

update-terminate) Delegated Admin

relationships with customers and role

assignments to security groups for

active Delegated Admin relationships

without a signed-in user.

Allows the app to manage (create-

update-terminate) Delegated Admin

relationships with customers as well as

role assignments to security groups for

active Delegated Admin relationships

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

81b4724a-58aa-41c1-8a55-

84ef97466587

a197cdc4-a8e8-4d49-9d35-

4ca7c83887b4

DisplayText

Read all delegated permission grants

Read delegated permission grants

Description

Allows the app to read all delegated

permission grants, without a signed-

in user.

Allows the app to read delegated

permission grants, on behalf of the

signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

8e8e4742-1d95-4f68-9d56-

6ee75648c72a

41ce6ca6-6826-4807-84f1-

1c82854f7ee5

DisplayText

Manage all delegated permission

grants

Manage all delegated permission

grants

**DelegatedPermissionGrant.Read.All**

ﾉ

**Expand table**

**DelegatedPermissionGrant.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to manage permission

grants for delegated permissions

exposed by any API (including

Microsoft Graph), without a signed-in

user.

Allows the app to manage permission

grants for delegated permissions

exposed by any API (including

Microsoft Graph), on behalf of the

signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

bac3b9c2-b516-4ef4-bd3b-c2ef73d8d804

DisplayText

-

Communicate with user devices

Description

-

Allows the app to launch another app or communicate with

another app on a user's device on behalf of the signed-in user.

AdminConsentRequired

-

No

![](./assets/output_210_1.png)![](./assets/output_210_2.png)

The _Device.Command_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

-

edc92e89-a987-48a9-911a-a7b1967dd7b1

DisplayText

-

Create devices based on owned device templates

Description

-

Allows the app to create device objects based on device

templates owned by the signed-in user, on behalf of the signed

in user.

AdminConsentRequired

-

Yes

**Device.Command**

ﾉ

**Expand table**

**Device.CreateFromOwnedTemplate**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

11d4cd79-5ba5-460f-803f-e22c8ab85ccd

DisplayText

-

Read user devices

Description

-

Allows the app to read a user's list of devices on behalf of the

signed-in user.

AdminConsentRequired

-

No

![](./assets/output_211_1.png)![](./assets/output_211_2.png)

The _Device.Read_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

7438b122-aefc-4978-80ed-

43db9fcc7715

951183d1-1a61-466f-a6d1-

1fde911bfd95

DisplayText

Read all devices

Read all devices

Description

Allows the app to read your

organization's devices' configuration

information without a signed-in user.

Allows the app to read your

organization's devices' configuration

information on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

![](./assets/output_211_3.png)![](./assets/output_211_4.png)

The _Device.Read.All_ delegated permission is available for consent in personal Microsoft

accounts.

**Device.Read**

ﾉ

**Expand table**

**Device.Read.All**

ﾉ

**Expand table**

**Device.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

1138cb37-bd11-4084-a2b7-9f71582aeddb

-

DisplayText

Read and write devices

-

Description

Allows the app to read and write all device properties without a

signed in user. Does not allow device creation, device deletion or

update of device alternative security identifiers.

-

AdminConsentRequired

Yes

-

Before December 3rd, 2020, when the application permission _Device.ReadWrite.All_ was granted,

the Device Managers directory role was also assigned to the app's service principal. This

directory role assignment is not removed automatically when the associated application

permissions is revoked. To ensure that an application's access to read or write to devices is

removed, customers must also remove any related directory roles that were granted to the

application.

A service update disabling this behavior began rolling out on December 3rd, 2020. Deployment

to all customers completed on January 11th, 2021. Directory roles are no longer automatically

assigned when application permissions are granted.

**Category**

**Application**

**Delegated**

Identifier

884b599e-4d48-43a5-ba94-

15c414d00588

280b3b69-0437-44b1-bc20-

3b2fca1ee3e9

DisplayText

Read device local credential

passwords

Read device local credential passwords

Description

Allows the app to read device local

credential properties including

passwords, without a signed-in user.

Allows the app to read device local

credential properties including

passwords, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**DeviceLocalCredential.Read.All**

ﾉ

**Expand table**

**DeviceLocalCredential.ReadBasic.All**

**Category**

**Application**

**Delegated**

Identifier

db51be59-e728-414b-b800-

e0f010df1a79

9917900e-410b-4d15-846e-

42a357488545

DisplayText

Read device local credential

properties

Read device local credential properties

Description

Allows the app to read device local

credential properties excluding

passwords, without a signed-in user.

Allows the app to read device local

credential properties excluding

passwords, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7a6ee1e7-141e-4cec-ae74-

d9db155731ff

4edf5f54-4666-44af-9de9-

0144fb4b6e8c

DisplayText

Read Microsoft Intune apps

Read Microsoft Intune apps

Description

Allows the app to read the properties,

group assignments and status of apps,

app configurations and app protection

policies managed by Microsoft Intune,

without a signed-in user.

Allows the app to read the

properties, group assignments and

status of apps, app configurations

and app protection policies

managed by Microsoft Intune.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

ﾉ

**Expand table**

**DeviceManagementApps.Read.All**

ﾉ

**Expand table**

**DeviceManagementApps.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

78145de6-330d-4800-a6ce-

494ff2d33d07

7b3f05d5-f68c-4b8d-8c59-

a2ecd12f24af

DisplayText

Read and write Microsoft Intune apps

Read and write Microsoft Intune

apps

Description

Allows the app to read and write the

properties, group assignments and

status of apps, app configurations and

app protection policies managed by

Microsoft Intune, without a signed-in

user.

Allows the app to read and write the

properties, group assignments and

status of apps, app configurations

and app protection policies

managed by Microsoft Intune.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

315b6e8c-d92a-4691-919d-

00ce76d1344a

ac5c8443-d999-471f-9247-

ce92cf5c5560

DisplayText

Read Microsoft Cloud PKI objects

Read Microsoft Cloud PKI objects

Description

Allows the app to read certification

authority information without a

signed-in user.

Allows the app to read certification

authority information on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**DeviceManagementCloudCA.Read.All**

ﾉ

**Expand table**

**DeviceManagementCloudCA.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

f15eb2ba-ef8a-4f70-991d-

da5d045154e2

93028c58-65aa-48db-a706-

1fe4ada325ec

DisplayText

Read and write Microsoft Cloud PKI

objects

Read and write Microsoft Cloud PKI

objects

Description

Allows the app to read and write

certification authority information

without a signed-in user.

Allows the app to read and write

certification authority information on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

dc377aa6-52d8-4e23-b271-

2a7ae04cedf3

f1493658-876a-4c87-8fa7-

edb559b3476a

DisplayText

Read Microsoft Intune device

configuration and policies

Read Microsoft Intune Device

Configuration and Policies

Description

Allows the app to read properties of

Microsoft Intune-managed device

configuration and device compliance

policies and their assignment to groups,

without a signed-in user.

Allows the app to read properties of

Microsoft Intune-managed device

configuration and device

compliance policies and their

assignment to groups.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

**DeviceManagementConfiguration.Read.All**

ﾉ

**Expand table**

**DeviceManagementConfiguration.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

9241abd9-d0e6-425a-bd4f-

47ba86e767a4

0883f392-0a7a-443d-8c76-

16a6d39c7b63

DisplayText

Read and write Microsoft Intune device

configuration and policies

Read and write Microsoft Intune

Device Configuration and Policies

Description

Allows the app to read and write

properties of Microsoft Intune-managed

device configuration and device

compliance policies and their

assignment to groups, without a

signed-in user.

Allows the app to read and write

properties of Microsoft Intune-

managed device configuration and

device compliance policies and their

assignment to groups.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

5b07b0dd-2377-4e44-a38d-

703f09a0dc3c

3404d2bf-2b13-457e-a330-

c24615765193

DisplayText

Perform user-impacting remote actions

on Microsoft Intune devices

Perform user-impacting remote

actions on Microsoft Intune devices

Description

Allows the app to perform remote high

impact actions such as wiping the

device or resetting the passcode on

devices managed by Microsoft Intune,

without a signed-in user.

Allows the app to perform remote

high impact actions such as wiping

the device or resetting the passcode

on devices managed by Microsoft

Intune.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

**DeviceManagementManagedDevices.PrivilegedOperations.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

2f51be20-0bb4-4fed-bf7b-db946066c75e

314874da-47d6-4978-88dc-

cf0d37f0bb82

DisplayText

Read Microsoft Intune devices

Read Microsoft Intune devices

Description

Allows the app to read the properties of

devices managed by Microsoft Intune,

without a signed-in user.

Allows the app to read the

properties of devices managed by

Microsoft Intune.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

243333ab-4d21-40cb-a475-

36241daa0842

44642bfe-8385-4adc-8fc6-

fe3cb2c375c3

DisplayText

Read and write Microsoft Intune devices

Read and write Microsoft Intune

devices

Description

Allows the app to read and write the

properties of devices managed by

Microsoft Intune, without a signed-in

user. Does not allow high impact

operations such as remote wipe and

password reset on the device's owner

Allows the app to read and write the

properties of devices managed by

Microsoft Intune. Does not allow

high impact operations such as

remote wipe and password reset on

the device's owner.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

**DeviceManagementManagedDevices.Read.All**

ﾉ

**Expand table**

**DeviceManagementManagedDevices.ReadWrite.All**

ﾉ

**Expand table**

These permissions aren't supported for personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

58ca0d9a-1575-47e1-a3cb-

007ef2e4583b

49f0cc30-024c-4dfd-ab3e-

82e137ee5431

DisplayText

Read Microsoft Intune RBAC settings

Read Microsoft Intune RBAC

settings

Description

Allows the app to read the properties

relating to the Microsoft Intune Role-

Based Access Control (RBAC) settings,

without a signed-in user.

Allows the app to read the

properties relating to the Microsoft

Intune Role-Based Access Control

(RBAC) settings.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

e330c4f0-4170-414e-a55a-

2f022ec2b57b

0c5e8a55-87a6-4556-93ab-

adc52c4d862d

DisplayText

Read and write Microsoft Intune RBAC

settings

Read and write Microsoft Intune

RBAC settings

Description

Allows the app to read and write the

properties relating to the Microsoft

Intune Role-Based Access Control

(RBAC) settings, without a signed-in

user.

Allows the app to read and write

the properties relating to the

Microsoft Intune Role-Based Access

Control (RBAC) settings.

AdminConsentRequired

Yes

Yes

**DeviceManagementRBAC.Read.All**

ﾉ

**Expand table**

**DeviceManagementRBAC.ReadWrite.All**

ﾉ

**Expand table**

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

c7a5be92-2b3d-4540-8a67-

c96dcaae8b43

d32381d8-ee89-4220-9c83-

b672aa68d404

DisplayText

Read Microsoft Intune Scripts

Read Microsoft Intune Scripts

Description

Allows the app to read Microsoft

Intune device compliance scripts,

device management scripts, device

shell scripts, device custom attribute

shell scripts and device health scripts,

without a signed-in user.

Allows the app to read Microsoft

Intune device compliance scripts,

device management scripts, device

shell scripts, device custom attribute

shell scripts and device health scripts

on behalf of the signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

9255e99d-faf5-445e-bbf7-

cb71482737c4

8b9d79d0-ad75-4566-8619-

f7500ecfcebe

DisplayText

Read and write Microsoft Intune

Scripts

Read and write Microsoft Intune

Scripts

Description

Allows the app to read and write

Microsoft Intune device compliance

scripts, device management scripts,

device shell scripts, device custom

attribute shell scripts and device

health scripts, without a signed-in

user.

Allows the app to read and write

Microsoft Intune device compliance

scripts, device management scripts,

device shell scripts, device custom

attribute shell scripts and device

health scripts on behalf of the signed

in user.

**DeviceManagementScripts.Read.All**

ﾉ

**Expand table**

**DeviceManagementScripts.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

06a5fe6d-c49d-46a7-b082-

56b1b14103c7

8696daa5-bce5-4b2e-83f9-

51b6defc4e1e

DisplayText

Read Microsoft Intune configuration

Read Microsoft Intune

configuration

Description

Allows the app to read Microsoft Intune

service properties including device

enrollment and third party service

connection configuration, without a

signed-in user.

Allows the app to read Microsoft

Intune service properties including

device enrollment and third party

service connection configuration.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

5ac13192-7ace-4fcf-b828-

1a26f28068ee

662ed50a-ac44-4eef-ad86-

62eed9be2a29

DisplayText

Read and write Microsoft Intune

configuration

Read and write Microsoft Intune

configuration

Description

Allows the app to read and write

Microsoft Intune service properties

including device enrollment and third

Allows the app to read and write

Microsoft Intune service properties

including device enrollment and

**DeviceManagementServiceConfig.Read.All**

ﾉ

**Expand table**

**DeviceManagementServiceConfig.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

party service connection configuration,

without a signed-in user.

third party service connection

configuration.

AdminConsentRequired

Yes

Yes

Using the Microsoft Graph APIs to configure Intune controls and policies still requires that the

Intune service is correctly licensed by the customer.

These permissions aren't supported for personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

abf6441f-0772-4932-96e7-

0191478dd73a

0b1717ff-3e42-4a73-8c29-

e6b2e1093960

DisplayText

Create device template

Create device templates

Description

Allows the app to create device

templates. The app is marked as

owner of the created device

template. As a member of owners,

the app will be allowed to manage

devices created from the template.

Allows the app to create device

templates on behalf of the signed in

user. The user is marked as owners of

the created device template. As a

member of owners, the user will be

allowed to manage devices created

from the template.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

dd9febb5-0c6d-419f-b256-

3afe12c6adeb

2bcae0b0-aa93-48e4-a9e4-

855482dffdcd

DisplayText

Read all device templates

Read all device templates

**DeviceTemplate.Create**

ﾉ

**Expand table**

**DeviceTemplate.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read all device

templates, without a signed-in user.

Allows the app to read all device

templates, on behalf of the signed in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

9fadb66e-6421-4744-aede-

4ab6fb98a884

2d372e98-f1ae-406c-a157-

2ea83f6f5e4a

DisplayText

Read and write all device templates

Read and write all device templates

Description

Allows the app to create, read, update

and delete any device template,

without a signed-in user. It also allows

the app to add or remove owners on

any device template.

Allows the app to create, read, update

and delete the device template, on

behalf of the signed in user. It also

allows the app to add or remove

owners on any device template.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

0e263e50-5827-48a4-b97c-d940288653c7

DisplayText

-

Access directory as the signed in user

Description

-

Allows the app to have the same access to information in the

directory as the signed-in user.

AdminConsentRequired

-

Yes

**DeviceTemplate.ReadWrite.All**

ﾉ

**Expand table**

**Directory.AccessAsUser.All**

ﾉ

**Expand table**

Ｕ **Caution**

**Category**

**Application**

**Delegated**

Identifier

7ab1d382-f21e-4acd-a863-ba3e13f7da61

06da0dbc-49e2-44d2-8312-

53f166ab848a

DisplayText

Read directory data

Read directory data

Description

Allows the app to read data in your

organization's directory, such as users,

groups and apps, without a signed-in

user.

Allows the app to read data in

your organization's directory, such

as users, groups and apps.

AdminConsentRequired

Yes

Yes

Before December 3rd, 2020, when the application permission _Directory.Read.All_ was granted,

the Directory Readers directory role was also assigned to the app's service principal. This

directory role isn't removed automatically when the associated application permissions are

revoked. To remove an application's access to read or write to the directory, customers must

also remove any directory roles that were granted to the application.

A service update disabling this behavior began rolling out on December 3rd, 2020. Deployment

to all customers completed on January 11th, 2021. Directory roles are no longer automatically

assigned when application permissions are granted.

Directory permissions grant broad access to directory (Microsoft Entra ID) resources such

as **user**, **group**, and **device** in an organization. Whenever possible, choose permissions

specific to these resources and avoid using directory permissions.

Directory permissions might be deprecated in the future.

**Directory.Read.All**

ﾉ

**Expand table**

Ｕ **Caution**

Directory permissions grant broad access to directory (Microsoft Entra ID) resources such

as **user**, **group**, and **device** in an organization. Whenever possible, choose permissions

specific to these resources and avoid using directory permissions.

Directory permissions might be deprecated in the future.

**Category**

**Application**

**Delegated**

Identifier

19dbc75e-c2e2-444c-a770-

ec69d8559fc7

c5366453-9fb0-48a5-a156-

24f0c49a4b84

DisplayText

Read and write directory data

Read and write directory data

Description

Allows the app to read and write

data in your organization's directory,

such as users, and groups, without a

signed-in user. Does not allow user

or group deletion.

Allows the app to read and write data

in your organization's directory, such

as users, and groups. It does not allow

the app to delete users or groups, or

reset user passwords.

AdminConsentRequired

Yes

Yes

Before December 3rd, 2020, when the application permission _Directory.ReadWrite.All_ was

granted, the Directory Writers directory role was also assigned. This directory role isn't

removed automatically when the associated application permissions are revoked. To remove an

application's access to read or write to the directory, customers must also remove any directory

roles that were granted to the application.

A service update disabling this behavior began rolling out on December 3rd, 2020. Deployment

to all customers completed on January 11, 2021. Directory roles are no longer automatically

assigned when application permissions are granted.

**Directory.ReadWrite.All**

ﾉ

**Expand table**

Ｕ **Caution**

Directory permissions grant broad access to directory (Microsoft Entra ID) resources such

as **user**, **group**, and **device** in an organization. Whenever possible, choose permissions

specific to these resources and avoid using directory permissions.

Directory permissions might be deprecated in the future.

**DirectoryRecommendations.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

ae73097b-cb2a-4447-b064-

5d80f6093921

34d3bd24-f6a6-468c-b67c-

0c365c1d6410

DisplayText

Read all Azure AD recommendations

Read Azure AD recommendations

Description

Allows the app to read all Azure AD

recommendations, without a signed-

in user.

Allows the app to read Azure AD

recommendations, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

0e9eea12-4f01-45f6-9b8d-

3ea4c8144158

f37235e8-90a0-4189-93e2-

e55b53867ccd

DisplayText

Read and update all Azure AD

recommendations

Read and update Azure AD

recommendations

Description

Allows the app to read and update all

Azure AD recommendations, without

a signed-in user.

Allows the app to read and update

Azure AD recommendations, on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

c0e5a7b0-e8b7-40a7-b8e0-

8249e6ea81d5

33203a2a-a761-40f0-8a7c-

a7e74a9f8ac6

DisplayText

Read internal federation configuration

for a domain.

Read internal federation configuration

for a domain.

Description

Allows the app to read internal

federation configuration for a domain.

Allows the app to read internal

federation configuration for a

**DirectoryRecommendations.ReadWrite.All**

ﾉ

**Expand table**

**Domain-InternalFederation.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

domain.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

64d40371-8d58-4270-bc8a-

b4a66de36b9a

857bd3ea-490e-4284-88a7-

a7de1893b6ee

DisplayText

Create, read, update and delete

internal federation configuration for a

domain.

Create, read, update and delete

internal federation configuration for a

domain.

Description

Allows the app to create, read, update

and delete internal federation

configuration for a domain.

Allows the app to create, read, update

and delete internal federation

configuration for a domain.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

dbb9058a-0e50-45d7-ae91-

66909b5d4664

2f9ee017-59c1-4f1d-9472-

bd5529a7b311

DisplayText

Read domains

Read domains.

Description

Allows the app to read all domain

properties without a signed-in user.

Allows the app to read all domain

properties on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Domain-InternalFederation.ReadWrite.All**

ﾉ

**Expand table**

**Domain.Read.All**

ﾉ

**Expand table**

**Domain.ReadWrite.All**

**Category**

**Application**

**Delegated**

Identifier

7e05723c-0bb0-42da-be95-

ae9f08a6e53c

0b5d694c-a244-4bde-86e6-

eb5cd07730fe

DisplayText

Read and write domains

Read and write domains

Description

Allows the app to read and write all

domain properties without a signed

in user. Also allows the app to add,

verify and remove domains.

Allows the app to read and write all

domain properties on behalf of the

signed-in user. Also allows the app to

add, verify and remove domains.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

ff91d191-45a0-43fd-b837-bd682c4a0b0f

DisplayText

-

Access mailboxes via Exchange ActiveSync

Description

-

Allows the app to have the same access to mailboxes as the

signed-in user via Exchange ActiveSync.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

50180013-6191-4d1e-a373-

e590ff4e66af

99201db3-7652-4d5a-809a-

bdb94f85fe3c

DisplayText

Read all eDiscovery objects

Read all eDiscovery objects

Description

Allows the app to read eDiscovery

objects such as cases, custodians,

Allows the app to read eDiscovery

objects such as cases, custodians,

ﾉ

**Expand table**

**EAS.AccessAsUser.All**

ﾉ

**Expand table**

**eDiscovery.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

review sets and other related objects

without a signed-in user.

review sets and other related objects

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

b2620db1-3bf7-4c5b-9cb9-

576d29eac736

acb8f680-0834-4146-b69e-

4ab1b39745ad

DisplayText

Read and write all eDiscovery objects

Read and write all eDiscovery objects

Description

Allows the app to read and write

eDiscovery objects such as cases,

custodians, review sets and other

related objects without a signed-in

user.

Allows the app to read and write

eDiscovery objects such as cases,

custodians, review sets and other

related objects on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

8523895c-6081-45bf-8a5d-f062a2f12c9f

DisplayText

-

Read education app settings

Description

-

Read the state and settings of all Microsoft education apps on

behalf of the user.

AdminConsentRequired

-

Yes

**eDiscovery.ReadWrite.All**

ﾉ

**Expand table**

**EduAdministration.Read**

ﾉ

**Expand table**

**EduAdministration.Read.All**

**Category**

**Application**

**Delegated**

Identifier

7c9db06a-ec2d-4e7b-a592-5a1e30992566

-

DisplayText

Read Education app settings

-

Description

Read the state and settings of all Microsoft education apps.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

63589852-04e3-46b4-bae9-15d5b1050748

DisplayText

-

Manage education app settings

Description

-

Manage the state and settings of all Microsoft education apps

on behalf of the user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

9bc431c3-b8bc-4a8d-a219-40f10f92eff6

-

DisplayText

Manage education app settings

-

Description

Manage the state and settings of all Microsoft education apps.

-

AdminConsentRequired

Yes

-

ﾉ

**Expand table**

**EduAdministration.ReadWrite**

ﾉ

**Expand table**

**EduAdministration.ReadWrite.All**

ﾉ

**Expand table**

**EduAssignments.Read**

**Category**

**Application**

**Delegated**

Identifier

-

091460c9-9c4a-49b2-81ef-1f3d852acce2

DisplayText

-

Read users' class assignments and their grades

Description

-

Allows the app to read assignments and their grades on behalf

of the user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

4c37e1b6-35a1-43bf-926a-6f30f2cdf585

-

DisplayText

Read all class assignments with grades

-

Description

Allows the app to read all class assignments with grades for all

users without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

c0b0103b-c053-4b2e-9973-9f3a544ec9b8

DisplayText

-

Read users' class assignments without grades

Description

-

Allows the app to read assignments without grades on behalf of

the user.

AdminConsentRequired

-

Yes

ﾉ

**Expand table**

**EduAssignments.Read.All**

ﾉ

**Expand table**

**EduAssignments.ReadBasic**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

6e0a958b-b7fc-4348-b7c4-a6ab9fd3dd0e

-

DisplayText

Read all class assignments without grades

-

Description

Allows the app to read all class assignments without grades for all

users without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

2f233e90-164b-4501-8bce-31af2559a2d3

DisplayText

-

Read and write users' class assignments and their grades

Description

-

Allows the app to read and write assignments and their grades

on behalf of the user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

0d22204b-6cad-4dd0-8362-3e3f2ae699d9

-

DisplayText

Create, read, update and delete all class assignments with grades

-

Description

Allows the app to create, read, update and delete all class

assignments with grades for all users without a signed-in user.

-

AdminConsentRequired

Yes

-

**EduAssignments.ReadBasic.All**

ﾉ

**Expand table**

**EduAssignments.ReadWrite**

ﾉ

**Expand table**

**EduAssignments.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

2ef770a1-622a-47c4-93ee-28d6adbed3a0

DisplayText

-

Read and write users' class assignments without grades

Description

-

Allows the app to read and write assignments without grades on

behalf of the user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

f431cc63-a2de-48c4-8054-a34bc093af84

-

DisplayText

Create, read, update and delete all class assignments without

grades

-

Description

Allows the app to create, read, update and delete all class

assignments without grades for all users without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

484859e8-b9e2-4e92-b910-84db35dadd29

DisplayText

-

Read the user's class modules and resources

Description

-

Allows the app to read the user's modules and resources on

behalf of the signed-in user.

**EduAssignments.ReadWriteBasic**

ﾉ

**Expand table**

**EduAssignments.ReadWriteBasic.All**

ﾉ

**Expand table**

**EduCurricula.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

6cdb464c-3a03-40f8-900b-4cb7ea1da9c0

-

DisplayText

Read all class modules and resources

-

Description

Allows the app to read all modules and resources, without a

signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

4793c53b-df34-44fd-8d26-d15c517732f5

DisplayText

-

Read and write the user's class modules and resources

Description

-

Allows the app to read and write user's modules and resources

on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

6a0c2318-d59d-4c7d-bf2e-5f3902dc2593

-

**EduCurricula.Read.All**

ﾉ

**Expand table**

**EduCurricula.ReadWrite**

ﾉ

**Expand table**

**EduCurricula.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write all class modules and resources

-

Description

Allows the app to read and write all modules and resources,

without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

ad248c30-1919-40c8-b3d2-304481894e88

-

DisplayText

Read all tenant reading assignments submissions data

-

Description

Allows the app to read all tenant users reading assignments

submissions data without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

040330d7-be7e-4130-b349-a6eb3a56e2f8

-

DisplayText

Read all tenant reading assignments submissions data

-

Description

Allows the app to read all tenant users reading assignments

submissions data (excludes student-identifying information)

without a signed-in user.

-

AdminConsentRequired

Yes

-

**EduReports-Reading.Read.All**

ﾉ

**Expand table**

**EduReports-Reading.ReadAnonymous.All**

ﾉ

**Expand table**

**EduReports-Reflect.Read.All**

**Category**

**Application**

**Delegated**

Identifier

c5debf73-bdc8-473d-bf07-f4074ad05f71

-

DisplayText

Read all tenant reflect check-ins submissions data

-

Description

Allows the app to read all tenant users reflect check-ins

submissions data without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

f5d05dba-7ef0-46fc-b62c-a7282555f428

-

DisplayText

Read all tenant reflect check-ins submissions data

-

Description

Allows the app to read all tenant users reflect check-ins

submissions data (excludes responder-identifying information)

without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

a4389601-22d9-4096-ac18-36a927199112

DisplayText

-

Read users' view of the roster

Description

-

Allows the app to read the structure of schools and classes in an

organization's roster and education-specific information about

users to be read on behalf of the user.

AdminConsentRequired

-

Yes

ﾉ

**Expand table**

**EduReports-Reflect.ReadAnonymous.All**

ﾉ

**Expand table**

**EduRoster.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

e0ac9e1b-cb65-4fc5-87c5-1a8bc181f648

-

DisplayText

Read the organization's roster

-

Description

Allows the app to read the structure of schools and classes in the

organization's roster and education-specific information about all

users to be read.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

5d186531-d1bf-4f07-8cea-7c42119e1bd9

DisplayText

-

Read a limited subset of users' view of the roster

Description

-

Allows the app to read a limited subset of the properties from

the structure of schools and classes in an organization's roster

and a limited subset of properties about users to be read on

behalf of the user. Includes name, status, education role, email

address and photo.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

0d412a8c-a06c-439f-b3ec-8abcf54d2f96

-

DisplayText

Read a limited subset of the organization's roster

-

**EduRoster.Read.All**

ﾉ

**Expand table**

**EduRoster.ReadBasic**

ﾉ

**Expand table**

**EduRoster.ReadBasic.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read a limited subset of properties from both

the structure of schools and classes in the organization's roster

and education-specific information about all users. Includes

name, status, role, email address and photo.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

359e19a6-e3fa-4d7f-bcab-d28ec592b51e

DisplayText

-

Read and write users' view of the roster

Description

-

Allows the app to read and write the structure of schools and

classes in an organization's roster and education-specific

information about users to be read and written on behalf of the

user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

d1808e82-ce13-47af-ae0d-f9b254e6d58a

-

DisplayText

Read and write the organization's roster

-

Description

Allows the app to read and write the structure of schools and

classes in the organization's roster and education-specific

information about all users to be read and written.

-

AdminConsentRequired

Yes

-

**EduRoster.ReadWrite**

ﾉ

**Expand table**

**EduRoster.ReadWrite.All**

ﾉ

**Expand table**

**email**

**Category**

**Application**

**Delegated**

Identifier

-

64a6cdd6-aab1-4aaf-94b8-3cc8405e90d0

DisplayText

-

View users' email address

Description

-

Allows the app to read your users' primary email address

AdminConsentRequired

-

No

_email_ is an OpenID Connect (OIDC) scope.

You can use the OIDC scopes to specify artifacts that you want returned in Microsoft identity

platform authorization and token requests. The Microsoft identity platform v1.0 and v2.0

endpoints support OIDC scopes differently.

With the Microsoft identity platform v1.0 endpoint, only the _openid_ scope is used. You specify it

in the _scope_ parameter in an authorization request to return an ID token when you use the

OpenID Connect protocol to sign in a user to your app. For more information, see Microsoft

identity platform and OAuth 2.0 authorization code flow. To successfully return an ID token,

you must also make sure that the _User.Read_ permission is configured when you register your

app.

With the Microsoft identity platform v2.0 endpoint, you specify the _offline\_access_ scope in the

**scope** parameter to explicitly request a refresh token when using the OAuth 2.0 or OpenID

Connect protocols. With OpenID Connect, you specify the _openid_ scope to request an ID token.

You can also specify the _email_ scope, _profile_ scope, or both to return additional claims in the ID

token. You don't need to specify the _User.Read_ permission to return an ID token with the v2.0

endpoint. For more information, see OpenID Connect scopes.

The Microsoft Authentication Library (MSAL) currently specifies _offline\_access_, _openid_, _profile_,

and _email_ by default in authorization and token requests. Therefore, for the default case, if you

specify these scopes explicitly, the Microsoft identity platform might return an error.

**Category**

**Application**

**Delegated**

Identifier

e1d2136d-eaaf-427a-a7db-f97dbe847c27

-

ﾉ

**Expand table**

**EngagementConversation.Migration.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write all Viva Engage conversations

-

Description

Allows the app to create Viva Engage conversations without a

signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

2c495153-cd0e-41b4-9980-

3bcecf1ca22f

c55541d9-2cdd-4fad-8ead-

0c08fae5b0c8

DisplayText

Read all Viva Engage conversations

Read all Viva Engage conversations

Description

Allows the app to list Viva Engage

conversations, and to read their

properties without a signed-in user.

Allows the app to read Viva Engage

conversations, and to read their

properties on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

bfbd4840-fba0-43a7-93a9-465b687e47d0

ebbfd079-1634-4640-8618-

68b19ebbed1d

DisplayText

Read and write all Viva Engage

conversations

Read and write all Viva Engage

conversations

Description

Allows the app to create Viva Engage

conversations, read all conversation

properties, update conversation

properties, and delete conversations

without a signed-in user.

Allows the app to create Viva

Engage conversations and read all

conversation properties on behalf

of the signed-in user.

**EngagementConversation.Read.All**

ﾉ

**Expand table**

**EngagementConversation.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

d746beae-b46e-446e-924a-

5b805a5c4467

58c5819e-29bd-4400-ad52-

82cd82a63fbd

DisplayText

Read all Viva Engage Teams QA

conversations

Read all Viva Engage Teams QA

conversations

Description

Allows the app to list Viva Engage

Teams QA conversations, and to read

their properties without a signed-in

user.

Allows the app to read Viva Engage

Teams QA conversations, and to read

their properties on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

9f1da0fc-345c-4dfb-bab5-5215a073a417

DisplayText

-

Read a user's Viva Engage roles

Description

-

Allows the app to list a user's Viva Engage roles, on behalf of the

signed-in user.

AdminConsentRequired

-

No

**EngagementMeetingConversation.Read.All**

ﾉ

**Expand table**

**EngagementRole.Read**

ﾉ

**Expand table**

**EngagementRole.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

30614864-4114-45ef-bdd9-

0dd7894a1cc4

3cad91a5-8413-4c4a-acfe-

dfeb83d1366d

DisplayText

Read all Viva Engage roles and role

memberships

Read all Viva Engage roles and role

memberships

Description

Allows the app to list all Viva Engage

roles and role memberships without

a signed-in user.

Allows the app to list all Viva Engage

roles and role memberships on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

3ede5358-7366-4da8-a2f7-

472bf9c7cc34

4905982d-6459-4ccd-949c-

949fefc0a8f2

DisplayText

Modify Viva Engage role membership

Modify Viva Engage role membership

Description

Allows the app to assign Viva Engage

role to a user, and remove a Viva

Engage role from a user without a

signed-in user.

Allows the app to assign Viva Engage

role to a user, and remove a Viva

Engage role from a user behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

c74fd47d-ed3c-45c3-9a9e-

b8676de685d2

5449aa12-1393-4ea2-a7c7-

d0e06c1a56b2

DisplayText

Read all entitlement management

resources

Read all entitlement management

resources

**EngagementRole.ReadWrite.All**

ﾉ

**Expand table**

**EntitlementManagement.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read access

packages and related entitlement

management resources without a

signed-in user.

Allows the app to read access

packages and related entitlement

management resources on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

9acd699f-1e81-4958-b001-

93b1d2506e19

ae7a573d-81d7-432b-ad44-

4ed5c9d89038

DisplayText

Read and write all entitlement

management resources

Read and write entitlement management

resources

Description

Allows the app to read and write

access packages and related

entitlement management resources

without a signed-in user.

Allows the app to request access to and

management of access packages and

related entitlement management

resources on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

e9fdcbbb-8807-410f-b9ec-8d5468c7c2ac

DisplayText

-

Read and write entitlement management resources related to

self-service operations

Description

-

Allows the app to manage self-service entitlement management

resources on behalf of the signed-in user. This includes

operations such as requesting access and approving access of

others.

**EntitlementManagement.ReadWrite.All**

ﾉ

**Expand table**

**EntitlementMgmt-SubjectAccess.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

b7f6385c-6ce6-4639-a480-

e23c42ed9784

f7dd3bed-5eec-48da-bc73-

1c0ef50bc9a1

DisplayText

Read all authentication event

listeners

Read your organization's

authentication event listeners

Description

Allows the app to read your

organization's authentication event

listeners without a signed-in user.

Allows the app to read your

organization's authentication event

listeners on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

0edf5e9e-4ce8-468a-8432-

d08631d18c43

d11625a6-fe21-4fc6-8d3d-

063eba5525ad

DisplayText

Read and write all authentication

event listeners

Read and write your organization's

authentication event listeners

Description

Allows the app to read or write your

organization's authentication event

listeners without a signed-in user.

Allows the app to read or write your

organization's authentication event

listeners on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**EventListener.Read.All**

ﾉ

**Expand table**

**EventListener.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

9769c687-087d-48ac-9cb3-c37dde652038

DisplayText

-

Access mailboxes as the signed-in user via Exchange Web

Services

Description

-

Allows the app to have the same access to mailboxes as the

signed-in user via Exchange Web Services.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

1914711b-a1cb-4793-b019-

c2ce0ed21b8c

a38267a5-26b6-4d76-9493-935b7599116b

DisplayText

Read all external connections

Read all external connections

Description

Allows the app to read all

external connections without a

signed-in user.

Allows the app to read all external

connections on behalf of a signed-in user.

The signed-in user must be an administrator.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

34c37bc0-2b40-4d5e-85e1-

2365cd256d79

bbbbd9b3-3566-4931-ac37-2b2180d9e334

DisplayText

Read and write all external

connections

Read and write all external connections

**EWS.AccessAsUser.All**

ﾉ

**Expand table**

**ExternalConnection.Read.All**

ﾉ

**Expand table**

**ExternalConnection.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read and

write all external connections

without a signed-in user.

Allows the app to read and write all external

connections on behalf of a signed-in user.

The signed-in user must be an administrator.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f431331c-49a6-499f-be1c-

62af19c34a9d

4082ad95-c812-4f02-be92-

780c4c4f1830

DisplayText

Read and write external connections

Read and write external connections

Description

Allows the app to read and write

external connections without a

signed-in user. The app can only

read and write external connections

that it is authorized to, or it can

create new external connections.

Allows the app to read and write

settings of external connections on

behalf of a signed-in user. The signed-

in user must be an administrator. The

app can only read and write settings of

connections that it is authorized to.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7a7cffad-37d2-4f48-afa4-

c6ab129adcc2

922f9392-b1b7-483c-a4be-0089be7704fb

DisplayText

Read all external items

Read items in external datasets

Description

Allows the app to read all external

items without a signed-in user.

Allow the app to read external datasets

and content, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**ExternalConnection.ReadWrite.OwnedBy**

ﾉ

**Expand table**

**ExternalItem.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

38c3d6ee-69ee-422f-b954-

e17819665354

b02c54f8-eb48-4c50-a9f0-a149e5a2012f

DisplayText

Read and write items in external

datasets

Read and write all external items

Description

Allow the app to read or write

items in all external datasets that

the app is authorized to access

Allows the app to read and write all

external items on behalf of a signed-in

user. The signed-in user must be an

administrator.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

8116ae0f-55c2-452d-9944-

d18420f5b2c8

4367b9d7-cee7-4995-853c-a0bdfe95c1f9

DisplayText

Read and write external items

Read and write external items

Description

Allows the app to read and write

external items without a signed-in

user. The app can only read

external items of the connection

that it is authorized to.

Allows the app to read and write external

items on behalf of a signed-in user. The

signed-in user must be an administrator.

The app can only read external items of

the connection that it is authorized to.

AdminConsentRequired

Yes

Yes

**ExternalItem.ReadWrite.All**

ﾉ

**Expand table**

**ExternalItem.ReadWrite.OwnedBy**

ﾉ

**Expand table**

**ExternalUserProfile.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

1987d7a0-d602-4262-ab90-

cfdd43b37545

47167bec-55a7-4caf-9ecc-

8d4566e3cfb1

DisplayText

Read all external user profiles

Read external user profiles

Description

Allows the app to read available

properties of external user profiles,

without a signed-in user.

Allows the app to read available

properties of external user profiles, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

761327c9-d819-4c08-9a5f-

874cd2826608

c6068dc7-a791-46a4-a811-

b8228e6649ab

DisplayText

Read and write all external user

profiles

Read and write external user profiles

Description

Allows the app to read and write

available properties of external user

profiles, without a signed-in user.

Allows the app to read and write

available properties of external user

profiles, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

3a1e4806-a744-4c70-80fc-223bf8582c46

DisplayText

-

Read your family info

Description

-

Allows the app to read your family information, members and

their basic profile.

**ExternalUserProfile.ReadWrite.All**

ﾉ

**Expand table**

**Family.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

65891b00-2fd9-4e33-be27-04a53132e3df

-

DisplayText

Ingest SharePoint and OneDrive content to make it available in

the search index

-

Description

Allows the app to ingest SharePoint and OneDrive content to

make it available in the search index, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

766c601b-c009-4438-8290-c8b05fa00c4b

-

DisplayText

Manage onboarding for a Hybrid Cloud tenant

-

Description

Allows the app to manage onboarding for a Hybrid Cloud tenant,

without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

10465720-29dd-4523-a11a-6a75c743c9d9

**FileIngestion.Ingest**

ﾉ

**Expand table**

**FileIngestionHybridOnboarding.Manage**

ﾉ

**Expand table**

**Files.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

-

Read user files

Description

-

Allows the app to read the signed-in user's files.

AdminConsentRequired

-

No

![](./assets/output_249_1.png)![](./assets/output_249_2.png)

The _Files.Read_ delegated permission is available for consent in personal Microsoft accounts.

For personal accounts, _Files.Read_ also grant access to files shared with the signed-in user.

**Category**

**Application**

**Delegated**

Identifier

01d4889c-1287-42c6-ac1f-5d1e02578ef6

df85f4d6-205c-4ac5-a5ea-

6bf408dba283

DisplayText

Read files in all site collections

Read all files that user can access

Description

Allows the app to read all files in all site

collections without a signed in user.

Allows the app to read all files the

signed-in user can access.

AdminConsentRequired

Yes

No

![](./assets/output_249_3.png)![](./assets/output_249_4.png)

The _Files.Read.All_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

-

5447fe39-cb82-4c1a-b977-520e67e724eb

DisplayText

-

Read files that the user selects (preview)

Description

-

(Preview) Allows the app to read files that the user selects. The

app has access for several hours after the user selects a file.

AdminConsentRequired

-

No

**Files.Read.All**

ﾉ

**Expand table**

**Files.Read.Selected**

ﾉ

**Expand table**

The _Files.Read.Selected_ delegated permission is only valid on work or school accounts and is

only exposed for working with Office 365 file handlers (v1.0). It should not be used for directly

calling Microsoft Graph APIs.

**Category**

**Application**

**Delegated**

Identifier

-

5c28f0bf-8a70-41f1-8ab2-9032436ddb65

DisplayText

-

Have full access to user files

Description

-

Allows the app to read, create, update and delete the signed-in

user's files.

AdminConsentRequired

-

No

![](./assets/output_250_1.png)![](./assets/output_250_2.png)

The _Files.ReadWrite_ delegated permission is available for consent in personal Microsoft

accounts.

For personal accounts, _Files.ReadWrite_ also grant access to files shared with the signed-in user.

**Category**

**Application**

**Delegated**

Identifier

75359482-378d-4052-8f01-

80520e7db3cd

863451e7-0667-486c-a5d6-

d135439485f0

DisplayText

Read and write files in all site collections

Have full access to all files user can

access

Description

Allows the app to read, create, update

and delete all files in all site collections

without a signed in user.

Allows the app to read, create,

update and delete all files the

signed-in user can access.

AdminConsentRequired

Yes

No

![](./assets/output_250_3.png)![](./assets/output_250_4.png)

The _Files.ReadWrite.All_ delegated permission is available for consent in personal Microsoft

accounts.

**Files.ReadWrite**

ﾉ

**Expand table**

**Files.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

b47b160b-1054-4efd-9ca0-

e2f614696086

8019c312-3263-48e6-825e-

2b833497195b

DisplayText

Have full access to the application's

folder without a signed in user.

Have full access to the application's

folder (preview)

Description

Allows the app to read, create, update

and delete files in the application's

folder without a signed in user.

(Preview) Allows the app to read,

create, update and delete files in the

application's folder.

AdminConsentRequired

Yes

No

![](./assets/output_251_1.png)![](./assets/output_251_2.png)

The _Files.ReadWrite.AppFolder_ delegated permission is available for consent in personal

Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

-

17dde5bd-8c17-420f-a486-969730c1b827

DisplayText

-

Read and write files that the user selects (preview)

Description

-

(Preview) Allows the app to read and write files that the user

selects. The app has access for several hours after the user

selects a file.

AdminConsentRequired

-

No

The _Files.ReadWrite.Selected_ delegated permission is only valid on work or school accounts and

is only exposed for working with Office 365 file handlers (v1.0). It should not be used for

directly calling Microsoft Graph APIs.

**Files.ReadWrite.AppFolder**

ﾉ

**Expand table**

**Files.ReadWrite.Selected**

ﾉ

**Expand table**

**Files.SelectedOperations.Selected**

**Category**

**Application**

**Delegated**

Identifier

bd61925e-3bf4-4d62-bc0b-

06b06c96d95c

ef2779dc-ef1b-4211-8310-

8a0ac2450081

DisplayText

Access selected Files without a

signed in user.

Access selected Files, on behalf of the

signed-in user

Description

Allow the application to access a

subset of files without a signed in

user. The specific files and the

permissions granted will be

configured in SharePoint Online or

OneDrive.

Allow the application to access files

explicitly permissioned to the

application on behalf of the signed in

user. The specific files and the

permissions granted will be configured

in SharePoint Online or OneDrive.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

527b6d64-cdf5-4b8b-b336-4aa0b8ca2ce5

DisplayText

-

Manage all file storage containers

Description

-

Allows the application to utilize the file storage container

administration capabilities on behalf of an administrator user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

40dc41bc-0f7e-42ff-89bd-

d9516947e474

085ca537-6565-41c2-aca7-

db852babc212

DisplayText

Access selected file storage

containers

Access selected file storage containers

ﾉ

**Expand table**

**FileStorageContainer.Manage.All**

ﾉ

**Expand table**

**FileStorageContainer.Selected**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the application to utilize the

file storage container platform to

manage containers, without a signed-

in user. The specific file storage

containers and the permissions

granted to them will be configured in

Microsoft 365 by the developer of

each container type.

Allows the application to utilize the file

storage container platform to manage

containers on behalf of the signed in

user. The specific file storage

containers and the permissions

granted to them will be configured in

Microsoft 365 by the developer of

each container type.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

8e6ec84c-5fcd-4cc7-ac8a-2296efc0ed9b

DisplayText

-

Manage file storage container types on behalf of the signed in

user

Description

-

Allows the application to manage file storage container types on

behalf of the signed in user. The user must be a SharePoint

Embedded Admin or Global Admin.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

c319a7df-930e-44c0-a43b-7e5e9c7f4f24

DisplayText

-

Manage file storage container type registrations on behalf of the

signed in user

Description

-

Allows the application to manage file storage container type

registrations on behalf of the signed in user. The user must be a

SharePoint Embedded Admin or Global Admin.

**FileStorageContainerType.Manage.All**

ﾉ

**Expand table**

**FileStorageContainerTypeReg.Manage.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

2dcc6599-bd30-442b-8f11-

90f88ad441dc

d1e4f63a-1569-475c-b9b2-bdc140405e38

DisplayText

Access selected file storage

container type registrations

Access selected file storage container type

registrations.

Description

Allows the application to

manage file storage container

type registrations without a

signed-in user.

Allows the application to manage selected file

storage container type registrations on behalf

of the signed in user. The user must be a

SharePoint Embedded Admin or Global

Admin.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

-

f534bf13-55d4-45a9-8f3c-c92fe64d6131

DisplayText

-

Read and write financials data

Description

-

Allows the app to read and write financials data on behalf of the

signed-in user.

AdminConsentRequired

-

No

**FileStorageContainerTypeReg.Selected**

ﾉ

**Expand table**

**Financials.ReadWrite.All**

ﾉ

**Expand table**

**Goals-Export.Read.All**

**Category**

**Application**

**Delegated**

Identifier

-

092211d9-ca1a-427b-813e-b79c7653fe71

DisplayText

-

Read all goals and export jobs that a user can access

Description

-

Allows the app to read all goals and export jobs that the signed-

in user can access.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

2edeb9fd-4228-480c-a26d-2ed52011cf3d

DisplayText

-

Have full access to all goals and export jobs a user can access

Description

-

Allows the app to read goals, create and read export jobs that

the signed-in user can access.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

4f0a8235-6f6f-4ec7-9500-34b452a4a0c3

c92fbbc2-50e0-4842-93ef-

385c3293ea3d

DisplayText

Read all group conversations

Read group conversations

Description

Allows the app to read conversations of

the groups this app has access to

without a signed-in user.

Allows the app to read group

conversations that the signed-in

user has access to.

AdminConsentRequired

Yes

Yes

ﾉ

**Expand table**

**Goals-Export.ReadWrite.All**

ﾉ

**Expand table**

**Group-Conversation.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

6679c91b-820a-4900-ab47-

e97b197a89c4

302bcbb5-855a-4e49-ae20-

94a331b0281e

DisplayText

Read and write all group conversations

Read and write group conversations

Description

Allows the app to read and write

conversations of the groups this app has

access to without a signed-in user.

Allows the app to read and write

group conversations that the

signed-in user has access to.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2d9bd318-b883-40be-9df7-

63ec4fcdc424

37e00479-5776-4659-aecf-

4841ec5d590a

DisplayText

Read and update the on-premises

sync behavior of groups

Read and update the on-premises sync

behavior of groups

Description

Allows the app to update the on-

premises sync behavior of all

groups without a signed-in user.

Allows the app to read and update the

on-premises sync behavior of groups on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

bf7b1a76-6e77-406b-b258-bf5c7720e98f

-

DisplayText

Create groups

-

**Group-Conversation.ReadWrite.All**

ﾉ

**Expand table**

**Group-OnPremisesSyncBehavior.ReadWrite.All**

ﾉ

**Expand table**

**Group.Create**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to create groups without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

5b567255-7703-4780-807c-

7be8301ae99b

5f8c59db-677d-491f-a6b8-5f174b11ec1d

DisplayText

Read all groups

Read all groups

Description

Allows the app to read group

properties and memberships,

and read conversations for all

groups, without a signed-in

user.

Allows the app to list groups, and to read their

properties and all group memberships on

behalf of the signed-in user. Also allows the

app to read calendar, conversations, files, and

other group content for all groups the signed-

in user can access.

AdminConsentRequired

Yes

Yes

For Microsoft 365 groups, _Group._\\* permissions grant the app access to the contents of the

group; for example, conversations, files, notes, and so on.

In some cases, an app might need extra permissions to read some group properties like `member`

and `memberOf` . For example, if a group has one or more service principals as members, the app

also needs permissions to read service principals, otherwise Microsoft Graph returns an error or

limited information. To read the full information, the app also needs permissions in the

organization to read service principals. For more information, see Limited information returned

for inaccessible member objects.

_Group._\\* permissions are used to control access to Microsoft Teams resources and APIs.

Personal Microsoft accounts are not supported.

_Group._\\* permissions are also used to control access to Microsoft Planner resources and APIs.

Only delegated permissions are supported for Microsoft Planner APIs; application permissions

are not supported. Personal Microsoft accounts are not supported.

**Group.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

62a82d76-70ea-41e2-9197-

370581804d09

4e46008b-f24c-477d-8fff-

7bb4ec7aafe0

DisplayText

Read and write all groups

Read and write all groups

Description

Allows the app to create groups, read all

group properties and memberships,

update group properties and

memberships, and delete groups. Also

allows the app to read and write

conversations. All of these operations

can be performed by the app without a

signed-in user.

Allows the app to create groups

and read all group properties and

memberships on behalf of the

signed-in user. Additionally allows

group owners to manage their

groups and allows group members

to update group content.

AdminConsentRequired

Yes

Yes

For Microsoft 365 groups, _Group._\\* permissions grant the app access to the contents of the

group; for example, conversations, files, notes, and so on.

In some cases, an app may need extra properties to update some group properties and

relationships like `member` and `memberOf` . For example, to add a servicePrincipal object as a

member, the app also needs permissions to write the service principal, otherwise Microsoft

Graph returns an error. For more information, see Limited information returned for inaccessible

member objects.

_Group._\\* permissions are used to control access to Microsoft Teams resources and APIs.

Personal Microsoft accounts are not supported.

_Group._\\* permissions are also used to control access to Microsoft Planner resources and APIs.

Only delegated permissions are supported for Microsoft Planner APIs; application permissions

are not supported. Personal Microsoft accounts are not supported.

**Group.ReadWrite.All**

ﾉ

**Expand table**

**GroupMember.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

98830695-27a2-44f7-8c18-

0c3ebc9698f6

bc024368-1153-4739-b217-

4326f2e966d0

DisplayText

Read all group memberships

Read group memberships

Description

Allows the app to read

memberships and basic group

properties for all groups without a

signed-in user.

Allows the app to list groups, read basic

group properties and read membership

of all groups the signed-in user has

access to.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

dbaae8cf-10b5-4b86-a4a1-

f871c94c6695

f81125ac-d3b7-4573-a3b2-

7099cc39df9e

DisplayText

Read and write all group memberships

Read and write group memberships

Description

Allows the app to list groups, read

basic properties, read and update the

membership of the groups this app has

access to without a signed-in user.

Group properties and owners cannot

be updated and groups cannot be

deleted.

Allows the app to list groups, read

basic properties, read and update the

membership of the groups the

signed-in user has access to. Group

properties and owners cannot be

updated and groups cannot be

deleted.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f3c4f514-c65a-43f5-bfce-

1735872258dd

2eb2bc92-94ef-4c6b-b4ab-

2a09bc975e0e

**GroupMember.ReadWrite.All**

ﾉ

**Expand table**

**GroupSettings.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read all group settings

Read all group settings that user can

access

Description

Allows the app to read a list of

tenant-level or group-specific group

settings objects, without a signed-in

user.

Allows the app to read a list of tenant-

level or group-specific group settings

objects, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

546168c3-1183-4281-9491-

fafb24dea37e

c1691a6d-99e2-4cfa-b4b5-9e4d67dc0f36

DisplayText

Read and write all group settings

Read and write all group settings that user

can access

Description

Allows the app to create, read,

update, and delete on the list of

tenant-level or group-specific

group settings objects, without a

signed-in user.

Allows the app to create, read, update,

and delete on the list of tenant-level or

group-specific group settings objects that

you have access to in the organization, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

5183ed5d-b7f8-4e9a-915e-dafb46b9cb62

74b4ff32-4917-4536-a66d-

38a4861e6220

DisplayText

Read all scenario health monitoring alert

Read all scenario health

monitoring alerts

**GroupSettings.ReadWrite.All**

ﾉ

**Expand table**

**HealthMonitoringAlert.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read all scenario health

monitoring alerts, without a signed-in user.

Allows the app to read all

scenario health monitoring alerts

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ac29eb50-f2f9-4518-a117-

4bef18e84c7d

b7c60f27-2195-4d5f-96a7-

6b98bdfd9664

DisplayText

Read and write all scenario

monitoring alerts

Read and write all scenario monitoring

alerts

Description

Allows the app to read and write all

scenario monitoring alerts, without a

signed-in user.

Allows the app to read and write all

scenario monitoring alerts, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

bb424d73-e898-4c97-9d42-688c32810003

fb873030-8626-47e6-96ff-

8a5bff3b725f

DisplayText

Read all scenario health monitoring alert

configurations

Read all scenario health

monitoring alert configurations

Description

Allows the app to read all scenario health

monitoring alert configurations, without a

signed-in user.

Allows the app to read all

scenario health monitoring alert

configurations

AdminConsentRequired

Yes

Yes

**HealthMonitoringAlert.ReadWrite.All**

ﾉ

**Expand table**

**HealthMonitoringAlertConfig.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

432e76f0-8af6-4315-a853-

66ab9538f480

b3e5ebc6-1c23-4337-8286-

3f27165addb4

DisplayText

Read and write all scenario

monitoring alerts

Read and write all scenario monitoring

alert configurations.

Description

Allows the app to read and write

all scenario monitoring alerts,

without a signed-in user.

Allows the app to read and write all

scenario monitoring alert configurations,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e321f0bb-e7f7-481e-bb28-

e3b0b32d4bd0

43781733-b5a7-4d1b-98f4-

e8edff23e1a9

DisplayText

Read identity providers

Read identity providers

Description

Allows the app to read your

organization's identity (authentication)

providers' properties without a signed

in user.

Allows the app to read your

organization's identity

(authentication) providers' properties

on behalf of the user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

90db2b9a-d928-4d33-a4dd-

8442ae3d41e4

f13ce604-1677-429f-90bd-

8a10b9f01325

**HealthMonitoringAlertConfig.ReadWrite.All**

ﾉ

**Expand table**

**IdentityProvider.Read.All**

ﾉ

**Expand table**

**IdentityProvider.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write identity providers

Read and write identity providers

Description

Allows the app to read and write your

organization's identity (authentication)

providers' properties without a signed

in user.

Allows the app to read and write your

organization's identity

(authentication) providers' properties

on behalf of the user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

6e472fd1-ad78-48da-a0f0-

97ab2c6b769e

8f6a01e7-0391-4ee5-aa22-

a3af122cef27

DisplayText

Read all identity risk event

information

Read identity risk event information

Description

Allows the app to read the identity

risk event information for your

organization without a signed in

user.

Allows the app to read identity risk

event information for all users in your

organization on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

db06fb33-1953-4b7b-a2ac-

f1e2c854f7ae

9e4862a5-b68f-479e-848a-

4e07e25c9916

DisplayText

Read and write all risk detection

information

Read and write risk event information

Description

Allows the app to read and update

identity risk detection information

for your organization without a

Allows the app to read and update

identity risk event information for all

users in your organization on behalf of

**IdentityRiskEvent.Read.All**

ﾉ

**Expand table**

**IdentityRiskEvent.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

signed-in user. Update operations

include confirming risk event

detections.

the signed-in user. Update operations

include confirming risk event

detections.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

4aadfb66-d49a-414a-a883-

d8c240b6fa33

3215c57f-3faa-4295-95c2-

6f14a5bc6124

DisplayText

Read all risky agents information

Read risky agents information

Description

Allows the app to read the risky

agents information in your

organization without a signed-in user.

Allows the app to read risky agents

information in your organization, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

dca4e4fd-a7cf-4e6f-86d1-

d1ec094d766e

d343bdeb-db6a-4e06-97da-9dafc2d61c60

DisplayText

Read and write risky agents

information

Read and write risky agents information

Description

Allows the app to read and

update risky agents

information in your

organization without a signed-

in user.

Allows the app to read and update identity

risky agents information for all agents in your

organization on behalf of the signed-in user.

Update operations include dismissing risky

agents.

AdminConsentRequired

Yes

Yes

**IdentityRiskyAgent.Read.All**

ﾉ

**Expand table**

**IdentityRiskyAgent.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

607c7344-0eed-41e5-823a-

9695ebe1b7b0

ea5c4ab0-5a73-4f35-8272-

5d5337884e5d

DisplayText

Read all identity risky service

principal information

Read all identity risky service principal

information

Description

Allows the app to read all risky

service principal information for

your organization, without a signed-

in user.

Allows the app to read all identity risky

service principal information for your

organization, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

cb8d6980-6bcb-4507-afec-

ed6de3a2d798

bb6f654c-d7fd-4ae3-85c3-fc380934f515

DisplayText

Read and write all identity

risky service principal

information

Read and write all identity risky service

principal information

Description

Allows the app to read and

update identity risky service

principal for your

organization, without a

signed-in user.

Allows the app to read and update identity

risky service principal information for all

service principals in your organization, on

behalf of the signed-in user. Update

operations include dismissing risky service

principals.

AdminConsentRequired

Yes

Yes

**IdentityRiskyServicePrincipal.Read.All**

ﾉ

**Expand table**

**IdentityRiskyServicePrincipal.ReadWrite.All**

ﾉ

**Expand table**

**IdentityRiskyUser.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

dc5007c0-2d7d-4c42-879c-

2dab87571379

d04bb851-cb7c-4146-97c7-

ca3e71baf56c

DisplayText

Read all identity risky user

information

Read identity risky user information

Description

Allows the app to read the identity

risky user information for your

organization without a signed in

user.

Allows the app to read identity risky

user information for all users in your

organization on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

656f6061-f9fe-4807-9708-

6a2e0934df76

e0a7cdbb-08b0-4697-8264-

0069786e9674

DisplayText

Read and write all risky user

information

Read and write risky user information

Description

Allows the app to read and update

identity risky user information for

your organization without a signed-

in user. Update operations include

dismissing risky users.

Allows the app to read and update

identity risky user information for all

users in your organization on behalf of

the signed-in user. Update operations

include dismissing risky users.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

1b0c317f-dd31-4305-9932-

259a8b6e8099

2903d63d-4611-4d43-99ce-

a33f3f52e343

DisplayText

Read all identity user flows

Read all identity user flows

**IdentityRiskyUser.ReadWrite.All**

ﾉ

**Expand table**

**IdentityUserFlow.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read your

organization's user flows, without a

signed-in user.

Allows the app to read your

organization's user flows, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

65319a09-a2be-469d-8782-

f6b07debf789

281892cc-4dbf-4e3a-b6cc-

b21029bb4e82

DisplayText

Read and write all identity user flows

Read and write all identity user flows

Description

Allows the app to read or write your

organization's user flows, without a

signed-in user.

Allows the app to read or write your

organization's user flows, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

652390e4-393a-48de-9484-05f9b1212954

DisplayText

-

Read and write access to mailboxes via IMAP.

Description

-

Allows the app to have the same access to mailboxes as the

signed-in user via IMAP protocol.

AdminConsentRequired

-

No

![](./assets/output_267_1.png)![](./assets/output_267_2.png)

The _IMAP.AccessAsUser.All_ delegated permission is available for consent in personal

Microsoft accounts.

**IdentityUserFlow.ReadWrite.All**

ﾉ

**Expand table**

**IMAP.AccessAsUser.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

7ab52c2f-a2ee-4d98-9ebc-

725e3934aae2

d19c0de5-7ecb-4aba-b090-

da35ebcd5425

DisplayText

View data connector definitions

View data connector definitions

Description

Allows the app to read data

connectors without a signed-in user.

Allows the app to read data connectors

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

eda0971c-482e-4345-b28f-

69c309cb8a34

5ce933ac-3997-4280-aed0-

cc072e5c062a

DisplayText

Manage data connector definitions

Manage data connector definitions

Description

Allows the app to read and write

data connectors without a signed-in

user.

Allows the app to read and write data

connectors on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

9334c44b-a7c6-4350-8036-

6bf8e02b4c1f

fc47391d-ab2c-410f-9059-

5600f7af660d

DisplayText

Upload files to a data connector

Upload files to a data connector

**IndustryData-DataConnector.Read.All**

ﾉ

**Expand table**

**IndustryData-DataConnector.ReadWrite.All**

ﾉ

**Expand table**

**IndustryData-DataConnector.Upload**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to upload data files

to a data connector without a

signed-in user.

Allows the app to upload data files to a

data connector on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

305f6ba2-049a-4b1b-88bb-

fe7e08758a00

cb0774da-a605-42af-959c-

32f438fb38f4

DisplayText

View inbound flow definitions

View inbound flow definitions

Description

Allows the app to read inbound data

flows without a signed-in user.

Allows the app to read inbound data

flows on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e688c61f-d4c6-4d64-a197-

3bcf6ba1d6ad

97044676-2cec-40ee-bd70-

38df444c9e70

DisplayText

Manage inbound flow definitions

Manage inbound flow definitions

Description

Allows the app to read and write

inbound data flows without a

signed-in user.

Allows the app to read and write

inbound data flows on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**IndustryData-InboundFlow.Read.All**

ﾉ

**Expand table**

**IndustryData-InboundFlow.ReadWrite.All**

ﾉ

**Expand table**

**IndustryData-OutboundFlow.Read.All**

**Category**

**Application**

**Delegated**

Identifier

61d0354c-5d88-483c-b974-

a37ec3395a2c

4741a003-8952-4be4-9217-

33a0ac327122

DisplayText

View outbound flow definitions

View outbound flow definitions

Description

Allows the app to read outbound

data flows without a signed-in user.

Allows the app to read outbound data

flows on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

24a65b4a-e501-47e2-8849-

d679517887f0

aeb68e0b-e562-4a1f-b6dd-

3484ad0cbb4b

DisplayText

Manage outbound flow definitions

Manage outbound flow definitions

Description

Allows the app to read and write

outbound data flows without a

signed-in user.

Allows the app to read and write

outbound data flows on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

6ee891c3-74a4-4148-8463-

0c834375dfaf

a3f96ffe-cb84-40a8-ac85-

582d7ef97c2a

DisplayText

View reference definitions

View reference definitions

Description

Allows the app to read reference

definitions without a signed-in user.

Allows the app to read reference

definitions on behalf of the signed-in

user.

ﾉ

**Expand table**

**IndustryData-OutboundFlow.ReadWrite.All**

ﾉ

**Expand table**

**IndustryData-ReferenceDefinition.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

bda16293-63d3-45b7-b16b-

833841d27d56

a757d430-be6d-430f-af57-

28aabe79d247

DisplayText

Manage reference definitions

Manage reference definitions

Description

Allows the app to read and write

reference definitions without a

signed-in user.

Allows the app to read and write

reference definitions on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f6f5d10b-3024-4d1d-b674-

aae4df4a1a73

92685235-50c4-4702-b2c8-

36043db6fa79

DisplayText

View current and previous runs

View current and previous runs

Description

Allows the app to read current and

previous IndustryData runs without a

signed-in user.

Allows the app to read current and

previous IndustryData runs on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**IndustryData-ReferenceDefinition.ReadWrite.All**

ﾉ

**Expand table**

**IndustryData-Run.Read.All**

ﾉ

**Expand table**

**IndustryData-Run.Start**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

7e429772-5b5e-47c0-8fd6-

7279294c8033

f03a6d0e-0989-460f-80b2-

e57c8561763e

DisplayText

View and start runs

View and start runs

Description

Allows the app to view and start

IndustryData runs without a signed-

in user.

Allows the app to view and start

IndustryData runs on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

bc167a60-39fe-4865-8b44-

78400fc6ed03

49b7016c-89ae-41e7-bd6f-

b7170c5490bf

DisplayText

View source system definitions

View source system definitions

Description

Allows the app to read source

system definitions without a signed-

in user.

Allows the app to read source system

definitions on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7d866958-e06e-4dd6-91c6-

a086b3f5cfeb

9599f005-05d6-4ea7-b1b1-

4929768af5d0

DisplayText

Manage source system definitions

Manage source system definitions

Description

Allows the app to read and write

source system definitions without a

signed-in user.

Allows the app to read and write source

system definitions on behalf of the

signed-in user.

**IndustryData-SourceSystem.Read.All**

ﾉ

**Expand table**

**IndustryData-SourceSystem.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7c55c952-b095-4c23-a522-

022bce4cc1e3

c9d51f28-8ccd-42b2-a836-

fd8fe9ebf2ae

DisplayText

Read time period definitions

Read time period definitions

Description

Allows the app to read time period

definitions without a signed-in user.

Allows the app to read time period

definitions on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7afa7744-a782-4a32-b8c2-

e3db637e8de7

b6d56528-3032-4f9d-830f-

5a24a25e6661

DisplayText

Manage time period definitions

Manage time period definitions

Description

Allows the app to read and write

time period definitions without a

signed-in user.

Allows the app to read and write time

period definitions on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**IndustryData-TimePeriod.Read.All**

ﾉ

**Expand table**

**IndustryData-TimePeriod.ReadWrite.All**

ﾉ

**Expand table**

**IndustryData.ReadBasic.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

4f5ac95f-62fd-472c-b60f-

125d24ca0bc5

60382b96-1f5e-46ea-a544-

0407e489e588

DisplayText

View basic service and resource

information

Read basic Industry Data service and

resource definitions

Description

Allows the app to read basic

service and resource information

without a signed-in user.

Allows the app to read basic Industry

Data service and resource information on

behalf of the signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

-

12f4bffb-b598-413c-984b-db99728f8b54

DisplayText

-

Read configurations for protecting organizational data

applicable to the user

Description

-

Allows the app to read the configurations applicable to the

signed-in user for protecting organizational data, on behalf of

the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

14f49b9f-4bf2-4d24-b80e-b27ec58409bd

-

DisplayText

Read all configurations for protecting organizational data

applicable to users

-

Description

Allows the app to read all configurations applicable to users for

protecting organizational data, without a signed-in user.

-

**InformationProtectionConfig.Read**

ﾉ

**Expand table**

**InformationProtectionConfig.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

cbe6c7e4-09aa-4b8d-b3c3-2dbb59af4b54

-

DisplayText

Sign digests for data

-

Description

Allows an app to sign digests for data without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

287bd98c-e865-4e8c-bade-1a85523195b9

-

DisplayText

Create protected content

-

Description

Allows the app to create protected content without a signed-in

user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

4ad84827-5578-4e18-ad7a-86530b12f884

DisplayText

-

Read user sensitivity labels and label policies.

**InformationProtectionContent.Sign.All**

ﾉ

**Expand table**

**InformationProtectionContent.Write.All**

ﾉ

**Expand table**

**InformationProtectionPolicy.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Allows an app to read information protection sensitivity labels

and label policy settings, on behalf of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

19da66cb-0fb0-4390-b071-ebc76a349482

-

DisplayText

Read all published labels and label policies for an organization.

-

Description

Allows an app to read published sensitivity labels and label policy

settings for the entire organization or a specific user, without a

signed in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

34cbd96c-d824-4755-90d3-

1008ef47efc1

7d249730-51a3-4180-8ec1-

214f144f1bff

DisplayText

Read all user metrics insights

Read user metrics insights

Description

Allows an app to read all user metrics

insights, such as daily and monthly

active users, without a signed-in user.

Allows an app to read user metrics

insights, such as daily and monthly

active users, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**InformationProtectionPolicy.Read.All**

ﾉ

**Expand table**

**Insights-UserMetric.Read.All**

ﾉ

**Expand table**

**LearningAssignedCourse.Read**

**Category**

**Application**

**Delegated**

Identifier

-

ac08cdae-e845-41db-adf9-5899a0ec9ef6

DisplayText

-

Read user's assignments

Description

-

Allows the app to read data for the learner's assignments in the

organization's directory, on behalf of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

535e6066-2894-49ef-ab33-e2c6d064bb81

-

DisplayText

Read all assignments

-

Description

Allows the app to read data for all assignments in the

organization's directory, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

236c1cbd-1187-427f-b0f5-b1852454973b

-

DisplayText

Read and write all assignments

-

Description

Allows the app to create, update, read and delete all assignments

in the organization's directory, without a signed-in user.

-

AdminConsentRequired

Yes

-

ﾉ

**Expand table**

**LearningAssignedCourse.Read.All**

ﾉ

**Expand table**

**LearningAssignedCourse.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

8740813e-d8aa-4204-860e-

2a0f8f84dbc8

ea4c1fd9-6a9f-4432-8e5d-

86e06cc0da77

DisplayText

Read all learning content

Read learning content

Description

Allows the app to read all learning

content in the organization's

directory, without a signed-in user.

Allows the app to read learning

content in the organization's directory,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

444d6fcb-b738-41e5-b103-

ac4f2a2628a3

53cec1c4-a65f-4981-9dc1-

ad75dbf1c077

DisplayText

Manage all learning content

Manage learning content

Description

Allows the app to manage all learning

content in the organization's

directory, without a signed-in user.

Allows the app to manage learning

content in the organization's directory,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

dd8ce36f-9245-45ea-a99e-8ac398c22861

DisplayText

-

Read learning provider

**LearningContent.Read.All**

ﾉ

**Expand table**

**LearningContent.ReadWrite.All**

ﾉ

**Expand table**

**LearningProvider.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Allows the app to read data for the learning provider in the

organization's directory, on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

40c2eb57-abaf-49f5-9331-e90fd01f7130

DisplayText

-

Manage learning provider

Description

-

Allows the app to create, update, read, and delete data for the

learning provider in the organization's directory, on behalf of the

signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

f6403ef7-4a96-47be-a190-69ba274c3f11

DisplayText

-

Read user's self-initiated courses

Description

-

Allows the app to read data for the learner's self-initiated

courses in the organization's directory, on behalf of the signed-

in user.

AdminConsentRequired

-

No

**LearningProvider.ReadWrite**

ﾉ

**Expand table**

**LearningSelfInitiatedCourse.Read**

ﾉ

**Expand table**

**LearningSelfInitiatedCourse.Read.All**

**Category**

**Application**

**Delegated**

Identifier

467524fc-ed22-4356-a910-af61191e3503

-

DisplayText

Read all self-initiated courses

-

Description

Allows the app to read data for all self-initiated courses in the

organization's directory, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

7654ed61-8965-4025-846a-0856ec02b5b0

-

DisplayText

Read and write all self-initiated courses

-

Description

Allows the app to create, update, read and delete all self-initiated

courses in the organization's directory, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

e2f98668-2877-4f38-a2f4-

8202e0717aa1

f395577a-0960-456b-979f-

7228de0c5996

DisplayText

Read all license assignments.

Read all license assignments.

Description

Allows an app to read license

assignments for users and groups,

without a signed-in user.

Allows an app to read license

assignments for users and groups, on

behalf of the signed-in user.

AdminConsentRequired

Yes

No

ﾉ

**Expand table**

**LearningSelfInitiatedCourse.ReadWrite.All**

ﾉ

**Expand table**

**LicenseAssignment.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

5facf0c1-8979-4e95-abcf-

ff3d079771c0

f55016cc-149c-447e-8f21-

7cf3ec1d6350

DisplayText

Manage all license assignments

Manage all license assignments

Description

Allows an app to manage license

assignments for users and groups,

without a signed-in user.

Allows an app to manage license

assignments for users and groups, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2cb19e7d-9012-40bf-9a22-

69fc776af8b0

2973a298-1d69-4f87-8d30-

7025f0ec19d7

DisplayText

Read all Lifecycle workflows custom

task extensionss

Read all Lifecycle workflows custom

task extensions

Description

Allows the app to read all Lifecycle

workflows custom task extensions

without a signed-in user.

Allows the app to read all Lifecycle

workflows custom task extensions on

behalf of a signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

3351c766-bacc-4d93-94fa-

f2c8b1986ee7

ef6bafb1-3019-4a22-a332-

103aff92225f

**LicenseAssignment.ReadWrite.All**

ﾉ

**Expand table**

**LifecycleWorkflows-CustomExt.Read.All**

ﾉ

**Expand table**

**LifecycleWorkflows-CustomExt.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write all Lifecycle workflows

custom task extensions

Read and write all Lifecycle workflows

custom task extensions

Description

Allows the app to create, update, list,

read and delete all Lifecycle workflows

custom task extensions without a

signed-in user.

Allows the app to create, update, list,

read and delete all Lifecycle workflows

custom task extensions on behalf of a

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

fe615156-48b5-4c83-b613-

e6e31a43c446

4d3d7f81-163f-426a-8432-

5638d2e82083

DisplayText

Read all Lifecycle workflows reports

Read all Lifecycle workflows reports

Description

Allows the app to read all Lifecycle

workflows reports without a signed-

in user.

Allows the app to read all Lifecycle

workflows reports on behalf of a

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

3a87a643-13d2-47aa-8d6a-

b0a8377cb03b

df1c25b3-072c-45cd-8403-

c63441e4cca1

DisplayText

Run workflows on-demand in

Lifecycle workflows

Run workflows on-demand in Lifecycle

workflows

Description

Allows the app run workflows on-

demand without a signed-in user.

Allows the app to run workflows on-

demand on behalf of a signed-in user.

AdminConsentRequired

Yes

Yes

**LifecycleWorkflows-Reports.Read.All**

ﾉ

**Expand table**

**LifecycleWorkflows-Workflow.Activate**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

03b0ad3e-fc2b-4ef1-b0ff-

252e865cb608

7fabe5bd-2e47-4e61-b924-

327117024e18

DisplayText

Read all workflows in Lifecycle

workflows

Read all workflows in Lifecycle

workflows

Description

Allows the app to list and read all

workflows and tasks without a

signed-in user.

Allows the app to list and read all

workflows and tasks on behalf of a

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

021ea6db-c06b-45c6-8c9c-

c1cd9a37a483

789c445d-433c-4575-a1fc-

367a58a1bd4a

DisplayText

List all workflows in Lifecycle

workflows

List all workflows in Lifecycle workflows

Description

Allows the app to list all workflows

without a signed-in user.

Allows the app to list all workflows on

behalf of a signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

94c88098-1d9d-4c42-a356-

29e49f0c-a053-4cc5-a4b1-

**LifecycleWorkflows-Workflow.Read.All**

ﾉ

**Expand table**

**LifecycleWorkflows-Workflow.ReadBasic.All**

ﾉ

**Expand table**

**LifecycleWorkflows-Workflow.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

4d5a95312554

7da0c8c1e643

DisplayText

Read and write all workflows in

Lifecycle workflows

Read and write all workflows in

Lifecycle workflows

Description

Allows the app to create, update, list,

read and delete all workflows and

tasks in lifecycle workflows without a

signed-in user.

Allows the app to create, update, list,

read and delete all workflows and

tasks in lifecycle workflows on behalf

of a signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7c67316a-232a-4b84-be22-

cea2c0906404

9bcb9916-765a-42af-bf77-

02282e26b01a

DisplayText

Read all lifecycle workflows resources

Read all lifecycle workflows resources

Description

Allows the app to list and read all

workflows, tasks and related lifecycle

workflows resources without a

signed-in user.

Allows the app to list and read all

workflows, tasks and related lifecycle

workflows resources on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

5c505cf4-8424-4b8e-aa14-

ee06e3bb23e3

84b9d731-7db8-4454-8c90-

fd9e95350179

DisplayText

Read and write all lifecycle workflows

resources

Read and write all lifecycle workflows

resources

Description

Allows the app to create, update, list,

read and delete all workflows, tasks

Allows the app to create, update, list,

read and delete all workflows, tasks

**LifecycleWorkflows.Read.All**

ﾉ

**Expand table**

**LifecycleWorkflows.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

and related lifecycle workflows

resources without a signed-in user.

and related lifecycle workflows

resources on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

de4e4161-a10a-4dfd-809c-

e328d89aefeb

d6d361b3-211a-4191-9fa7-

15f72de4aac4

DisplayText

Access selected ListItems without a

signed in user.

Access selected ListItems, on behalf of

the signed-in user

Description

Allow the application to access a

subset of listitems without a signed in

user. The specific listitems and the

permissions granted will be

configured in SharePoint Online.

Allow the application to access a

subset of listitems on behalf of the

signed in user. The specific listitems

and the permissions granted will be

configured in SharePoint Online.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

23c5a9bd-d900-4ecf-be26-

a0689755d9e5

033b51ee-d6fa-4add-b627-

ee680c7212b5

DisplayText

Access selected Lists without a signed

in user.

Access selected Lists, on behalf of the

signed-in user

Description

Allow the application to access a

subset of lists without a signed in

user. The specific lists and the

permissions granted will be

configured in SharePoint Online.

Allow the application to access a

subset of lists on behalf of the signed

in user. The specific lists and the

permissions granted will be configured

in SharePoint Online.

**ListItems.SelectedOperations.Selected**

ﾉ

**Expand table**

**Lists.SelectedOperations.Selected**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

f3af82f6-18e0-4a41-8dc8-a03c11854a8d

DisplayText

-

Read and write the user's mail, including modifying existing

non-draft mails

Description

-

Allows the app to create, read, update, and delete email,

including contents of non-draft emails in user mailboxes, on

behalf of the signed-in user. Does not include permission to

send mail.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

e118f1da-5c1c-46cf-bff6-8858d786f46f

-

DisplayText

Read and write mail in all mailboxes, including modifying existing

non-draft mails

-

Description

Allows the app to create, read, update, and delete all email,

including contents of non-draft emails in user mailboxes, without

a signed-in user. Does not include permission to send mail.

-

AdminConsentRequired

Yes

-

**Mail-Advanced.ReadWrite**

ﾉ

**Expand table**

**Mail-Advanced.ReadWrite.All**

ﾉ

**Expand table**

**Mail-Advanced.ReadWrite.Shared**

**Category**

**Application**

**Delegated**

Identifier

-

bebf0bb6-2ff3-4295-a17d-f3561da294fb

DisplayText

-

Read and write all mail the user can access, including modifying

existing non-draft mails

Description

-

Allows the app to create, read, update, and delete mail including

contents of non-draft emails for all mails a user has permission

to access, on behalf of the signed-in user. This includes their

own and shared mail. Does not include permission to send mail.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

810c84a8-4a9e-49e6-bf7d-12d183f40d01

570282fd-fa5c-430d-a7fd-

fc8dc98a9dca

DisplayText

Read mail in all mailboxes

Read user mail

Description

Allows the app to read mail in all

mailboxes without a signed-in user.

Allows the app to read the

signed-in user's mailbox.

AdminConsentRequired

Yes

No

![](./assets/output_287_1.png)![](./assets/output_287_2.png)

The _Mail.Read_ delegated permission is available for consent in personal Microsoft accounts.

Administrators can configure application access policy to limit app access to _specific_ mailboxes

and not to all the mailboxes in the organization, even if the app has been granted the

_Mail.Read_ application permission.

_Mail.Read_ is valid valid for both Microsoft accounts and work or school accounts.

ﾉ

**Expand table**

**Mail.Read**

ﾉ

**Expand table**

**Mail.Read.Shared**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

7b9103a5-4610-446b-9670-80643382c1fa

DisplayText

-

Read user and shared mail

Description

-

Allows the app to read mail a user can access, including their

own and shared mail.

AdminConsentRequired

-

No

_Mail.Read.Shared_ is only valid for work or school accounts.

**Category**

**Application**

**Delegated**

Identifier

6be147d2-ea4f-4b5a-a3fa-3eab6f3c140a

a4b8392a-d8d1-4954-a029-

8e668a39a170

DisplayText

Read basic mail in all mailboxes

Read user basic mail

Description

Allows the app to read basic mail

properties in all mailboxes without a

signed-in user. Includes all properties

except body, previewBody, attachments

and any extended properties.

Allows the app to read email in

the signed-in user's mailbox

except body, previewBody,

attachments and any extended

properties.

AdminConsentRequired

Yes

No

![](./assets/output_288_1.png)![](./assets/output_288_2.png)

The _Mail.ReadBasic_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

693c5e45-0940-467d-9b8a-1022fb9d42ef

-

DisplayText

Read basic mail in all mailboxes

-

**Mail.ReadBasic**

ﾉ

**Expand table**

**Mail.ReadBasic.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read basic mail properties in all mailboxes

without a signed-in user. Includes all properties except body,

previewBody, attachments and any extended properties.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

b11fa0e7-fdb7-4dc9-b1f1-59facd463480

DisplayText

-

Read user and shared basic mail

Description

-

Allows the app to read mail the signed-in user can access,

including their own and shared mail, except for body,

bodyPreview, uniqueBody, attachments, extensions, and any

extended properties.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

e2a3a72e-5f79-4c64-b1b1-

878b674786c9

024d486e-b451-40bb-833d-

3e66d98c5c73

DisplayText

Read and write mail in all mailboxes

Read and write access to user mail

Description

Allows the app to create, read, update,

and delete mail in all mailboxes without

a signed-in user. Does not include

permission to send mail.

Allows the app to create, read,

update, and delete email in user

mailboxes. Does not include

permission to send mail.

AdminConsentRequired

Yes

No

**Mail.ReadBasic.Shared**

ﾉ

**Expand table**

**Mail.ReadWrite**

ﾉ

**Expand table**

![](./assets/output_290_1.png)![](./assets/output_290_2.png)

The _Mail.ReadWrite_ delegated permission is available for consent in personal Microsoft

accounts.

Administrators can configure application access policy to limit app access to _specific_ mailboxes

and not to all the mailboxes in the organization, even if the app has been granted the

_Mail.ReadWrite_ application permission.

**Category**

**Application**

**Delegated**

Identifier

-

5df07973-7d5d-46ed-9847-1271055cbd51

DisplayText

-

Read and write user and shared mail

Description

-

Allows the app to create, read, update, and delete mail a user

has permission to access, including their own and shared mail.

Does not include permission to send mail.

AdminConsentRequired

-

No

_Mail.ReadWrite.Shared_ is only valid for work or school accounts.

**Category**

**Application**

**Delegated**

Identifier

b633e1c5-b582-4048-a93e-

9f11b44c7e96

e383f46e-2787-4529-855e-

0e479a3ffac0

DisplayText

Send mail as any user

Send mail as a user

Description

Allows the app to send mail as any user

without a signed-in user.

Allows the app to send mail as

users in the organization.

AdminConsentRequired

Yes

No

![](./assets/output_290_3.png)![](./assets/output_290_4.png)

The _Mail.Send_ delegated permission is available for consent in personal Microsoft accounts.

**Mail.ReadWrite.Shared**

ﾉ

**Expand table**

**Mail.Send**

ﾉ

**Expand table**

Administrators can configure application access policy to limit app access to _specific_ mailboxes

and not to all the mailboxes in the organization, even if the app has been granted the

_Mail.Send_ application permission.

_Mail.Send_ is valid valid for both Microsoft accounts and work or school accounts.

With the _Mail.Send_ permission, an app can send mail and save a copy to the user's Sent Items

folder, even if the app isn't granted the _Mail.ReadWrite_ or _Mail.ReadWrite.Shared_ permission.

**Category**

**Application**

**Delegated**

Identifier

-

a367ab51-6b49-43bf-a716-a1fb06d2a174

DisplayText

-

Send mail on behalf of others

Description

-

Allows the app to send mail as the signed-in user, including

sending on-behalf of others.

AdminConsentRequired

-

No

_Mail.Send.Shared_ is only valid for work or school accounts.

With the _Mail.Send.Shared_ permission, an app can send mail and save a copy to the user's Sent

Items folder, even if the app isn't granted the _Mail.ReadWrite_ or _Mail.ReadWrite.Shared_

permission.

**Category**

**Application**

**Delegated**

Identifier

27d9d776-f4d2-426d-80ad-

5f22f2b01b0a

dce2e6fc-0f4b-40da-94e2-14b4477f3d92

DisplayText

Read all users' UserConfiguration

objects

Read user's UserConfiguration objects

Description

Allows the app to read all users'

UserConfiguration objects.

Allows the app to read user's

UserConfiguration objects, on behalf of the

**Mail.Send.Shared**

ﾉ

**Expand table**

**MailboxConfigItem.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

aa6d92d4-b25a-4640-aefe-

3e3231e5e736

7d461784-7715-4b09-9f90-

91a6d8722652

DisplayText

Read and write all users'

UserConfiguration objects

Read and write user's UserConfiguration

objects

Description

Allows the app to create, read,

update and delete all users'

UserConfiguration objects.

Allows the app to create, read, update

and delete user's UserConfiguration

objects, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

52dc2051-4958-4636-8f2a-281d39c6981c

DisplayText

-

Read a user's mailbox folders

Description

-

Allows the app to read the user's mailbox folders, on behalf of

the signed-in user.

AdminConsentRequired

-

No

**MailboxConfigItem.ReadWrite**

ﾉ

**Expand table**

**MailboxFolder.Read**

ﾉ

**Expand table**

**MailboxFolder.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

99280d24-a782-4793-93cc-0888549957f6

-

DisplayText

Read all the users' mailbox folders

-

Description

Allows the app to read all the users' mailbox folders, without

signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

077fde41-7e0b-4c5b-bcd1-e9d743a30c80

DisplayText

-

Read and write a user's mailbox folders

Description

-

Allows the app to read and write the user's mailbox folders, on

behalf of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

fef87b92-8391-4589-9da7-eb93dab7dc8a

-

DisplayText

Read and write all the users' mailbox folders

-

Description

Allows the app to read and write all the users' mailbox folders,

without signed-in user.

-

AdminConsentRequired

Yes

-

**MailboxFolder.ReadWrite**

ﾉ

**Expand table**

**MailboxFolder.ReadWrite.All**

ﾉ

**Expand table**

**MailboxItem.ImportExport**

**Category**

**Application**

**Delegated**

Identifier

-

df96e8a0-f4e1-4ecf-8d83-a429f822cbd6

DisplayText

-

Allows the app to perform backup and restore of mailbox items

Description

-

Allows the app to backup, restore, and modify mailbox items on

behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

76577085-e73d-4f1d-b26a-85fb33892327

-

DisplayText

Allows the app to perform backup and restore for all mailbox

items

-

Description

Allows the app to backup, restore, and modify all mailbox items

without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

82305458-296d-4edd-8b0b-74dd74c34526

DisplayText

-

Read a user's mailbox items

Description

-

Allows the app to read the user's mailbox items, on behalf of the

signed-in user.

AdminConsentRequired

-

No

ﾉ

**Expand table**

**MailboxItem.ImportExport.All**

ﾉ

**Expand table**

**MailboxItem.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

7d9f353d-a7bd-4fbb-822a-26d5dd39a3ce

-

DisplayText

Read all the users' mailbox items

-

Description

Allows the app to read all the users' mailbox items, without

signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

40f97065-369a-49f4-947c-6a255697ae91

87f447af-9fa4-4c32-9dfa-

4a57a73d18ce

DisplayText

Read all user mailbox settings

Read user mailbox settings

Description

Allows the app to read user's mailbox

settings without a signed-in user. Does

not include permission to send mail.

Allows the app to the read user's

mailbox settings. Does not include

permission to send mail.

AdminConsentRequired

Yes

No

![](./assets/output_295_1.png)![](./assets/output_295_2.png)

The _MailboxSettings.Read_ delegated permission is available for consent in personal

Microsoft accounts.

Administrators can configure application access policy to limit app access to _specific_ mailboxes

and not to all the mailboxes in the organization, even if the app has been granted the

_MailboxSettings.Read_ application permission.

_MailboxSettings.Read_ is valid valid for both Microsoft accounts and work or school accounts.

**MailboxItem.Read.All**

ﾉ

**Expand table**

**MailboxSettings.Read**

ﾉ

**Expand table**

**MailboxSettings.ReadWrite**

**Category**

**Application**

**Delegated**

Identifier

6931bccd-447a-43d1-b442-

00a195474933

818c620a-27a9-40bd-a6a5-

d96f7d610b4b

DisplayText

Read and write all user mailbox settings

Read and write user mailbox

settings

Description

Allows the app to create, read, update,

and delete user's mailbox settings

without a signed-in user. Does not

include permission to send mail.

Allows the app to create, read,

update, and delete user's mailbox

settings. Does not include

permission to send mail.

AdminConsentRequired

Yes

No

![](./assets/output_296_1.png)![](./assets/output_296_2.png)

The _MailboxSettings.ReadWrite_ delegated permission is available for consent in personal

Microsoft accounts.

Administrators can configure application access policy to limit app access to _specific_ mailboxes

and not to all the mailboxes in the organization, even if the app has been granted the

_MailboxSettings.ReadWrite_ application permission.

_MailboxSettings.ReadWrite_ is valid valid for both Microsoft accounts and work or school

accounts.

**Category**

**Application**

**Delegated**

Identifier

-

dc34164e-6c4a-41a0-be89-3ae2fbad7cd3

DisplayText

-

Read all managed tenant information

Description

-

Allows the app to read all managed tenant information on

behalf of the signed-in user.

AdminConsentRequired

-

Yes

ﾉ

**Expand table**

**ManagedTenants.Read.All**

ﾉ

**Expand table**

**ManagedTenants.ReadWrite.All**

**Category**

**Application**

**Delegated**

Identifier

-

b31fa710-c9b3-4d9e-8f5e-8036eecddab9

DisplayText

-

Read and write all managed tenant information

Description

-

Allows the app to read and write all managed tenant

information on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

658aa5d8-239f-45c4-aa12-

864f4fc7e490

f6a3db3e-f7e8-4ed2-a414-557c8c9830be

DisplayText

Read all hidden memberships

Read hidden memberships

Description

Allows the app to read the

memberships of hidden

groups and administrative

units without a signed-in user.

Allows the app to read the memberships of

hidden groups and administrative units on

behalf of the signed-in user, for those hidden

groups and administrative units that the

signed-in user has access to.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

4f994bc0-31bb-44bb-b480-

7a7c1be8c02e

526aa72a-5878-49fe-bf4e-

357973af9b06

DisplayText

Read all multi-tenant organization

details and tenants

Read multi-tenant organization details

and tenants

ﾉ

**Expand table**

**Member.Read.Hidden**

ﾉ

**Expand table**

**MultiTenantOrganization.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read all multi-

tenant organization details and

tenants, without a signed-in user.

Allows the app to read multi-tenant

organization details and tenants on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f9c2b2a7-3895-4b2e-80f6-

c924b456e50b

225db56b-15b2-4daa-acb3-

0eec2bbe4849

DisplayText

Read multi-tenant organization basic

details and active tenants

Read multi-tenant organization basic

details and active tenants

Description

Allows the app to read multi-tenant

organization basic details and active

tenants, without a signed-in user.

Allows the app to read multi-tenant

organization basic details and active

tenants on behalf of the signed-in

user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

920def01-ca61-4d2d-b3df-

105b46046a70

77af1528-84f3-4023-8d90-

d219cd433108

DisplayText

Read and write all multi-tenant

organization details and tenants

Read and write multi-tenant

organization details and tenants

Description

Allows the app to read and write all

multi-tenant organization details and

tenants, without a signed-in user.

Allows the app to read and write

multi-tenant organization details and

tenants on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**MultiTenantOrganization.ReadBasic.All**

ﾉ

**Expand table**

**MultiTenantOrganization.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

6daaff82-2880-496d-9d80-

57e8e31195e2

51ae584e-e736-4718-897b-

10af70f8e3cc

DisplayText

Read all configurations used for

mutual-TLS client authentication.

Read all configurations used for

mutual-TLS client authentication.

Description

Allows the app to read configuration

used for OAuth 2.0 mutual-TLS client

authentication, without a signed-in

user. This includes reading trusted

certificate authorities.

Allows the app to read configuration

used for OAuth 2.0 mutual-TLS client

authentication, on behalf of the

signed-in user. This includes reading

trusted certificate authorities.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

78bbf8cf-07d8-45ba-b0eb-

1a7b48efbcf1

a51115bc-f64f-498f-bcee-

00dcd28f4a03

DisplayText

Read and write all configurations

used for mutual-TLS client

authentication.

Read and write all configurations used

for mutual-TLS client authentication.

Description

Allows the app to read and update

configuration used for OAuth 2.0

mutual-TLS client authentication,

without a signed-in user. This

includes reading and updating

trusted certificate authorities.

Allows the app to read and update

configuration used for OAuth 2.0

mutual-TLS client authentication, on

behalf of the signed-in user. This

includes adding and updating trusted

certificate authorities.

AdminConsentRequired

Yes

Yes

**MutualTlsOauthConfiguration.Read.All**

ﾉ

**Expand table**

**MutualTlsOauthConfiguration.ReadWrite.All**

ﾉ

**Expand table**

**NetworkAccess-Reports.Read.All**

**Category**

**Application**

**Delegated**

Identifier

40049381-3cc1-42af-94ec-

5ce755db4b0d

b0c61509-cfc3-42bd-9bd4-

66d81785fee4

DisplayText

Read all network access reports

Read all network access reports

Description

Allows the app to read all network

access reports without a signed-in

user.

Allows the app to read all network

access reports on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e30060de-caa5-4331-99d3-

6ac6c966a9a4

2f7013e0-ab4e-447f-a5e1-

5d419950692d

DisplayText

Read all network access information

Read all network access

information

Description

Allows the app to read all network access

information and configuration settings

without a signed-in user.

Allows the app to read all network

access information on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

b10642fc-a6cf-4c46-87f9-

e1f96c2a18aa

ae2df9c5-f18d-4ec4-a51b-

bdeb807f177b

DisplayText

Read and write all network access

information

Read and write all network access

information

ﾉ

**Expand table**

**NetworkAccess.Read.All**

ﾉ

**Expand table**

**NetworkAccess.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read and write all

network access information and

configuration settings without a

signed-in user.

Allows the app to read and write all

network access information and

configuration settings on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

39ae4a24-1ef0-49e8-9d63-

2a66f5c39edd

4051c7fc-b429-4804-8d80-

8f1f8c24a6f7

DisplayText

Read properties of all branches for

network access

Read properties of branches for

network access

Description

Allows the app to read your

organization's network access

branches, without a signed-in user.

Allows the app to read your

organization's branches for network

access on behalf of the signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

8137102d-ec16-4191-aaf8-

7aeda8026183

b8a36cc2-b810-461a-baa4-

a7281e50bd5c

DisplayText

Read and write properties of all

branches for network access

Read and write properties of branches

for network access

Description

Allows the app to read and write

your organization's network access

branches, without a signed-in user.

Allows the app to read and write your

organization's branches for network

access on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**NetworkAccessBranch.Read.All**

ﾉ

**Expand table**

**NetworkAccessBranch.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

8a3d36bf-cb46-4bcc-bec9-

8d92829dab84

ba22922b-752c-446f-89d7-

a2d92398fceb

DisplayText

Read all security and routing

policies for network access

Read security and routing policies for

network access

Description

Allows the app to read your

organization's network access

policies, without a signed-in user.

Allows the app to read your

organization's security and routing

network access policies on behalf of the

signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

f0c341be-8348-4989-8e43-

660324294538

b1fbad0f-ef6e-42ed-8676-bca7fa3e7291

DisplayText

Read and write all security and

routing policies for network access

Read and write security and routing

policies for network access

Description

Allows the app to read and write

your organization's network access

policies, without a signed-in user.

Allows the app to read and write your

organization's security and routing

network access policies on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**NetworkAccessPolicy.Read.All**

ﾉ

**Expand table**

**NetworkAccessPolicy.ReadWrite.All**

ﾉ

**Expand table**

**Notes.Create**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

9d822255-d64d-4b7a-afdb-833b9a97ed02

DisplayText

-

Create user OneNote notebooks

Description

-

Allows the app to read the titles of OneNote notebooks and

sections and to create new pages, notebooks, and sections on

behalf of the signed-in user.

AdminConsentRequired

-

No

![](./assets/output_303_1.png)![](./assets/output_303_2.png)

The _Notes.Create_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

-

371361e4-b9e2-4a3f-8315-2a301a3b0a3d

DisplayText

-

Read user OneNote notebooks

Description

-

Allows the app to read OneNote notebooks on behalf of the

signed-in user.

AdminConsentRequired

-

No

![](./assets/output_303_3.png)![](./assets/output_303_4.png)

The _Notes.Read_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

3aeca27b-ee3a-4c2b-8ded-

80376e2134a4

dfabfca6-ee36-4db2-8208-

7a28381419b3

DisplayText

Read all OneNote notebooks

Read all OneNote notebooks that user

can access

**Notes.Read**

ﾉ

**Expand table**

**Notes.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read all the

OneNote notebooks in your

organization, without a signed-in

user.

Allows the app to read OneNote

notebooks that the signed-in user has

access to in the organization.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

-

615e26af-c38a-4150-ae3e-c3b0d4cb1d6a

DisplayText

-

Read and write user OneNote notebooks

Description

-

Allows the app to read, share, and modify OneNote notebooks

on behalf of the signed-in user.

AdminConsentRequired

-

No

![](./assets/output_304_1.png)![](./assets/output_304_2.png)

The _Notes.ReadWrite_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

0c458cef-11f3-48c2-a568-

c66751c238c0

64ac0503-b4fa-45d9-b544-

71a463f05da0

DisplayText

Read and write all OneNote

notebooks

Read and write all OneNote notebooks

that user can access

Description

Allows the app to read all the

OneNote notebooks in your

organization, without a signed-in

user.

Allows the app to read, share, and

modify OneNote notebooks that the

signed-in user has access to in the

organization.

**Notes.ReadWrite**

ﾉ

**Expand table**

**Notes.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

-

ed68249d-017c-4df5-9113-e684c7f8760b

DisplayText

-

Limited notebook access (deprecated)

Description

-

This is deprecated! Do not use! This permission no longer has

any effect. You can safely consent to it. No additional privileges

will be granted to the app.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

-

89497502-6e42-46a2-8cb2-427fd3df970a

DisplayText

-

Deliver and manage user notifications for this app

Description

-

Allows the app to deliver its notifications on behalf of signed-in

users. Also allows the app to read, update, and delete the user's

notification items for this app.

AdminConsentRequired

-

No

![](./assets/output_305_1.png)![](./assets/output_305_2.png)

The _Notifications.ReadWrite.CreatedByApp_ delegated permission is available for consent in

personal Microsoft accounts.

**Notes.ReadWrite.CreatedByApp**

ﾉ

**Expand table**

**Notifications.ReadWrite.CreatedByApp**

ﾉ

**Expand table**

**offline\_access**

**Category**

**Application**

**Delegated**

Identifier

-

7427e0e9-2fba-42fe-b0c0-848c9e6a8182

DisplayText

-

Maintain access to data you have given it access to

Description

-

Allows the app to see and update the data you gave it access to,

even when users are not currently using the app. This does not

give the app any additional permissions.

AdminConsentRequired

-

No

_offline\_access_ is an OpenID Connect (OIDC) scope.

You can use the OIDC scopes to specify artifacts that you want returned in Microsoft identity

platform authorization and token requests. The Microsoft identity platform v1.0 and v2.0

endpoints support OIDC scopes differently.

With the Microsoft identity platform v1.0 endpoint, only the _openid_ scope is used. You specify it

in the _scope_ parameter in an authorization request to return an ID token when you use the

OpenID Connect protocol to sign in a user to your app. For more information, see Microsoft

identity platform and OAuth 2.0 authorization code flow. To successfully return an ID token,

you must also make sure that the _User.Read_ permission is configured when you register your

app.

With the Microsoft identity platform v2.0 endpoint, you specify the _offline\_access_ scope in the

**scope** parameter to explicitly request a refresh token when using the OAuth 2.0 or OpenID

Connect protocols. With OpenID Connect, you specify the _openid_ scope to request an ID token.

You can also specify the _email_ scope, _profile_ scope, or both to return additional claims in the ID

token. You don't need to specify the _User.Read_ permission to return an ID token with the v2.0

endpoint. For more information, see OpenID Connect scopes.

The Microsoft Authentication Library (MSAL) currently specifies _offline\_access_, _openid_, _profile_,

and _email_ by default in authorization and token requests. Therefore, for the default case, if you

specify these scopes explicitly, the Microsoft identity platform might return an error.

ﾉ

**Expand table**

**OnlineMeetingAiInsight.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

c0cf7895-985f-42d4-a693-

b618f36674ad

166741d6-eeb8-46fe-91f4-

817d2af7bc88

DisplayText

Read all AI Insights for online

meetings.

Read all AI Insights for online

meetings.

Description

Allows the app to read all AI Insights

for all online meetings, without a

signed-in user.

Allows the app to read all AI Insights

for online meetings, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

01892c31-3b66-4bcf-b5f5-bf0a03d5ed9f

-

DisplayText

Read all AI Insights for online meetings where the Teams

application is installed.

-

Description

Allows the teams-app to read all aiInsights for online meetings

where the Teams-app is installed, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

df01ed3b-eb61-4eca-9965-

6b3d789751b2

110e5abb-a10c-4b59-8b55-

9b4daa4ef743

DisplayText

Read online meeting artifacts

Read user's online meeting artifacts

Description

Allows the app to read online meeting

artifacts in your organization, without a

signed-in user.

Allows the app to read online

meeting artifacts on behalf of the

signed-in user.

**OnlineMeetingAiInsight.Read.Chat**

ﾉ

**Expand table**

**OnlineMeetingArtifact.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

No

Administrators can configure application access policy to allow apps to access online meetings

on behalf of a user.

**Category**

**Application**

**Delegated**

Identifier

a4a08342-c95d-476b-b943-

97e100569c8d

190c2bb6-1fdd-4fec-9aa2-

7d571b5e1fe3

DisplayText

Read all recordings of online

meetings.

Read all recordings of online meetings.

Description

Allows the app to read all recordings

of all online meetings, without a

signed-in user.

Allows the app to read all recordings

of online meetings, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

Administrators can configure application access policy to allow apps to access online meetings

on behalf of a user.

**Category**

**Application**

**Delegated**

Identifier

-

9be106e1-f4e3-4df5-bdff-e4bc531cbe43

DisplayText

-

Read user's online meetings

Description

-

Allows the app to read online meeting details on behalf of the

signed-in user.

AdminConsentRequired

-

No

**OnlineMeetingRecording.Read.All**

ﾉ

**Expand table**

**OnlineMeetings.Read**

ﾉ

**Expand table**

Administrators can configure application access policy to allow apps to access online meetings

on behalf of a user.

**Category**

**Application**

**Delegated**

Identifier

c1684f21-1984-47fa-9d61-2dc8c296bb70

-

DisplayText

Read online meeting details

-

Description

Allows the app to read online meeting details in your

organization, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

a65f2972-a4f8-4f5e-afd7-69ccb046d5dc

DisplayText

-

Read and create user's online meetings

Description

-

Allows the app to read and create online meetings on behalf of

the signed-in user.

AdminConsentRequired

-

No

Administrators can configure application access policy to allow apps to access online meetings

on behalf of a user.

**OnlineMeetings.Read.All**

ﾉ

**Expand table**

**OnlineMeetings.ReadWrite**

ﾉ

**Expand table**

**OnlineMeetings.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

b8bb2037-6e08-44ac-a4ea-4674e010e2a4

-

DisplayText

Read and create online meetings

-

Description

Allows the app to read and create online meetings as an

application in your organization.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

a4a80d8d-d283-4bd8-8504-

555ec3870630

30b87d18-ebb1-45db-97f8-

82ccb1f0190c

DisplayText

Read all transcripts of online

meetings.

Read all transcripts of online meetings.

Description

Allows the app to read all transcripts

of all online meetings, without a

signed-in user.

Allows the app to read all transcripts

of online meetings, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

Administrators can configure application access policy to allow apps to access online meetings

on behalf of a user.

**Category**

**Application**

**Delegated**

Identifier

bb70e231-92dc-4729-aff5-

697b3f04be95

f6609722-4100-44eb-b747-

e6ca0536989d

DisplayText

Read all on-premises directory

synchronization information

Read all on-premises directory

synchronization information

**OnlineMeetingTranscript.Read.All**

ﾉ

**Expand table**

**OnPremDirectorySynchronization.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read all on-

premises directory synchronization

information for the organization,

without a signed-in user.

Allows the app to read all on-premises

directory synchronization information

for the organization, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

c22a92cc-79bf-4bb1-8b6c-

e0a05d3d80ce

c2d95988-7604-4ba1-aaed-

38a5f82a51c7

DisplayText

Read and write all on-premises

directory synchronization information

Read and write all on-premises

directory synchronization information

Description

Allows the app to read and write all

on-premises directory

synchronization information for the

organization, without a signed-in

user.

Allows the app to read and write all

on-premises directory synchronization

information for the organization, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

0b57845e-aa49-4e6f-8109-

ce654fffa618

8c4d5184-71c2-4bf8-bb9d-

bc3378c9ad42

DisplayText

Manage on-premises published

resources

Manage on-premises published

resources

Description

Allows the app to create, view,

update and delete on-premises

published resources, on-premises

agents and agent groups, as part of

Allows the app to manage hybrid

identity service configuration by

creating, viewing, updating and deleting

on-premises published resources, on-

**OnPremDirectorySynchronization.ReadWrite.All**

ﾉ

**Expand table**

**OnPremisesPublishingProfiles.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

a hybrid identity configuration,

without a signed in user.

premises agents and agent groups, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

37f7f235-527c-4136-accd-4a02d197296e

DisplayText

-

Sign users in

Description

-

Allows users to sign in to the app with their work or school

accounts and allows the app to see basic user profile

information.

AdminConsentRequired

-

No

_openid_ is an OpenID Connect (OIDC) scope.

You can use the OIDC scopes to specify artifacts that you want returned in Microsoft identity

platform authorization and token requests. The Microsoft identity platform v1.0 and v2.0

endpoints support OIDC scopes differently.

With the Microsoft identity platform v1.0 endpoint, only the _openid_ scope is used. You specify it

in the _scope_ parameter in an authorization request to return an ID token when you use the

OpenID Connect protocol to sign in a user to your app. For more information, see Microsoft

identity platform and OAuth 2.0 authorization code flow. To successfully return an ID token,

you must also make sure that the _User.Read_ permission is configured when you register your

app.

With the Microsoft identity platform v2.0 endpoint, you specify the _offline\_access_ scope in the

**scope** parameter to explicitly request a refresh token when using the OAuth 2.0 or OpenID

Connect protocols. With OpenID Connect, you specify the _openid_ scope to request an ID token.

You can also specify the _email_ scope, _profile_ scope, or both to return additional claims in the ID

token. You don't need to specify the _User.Read_ permission to return an ID token with the v2.0

endpoint. For more information, see OpenID Connect scopes.

**openid**

ﾉ

**Expand table**

The Microsoft Authentication Library (MSAL) currently specifies _offline\_access_, _openid_, _profile_,

and _email_ by default in authorization and token requests. Therefore, for the default case, if you

specify these scopes explicitly, the Microsoft identity platform might return an error.

**Category**

**Application**

**Delegated**

Identifier

498476ce-e0fe-48b0-b801-

37ba7e2685c6

4908d5b9-3fb2-4b1e-9336-

1888b7937185

DisplayText

Read organization information

Read organization information

Description

Allows the app to read the

organization and related resources,

without a signed-in user. Related

resources include things like

subscribed skus and tenant branding

information.

Allows the app to read the

organization and related resources, on

behalf of the signed-in user. Related

resources include things like

subscribed skus and tenant branding

information.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

292d869f-3427-49a8-9dab-

8c70152b74e9

46ca0847-7e6b-426e-9775-

ea810a948356

DisplayText

Read and write organization

information

Read and write organization

information

Description

Allows the app to read and write the

organization and related resources,

without a signed-in user. Related

resources include things like

subscribed skus and tenant branding

information.

Allows the app to read and write the

organization and related resources, on

behalf of the signed-in user. Related

resources include things like

subscribed skus and tenant branding

information.

AdminConsentRequired

Yes

Yes

**Organization.Read.All**

ﾉ

**Expand table**

**Organization.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

eb76ac34-0d62-4454-b97c-

185e4250dc20

9082f138-6f02-4f3a-9f4d-

5f3c2ce5c688

DisplayText

Read organizational branding

information

Read organizational branding

information

Description

Allows the app to read the

organizational branding information,

without a signed-in user.

Allows the app to read the

organizational branding information,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

d2ebfbc1-a5f8-424b-83a6-

56ab5927a73c

15ce63de-b141-4c9a-a9a5-

241bf27c6aaf

DisplayText

Read and write organizational

branding information

Read and write organizational

branding information

Description

Allows the app to read and write the

organizational branding information,

without a signed-in user.

Allows the app to read and write the

organizational branding information,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**OrganizationalBranding.Read.All**

ﾉ

**Expand table**

**OrganizationalBranding.ReadWrite.All**

ﾉ

**Expand table**

**OrgContact.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

e1a88a34-94c4-4418-be12-

c87b00e26bea

08432d1b-5911-483c-86df-

7980af5cdee0

DisplayText

Read organizational contacts

Read organizational contacts

Description

Allows the app to read all

organizational contacts without a

signed-in user. These contacts are

managed by the organization and are

different from a user's personal

contacts.

Allows the app to read all

organizational contacts on behalf of

the signed-in user. These contacts are

managed by the organization and are

different from a user's personal

contacts.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

56c84fa9-ea1f-4a15-90f2-

90ef41ece2c9

1e9b7a7e-4d64-44ff-acf5-

2e9651c1519f

DisplayText

Read organization-wide apps and

services settings

Read organization-wide apps and

services settings

Description

Allows the app to read organization-

wide apps and services settings,

without a signed-in user.

Allows the app to read organization-

wide apps and services settings on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

4a8e4191-c1c8-45f8-b801-

f9a1a5ee6ad3

c167b0e7-47c0-48e8-9eee-

9892f58018fa

DisplayText

Read and write organization-wide

apps and services settings

Read and write organization-wide apps

and services settings

**OrgSettings-AppsAndServices.Read.All**

ﾉ

**Expand table**

**OrgSettings-AppsAndServices.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read and write

organization-wide apps and services

settings, without a signed-in user.

Allows the app to read and write

organization-wide apps and services

settings on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

c18ae2dc-d9f3-4495-a93f-

18980a0e159f

9862d930-5aec-4a98-8d4f-

7277a8db9bcb

DisplayText

Read organization-wide Dynamics

customer voice settings

Read organization-wide Dynamics

customer voice settings

Description

Allows the app to read organization-

wide Dynamics customer voice

settings, without a signed-in user.

Allows the app to read organization-

wide Dynamics customer voice settings

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

c3f1cc32-8bbd-4ab6-bd33-

f270e0d9e041

4cea26fb-6967-4234-82c4-

c044414743f8

DisplayText

Read and write organization-wide

Dynamics customer voice settings

Read and write organization-wide

Dynamics customer voice settings

Description

Allows the app to read and write

organization-wide Dynamics

customer voice settings, without a

signed-in user.

Allows the app to read and write

organization-wide Dynamics customer

voice settings on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**OrgSettings-DynamicsVoice.Read.All**

ﾉ

**Expand table**

**OrgSettings-DynamicsVoice.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

434d7c66-07c6-4b1f-ab21-

417cf2cdaaca

210051a0-1ffc-435c-ae76-

02d226d05752

DisplayText

Read organization-wide Microsoft

Forms settings

Read organization-wide Microsoft

Forms settings

Description

Allows the app to read organization-

wide Microsoft Forms settings,

without a signed-in user.

Allows the app to read organization-

wide Microsoft Forms settings on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2cb92fee-97a3-4034-8702-

24a6f5d0d1e9

346c19ff-3fb2-4e81-87a0-

bac9e33990c1

DisplayText

Read and write organization-wide

Microsoft Forms settings

Read and write organization-wide

Microsoft Forms settings

Description

Allows the app to read and write

organization-wide Microsoft Forms

settings, without a signed-in user.

Allows the app to read and write

organization-wide Microsoft Forms

settings on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**OrgSettings-Forms.Read.All**

ﾉ

**Expand table**

**OrgSettings-Forms.ReadWrite.All**

ﾉ

**Expand table**

**OrgSettings-Microsoft365Install.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

6cdf1fb1-b46f-424f-9493-

07247caa22e2

8cbdb9f6-9c2e-451a-814d-

ec606e5d0212

DisplayText

Read organization-wide Microsoft

365 apps installation settings

Read organization-wide Microsoft 365

apps installation settings

Description

Allows the app to read organization-

wide Microsoft 365 apps installation

settings, without a signed-in user.

Allows the app to read organization-

wide Microsoft 365 apps installation

settings on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

83f7232f-763c-47b2-a097-

e35d2cbe1da5

1ff35e91-19eb-42d8-aa2d-

cc9891127ae5

DisplayText

Read and write organization-wide

Microsoft 365 apps installation

settings

Read and write organization-wide

Microsoft 365 apps installation

settings

Description

Allows the app to read and write

organization-wide Microsoft 365

apps installation settings, without a

signed-in user.

Allows the app to read and write

organization-wide Microsoft 365 apps

installation settings on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e4d9cd09-d858-4363-9410-

abb96737f0cf

7ff96f41-f022-45ba-acd8-

ef3f03063d6b

**OrgSettings-Microsoft365Install.ReadWrite.All**

ﾉ

**Expand table**

**OrgSettings-Todo.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read organization-wide Microsoft To

Do settings

Read organization-wide Microsoft To

Do settings

Description

Allows the app to read organization-

wide Microsoft To Do settings,

without a signed-in user.

Allows the app to read organization-

wide Microsoft To Do settings on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

5febc9da-e0d0-4576-bd13-

ae70b2179a39

087502c2-5263-433e-abe3-

8f77231a0627

DisplayText

Read and write organization-wide

Microsoft To Do settings

Read and write organization-wide

Microsoft To Do settings

Description

Allows the app to read and write

organization-wide Microsoft To Do

settings, without a signed-in user.

Allows the app to read and write

organization-wide Microsoft To Do

settings on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7c3e1994-38ff-4412-a99b-

9369f6bb7706

8804798e-5934-4e30-8ce3-

ef88257cecd4

DisplayText

Read all billing data for your

company's tenant

Read all billing data for your

company's tenant

Description

Allows the app to read all of billing

data from Microsoft for your

company's tenant, without a signed-in

Allows the app to read all of billing

data from Microsoft for your

company's tenant, on behalf of the

**OrgSettings-Todo.ReadWrite.All**

ﾉ

**Expand table**

**PartnerBilling.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

user. This includes reading billed and

unbilled azure usage and invoice

reconciliation data.

signed-in user. This includes reading

billed and unbilled Usage and Invoice

reconciliation data.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

21ffa320-2e7f-47d3-a466-

7ff04d2dd68d

5567b981-0bf1-4796-9038-

0648b46e116d

DisplayText

Read security alerts of customer

with CSP relationship

Read security alerts of customer with

CSP relationship

Description

Allows the app to read security

alerts of customer with CSP

relationship, without a signed-in

user.

Allows the app to read security alerts of

customer with CSP relationship on

behalf of the partner signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

04a2c935-5b4b-474a-be42-

11f53111f271

0cd2c1f6-94a1-4075-ab8c-

0b1aff2e1ad5

DisplayText

Read security alerts and update

status of security alerts of customer

with CSP relationship

Read security alerts and update status

of security alerts of customer with CSP

relationship

Description

Allows the app to read security alerts

and update status of alerts of

customer with CSP relationship,

without a signed-in user.

Allows the app to read security alerts

and update status of alerts of customer

with CSP relationship on behalf of the

partner signed-in user.

**PartnerSecurity.Read.All**

ﾉ

**Expand table**

**PartnerSecurity.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

bdfb26d9-bb36-49be-9b4c-

b8cbf4b05808

d88fd3fb-53d3-4c1c-8c39-

787fcac2ed7a

DisplayText

Read all pending external user

profiles

Read pending external user profiles

Description

Allows the app to read available

properties of pending external user

profiles, without a signed-in user.

Allows the app to read available

properties of pending external user

profiles, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

8363c2b8-6ff7-420b-9966-

c5884c2d48bc

93a1fb28-c908-4826-904e-

0c74ad352b73

DisplayText

Read and write all pending external

user profiles

Read and write pending external user

profiles

Description

Allows the app to read and write

available properties of pending

external user profiles, without a

signed-in user.

Allows the app to read and write

available properties of pending

external user profiles, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**PendingExternalUserProfile.Read.All**

ﾉ

**Expand table**

**PendingExternalUserProfile.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

ba47897c-39ec-4d83-8086-ee8256fa737d

DisplayText

-

Read users' relevant people lists

Description

-

Allows the app to read a ranked list of relevant people of the

signed-in user. The list includes local contacts, contacts from

social networking, your organization's directory, and people

from recent communications (such as email and Skype).

AdminConsentRequired

-

No

![](./assets/output_322_1.png)![](./assets/output_322_2.png)

The _People.Read_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

b528084d-ad10-4598-8b93-

929746b4d7d6

b89f9189-71a5-4e70-b041-

9887f0bc7e4a

DisplayText

Read all users' relevant people lists

Read all users' relevant people lists

Description

Allows the app to read any user's

scored list of relevant people,

without a signed-in user. The list can

include local contacts, contacts from

social networking, your

organization's directory, and people

from recent communications (such

as email and Skype).

Allows the app to read a scored list of

relevant people of the signed-in user or

other users in the signed-in user's

organization. The list can include local

contacts, contacts from social

networking, your organization's

directory, and people from recent

communications (such as email and

Skype).

AdminConsentRequired

Yes

Yes

**People.Read**

ﾉ

**Expand table**

**People.Read.All**

ﾉ

**Expand table**

**PeopleSettings.Read.All**

**Category**

**Application**

**Delegated**

Identifier

ef02f2e7-e22d-4c77-8614-

8f765683b86e

ec762c5f-388b-4b16-8693-

ac1efbc611bc

DisplayText

Read all tenant-wide people settings

Read tenant-wide people settings

Description

Allows the application to read

tenant-wide people settings without

a signed-in user.

Allows the application to read tenant-

wide people settings on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

b6890674-9dd5-4e42-bb15-

5af07f541ae1

e67e6727-c080-415e-b521-

e3f35d5248e9

DisplayText

Read and write all tenant-wide

people settings

Read and write tenant-wide people

settings

Description

Allows the application to read and

write tenant-wide people settings

without a signed-in user.

Allows the application to read and

write tenant-wide people settings on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

913b9306-0ce1-42b8-9137-

6a7df690a760

cb8f45a0-5c2e-4ea1-b803-

84b870a7d7ec

DisplayText

Read all company places

Read all company places

ﾉ

**Expand table**

**PeopleSettings.ReadWrite.All**

ﾉ

**Expand table**

**Place.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read company

places (conference rooms and room

lists) for calendar events and other

applications, without a signed-in

user.

Allows the app to read your company's

places (conference rooms and room

lists) for calendar events and other

applications, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

4c06a06a-098a-4063-868e-5dfee3827264

DisplayText

-

Read and write organization places

Description

-

Allows the app to manage organization places (conference

rooms and room lists) for calendar events and other

applications, on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

8b724a84-ceac-4fd9-897e-

e31ba8f2d7a3

4c7f93d2-6b0b-4e05-91aa-

87842f0a2142

DisplayText

Read all workplace devices

Read all workplace devices

Description

Allows the app to read all workplace

devices, without a signed-in user.

Allows the app to read all workplace

devices, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Place.ReadWrite.All**

ﾉ

**Expand table**

**PlaceDevice.Read.All**

ﾉ

**Expand table**

**PlaceDevice.ReadWrite.All**

**Category**

**Application**

**Delegated**

Identifier

2d510721-5c4e-43cd-bfdb-

ac0f8819fb92

eafd6a71-e95a-4f8a-bb6e-

fb84ab7fbd9e

DisplayText

Read and write all workplace devices

Read and write all workplace devices

Description

Allows the app to read and write all

workplace devices, without a signed-

in user.

Allows the app to read and write all

workplace devices, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

27fc435f-44e2-4b30-bf3c-e0ce74aed618

-

DisplayText

Read and write telemetry for all workplace devices.

-

Description

Allows the app to read and write telemetry for all workplace

devices, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

246dd0d5-5bd0-4def-940b-

0421030a5b68

572fea84-0151-49b2-9301-

11cb16974376

DisplayText

Read your organization's policies

Read your organization's policies

Description

Allows the app to read all your

organization's policies without a

signed in user.

Allows the app to read your

organization's policies on behalf of the

signed-in user.

ﾉ

**Expand table**

**PlaceDeviceTelemetry.ReadWrite.All**

ﾉ

**Expand table**

**Policy.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

![](./assets/output_326_1.png)![](./assets/output_326_2.png)

The _Policy.Read.All_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

8e3bc81b-d2f3-4b7b-838c-

32c88218d2f0

a6ff13ac-1851-4993-8ca9-

a671d70de2d5

DisplayText

Read authentication method policies

Read authentication method policies

Description

Allows the app to read all

authentication method policies for the

tenant, without a signed-in user.

Allows the app to read the

authentication method policies, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

37730810-e9ba-4e46-b07e-

8ca78d182097

633e0fce-8c58-4cfb-9495-

12bbd5a24f7c

DisplayText

Read your organization's conditional

access policies

Read your organization's conditional

access policies

Description

Allows the app to read your

organization's conditional access

policies, without a signed-in user.

Allows the app to read your

organization's conditional access

policies on behalf of the signed-in

user.

AdminConsentRequired

Yes

No

**Policy.Read.AuthenticationMethod**

ﾉ

**Expand table**

**Policy.Read.ConditionalAccess**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

bdba4817-6ba1-4a7c-8a01-

be9bc7c242dd

3616a4b0-6746-49c4-a678-

4c237599074d

DisplayText

Read your organization's device

configuration policies

Read your organization's device

configuration policies

Description

Allows the application to read your

organization's device configuration

policies without a signed-in user. For

example, device registration policy

can limit initial provisioning controls

using quota restrictions, additional

authentication and authorization

checks.

Allows the app to read your

organization's device configuration

policies on behalf of the signed-in

user. For example, device registration

policy can limit initial provisioning

controls using quota restrictions,

additional authentication and

authorization checks.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

b21b72f6-4e6a-4533-9112-

47eea9f97b28

d146432f-b803-4ed4-8d42-

ba74193a6ede

DisplayText

Read your organization's identity

protection policy

Read your organization's identity

protection policy

Description

Allows the app to read your

organization's identity protection

policy without a signed-in user.

Allows the app to read your

organization's identity protection

policy on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Policy.Read.DeviceConfiguration**

ﾉ

**Expand table**

**Policy.Read.IdentityProtection**

ﾉ

**Expand table**

**Policy.Read.PermissionGrant**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

9e640839-a198-48fb-8b9a-

013fd6f6cbcd

414de6ea-2d92-462f-b120-

6e2a809a6d01

DisplayText

Read consent and permission grant

policies

Read consent and permission grant

policies

Description

Allows the app to read policies

related to consent and permission

grants for applications, without a

signed-in user.

Allows the app to read policies related

to consent and permission grants for

applications, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

77c863fd-06c0-47ce-a7eb-

49773e89d319

4f5bc9c8-ea54-4772-973a-

9ca119cb0409

DisplayText

Read and write your organization's

directory access review default policy

Read and write your organization's

directory access review default policy

Description

Allows the app to read and write your

organization's directory access review

default policy without a signed-in

user.

Allows the app to read and write your

organization's directory access review

default policy on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

be74164b-cff1-491c-8741-

e671cb536e13

b27add92-efb2-4f16-84f5-

8108ba77985c

DisplayText

Read and write your organization's

application configuration policies

Read and write your organization's

application configuration policies

**Policy.ReadWrite.AccessReview**

ﾉ

**Expand table**

**Policy.ReadWrite.ApplicationConfiguration**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read and write your

organization's application

configuration policies, without a

signed-in user. This includes policies

such as activityBasedTimeoutPolicy,

claimsMappingPolicy,

homeRealmDiscoveryPolicy,

tokenIssuancePolicy and

tokenLifetimePolicy.

Allows the app to read and write your

organization's application

configuration policies on behalf of the

signed-in user. This includes policies

such as activityBasedTimeoutPolicy,

claimsMappingPolicy,

homeRealmDiscoveryPolicy,

tokenIssuancePolicy and

tokenLifetimePolicy.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

25f85f3c-f66c-4205-8cd5-

de92dd7f0cec

edb72de9-4252-4d03-a925-

451deef99db7

DisplayText

Read and write authentication flow

policies

Read and write authentication flow

policies

Description

Allows the app to read and write all

authentication flow policies for the

tenant, without a signed-in user.

Allows the app to read and write the

authentication flow policies, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

29c18626-4985-4dcd-85c0-

193eef327366

7e823077-d88e-468f-a337-

e18f1f0e6c7c

DisplayText

Read and write all authentication

method policies

Read and write authentication

method policies

**Policy.ReadWrite.AuthenticationFlows**

ﾉ

**Expand table**

**Policy.ReadWrite.AuthenticationMethod**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read and write all

authentication method policies for the

tenant, without a signed-in user.

Allows the app to read and write the

authentication method policies, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

![](./assets/output_330_1.png)![](./assets/output_330_2.png)

The _Policy.ReadWrite.AuthenticationMethod_ delegated permission is available for consent in

personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

fb221be6-99f2-473f-bd32-

01c6a0e9ca3b

edd3c878-b384-41fd-95ad-

e7407dd775be

DisplayText

Read and write your organization's

authorization policy

Read and write your organization's

authorization policy

Description

Allows the app to read and write your

organization's authorization policy

without a signed in user. For

example, authorization policies can

control some of the permissions that

the out-of-the-box user role has by

default.

Allows the app to read and write your

organization's authorization policy on

behalf of the signed-in user. For

example, authorization policies can

control some of the permissions that

the out-of-the-box user role has by

default.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

01c0a623-fc9b-48e9-b794-

0756f8e8f067

ad902697-1014-4ef5-81ef-

2b4301988e8c

DisplayText

Read and write your organization's

conditional access policies

Read and write your organization's

conditional access policies

**Policy.ReadWrite.Authorization**

ﾉ

**Expand table**

**Policy.ReadWrite.ConditionalAccess**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read and write

your organization's conditional

access policies, without a signed-in

user.

Allows the app to read and write your

organization's conditional access

policies on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

999f8c63-0a38-4f1b-91fd-

ed1947bdd1a9

4d135e65-66b8-41a8-9f8b-

081452c91774

DisplayText

Read and write your organization's

consent request policy

Read and write consent request policy

Description

Allows the app to read and write your

organization's consent requests

policy without a signed-in user.

Allows the app to read and write your

organization's consent requests policy

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

338163d7-f101-4c92-94ba-

ca46fe52447c

014b43d0-6ed4-4fc6-84dc-

4b6f7bae7d85

DisplayText

Read and write your organization's

cross tenant access policies

Read and write your organization's

cross tenant access policies

Description

Allows the app to read and write your

organization's cross-tenant access

policies and configuration for

automatic user consent settings to

suppress consent prompts for users of

Allows the app to read and write your

organization's cross-tenant access

policies and configuration for

automatic user consent settings to

suppress consent prompts for users of

**Policy.ReadWrite.ConsentRequest**

ﾉ

**Expand table**

**Policy.ReadWrite.CrossTenantAccess**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

the other tenant on behalf of the

signed-in user.

the other tenant on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

a6325ae7-2b73-4dbd-abed-

fbeacfbf8696

9ef7463f-1d39-406f-89ea-

3483a4645e1c

DisplayText

Read and write your organization's

M365 cross tenant access capabilities

Read and write your organization's

M365 cross tenant access capabilities

Description

Allows the app to read and write

your organization's M365 cross

tenant access capabilities without a

signed-in user.

Allows the app to read and write your

organization's M365 cross tenant

access capabilities on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

230fb2d5-aa21-49c1-bfa7-

ae1be179d867

40b534c3-9552-4550-901b-

23879c90bcf9

DisplayText

Read and write your organization's

device configuration policies

Read and write your organization's

device configuration policies

Description

Allows the application to read and

write your organization's device

configuration policies without a

signed-in user. For example, device

registration policy can limit initial

provisioning controls using quota

Allows the app to read and write your

organization's device configuration

policies on behalf of the signed-in

user. For example, device registration

policy can limit initial provisioning

controls using quota restrictions,

**Policy.ReadWrite.CrossTenantCapability**

ﾉ

**Expand table**

**Policy.ReadWrite.DeviceConfiguration**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

restrictions, additional authentication

and authorization checks.

additional authentication and

authorization checks.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

03cc4f92-788e-4ede-b93f-

199424d144a5

b5219784-1215-45b5-b3f1-

88fe1081f9c0

DisplayText

Read and write your organization's

external identities policy

Read and write your organization's

external identities policy

Description

Allows the application to read and

update the organization's external

identities policy without a signed-in

user. For example, external identities

policy controls if users invited to

access resources in your organization

via B2B collaboration or B2B direct

connect are allowed to self-service

leave.

Allows the application to read and

update the organization's external

identities policy on behalf of the

signed-in user. For example, external

identities policy controls if users

invited to access resources in your

organization via B2B collaboration or

B2B direct connect are allowed to self-

service leave.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2044e4f1-e56c-435b-925c-

44cd8f6ba89a

92a38652-f13b-4875-bc77-

6e1dbb63e1b2

DisplayText

Read and write feature rollout

policies

Read and write your organization's

feature rollout policies

Description

Allows the app to read and write

feature rollout policies without a

Allows the app to read and write your

organization's feature rollout policies on

**Policy.ReadWrite.ExternalIdentities**

ﾉ

**Expand table**

**Policy.ReadWrite.FeatureRollout**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

signed-in user. Includes abilities to

assign and remove users and

groups to rollout of a specific

feature.

behalf of the signed-in user. Includes

abilities to assign and remove users and

groups to rollout of a specific feature.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

90bbca0b-227c-4cdc-8083-

1c6cfb95bac6

be1be369-4540-4ac9-8928-

79de99f70d8f

DisplayText

Read and write your organization's

federated token validation policy

Read and write your organization's

federated token validation policy

Description

Allows the application to read and

update the organization's federated

token validation policy without a

signed-in user.

Allows the application to read and

update the organization's federated

token validation policy on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2dcf8603-09eb-4078-b1ec-

d30a1a76b873

7256e131-3efb-4323-9854-

cf41c6021770

DisplayText

Read and write your organization's

identity protection policy

Read and write your organization's

identity protection policy

Description

Allows the app to read and write your

organization's identity protection

policy without a signed-in user.

Allows the app to read and write your

organization's identity protection

policy on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Policy.ReadWrite.FedTokenValidation**

ﾉ

**Expand table**

**Policy.ReadWrite.IdentityProtection**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

a8ead177-1889-4546-9387-f25e658e2a79

DisplayText

-

Read and write your organization's mobility management

policies

Description

-

Allows the app to read and write your organization's mobility

management policies on behalf of the signed-in user. For

example, a mobility management policy can set the enrollment

scope for a given mobility management application.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

a402ca1c-2696-4531-972d-

6e5ee4aa11ea

2672f8bb-fd5e-42e0-85e1-

ec764dd2614e

DisplayText

Manage consent and permission

grant policies

Manage consent and permission grant

policies

Description

Allows the app to manage policies

related to consent and permission

grants for applications, without a

signed-in user.

Allows the app to manage policies

related to consent and permission

grants for applications, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Policy.ReadWrite.MobilityManagement**

ﾉ

**Expand table**

**Policy.ReadWrite.PermissionGrant**

ﾉ

**Expand table**

**Policy.ReadWrite.SecurityDefaults**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

1c6e93a6-28e2-4cbb-9f64-

1a46a821124d

0b2a744c-2abf-4f1e-ad7e-

17a087e2be99

DisplayText

Read and write your organization's

security defaults policy

Read and write your organization's

security defaults policy

Description

Allows the app to read and write your

organization's security defaults

policy, without a signed-in user.

Allows the app to read and write your

organization's security defaults policy

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

79a677f7-b79d-40d0-a36a-

3e6f8688dd7a

cefba324-1a70-4a6e-9c1d-

fd670b7ae392

DisplayText

Read and write your organization's

trust framework policies

Read and write your organization's

trust framework policies

Description

Allows the app to read and write

your organization's trust framework

policies without a signed in user.

Allows the app to read and write your

organization's trust framework policies

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

d7b7f2d9-0f45-4ea1-9d42-e50810c06991

DisplayText

-

Read and write access to mailboxes via POP.

Description

-

Allows the app to have the same access to mailboxes as the

signed-in user via POP protocol.

**Policy.ReadWrite.TrustFramework**

ﾉ

**Expand table**

**POP.AccessAsUser.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

No

![](./assets/output_337_1.png)![](./assets/output_337_2.png)

The _POP.AccessAsUser.All_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

-

76bc735e-aecd-4a1d-8b4c-2b915deabb79

DisplayText

-

Read user's presence information

Description

-

Allows the app to read presence information on behalf of the

signed-in user. Presence information includes activity,

availability, status note, calendar out-of-office message,

timezone and location.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

a70e0c2d-e793-494c-94c4-

118fa0a67f42

9c7a330d-35b3-4aa1-963d-

cb2b9f927841

DisplayText

Read presence information for all

users

Read presence information of all users

in your organization

Description

Allows the app to read presence

information of all users in the

directory without a signed-in user.

Presence information includes

activity, availability, status note,

calendar out-of-office message,

timezone and location.

Allows the app to read presence

information of all users in the directory

on behalf of the signed-in user.

Presence information includes activity,

availability, status note, calendar out-

of-office message, timezone and

location.

**Presence.Read**

ﾉ

**Expand table**

**Presence.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

-

8d3c54a7-cf58-4773-bf81-c0cd6ad522bb

DisplayText

-

Read and write a user's presence information

Description

-

Allows the app to read the presence information and write

activity and availability on behalf of the signed-in user. Presence

information includes activity, availability, status note, calendar

out-of-office message, timezone and location.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

83cded22-8297-4ff6-a7fa-e97e9545a259

-

DisplayText

Read and write presence information for all users

-

Description

Allows the app to read all presence information and write activity

and availability of all users in the directory without a signed-in

user. Presence information includes activity, availability, status

note, calendar out-of-office message, time zone and location.

-

AdminConsentRequired

Yes

-

**Presence.ReadWrite**

ﾉ

**Expand table**

**Presence.ReadWrite.All**

ﾉ

**Expand table**

**PrintConnector.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

d69c2d6d-4f72-4f99-a6b9-663e32f8cf68

DisplayText

-

Read print connectors

Description

-

Allows the application to read print connectors on behalf of the

signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

79ef9967-7d59-4213-9c64-4b10687637d8

DisplayText

-

Read and write print connectors

Description

-

Allows the application to read and write print connectors on

behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

90c30bed-6fd1-4279-bf39-714069619721

DisplayText

-

Register printers

Description

-

Allows the application to create (register) printers on behalf of

the signed-in user.

AdminConsentRequired

-

Yes

**PrintConnector.ReadWrite.All**

ﾉ

**Expand table**

**Printer.Create**

ﾉ

**Expand table**

**Printer.FullControl.All**

**Category**

**Application**

**Delegated**

Identifier

-

93dae4bd-43a1-4a23-9a1a-92957e1d9121

DisplayText

-

Register, read, update, and unregister printers

Description

-

Allows the application to create (register), read, update, and

delete (unregister) printers on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

9709bb33-4549-49d4-8ed9-

a8f65e45bb0f

3a736c8a-018e-460a-b60c-

863b2683e8bf

DisplayText

Read printers

Read printers

Description

Allows the application to read

printers without a signed-in user.

Allows the application to read printers

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f5b3f73d-6247-44df-a74c-

866173fddab0

89f66824-725f-4b8f-928e-

e1c5258dc565

DisplayText

Read and update printers

Read and update printers

Description

Allows the application to read and

update printers without a signed-in

user. Does not allow creating

(registering) or deleting

(unregistering) printers.

Allows the application to read and

update printers on behalf of the

signed-in user. Does not allow creating

(registering) or deleting (unregistering)

printers.

ﾉ

**Expand table**

**Printer.Read.All**

ﾉ

**Expand table**

**Printer.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

ed11134d-2f3f-440d-a2e1-411efada2502

DisplayText

-

Read printer shares

Description

-

Allows the application to read printer shares on behalf of the

signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

-

5fa075e9-b951-4165-947b-c63396ff0a37

DisplayText

-

Read basic information about printer shares

Description

-

Allows the application to read basic information about printer

shares on behalf of the signed-in user. Does not allow reading

access control information.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

-

06ceea37-85e2-40d7-bec3-91337a46038f

**PrinterShare.Read.All**

ﾉ

**Expand table**

**PrinterShare.ReadBasic.All**

ﾉ

**Expand table**

**PrinterShare.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

-

Read and write printer shares

Description

-

Allows the application to read and update printer shares on

behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

21f0d9c0-9f13-48b3-94e0-b6b231c7d320

DisplayText

-

Create print jobs

Description

-

Allows the application to create print jobs on behalf of the

signed-in user and upload document content to print jobs that

the signed-in user created.

AdminConsentRequired

-

No

In this to _PrintJob.Create_, the app requires at least the _Printer.Read.All_ (or a more prviliged

permission) because print jobs are stored within printers.

**Category**

**Application**

**Delegated**

Identifier

58a52f47-9e36-4b17-9ebe-ce4ef7f3e6c8

-

DisplayText

Perform advanced operations on print jobs

-

Description

Allows the application to perform advanced operations like

redirecting a print job to another printer without a signed-in user.

Also allows the application to read and update the metadata of

print jobs.

-

AdminConsentRequired

Yes

-

**PrintJob.Create**

ﾉ

**Expand table**

**PrintJob.Manage.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

248f5528-65c0-4c88-8326-876c7236df5e

DisplayText

-

Read user's print jobs

Description

-

Allows the application to read the metadata and document

content of print jobs that the signed-in user created.

AdminConsentRequired

-

No

In this to _PrintJob.Read_, the app requires at least the _Printer.Read.All_ (or a more prviliged

permission) because print jobs are stored within printers.

**Category**

**Application**

**Delegated**

Identifier

ac6f956c-edea-44e4-bd06-

64b1b4b9aec9

afdd6933-a0d8-40f7-bd1a-

b5d778e8624b

DisplayText

Read print jobs

Read print jobs

Description

Allows the application to read the

metadata and document content of

print jobs without a signed-in user.

Allows the application to read the

metadata and document content of

print jobs on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

In this to _PrintJob.Read.All_, the app requires at least the _Printer.Read.All_ (or a more prviliged

permission) because print jobs are stored within printers.

**PrintJob.Read**

ﾉ

**Expand table**

**PrintJob.Read.All**

ﾉ

**Expand table**

**PrintJob.ReadBasic**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

6a71a747-280f-4670-9ca0-a9cbf882b274

DisplayText

-

Read basic information of user's print jobs

Description

-

Allows the application to read the metadata of print jobs that

the signed-in user created. Does not allow access to print job

document content.

AdminConsentRequired

-

No

In this to _PrintJob.ReadBasic_, the app requires at least the _Printer.Read.All_ (or a more prviliged

permission) because print jobs are stored within printers.

**Category**

**Application**

**Delegated**

Identifier

fbf67eee-e074-4ef7-b965-

ab5ce1c1f689

04ce8d60-72ce-4867-85cf-

6d82f36922f3

DisplayText

Read basic information for print jobs

Read basic information of print jobs

Description

Allows the application to read the

metadata of print jobs without a

signed-in user. Does not allow access

to print job document content.

Allows the application to read the

metadata of print jobs on behalf of the

signed-in user. Does not allow access

to print job document content.

AdminConsentRequired

Yes

Yes

In this to _PrintJob.ReadBasic.All_, the app requires at least the _Printer.Read.All_ (or a more

prviliged permission) because print jobs are stored within printers.

**Category**

**Application**

**Delegated**

Identifier

-

b81dd597-8abb-4b3f-a07a-820b0316ed04

**PrintJob.ReadBasic.All**

ﾉ

**Expand table**

**PrintJob.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

-

Read and write user's print jobs

Description

-

Allows the application to read and update the metadata and

document content of print jobs that the signed-in user created.

AdminConsentRequired

-

No

In this to _PrintJob.ReadWrite_, the app requires at least the _Printer.Read.All_ (or a more prviliged

permission) because print jobs are stored within printers.

**Category**

**Application**

**Delegated**

Identifier

5114b07b-2898-4de7-a541-

53b0004e2e13

036b9544-e8c5-46ef-900a-

0646cc42b271

DisplayText

Read and write print jobs

Read and write print jobs

Description

Allows the application to read and

update the metadata and document

content of print jobs without a

signed-in user.

Allows the application to read and

update the metadata and document

content of print jobs on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

In this to _PrintJob.ReadWrite.All_, the app requires at least the _Printer.Read.All_ (or a more

prviliged permission) because print jobs are stored within printers.

**Category**

**Application**

**Delegated**

Identifier

-

6f2d22f2-1cb6-412c-a17c-3336817eaa82

DisplayText

-

Read and write basic information of user's print jobs

Description

-

Allows the application to read and update the metadata of print

jobs that the signed-in user created. Does not allow access to

**PrintJob.ReadWrite.All**

ﾉ

**Expand table**

**PrintJob.ReadWriteBasic**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

print job document content.

AdminConsentRequired

-

No

In this to _PrintJob.ReadWriteBasic_, the app requires at least the _Printer.Read.All_ (or a more

prviliged permission) because print jobs are stored within printers.

**Category**

**Application**

**Delegated**

Identifier

57878358-37f4-4d3a-8c20-

4816e0d457b1

3a0db2f6-0d2a-4c19-971b-

49109b19ad3d

DisplayText

Read and write basic information for

print jobs

Read and write basic information of

print jobs

Description

Allows the application to read and

update the metadata of print jobs

without a signed-in user. Does not

allow access to print job document

content.

Allows the application to read and

update the metadata of print jobs on

behalf of the signed-in user. Does not

allow access to print job document

content.

AdminConsentRequired

Yes

Yes

In this to _PrintJob.ReadWriteBasic.All_, the app requires at least the _Printer.Read.All_ (or a more

prviliged permission) because print jobs are stored within printers.

**Category**

**Application**

**Delegated**

Identifier

b5991872-94cf-4652-9765-

29535087c6d8

490f32fd-d90f-4dd7-a601-

ff6cdc1a3f6c

DisplayText

Read tenant-wide print settings

Read tenant-wide print settings

Description

Allows the application to read tenant-

wide print settings without a signed-

Allows the application to read tenant-

wide print settings on behalf of the

**PrintJob.ReadWriteBasic.All**

ﾉ

**Expand table**

**PrintSettings.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

in user.

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

9ccc526a-c51c-4e5c-a1fd-74726ef50b8f

DisplayText

-

Read and write tenant-wide print settings

Description

-

Allows the application to read and write tenant-wide print

settings on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

456b71a7-0ee0-4588-9842-c123fcc8f664

-

DisplayText

Read, write and update print task definitions

-

Description

Allows the application to read and update print task definitions

without a signed-in user.

-

AdminConsentRequired

Yes

-

**PrintSettings.ReadWrite.All**

ﾉ

**Expand table**

**PrintTaskDefinition.ReadWrite.All**

ﾉ

**Expand table**

**PrivilegedAccess.Read.AzureAD**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

4cdc2547-9148-4295-8d11-

be0db1391d6b

b3a539c9-59cb-4ad5-825a-

041ddbdc2bdb

DisplayText

Read privileged access to Azure AD

roles

Read privileged access to Azure AD

Description

Allows the app to read time-based

assignment and just-in-time elevation

(including scheduled elevation) of

Azure AD built-in and custom

administrative roles in your

organization, without a signed-in user.

Allows the app to read time-based

assignment and just-in-time

elevation (including scheduled

elevation) of Azure AD built-in and

custom administrative roles, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

01e37dc9-c035-40bd-b438-

b2879c4870a6

d329c81c-20ad-4772-abf9-

3f6fdb7e5988

DisplayText

Read privileged access to Azure AD

groups

Read privileged access to Azure AD

groups

Description

Allows the app to read time-based

assignment and just-in-time elevation

(including scheduled elevation) of

Azure AD groups in your organization,

without a signed-in user.

Allows the app to read time-based

assignment and just-in-time

elevation (including scheduled

elevation) of Azure AD groups, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

5df6fe86-1be0-44eb-b916-

1d89d70c-dcac-4248-b214-

**PrivilegedAccess.Read.AzureADGroup**

ﾉ

**Expand table**

**PrivilegedAccess.Read.AzureResources**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

7bd443a71236

903c457af83a

DisplayText

Read privileged access to Azure

resources

Read privileged access to Azure

resources

Description

Allows the app to read time-based

assignment and just-in-time

elevation of user privileges to audit

Azure resources in your organization,

without a signed-in user.

Allows the app to read time-based

assignment and just-in-time elevation

of Azure resources (like your

subscriptions, resource groups, storage,

compute) on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

854d9ab1-6657-4ec8-be45-

823027bcd009

3c3c74f5-cdaa-4a97-b7e0-

4e788bfcfb37

DisplayText

Read and write privileged access to Azure

AD roles

Read and write privileged access

to Azure AD

Description

Allows the app to request and manage

time-based assignment and just-in-time

elevation (including scheduled elevation)

of Azure AD built-in and custom

administrative roles in your organization,

without a signed-in user.

Allows the app to request and

manage just in time elevation

(including scheduled elevation) of

users to Azure AD built-in

administrative roles, on behalf of

signed-in users.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2f6817f8-7b12-4f0f-bc18-

eeaf60705a9e

32531c59-1f32-461f-b8df-

6f8a3b89f73b

**PrivilegedAccess.ReadWrite.AzureAD**

ﾉ

**Expand table**

**PrivilegedAccess.ReadWrite.AzureADGroup**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write privileged access to

Azure AD groups

Read and write privileged access to

Azure AD groups

Description

Allows the app to request and manage

time-based assignment and just-in-

time elevation (including scheduled

elevation) of Azure AD groups in your

organization, without a signed-in user.

Allows the app to request and

manage time-based assignment and

just-in-time elevation (including

scheduled elevation) of Azure AD

groups, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

6f9d5abc-2db6-400b-a267-

7de22a40fb87

a84a9652-ffd3-496e-a991-

22ba5529156a

DisplayText

Read and write privileged access to

Azure resources

Read and write privileged access to

Azure resources

Description

Allows the app to request and

manage time-based assignment and

just-in-time elevation of Azure

resources (like your subscriptions,

resource groups, storage, compute)

in your organization, without a

signed-in user.

Allows the app to request and manage

time-based assignment and just-in-

time elevation of user privileges to

manage Azure resources (like

subscriptions, resource groups,

storage, compute) on behalf of the

signed-in users.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

cd4161cb-f098-48f8-a884-

1eda9a42434c

02a32cc4-7ab5-4b58-879a-

0586e0f7c495

**PrivilegedAccess.ReadWrite.AzureResources**

ﾉ

**Expand table**

**PrivilegedAssignmentSchedule.Read.AzureADGroup**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read assignment schedules for access

to Azure AD groups

Read assignment schedules for access

to Azure AD groups

Description

Allows the app to read time-based

assignment schedules for access to

Azure AD groups, without a signed-in

user.

Allows the app to read time-based

assignment schedules for access to

Azure AD groups, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

41202f2c-f7ab-45be-b001-

85c9728b9d69

06dbc45d-6708-4ef0-a797-

f797ee68bf4b

DisplayText

Read, create, and delete assignment

schedules for access to Azure AD

groups

Read, create, and delete assignment

schedules for access to Azure AD

groups

Description

Allows the app to read, create, and

delete time-based assignment

schedules for access to Azure AD

groups, without a signed-in user.

Allows the app to read, create, and

delete time-based assignment

schedules for access to Azure AD

groups, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

55d1104b-3821-413d-b3ca-

e2393d333cd3

ca5fe595-68ff-4dfd-907d-4509501a0e49

DisplayText

Delete assignment schedules for

access to Azure AD groups

Delete assignment schedules for access

to Azure AD groups

**PrivilegedAssignmentSchedule.ReadWrite.AzureADGroup**

ﾉ

**Expand table**

**PrivilegedAssignmentSchedule.Remove.AzureADGroup**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Delete time-based assignment

schedules for access to Azure AD

groups, without a signed-in user.

Allows the app to delete time-based

assignment schedules for access to Azure

AD groups, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

edb419d6-7edc-42a3-9345-

509bfdf5d87c

8f44f93d-ecef-46ae-a9bf-

338508d44d6b

DisplayText

Read eligibility schedules for access

to Azure AD groups

Read eligibility schedules for access to

Azure AD groups

Description

Allows the app to read time-based

eligibility schedules for access to

Azure AD groups, without a signed-

in user.

Allows the app to read time-based

eligibility schedules for access to Azure

AD groups, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

618b6020-bca8-4de6-99f6-

ef445fa4d857

ba974594-d163-484e-ba39-

c330d5897667

DisplayText

Read, create, and delete eligibility

schedules for access to Azure AD

groups

Read, create, and delete eligibility

schedules for access to Azure AD

groups

Description

Allows the app to read, create, and

delete time-based eligibility

Allows the app to read, create, and

delete time-based eligibility schedules

**PrivilegedEligibilitySchedule.Read.AzureADGroup**

ﾉ

**Expand table**

**PrivilegedEligibilitySchedule.ReadWrite.AzureADGroup**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

schedules for access to Azure AD

groups, without a signed-in user.

for access to Azure AD groups, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

55745561-7572-4314-a737-

a2c2a1b0dd2e

c5ea9ab4-9b41-4c09-a400-

53e652fb5096

DisplayText

Delete eligibility schedules for

access to Azure AD groups

Delete eligibility schedules for access to

Azure AD groups

Description

Delete time-based eligibility

schedules for access to Azure AD

groups, without a signed-in user.

Allows the app to delete time-based

eligibility schedules for access to Azure

AD groups, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

14dad69e-099b-42c9-810b-d002981feec1

DisplayText

-

View users' basic profile

Description

-

Allows the app to see your users' basic profile (e.g., name,

picture, user name, email address)

AdminConsentRequired

-

No

![](./assets/output_353_1.png)![](./assets/output_353_2.png)

The _profile_ delegated permission is available for consent in personal Microsoft accounts.

_profile_ is an OpenID Connect (OIDC) scope.

**PrivilegedEligibilitySchedule.Remove.AzureADGroup**

ﾉ

**Expand table**

**profile**

ﾉ

**Expand table**

You can use the OIDC scopes to specify artifacts that you want returned in Azure AD

authorization and token requests. They are supported differently by the Azure AD v1.0 and v2.0

endpoints.

With the Azure AD v1.0 endpoint, only the _openid_ scope is used. You specify it in the _scope_

parameter in an authorization request to return an ID token when you use the OpenID Connect

protocol to sign in a user to your app. For more information, see Authorize access to web

applications using OpenID Connect and Azure Active Directory. To successfully return an ID

token, you must also make sure that the _User.Read_ permission is configured when you register

your app.

With the Azure AD v2.0 endpoint, you specify the _offline\_access_ scope in the _scope_ parameter

to explicitly request a refresh token when using the OAuth 2.0 or OpenID Connect protocols.

With OpenID Connect, you specify the _openid_ scope to request an ID token. You can also

specify the _email_ scope, _profile_ scope, or both to return additional claims in the ID token. You

do not need to specify the _User.Read_ permission to return an ID token with the v2.0 endpoint.

For more information, see OpenID Connect scopes.

The Microsoft Authentication Library (MSAL) currently specifies _offline\_access_, _openid_, _profile_,

and _email_ by default in authorization and token requests. This means that, for the default case,

if you specify these scopes explicitly, Azure AD may return an error.

**Category**

**Application**

**Delegated**

Identifier

e24d31aa-e1ab-4c80-85fe-

23018690335d

469cd065-729e-4dee-b1fa-

d92e0fab6310

DisplayText

Read profile photo of a user or group

Read profile photo of a user or group

Description

Allows the app to read all profile

photos of users and groups, without

a signed-in user

Allows the app to read all profile

photos of users and groups, on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**ProfilePhoto.Read.All**

ﾉ

**Expand table**

**ProfilePhoto.ReadWrite.All**

**Category**

**Application**

**Delegated**

Identifier

27baa7f6-5dfb-4ba8-b1d3-

1e812c143013

f5b24df7-511e-48bb-ae88-

643f023b55e1

DisplayText

Read and write profile photo of a

user or group

Read and write profile photo of a user

or group

Description

Allows the app to read and write all

profile photos of users and groups,

without a signed-in user

Allows the app to read and write all

profile photos of users and groups, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

eedb7fdd-7539-4345-a38b-

4839e4a84cbd

c492a2e1-2f8f-4caa-b076-

99bbf6e40fe4

DisplayText

Read all programs

Read all programs that user can access

Description

Allows the app to read programs and

program controls in the

organization, without a signed-in

user.

Allows the app to read programs and

program controls that the signed-in

user has access to in the organization.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

60a901ed-09f7-4aa5-a16e-

7dd3d6f9de36

50fd364f-9d93-4ae1-b170-

300e87cccf84

DisplayText

Manage all programs

Manage all programs that user can

access

ﾉ

**Expand table**

**ProgramControl.Read.All**

ﾉ

**Expand table**

**ProgramControl.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read, update,

delete and perform actions on

programs and program controls in

the organization, without a signed-in

user.

Allows the app to read, update, delete

and perform actions on programs and

program controls that the signed-in

user has access to in the organization.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e5a76501-dbb0-492c-ab55-

5d09e8837263

98f5a27a-539a-48bc-a597-

f78e9e1e76bf

DisplayText

Compute Purview policies at tenant

scope

Compute Purview policies at tenant

scope

Description

Allows the app to identify Purview

data protection, compliance and

governance policy scopes defined for

all users across tenant.

Allows the app to identify Purview

data protection, compliance and

governance policy scopes defined for

all users across tenant.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

fe696d63-5e1f-4515-8232-

cccc316903c6

4fc04d16-a9fc-4c5e-8da4-

79b6c33638a4

DisplayText

Compute Purview policies for an

individual user

Compute Purview policies for an

individual user

Description

Allows the app to identify Purview

data protection, compliance and

Allows the app to identify Purview

data protection, compliance and

**ProtectionScopes.Compute.All**

ﾉ

**Expand table**

**ProtectionScopes.Compute.User**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

governance policy scopes defined for

an individual user.

governance policy scopes defined for

an individual user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

091937d3-3e38-47a1-8649-

b2f99d3035f1

95aec97b-cf27-4a8d-a67d-

42f60b5b38ef

DisplayText

Read all provisioning log data

Read provisioning log data

Description

Allows the app to read and query

your provisioning log activities,

without a signed-in user.

Allows the app to read and query your

provisioning log activities, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

214fda0c-514a-4650-b037-

b562b1a66124

04a4b2a2-3f26-4fc8-87ee-

9c46e68db175

DisplayText

Read all certificate based

authentication configurations

Read certificate based authentication

configurations

Description

Allows the application to read

certificate-based authentication

configuration such as all public key

infrastructures (PKI) and certificate

authorities (CA) configured for the

organization, without a signed-in

user.

Allows the application to read

certificate-based authentication

configuration such as all public key

infrastructures (PKI) and certificate

authorities (CA) configured for the

organization, on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**ProvisioningLog.Read.All**

ﾉ

**Expand table**

**PublicKeyInfrastructure.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

a2b63618-5350-462d-b1b3-

ba6eb3684e26

3591b7f3-dba8-4bad-b667-

7a64bd4f2b83

DisplayText

Read and write all certificate based

authentication configurations

Read and write certificate based

authentication configurations

Description

Allows the application to read and

write certificate-based authentication

configuration such as all public key

infrastructures (PKI) and certificate

authorities (CA) configured for the

organization, without a signed-in

user.

Allows the application to read and

write certificate-based authentication

configuration such as all public key

infrastructures (PKI) and certificate

authorities (CA) configured for the

organization, on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ee49e170-1dd1-4030-b44c-

61ad6e98f743

f73fa04f-b9a5-4df9-8843-993ce928925e

DisplayText

Read all Question and Answers

Read all Questions and Answers that the

user can access.

Description

Allows an app to read all question

and answers, without a signed-in

user.

Allows an app to read all question and

answer sets that the signed-in user can

access.

AdminConsentRequired

Yes

No

**PublicKeyInfrastructure.ReadWrite.All**

ﾉ

**Expand table**

**QnA.Read.All**

ﾉ

**Expand table**

**RealTimeActivityFeed.Read.All**

**Category**

**Application**

**Delegated**

Identifier

abafe00f-ea87-4c63-b8a8-

0e7bb0a88144

db5d5bae-0c9e-444e-9390-

8a5fea98c253

DisplayText

Access real-time enriched data in a

meeting as an app

Access real-time enriched data in a

meeting

Description

Allows the app to get direct access to

real-time enriched data in a meeting,

without a signed-in user.

Allows the app to get direct access to

real-time enriched data in a meeting,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ac3a2b8e-03a3-4da9-9ce0-

cbe28bf1accd

07f995eb-fc67-4522-ad66-

2b8ca8ea3efd

DisplayText

Read Records Management

configuration, labels and policies

Read Records Management

configuration, labels, and policies

Description

Allows the application to read any

data from Records Management,

such as configuration, labels, and

policies without the signed in user.

Allows the application to read any

data from Records Management, such

as configuration, labels, and policies

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

eb158f57-df43-4751-8b21-

b8932adb3d34

f2833d75-a4e6-40ab-86d4-

6dfe73c97605

ﾉ

**Expand table**

**RecordsManagement.Read.All**

ﾉ

**Expand table**

**RecordsManagement.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write Records Management

configuration, labels and policies

Read and write Records Management

configuration, labels, and policies

Description

Allow the application to create,

update and delete any data from

Records Management, such as

configuration, labels, and policies

without the signed in user.

Allow the application to create,

update and delete any data from

Records Management, such as

configuration, labels, and policies on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

230c1aed-a721-4c5d-9cb4-

a90514e508ef

02e97553-ed7b-43d0-ab3c-

f8bace0d040c

DisplayText

Read all usage reports

Read all usage reports

Description

Allows an app to read all service

usage reports without a signed-in

user. Services that provide usage

reports include Office 365 and Azure

Active Directory.

Allows an app to read all service usage

reports on behalf of the signed-in

user. Services that provide usage

reports include Office 365 and Azure

Active Directory.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ee353f83-55ef-4b78-82da-

555bfa2b4b95

84fac5f4-33a9-4100-aa38-

a20c6d29e5e7

DisplayText

Read all admin report settings

Read admin report settings

Description

Allows the app to read all admin

report settings, such as whether to

Allows the app to read admin report

settings, such as whether to display

**Reports.Read.All**

ﾉ

**Expand table**

**ReportSettings.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

display concealed information in

reports, without a signed-in user.

concealed information in reports, on

behalf of the signed-in user

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2a60023f-3219-47ad-baa4-

40e17cd02a1d

b955410e-7715-4a88-a940-

dfd551018df3

DisplayText

Read and write all admin report

settings

Read and write admin report settings

Description

Allows the app to read and update all

admin report settings, such as

whether to display concealed

information in reports, without a

signed-in user.

Allows the app to read and update

admin report settings, such as

whether to display concealed

information in reports, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

cb530fca-534b-4e72-aa74-bca7e8bbd06f

DisplayText

-

Read resource specific permissions granted on a chat

Description

-

Allows the app to read the resource specific permissions granted

on the chat, on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**ReportSettings.ReadWrite.All**

ﾉ

**Expand table**

**ResourceSpecificPermissionGrant.ReadForChat**

ﾉ

**Expand table**

**ResourceSpecificPermissionGrant.ReadForChat.All**

**Category**

**Application**

**Delegated**

Identifier

2ff643d8-43e4-4a9b-88c1-86cb4a4b4c2f

-

DisplayText

Read resource specific permissions granted on a chat

-

Description

Allows the app to read the resource specific permissions granted

on the chat without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

eafad40c-bf7a-415a-b7f8-acdf5706b58f

DisplayText

-

Read resource specific permissions granted on a team

Description

-

Allows the app to read the resource specific permissions granted

on the team, on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

ad4600ae-d900-42cb-a9a2-2415d05593d0

-

DisplayText

Read resource specific permissions granted on a team

-

Description

Allows the app to read the resource specific permissions granted

on the team without a signed-in user.

-

AdminConsentRequired

Yes

-

ﾉ

**Expand table**

**ResourceSpecificPermissionGrant.ReadForTeam**

ﾉ

**Expand table**

**ResourceSpecificPermissionGrant.ReadForTeam.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

f1d91a8f-88e7-4774-8401-b668d5bca0c5

DisplayText

-

Read resource specific permissions granted on a user account

Description

-

Allows the app to read the resource specific permissions granted

on a user account, on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

acfca4d5-f49f-40ed-9648-84068b474c73

-

DisplayText

Read all resource specific permissions granted on user accounts

-

Description

Allows the app to read all resource specific permissions granted

on user accounts, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

2a6baefd-edea-4ff6-b24e-

bebcaa27a50d

e197c06f-ae7b-4398-b0a2-

89f76ebca159

DisplayText

Read all identity risk prevention

providers

Read all identity risk prevention

providers

**ResourceSpecificPermissionGrant.ReadForUser**

ﾉ

**Expand table**

**ResourceSpecificPermissionGrant.ReadForUser.All**

ﾉ

**Expand table**

**RiskPreventionProviders.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read your

organization's risk prevention

providers, without a signed-in user.

Allows the app to read your

organization's risk prevention

providers, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7fc7225d-eb37-4c39-90f3-

a33a57cf1081

2a7babba-9623-4109-bc9c-

79728cf3bb4f

DisplayText

Read and write all identity risk

prevention providers

Read and write all identity risk

prevention providers

Description

Allows the app to read and write

your organization's risk prevention

providers, without a signed-in user.

Allows the app to read and write your

organization's risk prevention

providers, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

d5fe8ce8-684c-4c83-a52c-

46e882ce4be1

344a729c-0285-42c6-9014-

f12b9b8d6129

DisplayText

Read all active role assignments and

role schedules for your company's

directory

Read all active role assignments for

your company's directory

Description

Allows the app to read the active role-

based access control (RBAC)

assignments and schedules for your

company's directory, without a signed-

Allows the app to read the active

role-based access control (RBAC)

assignments for your company's

directory, on behalf of the signed-in

**RiskPreventionProviders.ReadWrite.All**

ﾉ

**Expand table**

**RoleAssignmentSchedule.Read.Directory**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

in user. This includes reading directory

role templates, and directory roles.

user. This includes reading directory

role templates, and directory roles.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

dd199f4a-f148-40a4-a2ec-

f0069cc799ec

8c026be3-8e26-4774-9372-8d5d6f21daff

DisplayText

Read, update, and delete all

policies for privileged role

assignments of your

company's directory

Read, update, and delete all active role

assignments for your company's directory

Description

Allows the app to read,

update, and delete policies for

privileged role-based access

control (RBAC) assignments of

your company's directory,

without a signed-in user.

Allows the app to read and manage the

active role-based access control (RBAC)

assignments for your company's directory, on

behalf of the signed-in user. This includes

managing active directory role membership,

and reading directory role templates,

directory roles and active memberships.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

d3495511-98b7-4df3-b317-

4e35c19f6129

f71cd05c-3fdb-4568-aef2-

e1cf62ee20d4

DisplayText

Delete all active role assignments of

your company's directory

Delete all active role assignments for

your company's directory

Description

Delete all active privileged role-

based access control (RBAC)

Allows the app to delete the active role-

based access control (RBAC)

**RoleAssignmentSchedule.ReadWrite.Directory**

ﾉ

**Expand table**

**RoleAssignmentSchedule.Remove.Directory**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

assignments of your company's

directory, without a signed-in user.

assignments for your company's

directory, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ff278e11-4a33-4d0c-83d2-

d01dc58929a5

eb0788c2-6d4e-4658-8c9e-

c0fb8053f03d

DisplayText

Read all eligible role assignments and

role schedules for your company's

directory

Read all eligible role assignments for

your company's directory

Description

Allows the app to read the eligible

role-based access control (RBAC)

assignments and schedules for your

company's directory, without a signed-

in user. This includes reading directory

role templates, and directory roles.

Allows the app to read the eligible

role-based access control (RBAC)

assignments for your company's

directory, on behalf of the signed-in

user. This includes reading directory

role templates, and directory roles.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

fee28b28-e1f3-4841-818e-

2704dc62245f

62ade113-f8e0-4bf9-a6ba-

5acb31db32fd

DisplayText

Read, update, and delete all eligible

role assignments and schedules for

your company's directory

Read, update, and delete all eligible

role assignments for your company's

directory

Description

Allows the app to read and manage

the eligible role-based access control

Allows the app to read and manage

the eligible role-based access control

**RoleEligibilitySchedule.Read.Directory**

ﾉ

**Expand table**

**RoleEligibilitySchedule.ReadWrite.Directory**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

(RBAC) assignments and schedules for

your company's directory, without a

signed-in user. This includes

managing eligible directory role

membership, and reading directory

role templates, directory roles and

eligible memberships.

(RBAC) assignments for your

company's directory, on behalf of the

signed-in user. This includes

managing eligible directory role

membership, and reading directory

role templates, directory roles and

eligible memberships.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

79c7e69c-0d9f-4eff-97a8-

49170a5a08ba

58ac4fa2-b484-4d6e-ba97-

beee2a574220

DisplayText

Delete all eligible role assignments

of your company's directory

Delete all eligible role assignments for

your company's directory

Description

Delete all eligible privileged role-

based access control (RBAC)

assignments of your company's

directory, without a signed-in user.

Allows the app to delete the eligible

role-based access control (RBAC)

assignments for your company's

directory, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

c7fbd983-d9aa-4fa7-84b8-

17382c103bc4

48fec646-b2ba-4019-8681-

8eb31435aded

DisplayText

Read role management data for all

RBAC providers

Read role management data for all

RBAC providers

**RoleEligibilitySchedule.Remove.Directory**

ﾉ

**Expand table**

**RoleManagement.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read role-based

access control (RBAC) settings for all

RBAC providers without a signed-in

user. This includes reading role

definitions and role assignments.

Allows the app to read the role-based

access control (RBAC) settings for all

RBAC providers, on behalf of the

signed-in user. This includes reading

role definitions and role assignments.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

031a549a-bb80-49b6-8032-

2068448c6a3c

9619b88a-8a25-48a7-9571-d23be0337a79

DisplayText

Read Cloud PC RBAC settings

Read Cloud PC RBAC settings

Description

Allows the app to read the

Cloud PC role-based access

control (RBAC) settings,

without a signed-in user.

Allows the app to read the Cloud PC role-

based access control (RBAC) settings, on

behalf of the signed-in user. This includes

reading Cloud PC role definitions and role

assignments.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

4d6e30d1-e64e-4ae7-bf9d-

c706cc928cef

dd689728-6eb8-4deb-bd38-2924a935f3de

DisplayText

Read M365 Defender RBAC

configuration

Read M365 Defender RBAC configuration

Description

Allows the app to read the

role-based access control

(RBAC) settings for your

Allows the app to read the role-based access

control (RBAC) settings for your company's

directory, on behalf of the signed-in user.

**RoleManagement.Read.CloudPC**

ﾉ

**Expand table**

**RoleManagement.Read.Defender**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

company's directory, without a

signed-in user.

This includes reading M365 Defender role

definitions and role assignments.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

483bed4a-2ad3-4361-a73b-

c83ccdbdc53c

741c54c3-0c1e-44a1-818b-

3f97ab4e8c83

DisplayText

Read all directory RBAC settings

Read directory RBAC settings

Description

Allows the app to read the role-based

access control (RBAC) settings for

your company's directory, without a

signed-in user. This includes reading

directory role templates, directory

roles and memberships.

Allows the app to read the role-based

access control (RBAC) settings for your

company's directory, on behalf of the

signed-in user. This includes reading

directory role templates, directory

roles and memberships.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

c769435f-f061-4d0b-8ff1-

3d39870e5f85

3bc15058-7858-4141-b24f-

ae43b4e80b52

DisplayText

Read Exchange Online RBAC

configuration

Read Exchange Online RBAC

configuration

Description

Allows the app to read the role-based

access control (RBAC) configuration

for your organization's Exchange

Online service, without a signed-in

user. This includes reading Exchange

management role definitions, role

Allows the app to read the role-based

access control (RBAC) settings for your

organization's Exchange Online

service, on behalf of the signed-in

user. This includes reading Exchange

management role definitions, role

**RoleManagement.Read.Directory**

ﾉ

**Expand table**

**RoleManagement.Read.Exchange**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

groups, role group membership, role

assignments, management scopes,

and role assignment policies.

groups, role group membership, role

assignments, management scopes,

and role assignment policies.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

274d0592-d1b6-44bd-af1d-

26d259bcb43a

501d06f8-07b8-4f18-b5c6-

c191a4af7a82

DisplayText

Read and write all Cloud PC RBAC

settings

Read and write Cloud PC RBAC

settings

Description

Allows the app to read and manage

the Cloud PC role-based access

control (RBAC) settings, without a

signed-in user. This includes reading

and managing Cloud PC role

definitions and memberships.

Allows the app to read and manage

the Cloud PC role-based access

control (RBAC) settings, on behalf of

the signed-in user. This includes

reading and managing Cloud PC role

definitions and role assignments.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

8b7e8c0a-7e9d-4049-97ec-

04b5e1bcaf05

d8914f8f-9f64-4bd1-b4d3-f5a701ed8457

DisplayText

Read M365 Defender RBAC

configuration

Read M365 Defender RBAC configuration

Description

Allows the app to read the

role-based access control

(RBAC) settings for your

Allows the app to read the role-based access

control (RBAC) settings for your company's

directory, on behalf of the signed-in user.

**RoleManagement.ReadWrite.CloudPC**

ﾉ

**Expand table**

**RoleManagement.ReadWrite.Defender**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

company's directory, without a

signed-in user.

This includes reading M365 Defender role

definitions and role assignments.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

9e3f62cf-ca93-4989-b6ce-

bf83c28f9fe8

d01b97e9-cbc0-49fe-810a-

750afd5527a3

DisplayText

Read and write all directory RBAC

settings

Read and write directory RBAC

settings

Description

Allows the app to read and manage

the role-based access control (RBAC)

settings for your company's directory,

without a signed-in user. This

includes instantiating directory roles

and managing directory role

membership, and reading directory

role templates, directory roles and

memberships.

Allows the app to read and manage

the role-based access control (RBAC)

settings for your company's directory,

on behalf of the signed-in user. This

includes instantiating directory roles

and managing directory role

membership, and reading directory

role templates, directory roles and

memberships.

AdminConsentRequired

Yes

Yes

**RoleManagement.ReadWrite.Directory**

ﾉ

**Expand table**

Ｕ **Caution**

Permissions that allow granting authorization, such as

_RoleManagement.ReadWrite.Directory_, allow an application to grant additional privileges

to itself, other applications, or any user. Use caution when granting any of these

permissions.

With the _RoleManagement.ReadWrite.Directory_ permission an application can read and

write `/directoryRoles` and `/roleManagement/directory/*` . This includes adding and

removing members to and from Microsoft Entra roles, and working with PIM for Microsoft

Entra roles APIs.

**Category**

**Application**

**Delegated**

Identifier

025d3225-3f02-4882-b4c0-

cd5b541a4e80

c1499fe0-52b1-4b22-bed2-

7a244e0e879f

DisplayText

Read and write Exchange Online RBAC

configuration

Read and write Exchange Online RBAC

configuration

Description

Allows the app to read and manage

the role-based access control (RBAC)

settings for your organization's

Exchange Online service, without a

signed-in user. This includes reading,

creating, updating, and deleting

Exchange management role

definitions, role groups, role group

membership, role assignments,

management scopes, and role

assignment policies.

Allows the app to read and manage

the role-based access control (RBAC)

settings for your organization's

Exchange Online service, on behalf of

the signed-in user. This includes

reading, creating, updating, and

deleting Exchange management role

definitions, role groups, role group

membership, role assignments,

management scopes, and role

assignment policies.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ef31918f-2d50-4755-8943-

b8638c0a077e

cce71173-f76d-446e-97ff-

efb2d82e11b1

DisplayText

Read all alert data for your company's

directory

Read all alert data for your company's

directory

Description

Allows the app to read all role-based

access control (RBAC) alerts for your

company's directory, without a

signed-in user. This includes reading

alert statuses, alert definitions, alert

configurations and incidents that lead

to an alert.

Allows the app to read the role-based

access control (RBAC) alerts for your

company's directory, on behalf of the

signed-in user. This includes reading

alert statuses, alert definitions, alert

configurations and incidents that lead

to an alert.

AdminConsentRequired

Yes

Yes

**RoleManagement.ReadWrite.Exchange**

ﾉ

**Expand table**

**RoleManagementAlert.Read.Directory**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

11059518-d6a6-4851-98ed-

509268489c4a

435644c6-a5b1-40bf-8f52-

fe8e5b53e19c

DisplayText

Read all alert data, configure alerts,

and take actions on all alerts for your

company's directory

Read all alert data, configure alerts,

and take actions on all alerts for your

company's directory

Description

Allows the app to read and manage

all role-based access control (RBAC)

alerts for your company's directory,

without a signed-in user. This includes

managing alert settings, initiating

alert scans, dismissing alerts,

remediating alert incidents, and

reading alert statuses, alert

definitions, alert configurations and

incidents that lead to an alert.

Allows the app to read and manage

the role-based access control (RBAC)

alerts for your company's directory, on

behalf of the signed-in user. This

includes managing alert settings,

initiating alert scans, dismissing alerts,

remediating alert incidents, and

reading alert statuses, alert definitions,

alert configurations and incidents that

lead to an alert.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

69e67828-780e-47fd-b28c-

7b27d14864e6

7e26fdff-9cb1-4e56-bede-

211fe0e420e8

DisplayText

Read all policies in PIM for Groups

Read all policies in PIM for Groups

Description

Allows the app to read policies in

Privileged Identity Management for

Groups, without a signed-in user.

Allows the app to read policies in

Privileged Identity Management for

Groups, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**RoleManagementAlert.ReadWrite.Directory**

ﾉ

**Expand table**

**RoleManagementPolicy.Read.AzureADGroup**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

fdc4c997-9942-4479-bfcb-

75a36d1138df

3de2cdbe-0ff5-47d5-bdee-

7f45b4749ead

DisplayText

Read all policies for privileged role

assignments of your company's

directory

Read all policies for privileged role

assignments of your company's

directory

Description

Allows the app to read policies for

privileged role-based access control

(RBAC) assignments of your

company's directory, without a

signed-in user.

Allows the app to read policies for

privileged role-based access control

(RBAC) assignments of your company's

directory, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

b38dcc4d-a239-4ed6-aa84-

6c65b284f97c

0da165c7-3f15-4236-b733-

c0b0f6abe41d

DisplayText

Read, update, and delete all policies

in PIM for Groups

Read, update, and delete all policies in

PIM for Groups

Description

Allows the app to read, update, and

delete policies in Privileged Identity

Management for Groups, without a

signed-in user.

Allows the app to read, update, and

delete policies in Privileged Identity

Management for Groups, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**RoleManagementPolicy.Read.Directory**

ﾉ

**Expand table**

**RoleManagementPolicy.ReadWrite.AzureADGroup**

ﾉ

**Expand table**

**RoleManagementPolicy.ReadWrite.Directory**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

31e08e0a-d3f7-4ca2-ac39-

7343fb83e8ad

1ff1be21-34eb-448c-9ac9-

ce1f506b2a68

DisplayText

Read, update, and delete all policies

for privileged role assignments of

your company's directory

Read, update, and delete all policies

for privileged role assignments of your

company's directory

Description

Allows the app to read, update, and

delete policies for privileged role-

based access control (RBAC)

assignments of your company's

directory, without a signed-in user.

Allows the app to read, update, and

delete policies for privileged role-

based access control (RBAC)

assignments of your company's

directory, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

0b21c159-dbf4-4dbb-a6f6-490e412c716e

-

DisplayText

Trigger working time policies and read the working time status

-

Description

Allows the app to trigger the working time policies and read the

working time status for other users in your organization, without

a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

7b2ebf90-d836-437f-b90d-

7b62722c4456

fccf6dd8-5706-49fa-811f-

69e2e1b585d0

DisplayText

Read all schedule items

Read user schedule items

**Schedule-WorkingTime.ReadWrite.All**

ﾉ

**Expand table**

**Schedule.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read all schedules,

schedule groups, shifts and

associated entities in the Teams or

Shifts application without a signed-in

user.

Allows the app to read schedule,

schedule groups, shifts and associated

entities in the Teams or Shifts

application on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

b7760610-0545-4e8a-9ec3-

cce9e63db01c

63f27281-c9d9-4f29-94dd-

6942f7f1feb0

DisplayText

Read and write all schedule items

Read and write user schedule items

Description

Allows the app to manage all

schedules, schedule groups, shifts and

associated entities in the Teams or

Shifts application without a signed-in

user.

Allows the app to manage schedule,

schedule groups, shifts and associated

entities in the Teams or Shifts

application on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7239b71d-b402-4150-b13d-

78ecfe8df441

07919803-6073-4cd8-bc55-

28077db0ee10

DisplayText

Read/Write schedule permissions for

a role

Read/Write schedule permissions for a

role.

Description

Allows the app to read/write

schedule permissions for a specific

Allows the app to read/write schedule

permissions for a specific role in Shifts

**Schedule.ReadWrite.All**

ﾉ

**Expand table**

**SchedulePermissions.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

role in Shifts application without a

signed-in user.

application on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ada977a5-b8b1-493b-9a91-

66c206d76ecf

7d307522-aa38-4cd0-bd60-

90c6f0ac50bd

DisplayText

Read your organization's search

configuration

Read your organization's search

configuration

Description

Allows the app to read search

configurations, without a signed-in

user.

Allows the app to read search

configuration, on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

0e778b85-fefa-466d-9eec-

750569d92122

b1a7d408-cab0-47d2-a2a5-

a74a3733600d

DisplayText

Read and write your organization's

search configuration

Read and write your organization's

search configuration

Description

Allows the app to read and write

search configurations, without a

signed-in user.

Allows the app to read and write

search configuration, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**SearchConfiguration.Read.All**

ﾉ

**Expand table**

**SearchConfiguration.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

5e0edab9-c148-49d0-b423-

ac253e121825

1638cddf-07a4-4de2-8645-

69c96cacad73

DisplayText

Read your organization's security

actions

Read your organization's security

actions

Description

Allows the app to read security

actions, without a signed-in user.

Allows the app to read security actions,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f2bf083f-0179-402a-bedb-

b2784de8a49b

dc38509c-b87d-4da0-bd92-

6bec988bac4a

DisplayText

Read and update your organization's

security actions

Read and update your organization's

security actions

Description

Allows the app to read or update

security actions, without a signed-in

user.

Allows the app to read or update

security actions, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

472e4a4d-bb4a-4026-98d1-

0b0d74cb74a5

bc257fb8-46b4-4b15-8713-

01e91bfbe4ea

**SecurityActions.Read.All**

ﾉ

**Expand table**

**SecurityActions.ReadWrite.All**

ﾉ

**Expand table**

**SecurityAlert.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read all security alerts

Read all security alerts

Description

Allows the app to read all security

alerts, without a signed-in user.

Allows the app to read all security

alerts, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ed4fca05-be46-441f-9803-

1873825f8fdb

471f2a7f-2a42-4d45-a2bf-

594d0838070d

DisplayText

Read and write to all security alerts

Read and write to all security alerts

Description

Allows the app to read and write to

all security alerts, without a signed-

in user.

Allows the app to read and write to all

security alerts, on behalf of the signed-

in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

b48f7ac2-044d-4281-b02f-

75db744d6f5f

53e6783e-b127-4a35-ab3a-

6a52d80a9077

DisplayText

Read metadata and detection details

for all emails in your organization

Read metadata and detection details

for emails in your organization

Description

Read email metadata and security

detection details, without a signed-in

user.

Read email metadata and security

detection details on behalf of the

signed in user.

AdminConsentRequired

Yes

Yes

**SecurityAlert.ReadWrite.All**

ﾉ

**Expand table**

**SecurityAnalyzedMessage.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

04c55753-2244-4c25-87fc-

704ab82a4f69

48eb8c83-6e58-46e7-a6d3-

8805822f5940

DisplayText

Read metadata, detection details, and

execute remediation actions on all

emails in your organization

Read metadata, detection details, and

execute remediation actions on emails

in your organization

Description

Read email metadata and security

detection details, and execute

remediation actions like deleting an

email, without a signed-in user.

Read email metadata, security

detection details, and execute

remediation actions like deleting an

email, on behalf of the signed in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

84499c31-ac2e-44d3-a0cf-a6c386d4dfe8

DisplayText

-

Read all Security Copilot resources for the signed-in user

Description

-

Allows the app to read all Security Copilot signed-in user's

resources on behalf of the signed-in user

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

-

206291b0-2167-47a7-a640-6cdc1df710ba

DisplayText

-

Read and write individually owned Security Copilot resources of

**SecurityAnalyzedMessage.ReadWrite.All**

ﾉ

**Expand table**

**SecurityCopilotWorkspaces.Read.All**

ﾉ

**Expand table**

**SecurityCopilotWorkspaces.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

the signed-in user

Description

-

Allows the app to read and write Security Copilot resources

owned by the signed-in user on their behalf.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

bf394140-e372-4bf9-a898-

299cfc7564e5

64733abd-851e-478a-bffb-

e47a14b18235

DisplayText

Read your organization's security

events

Read your organization's security

events

Description

Allows the app to read your

organization's security events

without a signed-in user.

Allows the app to read your

organization's security events on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

d903a879-88e0-4c09-b0c9-

82f6a1333f84

6aedf524-7e1c-45a7-bd76-

ded8cab8d0fc

DisplayText

Read and update your

organization's security events

Read and update your organization's

security events

Description

Allows the app to read your

organization's security events

without a signed-in user. Also

allows the app to update editable

properties in security events.

Allows the app to read your

organization's security events on behalf

of the signed-in user. Also allows the app

to update editable properties in security

events on behalf of the signed-in user.

**SecurityEvents.Read.All**

ﾉ

**Expand table**

**SecurityEvents.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

c5bc96f5-b4a1-4cfc-8189-d5f0d772278f

3e9ed69a-a48e-473c-8b97-

413016703a37

DisplayText

Read all identity security available identity

accounts

Read identity security available

identity accounts

Description

Allows the app to read all the identity

security available identity accounts

without a signed-in user.

Allows the app to read all the

identity security available identity

accounts

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

af2bf46f-7bf1-4be3-8bad-

e17e279e8462

818229ce-20e4-47bd-92f4-

bc94dbb37a56

DisplayText

Read and perform all identity

security available actions

Read and perform identity security

available actions

Description

Allows the app to read and write

identity security available actions

without a signed-in user.

Allows the app to read and write

identity security available actions on

behalf of the signed-in identity.

AdminConsentRequired

Yes

Yes

**SecurityIdentitiesAccount.Read.All**

ﾉ

**Expand table**

**SecurityIdentitiesActions.ReadWrite.All**

ﾉ

**Expand table**

**SecurityIdentitiesAutoConfig.Read.All**

**Category**

**Application**

**Delegated**

Identifier

58971758-9844-4fe4-9fba-

7e4ce7a659bf

8ff90903-1ecb-4f3a-b8b2-

42120374ecd6

DisplayText

Read sensors window auditing

configuration

Read sensors window auditing

configuration

Description

Allows the app to read sensors

window auditing configuration

without a signed-in user

Allows the app to read the sensors

window auditing configuration of the

signed in user

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

4f1f0deb-08d1-4ffb-8cca-

21dfc362b7c0

b810fdb4-8733-43bd-9b37-

fddb7215c69f

DisplayText

Read and write sensors window

auditing configuration

Read and write sensors window

auditing configuration

Description

Allows the app to read and write

sensors window auditing

configuration without a signed-in user

Allows the app to read and write the

sensors window auditing

configuration of the signed in user

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f8dcd971-5d83-4e1e-aa95-

ef44611ad351

a0d0da43-a6df-4416-b63d-

99c79991aae8

DisplayText

Read all identity security health issues

Read identity security health issues

ﾉ

**Expand table**

**SecurityIdentitiesAutoConfig.ReadWrite.All**

ﾉ

**Expand table**

**SecurityIdentitiesHealth.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read all the identity

security health issues without a signed-

in user.

Allows the app to read all the

identity security health issues of

signed user

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ab03ddd5-7ae4-4f2e-8af8-

86654f7e0a27

53e51eec-2d9b-4990-97f3-

c9aa5d5652c3

DisplayText

Read and write all identity security

health issues

Read and write identity security health

issues

Description

Allows the app to read and write

identity security health issues

without a signed-in user.

Allows the app to read and write

identity security health issues on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

5f0ffea2-f474-4cf2-9834-61cda2bcea5c

2c221239-7c5c-4b30-9355-

d84663bfcd96

DisplayText

Read all identity security sensors

Read identity security sensors

Description

Allows the app to read all the identity

security sensors without a signed-in

user.

Allows the app to read all the

identity security sensors of signed

user

AdminConsentRequired

Yes

Yes

**SecurityIdentitiesHealth.ReadWrite.All**

ﾉ

**Expand table**

**SecurityIdentitiesSensors.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

d4dcee6d-0774-412a-b06c-

aeabbd99e816

087c3ad9-c2ca-4b82-9885-

d5e25ce9e183

DisplayText

Read and write all identity security

sensors

Read and write identity security sensors

Description

Allows the app to read and write

identity security sensors without a

signed-in user.

Allows the app to read and write

identity security sensors on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

3e5d0bee-973f-4736-a123-

4e1ab146f3a8

c7d0a939-da1c-4aca-80fa-

d0a6cd924801

DisplayText

Read all identity security available user

actions

Read identity security available user

actions

Description

Allows the app to read all the identity

security available user actions without a

signed-in user.

Allows the app to read all the

identity security available user

actions of signed user

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

b4146a3a-dd4f-4af4-8d91-

7cc0eef3d041

bf230e97-1957-4df6-b3f6-

57f9029eacdf

**SecurityIdentitiesSensors.ReadWrite.All**

ﾉ

**Expand table**

**SecurityIdentitiesUserActions.Read.All**

ﾉ

**Expand table**

**SecurityIdentitiesUserActions.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and perform all identity security

available user actions

Read and perform identity security

available user actions

Description

Allows the app to read and write

identity security available user

actions without a signed-in user.

Allows the app to read and write

identity security available user actions

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

45cc0394-e837-488b-a098-

1918f48d186c

b9abcc4f-94fc-4457-9141-

d20ce80ec952

DisplayText

Read all security incidents

Read incidents

Description

Allows the app to read all security

incidents, without a signed-in user.

Allows the app to read security

incidents, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

34bf0e97-1971-4929-b999-

9e2442d941d7

128ca929-1a19-45e6-a3b8-

435ec44a36ba

DisplayText

Read and write to all security incidents

Read and write to incidents

Description

Allows the app to read and write to all

security incidents, without a signed-in

user.

Allows the app to read and write

security incidents, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**SecurityIncident.Read.All**

ﾉ

**Expand table**

**SecurityIncident.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

57f0b71b-a759-45a0-9a0f-

cc099fbd9a44

a4633e44-d355-4474-99df-

8c2de6b0e39e

DisplayText

Evaluate sensitivity labels

Evaluate sensitivity labels

Description

Allow the app to determine if there is

any sensitivity label to be applied

automatically to the content or

recommended to the user for manual

application, without a signed-in user.

Allow the app to determine if there is

any sensitivity label to be applied

automatically to the content or

recommended to the user for manual

application, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

986fa56a-6680-4aac-af09-

4d1765376739

a42e3c42-b31e-4919-b699-

696dca5dc9e7

DisplayText

Evaluate labels tenant scope.

Evaluate labels tenant scope.

Description

Allows the app to evaluate all

sensitivity label.

Allows the app to evaluate all

sensitivity label.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

3b8e7aad-f6e3-4299-83f8-

6fc6a5777f0b

1aeb73ce-68d7-49b7-913a-

eedc80844551

**SensitivityLabel.Evaluate**

ﾉ

**Expand table**

**SensitivityLabel.Evaluate.All**

ﾉ

**Expand table**

**SensitivityLabel.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Get labels application scope.

Get labels user scope.

Description

Allows the app to get sensitivity

labels.

Allows the app to get sensitivity labels.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e46a01e9-b2cf-4d89-8424-

bcdc6dd445ab

8b377c27-ea19-4863-a948-

8a8588c8f2c3

DisplayText

Get labels tenant scope.

Get labels app scope.

Description

Allows the app to get sensitivity labels.

Allows the app to get sensitivity

labels.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

2b655018-450a-4845-81e7-

d603b1ebffdb

1fe7aa48-9373-4a47-8df3-

168335e0f4c9

DisplayText

Read all Exchange service activity

Read all Exchange service activity

Description

Allows the app to read all Exchange

service activity, without a signed-in

user.

Allows the app to read all Exchange

service activity, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**SensitivityLabels.Read.All**

ﾉ

**Expand table**

**ServiceActivity-Exchange.Read.All**

ﾉ

**Expand table**

**ServiceActivity-Microsoft365Web.Read.All**

**Category**

**Application**

**Delegated**

Identifier

c766cb16-acc4-4663-ba09-

6eedef5876c5

d74c75b1-d5a9-479d-902d-

92f8f99182c1

DisplayText

Read all Microsoft 365 Web service

activity

Read all Microsoft 365 Web service

activity

Description

Allows the app to read all Microsoft

365 Web service activity, without a

signed-in user.

Allows the app to read all Microsoft

365 Web service activity, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

57b4f899-b8c5-47c7-bdd3-

c410c55602b7

347e3c16-30f3-4ac7-9b52-

fc3c053de9c9

DisplayText

Read all One Drive service activity

Read all One Drive service activity

Description

Allows the app to read all One Drive

service activity, without a signed-in

user.

Allows the app to read all One Drive

service activity, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

4dfee10b-fa4a-41b5-b34d-

ccf54cc0c394

404d76f0-e10e-460a-92be-

ef19600c54d1

DisplayText

Read all Teams service activity

Read all Teams service activity

ﾉ

**Expand table**

**ServiceActivity-OneDrive.Read.All**

ﾉ

**Expand table**

**ServiceActivity-Teams.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read all Teams

service activity, without a signed-in

user.

Allows the app to read all Teams service

activity, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

79c261e0-fe76-4144-aad5-

bdc68fbe4037

55896846-df78-47a7-aa94-

8d3d4442ca7f

DisplayText

Read service health

Read service health

Description

Allows the app to read your tenant's

service health information, without a

signed-in user. Health information

may include service issues or service

health overviews.

Allows the app to read your tenant's

service health information on behalf of

the signed-in user. Health information

may include service issues or service

health overviews.

AdminConsentRequired

Yes

Yes

![](./assets/output_390_1.png)![](./assets/output_390_2.png)

The _ServiceHealth.Read.All_ delegated permission is available for consent in personal

Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

1b620472-6534-4fe6-9df2-

4680e8aa28ec

eda39fa6-f8cf-4c3c-a909-

432c683e4c9b

DisplayText

Read service messages

Read service announcement messages

Description

Allows the app to read your tenant's

service announcement messages,

without a signed-in user. Messages

Allows the app to read your tenant's

service announcement messages on

behalf of the signed-in user. Messages

**ServiceHealth.Read.All**

ﾉ

**Expand table**

**ServiceMessage.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

may include information about new

or changed features.

may include information about new or

changed features.

AdminConsentRequired

Yes

Yes

![](./assets/output_391_1.png)![](./assets/output_391_2.png)

The _ServiceMessage.Read.All_ delegated permission is available for consent in personal

Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

-

636e1b0b-1cc2-4b1c-9aa9-4eeed9b9761b

DisplayText

-

Update user status on service announcement messages

Description

-

Allows the app to update service announcement messages' user

status on behalf of the signed-in user. The message status can

be marked as read, archive, or favorite.

AdminConsentRequired

-

Yes

![](./assets/output_391_3.png)![](./assets/output_391_4.png)

The _ServiceMessageViewpoint.Write_ delegated permission is available for consent in personal

Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

5256681e-b7f6-40c0-8447-

2d9db68797a0

9f9ce928-e038-4e3b-8faf-

7b59049a8ddc

DisplayText

Read service principal endpoints

Read service principal endpoints

Description

Allows the app to read service

principal endpoints

Allows the app to read service

principal endpoints

AdminConsentRequired

Yes

Yes

**ServiceMessageViewpoint.Write**

ﾉ

**Expand table**

**ServicePrincipalEndpoint.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

89c8469c-83ad-45f7-8ff2-

6e3d4285709e

7297d82c-9546-4aed-91df-

3d4f0a9b3ff0

DisplayText

Read and update service principal

endpoints

Read and update service principal

endpoints

Description

Allows the app to update service

principal endpoints

Allows the app to update service

principal endpoints

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

a0521574-fcd8-4742-b29c-

f796df57ea70

c608c170-08b5-466b-a8fe-

0b4074b01613

DisplayText

Read, write and manage SharePoint

Cross-Tenant migration settings and

tasks

Read, write and manage SharePoint

Cross-Tenant migration settings and

tasks

Description

Allows the app to read, write and

manage your tenant's SharePoint

Cross-Tenant migration settings and

tasks, without a signed-in user.

Allows the app to read, write and

manage your tenant's SharePoint

Cross-Tenant migration settings and

tasks, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**ServicePrincipalEndpoint.ReadWrite.All**

ﾉ

**Expand table**

**SharePointCrossTenantMigration.Manage.All**

ﾉ

**Expand table**

**SharePointCrossTenantMigration.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

f5fa52a5-b9ab-4dc3-885e-

9e5b4a67068e

00dcb678-f9af-4e73-acb1-

4f1657364629

DisplayText

Read SharePoint Cross-Tenant

migration settings and tasks

Read SharePoint Cross-Tenant

migration settings and tasks

Description

Allows the app to read your tenant's

SharePoint Cross-Tenant migration

settings and tasks, without a signed-

in user.

Allows the app to read your tenant's

SharePoint Cross-Tenant migration

settings and tasks, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

83d4163d-a2d8-4d3b-9695-

4ae3ca98f888

2ef70e10-5bfd-4ede-a5f6-

67720500b258

DisplayText

Read SharePoint and OneDrive

tenant settings

Read SharePoint and OneDrive tenant

settings

Description

Allows the application to read the

tenant-level settings of SharePoint

and OneDrive, without a signed-in

user.

Allows the application to read the

tenant-level settings in SharePoint and

OneDrive on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

19b94e34-907c-4f43-bde9-

38b1909ed408

aa07f155-3612-49b8-a147-

6c590df35536

DisplayText

Read and change SharePoint and

OneDrive tenant settings

Read and change SharePoint and

OneDrive tenant settings

**SharePointTenantSettings.Read.All**

ﾉ

**Expand table**

**SharePointTenantSettings.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the application to read and

change the tenant-level settings of

SharePoint and OneDrive, without a

signed-in user.

Allows the application to read and

change the tenant-level settings of

SharePoint and OneDrive on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

50f66e47-eb56-45b7-aaa2-75057d9afe08

DisplayText

-

Read short notes of the signed-in user

Description

-

Allows the app to read all the short notes a sign-in user has

access to.

AdminConsentRequired

-

No

![](./assets/output_394_1.png)![](./assets/output_394_2.png)

The _ShortNotes.Read_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

0c7d31ec-31ca-4f58-b6ec-9950b6b0de69

-

DisplayText

Read all users' short notes

-

Description

Allows the app to read all the short notes without a signed-in

user.

-

AdminConsentRequired

Yes

-

**ShortNotes.Read**

ﾉ

**Expand table**

**ShortNotes.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

328438b7-4c01-4c07-a840-e625a749bb89

DisplayText

-

Read, create, edit, and delete short notes of the signed-in user

Description

-

Allows the app to read, create, edit, and delete short notes of a

signed-in user.

AdminConsentRequired

-

No

![](./assets/output_395_1.png)![](./assets/output_395_2.png)

The _ShortNotes.ReadWrite_ delegated permission is available for consent in personal

Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

842c284c-763d-4a97-838d-79787d129bab

-

DisplayText

Read, create, edit, and delete all users' short notes

-

Description

Allows the app to read, create, edit, and delete all the short notes

without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

28e1fe78-598f-4df4-b55e-

18bf34218925

458e1edc-1e75-438c-8c7b-

c32115c9d373

DisplayText

Read all sign-in identifiers

Read SignInIdentifiers

**ShortNotes.ReadWrite**

ﾉ

**Expand table**

**ShortNotes.ReadWrite.All**

ﾉ

**Expand table**

**SignInIdentifier.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read your

organization's sign-in identifiers,

without a signed-in user.

Allows the app to read your

organization's sign-in identifiers, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

7fc588a2-ea2d-4d1f-bcf7-

33c324b149b8

b4673c3c-7b5a-4012-9826-

7c7e3c8db6af

DisplayText

Read and write all sign-in identifiers

Read and write all sign-in identifiers

Description

Allows the app to read and write your

organization's sign-in identifiers,

without a signed-in user.

Allows the app to read and write your

organization's sign-in identifiers, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e3530185-4080-478c-a4ab-39322704df58

-

DisplayText

Archive/reactivate Site Collections without a signed in user.

-

Description

Allow the application to archive/reactivate site collections without

a signed in user.

-

AdminConsentRequired

Yes

-

**SignInIdentifier.ReadWrite.All**

ﾉ

**Expand table**

**Sites.Archive.All**

ﾉ

**Expand table**

**Sites.Create.All**

**Category**

**Application**

**Delegated**

Identifier

80819dd8-2b3b-4551-a1ad-

2700fc44f533

0e2e68e1-3f32-4e10-9281-

f749e097fcbe

DisplayText

Create Site Collections without a

signed in user.

Create Site Collections, on behalf of

the signed-in user

Description

Allow the application to create site

collections without a signed in user.

Upon creation the application will be

granted Sites.Selected(application) +

FullControl to the newly created site.

Allow the application to create site

collections on behalf of the signed in

user. Upon creation the application

will be granted

Sites.Selected(delegated) +

FullControl to the newly created site.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

a82116e5-55eb-4c41-a434-

62fe8a61c773

5a54b8b3-347c-476d-8f8e-

42d5c7424d29

DisplayText

Have full control of all site

collections

Have full control of all site collections

Description

Allows the app to have full control

of all site collections without a

signed in user.

Allows the application to have full

control of all site collections on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

![](./assets/output_397_1.png)![](./assets/output_397_2.png)

The _Sites.FullControl.All_ delegated permission is available for consent in personal Microsoft

accounts.

ﾉ

**Expand table**

**Sites.FullControl.All**

ﾉ

**Expand table**

**Sites.Manage.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

0c0bf378-bf22-4481-8f81-

9e89a9b4960a

65e50fdc-43b7-4915-933e-

e8138f11f40a

DisplayText

Create, edit, and delete items and

lists in all site collections

Create, edit, and delete items and lists

in all site collections

Description

Allows the app to create or delete

document libraries and lists in all site

collections without a signed in user.

Allows the application to create or

delete document libraries and lists in all

site collections on behalf of the signed-

in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

332a536c-c7ef-4017-ab91-

336970924f0d

205e70e5-aba6-4c52-a976-

6d2d46c48043

DisplayText

Read items in all site collections

Read items in all site collections

Description

Allows the app to read documents

and list items in all site collections

without a signed in user.

Allows the application to read

documents and list items in all site

collections on behalf of the signed-in

user

AdminConsentRequired

Yes

No

![](./assets/output_398_1.png)![](./assets/output_398_2.png)

The _Sites.Read.All_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

9492366f-7969-46a4-8d15-

ed1a20078fff

89fe6a52-be36-487e-b7d8-

d061c450a026

**Sites.Read.All**

ﾉ

**Expand table**

**Sites.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write items in all site

collections

Edit or delete items in all site

collections

Description

Allows the app to create, read,

update, and delete documents and list

items in all site collections without a

signed in user.

Allows the application to edit or

delete documents and list items in all

site collections on behalf of the

signed-in user.

AdminConsentRequired

Yes

No

![](./assets/output_399_1.png)![](./assets/output_399_2.png)

The _Sites.ReadWrite.All_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

883ea226-0bf2-4a8f-9f9d-

92c9162a727d

f89c84ef-20d0-4b54-87e9-

02e856d66d53

DisplayText

Access selected site collections

Access selected Sites, on behalf of the

signed-in user

Description

Allow the application to access a

subset of site collections without a

signed in user. The specific site

collections and the permissions

granted will be configured in

SharePoint Online.

Allow the application to access a

subset of site collections on behalf of

the signed-in user. The specific site

collections and the permissions

granted will be configured in

SharePoint Online.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

-

258f6531-6087-4cc4-bb90-092c5fb3ed3f

**Sites.Selected**

ﾉ

**Expand table**

**SMTP.Send**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

-

Send emails from mailboxes using SMTP AUTH.

Description

-

Allows the app to be able to send emails from the user's mailbox

using the SMTP AUTH client submission protocol.

AdminConsentRequired

-

No

![](./assets/output_400_1.png)![](./assets/output_400_2.png)

The _SMTP.Send_ delegated permission is available for consent in personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

dcdfc277-41fd-4d68-ad0c-

c3057235bd8e

9b4aa4b1-aaf3-41b7-b743-

698b27e77ff6

DisplayText

Read SPIFFE trust domains and child

resources

Read SPIFFE trust domains and child

resources

Description

Allows the app to read your

organization's SPIFFE trust domains

and child resources without a signed in

user.

Allows the app to read your

organization's SPIFFE trust domains

and child resources on behalf of the

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

17b78cfd-eeff-447d-8bab-

2795af00055a

8ba47079-8c47-4bfe-b2ce-

13f28ef37247

DisplayText

Read and write SPIFFE trust domains

and child resources

Read and write SPIFFE trust domains

and child resources

Description

Allows the app to read and write your

organization's SPIFFE trust domains

Allows the app to read and write your

organization's SPIFFE trust domains

**SpiffeTrustDomain.Read.All**

ﾉ

**Expand table**

**SpiffeTrustDomain.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

and child resources without a signed

in user.

and child resources on behalf of the

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

6eff534b-699e-44d9-af61-a4182f0ec37e

fd1d61cb-4e4b-4d15-a6d2-

161348681d84

DisplayText

Read and write all Viva Engage storylines

Read and write all Viva Engage

storylines

Description

Allows the app to modify Viva Engage

storylines, read all storylines properties,

update storyline properties, and delete

storyline properties without a signed-in

user.

Allows the app to modify the Viva

Engage storyline and read all

storyline properties on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

ee1460f0-368b-4153-870a-

4e1ca7e72c42

9c3af74c-fd0f-4db4-b17a-

71939e2a9d77

DisplayText

Read all subject rights requests

Read subject rights requests

Description

Allows the app to read subject rights

requests without a signed-in user.

Allows the app to read subject rights

requests on behalf of the signed-in

user

AdminConsentRequired

Yes

Yes

**Storyline.ReadWrite.All**

ﾉ

**Expand table**

**SubjectRightsRequest.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

8387eaa4-1a3c-41f5-b261-

f888138e6041

2b8fcc74-bce1-4ae3-a0e8-

60c53739299d

DisplayText

Read and write all subject rights

requests

Read and write subject rights requests

Description

Allows the app to read and write

subject rights requests without a

signed in user.

Allows the app to read and write

subject rights requests on behalf of the

signed-in user

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

5f88184c-80bb-4d52-9ff2-757288b2e9b7

DisplayText

-

Read all webhook subscriptions

Description

-

Allows the app to read all webhook subscriptions on behalf of

the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

5ba43d2f-fa88-4db2-bd1c-

a67c5f0fb1ce

7aa02aeb-824f-4fbe-a3f7-

611f751f5b55

DisplayText

Read all Azure AD synchronization

data.

Read all Azure AD synchronization

data

**SubjectRightsRequest.ReadWrite.All**

ﾉ

**Expand table**

**Subscription.Read.All**

ﾉ

**Expand table**

**Synchronization.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the application to read Azure

AD synchronization information,

without a signed-in user.

Allows the app to read Azure AD

synchronization information, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

9b50c33d-700f-43b1-b2eb-

87e89b703581

7bb27fa3-ea8f-4d67-a916-

87715b6188bd

DisplayText

Read and write all Azure AD

synchronization data.

Read and write all Azure AD

synchronization data

Description

Allows the application to configure

the Azure AD synchronization service,

without a signed-in user.

Allows the app to configure the Azure

AD synchronization service, on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

db31e92a-b9ea-4d87-bf6a-

75a37a9ca35a

1a2e7420-4e92-4d2b-94cb-

fb2952e9ddf7

DisplayText

Upload user data to the identity

synchronization service

Upload user data to the identity

synchronization service

Description

Allows the application to upload bulk

user data to the identity

synchronization service, without a

signed-in user.

Allows the app to upload bulk user

data to the identity synchronization

service, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Synchronization.ReadWrite.All**

ﾉ

**Expand table**

**SynchronizationData-User.Upload**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

25c32ff3-849a-494b-b94f-20a8ac4e6774

-

DisplayText

Upload user data to the identity sync service for apps that this

application creates or owns

-

Description

Allows the application to upload bulk user data to the identity

synchronization service for apps that this application creates or

owns, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

f45671fb-e0fe-4b4b-be20-3d3ce43f1bcb

DisplayText

-

Read user's tasks and task lists

Description

-

Allows the app to read the signed-in user's tasks and task lists,

including any shared with the user. Doesn't include permission

to create, delete, or update anything.

AdminConsentRequired

-

No

![](./assets/output_404_1.png)![](./assets/output_404_2.png)

The _Tasks.Read_ delegated permission is available for consent in personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

f10e1f91-74ed-437f-a6fd-d6ae88e26c1f

-

**SynchronizationData-User.Upload.OwnedBy**

ﾉ

**Expand table**

**Tasks.Read**

ﾉ

**Expand table**

**Tasks.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read all users' tasks and tasklist

-

Description

Allows the app to read all users' tasks and task lists in your

organization, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

88d21fd4-8e5a-4c32-b5e2-4a1c95f34f72

DisplayText

-

Read user and shared tasks

Description

-

Allows the app to read tasks a user has permissions to access,

including their own and shared tasks.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

-

2219042f-cab5-40cc-b0d2-16b1540b4c5f

DisplayText

-

Create, read, update, and delete user's tasks and task lists

Description

-

Allows the app to create, read, update, and delete the signed-in

user's tasks and task lists, including any shared with the user.

AdminConsentRequired

-

No

![](./assets/output_405_1.png)![](./assets/output_405_2.png)

The _Tasks.ReadWrite_ delegated permission is available for consent in personal Microsoft

accounts.

**Tasks.Read.Shared**

ﾉ

**Expand table**

**Tasks.ReadWrite**

ﾉ

**Expand table**

**Tasks.ReadWrite.All**

**Category**

**Application**

**Delegated**

Identifier

44e666d1-d276-445b-a5fc-8815eeb81d55

-

DisplayText

Read and write all users' tasks and tasklists

-

Description

Allows the app to create, read, update and delete all users' tasks

and task lists in your organization, without a signed-in user

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

c5ddf11b-c114-4886-8558-8a4e557cd52b

DisplayText

-

Read and write user and shared tasks

Description

-

Allows the app to create, read, update, and delete tasks a user

has permissions to, including their own and shared tasks.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

23fc2474-f741-46ce-8465-

674744c5c361

7825d5d6-6049-4ce7-bdf6-

3b8d53f4bcd0

DisplayText

Create teams

Create teams

Description

Allows the app to create teams

without a signed-in user.

Allows the app to create teams on

behalf of the signed-in user.

AdminConsentRequired

Yes

No

ﾉ

**Expand table**

**Tasks.ReadWrite.Shared**

ﾉ

**Expand table**

**Team.Create**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

2280dda6-0bfd-44ee-a2f4-

cb867cfc4c1e

485be79e-c497-4b35-9400-0e3fa7f2a5d4

DisplayText

Get a list of all teams

Read the names and descriptions of teams

Description

Get a list of all teams, without

a signed-in user.

Read the names and descriptions of teams,

on behalf of the signed-in user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

660b7406-55f1-41ca-a0ed-

0b035e182f3e

2497278c-d82d-46a2-b1ce-

39d4cdde5570

DisplayText

Read the members of all teams

Read the members of teams

Description

Read the members of all teams,

without a signed-in user.

Read the members of teams, on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

0121dc95-1b9f-4aed-8bac-

58c5ac466691

4a06efd2-f825-4e34-813e-

82a57b03d1ee

DisplayText

Add and remove members from all

teams

Add and remove members from

teams

**Team.ReadBasic.All**

ﾉ

**Expand table**

**TeamMember.Read.All**

ﾉ

**Expand table**

**TeamMember.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Add and remove members from all

teams, without a signed-in user. Also

allows changing a team member's

role, for example from owner to non-

owner.

Add and remove members from

teams, on behalf of the signed-in user.

Also allows changing a member's role,

for example from owner to non-

owner.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

4437522e-9a86-4a41-a7da-

e380edd4a97d

2104a4db-3a2f-4ea0-9dba-

143d457dc666

DisplayText

Add and remove members with non-

owner role for all teams

Add and remove members with non-

owner role for all teams

Description

Add and remove members from all

teams, without a signed-in user. Does

not allow adding or removing a

member with the owner role.

Additionally, does not allow the app

to elevate an existing member to the

owner role.

Add and remove members from all

teams, on behalf of the signed-in user.

Does not allow adding or removing a

member with the owner role.

Additionally, does not allow the app to

elevate an existing member to the

owner role.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

0e755559-83fb-4b44-91d0-4cc721b9323e

DisplayText

-

Read user's teamwork activity feed

Description

-

Allows the app to read the signed-in user's teamwork activity

feed.

**TeamMember.ReadWriteNonOwnerRole.All**

ﾉ

**Expand table**

**TeamsActivity.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

70dec828-f620-4914-aa83-a29117306807

-

DisplayText

Read all users' teamwork activity feed

-

Description

Allows the app to read all users' teamwork activity feed, without a

signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

a267235f-af13-44dc-8385-

c1dc93023186

7ab1d787-bae7-4d5d-8db6-

37ea32df9186

DisplayText

Send a teamwork activity to any user

Send a teamwork activity as the user

Description

Allows the app to create new

notifications in users' teamwork

activity feeds without a signed in user.

These notifications may not be

discoverable or be held or governed

by compliance policies.

Allows the app to create new

notifications in users' teamwork

activity feeds on behalf of the signed

in user. These notifications may not be

discoverable or be held or governed

by compliance policies.

AdminConsentRequired

Yes

No

**TeamsActivity.Read.All**

ﾉ

**Expand table**

**TeamsActivity.Send**

ﾉ

**Expand table**

**TeamsAppInstallation.ManageSelectedForChat**

**Category**

**Application**

**Delegated**

Identifier

-

d1ba22c6-3f02-4c91-addb-bc3399bcca88

DisplayText

-

Manage installation and permission grants of selected Teams

apps in chats

Description

-

Allows the app to read, install, upgrade, and uninstall selected

Teams apps in chats the signed-in user can access. Gives the

ability to manage permission grants for accessing those specific

chats' data.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

22b74aab-d9e4-46f7-9424-f24b42307227

-

DisplayText

Manage installation and permission grants of selected Teams

apps in all chats

-

Description

Allows the app to read, install, upgrade, and uninstall selected

Teams apps in any chat, without a signed-in user. Gives the ability

to manage permission grants for accessing those specific chats'

data.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

c67b2d7e-6b80-4218-938a-05e73058e42d

DisplayText

-

Manage installation and permission grants of selected Teams

apps in teams

ﾉ

**Expand table**

**TeamsAppInstallation.ManageSelectedForChat.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ManageSelectedForTeam**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Allows the app to read, install, upgrade, and uninstall Teams

apps in teams the signed-in user can access. Gives the ability to

manage permission grants for accessing those specific teams'

data.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

b448d252-1f26-4227-b6ff-21ab510975a2

-

DisplayText

Manage installation and permission grants of selected Teams

apps in all teams

-

Description

Allows the app to read, install, upgrade, and uninstall selected

Teams apps in any team, without a signed-in user. Gives the

ability to manage permission grants for accessing those specific

teams' data.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

830c2bd9-c335-4caf-bf83-c07fa8a23ef1

DisplayText

-

Manage installation and permission grants of selected Teams

apps in users' personal scope

Description

-

Allows the app to read, install, upgrade, and uninstall seleected

Teams apps in user accounts, on behalf of the signed-in user.

Gives the ability to manage permission grants for accessing

those specific users' data.

AdminConsentRequired

-

Yes

**TeamsAppInstallation.ManageSelectedForTeam.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ManageSelectedForUser**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

e97a9235-5b3c-43c4-b37d-6786a173fae4

-

DisplayText

Manage installation and permission grants of selected Teams

apps for all user accounts

-

Description

Allows the app to read, install, upgrade, and uninstall selected

Teams apps in any user account, without a signed-in user. Gives

the ability to manage permission grants for accessing those

specific users' data.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

0fdf35a5-82f8-41ff-9ded-0b761cc73512

-

DisplayText

Read installed Teams apps for all installation scopes

-

Description

Allows the app to read the Teams apps that are installed in any

scope, without a signed-in user. Does not give the ability to read

application-specific settings.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

bf3fbf03-f35f-4e93-963e-47e4d874c37a

DisplayText

-

Read installed Teams apps in chats

**TeamsAppInstallation.ManageSelectedForUser.All**

ﾉ

**Expand table**

**TeamsAppInstallation.Read.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadForChat**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Allows the app to read the Teams apps that are installed in chats

the signed-in user can access. Does not give the ability to read

application-specific settings.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

cc7e7635-2586-41d6-adaa-a8d3bcad5ee5

-

DisplayText

Read installed Teams apps for all chats

-

Description

Allows the app to read the Teams apps that are installed in any

chat, without a signed-in user. Does not give the ability to read

application-specific settings.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

5248dcb1-f83b-4ec3-9f4d-a4428a961a72

DisplayText

-

Read installed Teams apps in teams

Description

-

Allows the app to read the Teams apps that are installed in

teams the signed-in user can access. Does not give the ability to

read application-specific settings.

AdminConsentRequired

-

Yes

**TeamsAppInstallation.ReadForChat.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadForTeam**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadForTeam.All**

**Category**

**Application**

**Delegated**

Identifier

1f615aea-6bf9-4b05-84bd-46388e138537

-

DisplayText

Read installed Teams apps for all teams

-

Description

Allows the app to read the Teams apps that are installed in any

team, without a signed-in user. Does not give the ability to read

application-specific settings.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

c395395c-ff9a-4dba-bc1f-8372ba9dca84

DisplayText

-

Read user's installed Teams apps

Description

-

Allows the app to read the Teams apps that are installed for the

signed-in user. Does not give the ability to read application-

specific settings.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

9ce09611-f4f7-4abd-a629-a05450422a97

-

DisplayText

Read installed Teams apps for all users

-

Description

Allows the app to read the Teams apps that are installed for any

user, without a signed-in user. Does not give the ability to read

application-specific settings.

-

AdminConsentRequired

Yes

-

ﾉ

**Expand table**

**TeamsAppInstallation.ReadForUser**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadForUser.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

0f3420c2-c6ec-46de-ab72-fd51267087d5

DisplayText

-

Read selected installed Teams apps in chats

Description

-

Allows the app to read the selected Teams apps that are

installed in chats the signed-in user can access. Does not give

the ability to read application-specific settings.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

53d40ddb-9b27-4c97-b800-985be6041990

-

DisplayText

Read selected installed Teams apps in all chats

-

Description

Allows the app to read the selected Teams apps that are installed

in any chat, without a signed-in user. Does not give the ability to

read application-specific settings.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

b55df1c0-db20-435b-aef2-afe6ed487e16

DisplayText

-

Read selected installed Teams apps in teams

**TeamsAppInstallation.ReadSelectedForChat**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadSelectedForChat.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadSelectedForTeam**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Allows the app to read the selected Teams apps that are

installed in teams the signed-in user can access. Does not give

the ability to read application-specific settings.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

93c6a289-70fd-489e-a053-6cf8f7d772f6

-

DisplayText

Read selected installed Teams apps in all teams

-

Description

Allows the app to read the selected Teams apps that are installed

in any team, without a signed-in user. Does not give the ability to

read application-specific settings.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

fe2e4e1d-101f-4fb2-9cb1-9d6659db45d4

DisplayText

-

Read user's selected installed Teams apps

Description

-

Allows the app to read the selected Teams apps that are

installed for the signed-in user. Does not give the ability to read

application-specific settings.

AdminConsentRequired

-

Yes

**TeamsAppInstallation.ReadSelectedForTeam.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadSelectedForUser**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadSelectedForUser.All**

**Category**

**Application**

**Delegated**

Identifier

44fb0e7c-1f9a-47f1-bb9e-7f92d48ed288

-

DisplayText

Read selected installed Teams apps for all users

-

Description

Allows an app to read, install, upgrade, and uninstall selected

apps to any user, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

e1408a66-8f82-451b-a2f3-3c3e38f7413f

DisplayText

-

Manage installed Teams apps in chats

Description

-

Allows the app to read, install, upgrade, and uninstall Teams

apps in chats the signed-in user can access. Gives the ability to

manage permission grants for accessing those specific chats'

data.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

6e74eff9-4a21-45d6-bc03-3a20f61f8281

-

DisplayText

Manage installation and permission grants of Teams apps for all

chats

-

Description

Allows the app to read, install, upgrade, and uninstall Teams apps

in any chat, without a signed-in user. Gives the ability to manage

permission grants for accessing those specific chats' data.

-

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteAndConsentForChat**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteAndConsentForChat.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

946349d5-2a9d-4535-abc0-7beeacaedd1d

DisplayText

-

Manage installed Teams apps in teams

Description

-

Allows the app to read, install, upgrade, and uninstall Teams

apps in teams the signed-in user can access. Gives the ability to

manage permission grants for accessing those specific teams'

data.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

b0c13be0-8e20-4bc5-8c55-963c23a39ce9

-

DisplayText

Manage installation and permission grants of Teams apps for all

teams

-

Description

Allows the app to read, install, upgrade, and uninstall Teams apps

in any team, without a signed-in user. Gives the ability to manage

permission grants for accessing those specific teams' data.

-

AdminConsentRequired

Yes

-

**TeamsAppInstallation.ReadWriteAndConsentForTeam**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteAndConsentForTeam.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteAndConsentForUser**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

2da62c49-dfbd-40df-ba16-fef3529d391c

DisplayText

-

Manage installation and permission grants of Teams apps in

users' personal scope

Description

-

Allows the app to read, install, upgrade, and uninstall Teams

apps in user accounts, on behalf of the signed-in user. Gives the

ability to manage permission grants for accessing those specific

users' data.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

32ca478f-f89e-41d0-aaf8-101deb7da510

-

DisplayText

Manage installation and permission grants of Teams apps in a

user account

-

Description

Allows the app to read, install, upgrade, and uninstall Teams apps

in any user account, without a signed-in user. Gives the ability to

manage permission grants for accessing those specific users' data.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

a0e0e18b-8fb2-458f-8130-da2d7cab9c75

DisplayText

-

Allow the Teams app to manage itself and its permission grants

in chats

Description

-

Allows a Teams app to read, install, upgrade, and uninstall itself

in chats the signed-in user can access, and manage its

permission grants for accessing those specific chats' data.

**TeamsAppInstallation.ReadWriteAndConsentForUser.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteAndConsentSelfForChat**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

ba1ba90b-2d8f-487e-9f16-80728d85bb5c

-

DisplayText

Allow the Teams app to manage itself and its permission grants

for all chats

-

Description

Allows a Teams app to read, install, upgrade, and uninstall itself

for any chat, without a signed-in user, and manage its permission

grants for accessing those specific chats' data.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

4a6bbf29-a0e1-4a4d-a7d1-cef17f772975

DisplayText

-

Allow the Teams app to manage itself and its permission grants

in teams

Description

-

Allows a Teams app to read, install, upgrade, and uninstall itself

in teams the signed-in user can access, and manage its

permission grants for accessing those specific teams' data.

AdminConsentRequired

-

Yes

**TeamsAppInstallation.ReadWriteAndConsentSelfForChat.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteAndConsentSelfForTeam**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteAndConsentSelfForTeam.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

1e4be56c-312e-42b8-a2c9-009600d732c0

-

DisplayText

Allow the Teams app to manage itself and its permission grants

for all teams

-

Description

Allows a Teams app to read, install, upgrade, and uninstall itself

for any team, without a signed-in user, and manage its permission

grants for accessing those specific teams' data.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

7a349935-c54d-44ab-ab66-1b460d315be7

DisplayText

-

Allow the Teams app to manage itself and its permission grants

in user accounts

Description

-

Allows a Teams app to read, install, upgrade, and uninstall itself

in user accounts, and manage its permission grants for accessing

those specific users' data, on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

a87076cf-6abd-4e56-8559-4dbdf41bef96

-

DisplayText

Allow the Teams app to manage itself and its permission grants in

all user accounts

-

Description

Allows a Teams app to read, install, upgrade, and uninstall itself

for any user account, without a signed-in user, and manage its

permission grants for accessing those specific users' data.

-

**TeamsAppInstallation.ReadWriteAndConsentSelfForUser**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteAndConsentSelfForUser.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

aa85bf13-d771-4d5d-a9e6-bca04ce44edf

DisplayText

-

Manage installed Teams apps in chats

Description

-

Allows the app to read, install, upgrade, and uninstall Teams

apps in chats the signed-in user can access. Does not give the

ability to read application-specific settings.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

9e19bae1-2623-4c4f-ab6e-2664615ff9a0

-

DisplayText

Manage Teams apps for all chats

-

Description

Allows the app to read, install, upgrade, and uninstall Teams apps

in any chat, without a signed-in user. Does not give the ability to

read application-specific settings.

-

AdminConsentRequired

Yes

-

**TeamsAppInstallation.ReadWriteForChat**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteForChat.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteForTeam**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

2e25a044-2580-450d-8859-42eeb6e996c0

DisplayText

-

Manage installed Teams apps in teams

Description

-

Allows the app to read, install, upgrade, and uninstall Teams

apps in teams the signed-in user can access. Does not give the

ability to read application-specific settings.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

5dad17ba-f6cc-4954-a5a2-a0dcc95154f0

-

DisplayText

Manage Teams apps for all teams

-

Description

Allows the app to read, install, upgrade, and uninstall Teams apps

in any team, without a signed-in user. Does not give the ability to

read application-specific settings.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

093f8818-d05f-49b8-95bc-9d2a73e9a43c

DisplayText

-

Manage user's installed Teams apps

Description

-

Allows the app to read, install, upgrade, and uninstall Teams

apps installed for the signed-in user. Does not give the ability to

read application-specific settings.

AdminConsentRequired

-

Yes

**TeamsAppInstallation.ReadWriteForTeam.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteForUser**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

74ef0291-ca83-4d02-8c7e-d2391e6a444f

-

DisplayText

Manage Teams apps for all users

-

Description

Allows the app to read, install, upgrade, and uninstall Teams apps

for any user, without a signed-in user. Does not give the ability to

read application-specific settings.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

690aa3b6-4b71-41c2-a990-77a8c4768d2b

DisplayText

-

Manage selected Teams apps installed in chats

Description

-

Allows the app to read, install, upgrade, and uninstall selected

Teams apps in chats the signed-in user can access. Does not give

the ability to read application-specific settings.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

25bbeaad-04be-4207-83ed-a263aae76ddf

-

DisplayText

Manage selected installed Teams apps in all chats

-

Description

Allows the app to read, install, upgrade, and uninstall selected

Teams apps in any chat, without a signed-in user. Does not give

-

**TeamsAppInstallation.ReadWriteForUser.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteSelectedForChat**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteSelectedForChat.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

the ability to read application-specific settings.

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

9131c833-9a49-4c54-b38f-615ecfc4fc69

DisplayText

-

Manage selected Teams apps installed in teams

Description

-

Allows the app to read, install, upgrade, and uninstall selected

Teams apps in teams the signed-in user can access. Does not

give the ability to read application-specific settings.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

7b5823ae-d0f2-424d-b90c-d843ffada7d9

-

DisplayText

Manage selected installed Teams apps in all teams

-

Description

Allows the app to read, install, upgrade, and uninstall selected

Teams apps in any team, without a signed-in user. Does not give

the ability to read application-specific settings.

-

AdminConsentRequired

Yes

-

**TeamsAppInstallation.ReadWriteSelectedForTeam**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteSelectedForTeam.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteSelectedForUser**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

ea819e27-c92a-4118-b83b-4540b125d744

DisplayText

-

Manage selected Teams apps installed for a user

Description

-

Allows the app to read, install, upgrade, and uninstall selected

Teams apps installed for the signed in user. Does not give the

ability to read application-specific settings.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

650a76ec-4118-4b25-9d3a-1f98048a5ee0

-

DisplayText

Manage selected Teams apps installed for all users

-

Description

Allows the app to read, install, upgrade, and uninstall selected

Teams apps for any user, without a signed-in user. Does not give

the ability to read application-specific settings.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

0ce33576-30e8-43b7-99e5-62f8569a4002

DisplayText

-

Allow the Teams app to manage itself in chats

Description

-

Allows a Teams app to read, install, upgrade, and uninstall itself

in chats the signed-in user can access.

AdminConsentRequired

-

Yes

**TeamsAppInstallation.ReadWriteSelectedForUser.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteSelfForChat**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

73a45059-f39c-4baf-9182-4954ac0e55cf

-

DisplayText

Allow the Teams app to manage itself for all chats

-

Description

Allows a Teams app to read, install, upgrade, and uninstall itself

for any chat, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

0f4595f7-64b1-4e13-81bc-11a249df07a9

DisplayText

-

Allow the app to manage itself in teams

Description

-

Allows a Teams app to read, install, upgrade, and uninstall itself

to teams the signed-in user can access.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

9f67436c-5415-4e7f-8ac1-3014a7132630

-

DisplayText

Allow the Teams app to manage itself for all teams

-

Description

Allows a Teams app to read, install, upgrade, and uninstall itself in

any team, without a signed-in user.

-

AdminConsentRequired

Yes

-

**TeamsAppInstallation.ReadWriteSelfForChat.All**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteSelfForTeam**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteSelfForTeam.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

207e0cb1-3ce7-4922-b991-5a760c346ebc

DisplayText

-

Allow the Teams app to manage itself for a user

Description

-

Allows a Teams app to read, install, upgrade, and uninstall itself

for the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

908de74d-f8b2-4d6b-a9ed-2a17b3b78179

-

DisplayText

Allow the app to manage itself for all users

-

Description

Allows a Teams app to read, install, upgrade, and uninstall itself to

any user, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

242607bd-1d2c-432c-82eb-

bdb27baa23ab

48638b3c-ad68-4383-8ac4-

e6880ee6ca57

DisplayText

Read all teams' settings

Read teams' settings

Description

Read all team's settings, without a

signed-in user.

Read all teams' settings, on behalf of

the signed-in user.

**TeamsAppInstallation.ReadWriteSelfForUser**

ﾉ

**Expand table**

**TeamsAppInstallation.ReadWriteSelfForUser.All**

ﾉ

**Expand table**

**TeamSettings.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

bdd80a03-d9bc-451d-b7c4-

ce7c63fe3c8f

39d65650-9d3e-4223-80db-

a335590d027e

DisplayText

Read and change all teams' settings

Read and change teams' settings

Description

Read and change all teams' settings,

without a signed-in user.

Read and change all teams' settings, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

1801e8f4-cf09-4c4e-a1b5-

036dfcca6c90

6997c35c-a586-440c-8a0b-

4ffe5d118dc0

DisplayText

Read and Write Teams policy user

assignment and unassigment for all

policy types.

Read and Write Teams policy user

assignment and unassigment for all

policy types.

Description

Allow the app to read or write/update

the policy assignment and

unassigment for Teams users for all

policy type categories.

Allow the app to read or write/update

the policy assignment and

unassigment for Teams users for all

policy type categories.

AdminConsentRequired

Yes

Yes

**TeamSettings.ReadWrite.All**

ﾉ

**Expand table**

**TeamsPolicyUserAssign.ReadWrite.All**

ﾉ

**Expand table**

**TeamsResourceAccount.Read.All**

**Category**

**Application**

**Delegated**

Identifier

b55aa226-33a1-4396-bcf4-

edce5e7a31c1

ea2cbd09-253c-4f69-a0e6-

07383c5f07cc

DisplayText

Read Teams resource accounts

Read Teams resource accounts

Description

Allows the app to read your tenant's

resource accounts without a signed-

in user.

Allows the app to read your tenant's

resource accounts on behalf of the

signed-in admin user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

49981c42-fd7b-4530-be03-

e77b21aed25e

a9ff19c2-f369-4a95-9a25-

ba9d460efc8e

DisplayText

Create tabs in Microsoft Teams.

Create tabs in Microsoft Teams.

Description

Allows the app to create tabs in any

team in Microsoft Teams, without a

signed-in user. This does not grant

the ability to read, modify or delete

tabs after they are created, or give

access to the content inside the tabs.

Allows the app to create tabs in any

team in Microsoft Teams, on behalf of

the signed-in user. This does not grant

the ability to read, modify or delete

tabs after they are created, or give

access to the content inside the tabs.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

46890524-499a-4bb2-ad64-

1476b4f3e1cf

59dacb05-e88d-4c13-a684-

59f1afc8cc98

DisplayText

Read tabs in Microsoft Teams.

Read tabs in Microsoft Teams.

ﾉ

**Expand table**

**TeamsTab.Create**

ﾉ

**Expand table**

**TeamsTab.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Read the names and settings of tabs

inside any team in Microsoft Teams,

without a signed-in user. This does

not give access to the content inside

the tabs.

Read the names and settings of tabs

inside any team in Microsoft Teams, on

behalf of the signed-in user. This does

not give access to the content inside

the tabs.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

a96d855f-016b-47d7-b51c-

1218a98d791c

b98bfd41-87c6-45cc-b104-

e2de4f0dafb9

DisplayText

Read and write tabs in Microsoft

Teams.

Read and write tabs in Microsoft

Teams.

Description

Read and write tabs in any team in

Microsoft Teams, without a signed-in

user. This does not give access to the

content inside the tabs.

Read and write tabs in any team in

Microsoft Teams, on behalf of the

signed-in user. This does not give

access to the content inside the tabs.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

ee928332-e9c2-4747-b4a0-f8c164b68de6

DisplayText

-

Allow the Teams app to manage all tabs in chats

Description

-

Allows a Teams app to read, install, upgrade, and uninstall all

tabs in chats the signed-in user can access.

AdminConsentRequired

-

Yes

**TeamsTab.ReadWrite.All**

ﾉ

**Expand table**

**TeamsTab.ReadWriteForChat**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

fd9ce730-a250-40dc-bd44-8dc8d20f39ea

-

DisplayText

Allow the Teams app to manage all tabs for all chats

-

Description

Allows a Teams app to read, install, upgrade, and uninstall all tabs

for any chat, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

c975dd04-a06e-4fbb-9704-62daad77bb49

DisplayText

-

Allow the Teams app to manage all tabs in teams

Description

-

Allows a Teams app to read, install, upgrade, and uninstall all

tabs to teams the signed-in user can access.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

6163d4f4-fbf8-43da-a7b4-060fe85ed148

-

DisplayText

Allow the Teams app to manage all tabs for all teams

-

Description

Allows a Teams app to read, install, upgrade, and uninstall all tabs

in any team, without a signed-in user.

-

AdminConsentRequired

Yes

-

**TeamsTab.ReadWriteForChat.All**

ﾉ

**Expand table**

**TeamsTab.ReadWriteForTeam**

ﾉ

**Expand table**

**TeamsTab.ReadWriteForTeam.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

c37c9b61-7762-4bff-a156-afc0005847a0

DisplayText

-

Allow the Teams app to manage all tabs for a user

Description

-

Allows a Teams app to read, install, upgrade, and uninstall all

tabs for the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

425b4b59-d5af-45c8-832f-bb0b7402348a

-

DisplayText

Allow the app to manage all tabs for all users

-

Description

Allows a Teams app to read, install, upgrade, and uninstall all tabs

for any user, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

0c219d04-3abf-47f7-912d-5cca239e90e6

DisplayText

-

Allow the Teams app to manage only its own tabs in chats

Description

-

Allows a Teams app to read, install, upgrade, and uninstall its

own tabs in chats the signed-in user can access.

**TeamsTab.ReadWriteForUser**

ﾉ

**Expand table**

**TeamsTab.ReadWriteForUser.All**

ﾉ

**Expand table**

**TeamsTab.ReadWriteSelfForChat**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

9f62e4a2-a2d6-4350-b28b-d244728c4f86

-

DisplayText

Allow the Teams app to manage only its own tabs for all chats

-

Description

Allows a Teams app to read, install, upgrade, and uninstall its own

tabs for any chat, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

f266662f-120a-4314-b26a-99b08617c7ef

DisplayText

-

Allow the Teams app to manage only its own tabs in teams

Description

-

Allows a Teams app to read, install, upgrade, and uninstall its

own tabs to teams the signed-in user can access.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

91c32b81-0ef0-453f-a5c7-4ce2e562f449

-

**TeamsTab.ReadWriteSelfForChat.All**

ﾉ

**Expand table**

**TeamsTab.ReadWriteSelfForTeam**

ﾉ

**Expand table**

**TeamsTab.ReadWriteSelfForTeam.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Allow the Teams app to manage only its own tabs for all teams

-

Description

Allows a Teams app to read, install, upgrade, and uninstall its own

tabs in any team, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

395dfec1-a0b9-465f-a783-8250a430cb8c

DisplayText

-

Allow the Teams app to manage only its own tabs for a user

Description

-

Allows a Teams app to read, install, upgrade, and uninstall its

own tabs for the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

3c42dec6-49e8-4a0a-b469-36cff0d9da93

-

DisplayText

Allow the Teams app to manage only its own tabs for all users

-

Description

Allows a Teams app to read, install, upgrade, and uninstall its own

tabs for any user, without a signed-in user.

-

AdminConsentRequired

Yes

-

**TeamsTab.ReadWriteSelfForUser**

ﾉ

**Expand table**

**TeamsTab.ReadWriteSelfForUser.All**

ﾉ

**Expand table**

**TeamsTelephoneNumber.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

39b17d18-680c-41f4-b9c2-

5f30629e7cb6

1bc6eab1-058d-4557-b011-

d4c41cec88b7

DisplayText

Read Tenant-Acquired Telephone

Number Details

Read Tenant-Acquired Telephone

Number Details

Description

Allows the app to read your tenant's

acquired telephone number details,

without a signed-in user. Acquired

telephone numbers may include

attributes related to assigned object,

emergency location, network site,

etc.

Allows the app to read your tenant's

acquired telephone number details on

behalf of the signed-in admin user.

Acquired telephone numbers may

include attributes related to assigned

object, emergency location, network

site, etc.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

0a42382f-155c-4eb1-9bdc-

21548ccaa387

424b07a8-1209-4d17-9fe4-

9018a93a1024

DisplayText

Read and Modify Tenant-Acquired

Telephone Number Details

Read and Modify Tenant-Acquired

Telephone Number Details

Description

Allows the app to read your tenant's

acquired telephone number details,

without a signed-in user. Acquired

telephone numbers may include

attributes related to assigned object,

emergency location, network site,

etc.

Allows the app to read and modify your

tenant's acquired telephone number

details on behalf of the signed-in admin

user. Acquired telephone numbers may

include attributes related to assigned

object, emergency location, network

site, etc.

AdminConsentRequired

Yes

Yes

**TeamsTelephoneNumber.ReadWrite.All**

ﾉ

**Expand table**

**TeamsUserConfiguration.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

a91eadaf-2c3c-4362-908b-

fb172d208fc6

5c469ce4-dab5-4afd-b9de-

14f1ba4004a7

DisplayText

Read Teams user configurations

Read Teams user configurations

Description

Allows the app to read your tenant's

user configurations, without a

signed-in user. User configuration

may include attributes related to

user, such as telephone number,

assigned policies, etc.

Allows the app to read your tenant's

user configurations on behalf of the

signed-in admin user. User

configuration may include attributes

related to user, such as telephone

number, assigned policies, etc.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

cd87405c-5792-4f15-92f7-debc0db6d1d6

DisplayText

-

Read available Teams templates

Description

-

Allows the app to read the available Teams templates, on behalf

of the signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

6323133e-1f6e-46d4-9372-ac33a0870636

-

DisplayText

Read all available Teams Templates

-

Description

Allows the app to read all available Teams Templates, without a

signed-user.

-

AdminConsentRequired

Yes

-

**TeamTemplates.Read**

ﾉ

**Expand table**

**TeamTemplates.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

dfb0dd15-61de-45b2-be36-d6a69fba3c79

-

DisplayText

Create chat and channel messages with anyone's identity and

with any timestamp

-

Description

Allows the app to create chat and channel messages, without a

signed in user. The app specifies which user appears as the

sender, and can backdate the message to appear as if it was sent

long ago. The messages can be sent to any chat or channel in the

organization.

-

AdminConsentRequired

Yes

-

![](./assets/output_438_1.png)![](./assets/output_438_2.png)

The _Teamwork.Migrate.All_ delegated permission is available for consent in personal

Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

75bcfbce-a647-4fba-ad51-

b63d73b210f4

594f4bb6-c083-4cf9-8aa8-

213823bdf351

DisplayText

Read organizational teamwork

settings

Read organizational teamwork settings

Description

Allows the app to read all teamwork

settings of the organization without

a signed-in user.

Allows the app to read the teamwork

settings of the organization, on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Teamwork.Migrate.All**

ﾉ

**Expand table**

**Teamwork.Read.All**

ﾉ

**Expand table**

**TeamworkAppSettings.Read.All**

**Category**

**Application**

**Delegated**

Identifier

475ebe88-f071-4bd7-af2b-

642952bd4986

44e060c4-bbdc-4256-a0b9-

dcc0396db368

DisplayText

Read Teams app settings

Read Teams app settings

Description

Allows the app to read the Teams

app settings without a signed-in

user.

Allows the app to read the Teams app

settings on behalf of the signed-in

user.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

ab5b445e-8f10-45f4-9c79-

dd3f8062cc4e

87c556f0-2bd9-4eed-bd74-

5dd8af6eaf7e

DisplayText

Read and write Teams app settings

Read and write Teams app settings

Description

Allows the app to read and write the

Teams app settings without a signed-

in user.

Allows the app to read and write the

Teams app settings on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

0591bafd-7c1c-4c30-a2a5-

2b9aacb1dfe8

b659488b-9d28-4208-b2be-

1c6652b3c970

DisplayText

Read Teams devices

Read Teams devices

Description

Allow the app to read the

management data for Teams devices,

Allow the app to read the management

data for Teams devices on behalf of the

ﾉ

**Expand table**

**TeamworkAppSettings.ReadWrite.All**

ﾉ

**Expand table**

**TeamworkDevice.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

without a signed-in user.

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

79c02f5b-bd4f-4713-bc2c-

a8a4a66e127b

ddd97ecb-5c31-43db-a235-

0ee20e635c40

DisplayText

Read and write Teams devices

Read and write Teams devices

Description

Allow the app to read and write the

management data for Teams devices,

without a signed-in user.

Allow the app to read and write the

management data for Teams devices

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

57587d0b-8399-45be-b207-8050cec54575

DisplayText

-

Read tags in Teams

Description

-

Allows the app to read tags in Teams, on behalf of the signed-in

user.

AdminConsentRequired

-

Yes

**TeamworkDevice.ReadWrite.All**

ﾉ

**Expand table**

**TeamworkTag.Read**

ﾉ

**Expand table**

**TeamworkTag.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

b74fd6c4-4bde-488e-9695-eeb100e4907f

-

DisplayText

Read tags in Teams

-

Description

Allows the app to read tags in Teams without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

539dabd7-b5b6-4117-b164-d60cd15a8671

DisplayText

-

Read and write tags in Teams

Description

-

Allows the app to read and write tags in Teams, on behalf of the

signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

a3371ca5-911d-46d6-901c-42c8c7a937d8

-

DisplayText

Read and write tags in Teams

-

Description

Allows the app to read and write tags in Teams without a signed-

in user.

-

AdminConsentRequired

Yes

-

**TeamworkTag.ReadWrite**

ﾉ

**Expand table**

**TeamworkTag.ReadWrite.All**

ﾉ

**Expand table**

**TeamworkUserInteraction.Read.All**

**Category**

**Application**

**Delegated**

Identifier

-

b4d26916-07e0-4daf-9096-9f6d9174aa96

DisplayText

-

Read all of the possible Teams interactions between the user and

other users

Description

-

Allows the app to read all of the possible Teams interactions

between the signed-in user and other users

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

ea047cc2-df29-4f3e-83a3-

205de61501ca

297f747b-0005-475b-8fef-

c890f5152b38

DisplayText

Read all term store data

Read term store data

Description

Allows the app to read all term store

data, without a signed-in user. This

includes all sets, groups and terms in

the term store.

Allows the app to read the term store

data that the signed-in user has access

to. This includes all sets, groups and

terms in the term store.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f12eb8d6-28e3-46e6-b2c0-

b7e4dc69fc95

6c37c71d-f50f-4bff-8fd3-

8a41da390140

DisplayText

Read and write all term store data

Read and write term store data

Description

Allows the app to read, edit or write all

term store data, without a signed-in

Allows the app to read or modify data

that the signed-in user has access to.

ﾉ

**Expand table**

**TermStore.Read.All**

ﾉ

**Expand table**

**TermStore.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

user. This includes all sets, groups and

terms in the term store.

This includes all sets, groups and

terms in the term store.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

f8f035bb-2cce-47fb-8bf5-7baf3ecbee48

-

DisplayText

Read threat assessment requests

-

Description

Allows an app to read your organization's threat assessment

requests, without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

cac97e40-6730-457d-ad8d-4852fddab7ad

DisplayText

-

Read and write threat assessment requests

Description

-

Allows an app to read your organization's threat assessment

requests on behalf of the signed-in user. Also allows the app to

create new requests to assess threats received by your

organization on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**ThreatAssessment.Read.All**

ﾉ

**Expand table**

**ThreatAssessment.ReadWrite.All**

ﾉ

**Expand table**

**ThreatHunting.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

dd98c7f5-2d42-42d3-a0e4-

633161547251

b152eca8-ea73-4a48-8c98-

1a6742673d99

DisplayText

Run hunting queries

Run hunting queries

Description

Allows the app to run hunting

queries, without a signed-in user.

Allows the app to run hunting queries,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

197ee4e9-b993-4066-898f-

d6aecc55125b

9cc427b4-2004-41c5-aa22-

757b755e9796

DisplayText

Read all threat indicators

Read all threat indicators

Description

Allows the app to read all the

indicators for your organization,

without a signed-in user.

Allows the app to read all the

indicators for your organization, on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

21792b6c-c986-4ffc-85de-

df9da54b52fa

91e7d36d-022a-490f-a748-

f8e011357b42

DisplayText

Manage threat indicators this app

creates or owns

Manage threat indicators this app

creates or owns

Description

Allows the app to create threat

indicators, and fully manage those

threat indicators (read, update and

delete), without a signed-in user. It

Allows the app to create threat

indicators, and fully manage those

threat indicators (read, update and

delete), on behalf of the signed-in

**ThreatIndicators.Read.All**

ﾉ

**Expand table**

**ThreatIndicators.ReadWrite.OwnedBy**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

cannot update any threat indicators it

does not own.

user. It cannot update any threat

indicators it does not own.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

e0b77adb-e790-44a3-b0a0-

257d06303687

f266d9c0-ccb9-4fb8-a228-

01ac0d8d6627

DisplayText

Read all Threat Intelligence

Information

Read all threat intelligence

information

Description

Allows the app to read threat

intelligence information, such as

indicators, observations, and and

articles, without a signed in user.

Allows the app to read threat

intelligence information, such as

indicators, observations, and articles,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

fd5353c6-26dd-449f-a565-c4e16b9fce78

DisplayText

-

Read threat submissions

Description

-

Allows the app to read the threat submissions and threat

submission policies owned by the signed-in user.

AdminConsentRequired

-

No

**ThreatIntelligence.Read.All**

ﾉ

**Expand table**

**ThreatSubmission.Read**

ﾉ

**Expand table**

**ThreatSubmission.Read.All**

**Category**

**Application**

**Delegated**

Identifier

86632667-cd15-4845-ad89-

48a88e8412e1

7083913a-4966-44b6-9886-

c5822a5fd910

DisplayText

Read all of the organization's threat

submissions

Read all threat submissions

Description

Allows the app to read your

organization's threat submissions and

to view threat submission policies

without a signed-in user.

Allows the app to read your

organization's threat submissions and

threat submission policies on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

68a3156e-46c9-443c-b85c-921397f082b5

DisplayText

-

Read and write threat submissions

Description

-

Allows the app to read the threat submissions and threat

submission policies owned by the signed-in user. Also allows the

app to create new threat submissions on behalf of the signed-in

user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

d72bdbf4-a59b-405c-8b04-

5995895819ac

8458e264-4eb9-4922-abe9-

768d58f13c7f

DisplayText

Read and write all of the

organization's threat submissions

Read and write all threat submissions

ﾉ

**Expand table**

**ThreatSubmission.ReadWrite**

ﾉ

**Expand table**

**ThreatSubmission.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the app to read your

organization's threat submissions and

threat submission policies without a

signed-in user. Also allows the app to

create new threat submissions

without a signed-in user.

Allows the app to read your

organization's threat submissions and

threat submission policies on behalf of

the signed-in user. Also allows the app

to create new threat submissions on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

926a6798-b100-4a20-a22f-

a4918f13951d

059e5840-5353-4c68-b1da-

666a033fc5e8

DisplayText

Read and write all of the

organization's threat submission

policies

Read and write all threat submission

policies

Description

Allows the app to read your

organization's threat submission

policies without a signed-in user.

Also allows the app to create new

threat submission policies without a

signed-in user.

Allows the app to read your

organization's threat submission

policies on behalf of the signed-in

user. Also allows the app to create new

threat submission policies on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

79c4c76f-409a-4f98-884d-e2c09291ec26

DisplayText

-

Read topic items

Description

-

Allows the app to read topics data on behalf of the signed-in

**ThreatSubmissionPolicy.ReadWrite.All**

ﾉ

**Expand table**

**Topic.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

fff194f1-7dce-4428-8301-

1badb5518201

7ad34336-f5b1-44ce-8682-

31d7dfcd9ab9

DisplayText

Read trust framework key sets

Read trust framework key sets

Description

Allows the app to read trust

framework key set properties without

a signed-in user.

Allows the app to read trust framework

key set properties on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

4a771c9a-1cf2-4609-b88e-

3d3e02d539cd

39244520-1e7d-4b4a-aee0-

57c65826e427

DisplayText

Read and write trust framework key

sets

Read and write trust framework key

sets

Description

Allows the app to read and write

trust framework key set properties

without a signed-in user.

Allows the app to read and write trust

framework key set properties on behalf

of the signed-in user.

AdminConsentRequired

Yes

Yes

**TrustFrameworkKeySet.Read.All**

ﾉ

**Expand table**

**TrustFrameworkKeySet.ReadWrite.All**

ﾉ

**Expand table**

**UnifiedGroupMember.Read.AsGuest**

**Category**

**Application**

**Delegated**

Identifier

-

73e75199-7c3e-41bb-9357-167164dbb415

DisplayText

-

Read unified group memberships as guest

Description

-

Allows the app to read basic unified group properties,

memberships and owners of the group the signed-in guest is a

member of.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

9d952b72-f741-4b40-9185-

8c53076c2339

550e695c-7511-40f4-ac79-

e8fb9c82552d

DisplayText

Convert an external user to internal

member user

Convert an external user to internal

memeber user

Description

Allow the app to convert an external

user to an internal member user,

without a signed-in user.

Allow the app to convert an external

user to an internal member user, on

behalf of signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

8556a004-db57-4d7a-8b82-

97a13428e96f

ed8d2a04-0374-41f1-aefe-

da8ac87ccc87

DisplayText

Read all users' lifecycle information

Read all users' lifecycle information

Description

Allows the app to read the lifecycle

information like

Allows the app to read the lifecycle

information like

ﾉ

**Expand table**

**User-ConvertToInternal.ReadWrite.All**

ﾉ

**Expand table**

**User-LifeCycleInfo.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

employeeLeaveDateTime of users in

your organization, without a signed-

in user.

employeeLeaveDateTime of users in

your organization, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

925f1248-0f97-47b9-8ec8-

538c54e01325

7ee7473e-bd4b-4c9f-987c-

bd58481f5fa2

DisplayText

Read and write all users' lifecycle

information

Read and write all users' lifecycle

information

Description

Allows the app to read and write the

lifecycle information like

employeeLeaveDateTime of users in

your organization, without a signed-

in user.

Allows the app to read and write the

lifecycle information like

employeeLeaveDateTime of users in

your organization, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

280d0935-0796-47d1-8d26-

273470a3f17a

6166886a-9576-433b-8544-

658177bdef1d

DisplayText

Read and write all secondary mail

addresses for users

Read and write secondary mail

addresses for users

Description

Allows the app to read and write

secondary mail addresses for all

users, without a signed-in user.

Allows the app to read and write

secondary mail addresses for all users,

on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**User-LifeCycleInfo.ReadWrite.All**

ﾉ

**Expand table**

**User-Mail.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

a94a502d-0281-4d15-8cd2-

682ac9362c4c

7ff9afdd-0cdb-439d-a61c-

fea3e9339e89

DisplayText

Read and update the on-premises

sync behavior of users

Read and update the on-premises sync

behavior of users

Description

Allows the app to update the on-

premises sync behavior of all users

without a signed-in user.

Allows the app to read and update the

on-premises sync behavior of users on

behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

cc117bb9-00cf-4eb8-b580-

ea2a878fe8f7

56760768-b641-451f-8906-

e1b8ab31bca7

DisplayText

Read and write all password profiles

and reset user passwords

Read and write password profiles and

reset user passwords

Description

Allows the app to read and write

password profiles and reset

passwords for all users, without a

signed-in user.

Allows the app to read and write

password profiles and reset passwords

for all users, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**User-OnPremisesSyncBehavior.ReadWrite.All**

ﾉ

**Expand table**

**User-PasswordProfile.ReadWrite.All**

ﾉ

**Expand table**

**User-Phone.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

86ceff06-c822-49ff-989a-

d912845ffe69

e29d5979-5b06-4a7f-ae24-

6a9348d2e1ff

DisplayText

Read and write all user mobile phone

and business phones

Read and write user mobile phone and

business phones

Description

Allows the app to read and write the

mobile phone and business phones

for all users, without a signed-in user.

Allows the app to read and write the

mobile phone and business phones for

all users, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

eccc023d-eccf-4e7b-9683-

8813ab36cecc

4bb440cd-2cf2-4f90-8004-

aa2acd2537c5

DisplayText

Delete and restore all users

Delete and restore users

Description

Allows the app to delete and restore

all users, without a signed-in user.

Allows the app to delete and restore all

users, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

3011c876-62b7-4ada-afa2-

506cbbecc68c

f92e74e7-2563-467f-9dd0-

902688cb5863

DisplayText

Enable and disable user accounts

Enable and disable user accounts

Description

Allows the app to enable and disable

users' accounts, without a signed-in

user.

Allows the app to enable and disable

users' accounts, on behalf of the

signed-in user.

**User.DeleteRestore.All**

ﾉ

**Expand table**

**User.EnableDisableAccount.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

405a51b5-8d8d-430b-9842-

8be4b0e9f324

405a51b5-8d8d-430b-9842-

8be4b0e9f324

DisplayText

Export user's data

Export user's data

Description

Allows the app to export data (e.g.

customer content or system-

generated logs), associated with any

user in your company, when the app

is used by a privileged user (e.g. a

Company Administrator).

Allows the app to export data (e.g.

customer content or system-

generated logs), associated with any

user in your company, when the app

is used by a privileged user (e.g. a

Company Administrator).

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

09850681-111b-4a89-9bed-

3f2cae46d706

63dd7cd9-b489-4adf-a28c-

ac38b9a0f962

DisplayText

Invite guest users to the organization

Invite guest users to the organization

Description

Allows the app to invite guest users

to the organization, without a

signed-in user.

Allows the app to invite guest users to

the organization, on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**User.Export.All**

ﾉ

**Expand table**

**User.Invite.All**

ﾉ

**Expand table**

**User.ManageIdentities.All**

**Category**

**Application**

**Delegated**

Identifier

c529cfca-c91b-489c-af2b-

d92990b66ce6

637d7bec-b31e-4deb-acc9-

24275642a2c9

DisplayText

Manage all users' identities

Manage user identities

Description

Allows the app to read, update and

delete identities that are associated

with a user's account, without a

signed in user. This controls the

identities users can sign-in with.

Allows the app to read, update and

delete identities that are associated

with a user's account that the signed-

in user has access to. This controls the

identities users can sign-in with.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

e1fe6dd8-ba31-4d61-89e7-88639da4683d

DisplayText

-

Sign in and read user profile

Description

-

Allows users to sign-in to the app, and allows the app to read

the profile of signed-in users. It also allows the app to read basic

company information of signed-in users.

AdminConsentRequired

-

No

![](./assets/output_454_1.png)![](./assets/output_454_2.png)

The _User.Read_ delegated permission is available for consent in personal Microsoft accounts.

The _User.Read_ permission also allows an app to read the basic company information of the

signed-in user for a work or school account through the organization resource. Information in

the following properties is available: **id**, **displayName**, and **verifiedDomains**.

ﾉ

**Expand table**

**User.Read**

ﾉ

**Expand table**

**User.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

df021288-bdef-4463-

88db-98f22de89214

a154be20-db9c-4678-8ab7-66f6cc099a59

DisplayText

Read all users' full profiles

Read all users' full profiles

Description

Allows the app to read

user profiles without a

signed in user.

Allows the app to read the full set of profile

properties, reports, and managers of other users

in your organization, on behalf of the signed-in

user.

AdminConsentRequired

Yes

Yes

![](./assets/output_455_1.png)![](./assets/output_455_2.png)

The _User.Read.All_ delegated permission is available for consent in personal Microsoft

accounts.

**Category**

**Application**

**Delegated**

Identifier

97235f07-e226-4f63-ace3-

39588e11d3a1

b340eb25-3456-403f-be2f-

af7a0d370277

DisplayText

Read all users' basic profiles

Read all users' basic profiles

Description

Allows the app to read a basic set of

profile properties of other users in

your organization without a signed-in

user. Includes display name, first and

last name, email address, open

extensions, and photo.

Allows the app to read a basic set of

profile properties of other users in

your organization on behalf of the

signed-in user. This includes display

name, first and last name, email

address and photo.

AdminConsentRequired

Yes

No

![](./assets/output_455_3.png)![](./assets/output_455_4.png)

The _User.ReadBasic.All_ delegated permission is available for consent in personal Microsoft

accounts.

The _User.ReadBasic.All_ permission constrains app access to reading a limited set of properties

for other users' work or school accounts. This basic profile includes only the following

properties:

displayName

givenName

**User.ReadBasic.All**

ﾉ

**Expand table**

id

mail

photo

securityIdentifier

surname

userPrincipalName

**Category**

**Application**

**Delegated**

Identifier

-

b4e74841-8e56-480b-be8b-910348b18b4c

DisplayText

-

Read and write access to user profile

Description

-

Allows the app to read your profile. It also allows the app to

update your profile information on your behalf.

AdminConsentRequired

-

No

![](./assets/output_456_1.png)![](./assets/output_456_2.png)

The _User.ReadWrite_ delegated permission is available for consent in personal Microsoft

accounts.

The _User.ReadWrite_ delegated permission allow the app to update the following profile

properties for the signed-in user's work or school account:

aboutMe

birthday

hireDate

interests

mobilePhone

mySite

pastProjects

photo

preferredName

responsibilities

schools

skills

**User.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

741f803b-c850-494e-b5df-

cde7c675a1ca

204e0828-b5ca-4ad8-b9f3-f32a958e7cc4

DisplayText

Read and write all users' full

profiles

Read and write all users' full profiles

Description

Allows the app to read and

update user profiles without

a signed in user.

Allows the app to read and write the full set of

profile properties, reports, and managers of

other users in your organization, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

![](./assets/output_457_1.png)![](./assets/output_457_2.png)

The _User.ReadWrite.All_ delegated permission is available for consent in personal Microsoft

accounts.

The _User.ReadWrite.All_ delegated and application permissions allow the app to update all the

declared properties for a user's work or school account except for their **passwordProfile** and

**employeeLeaveDateTime**.

Updating sensitive properties is only allowed on non-admin users and users with lesser-

privileged admin roles as indicated in Who can perform sensitive actions.

**Category**

**Application**

**Delegated**

Identifier

5652f862-b626-407b-a3e6-248aeb95763c

-

DisplayText

Read and write profiles of users that originate from an external

cloud.

-

Description

Allows the app to read and update external cloud user profiles

without a signed in user.

-

AdminConsentRequired

Yes

-

**User.ReadWrite.All**

ﾉ

**Expand table**

**User.ReadWrite.CrossCloud**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

77f3a031-c388-4f99-b373-

dc68676a979e

fc30e98b-8810-4501-81f5-

c20a3196387b

DisplayText

Revoke all sign in sessions for a user

Revoke all sign in sessions for a user

Description

Allow the app to revoke all sign in

sessions for a user, without a signed-

in user.

Allow the app to revoke all sign in

sessions for a user, on behalf of a

signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

47607519-5fb1-47d9-99c7-da4b48f369b1

DisplayText

-

Read and write app activity to users' activity feed

Description

-

Allows the app to read and report the signed-in user's activity in

the app.

AdminConsentRequired

-

No

![](./assets/output_458_1.png)![](./assets/output_458_2.png)

The _UserActivity.ReadWrite.CreatedByApp_ delegated permission is available for consent in

personal Microsoft accounts.

**Category**

**Application**

**Delegated**

Identifier

-

1f6b61c5-2f65-4135-9c9f-31c0f8d32b52

DisplayText

-

Read user authentication methods.

**User.RevokeSessions.All**

ﾉ

**Expand table**

**UserActivity.ReadWrite.CreatedByApp**

ﾉ

**Expand table**

**UserAuthenticationMethod.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Allows the app to read the signed-in user's authentication

methods, including phone numbers and Authenticator app

settings. This does not allow the app to see secret information

like the signed-in user's passwords, or to sign-in or otherwise

use the signed-in user's authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

38d9df27-64da-44fd-b7c5-

a6fbac20248f

aec28ec7-4d02-4e8c-b864-

50163aea77eb

DisplayText

Read all users' authentication

methods

Read all users' authentication methods

Description

Allows the app to read authentication

methods of all users in your

organization, without a signed-in

user. Authentication methods include

things like a user's phone numbers

and Authenticator app settings. This

does not allow the app to see secret

information like passwords, or to

sign-in or otherwise use the

authentication methods.

Allows the app to read authentication

methods of all users in your

organization that the signed-in user

has access to. Authentication methods

include things like a user's phone

numbers and Authenticator app

settings. This does not allow the app

to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

48971fc1-70d7-4245-af77-0beb29b53ee2

DisplayText

-

Read and write user authentication methods

**UserAuthenticationMethod.Read.All**

ﾉ

**Expand table**

**UserAuthenticationMethod.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Allows the app to read and write the signed-in user's

authentication methods, including phone numbers and

Authenticator app settings. This does not allow the app to see

secret information like the signed-in user's passwords, or to

sign-in or otherwise use the signed-in user's authentication

methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

50483e42-d915-4231-9639-

7fdb7fd190e5

b7887744-6746-4312-813d-

72daeaee7e2d

DisplayText

Read and write all users'

authentication methods

Read and write all users'

authentication methods.

Description

Allows the application to read and

write authentication methods of all

users in your organization, without a

signed-in user. Authentication

methods include things like a user's

phone numbers and Authenticator

app settings. This does not allow the

app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods

Allows the app to read and write

authentication methods of all users in

your organization that the signed-in

user has access to. Authentication

methods include things like a user's

phone numbers and Authenticator

app settings. This does not allow the

app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

12b23cea-90c1-4873-9094-f45c5f290f86

**UserAuthenticationMethod.ReadWrite.All**

ﾉ

**Expand table**

**UserAuthMethod-Email.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

-

Read the signed-in user's email authentication methods

Description

-

Allows the app to read the signed-in user's email authentication

methods. This does not allow the app to see secret information

like passwords, or to sign-in or otherwise use the authentication

methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

a1e58be0-1095-422b-b067-

73434bd7d40f

76caaf3a-ebdb-40a3-9299-

4196e636f290

DisplayText

Read all users' email methods

Read all users' email methods

Description

Allows the app to read email

methods of all users in your

organization, without a signed-in

user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

Allows the app to read email methods

of all users in your organization that

the signed-in user has access to. This

does not allow the app to see secret

information like passwords, or to sign-

in or otherwise use the authentication

methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

696aa421-62dc-4c99-be16-015b23444089

DisplayText

-

Read and write the signed-in user's email authentication

methods

Description

-

Allows the app to read and write the signed-in user's email

authentication methods. This does not allow the app to see

**UserAuthMethod-Email.Read.All**

ﾉ

**Expand table**

**UserAuthMethod-Email.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

e8ecb853-1435-4a49-95ba-

ec5b31b11672

074f680f-c89e-45be-880e-

5d0642860a1c

DisplayText

Read and write all users' email

methods

Read and write all users' email

methods.

Description

Allows the application to read and

write email methods of all users in

your organization, without a signed-in

user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

Allows the app to read and write email

methods of all users in your

organization that the signed-in user

has access to. This does not allow the

app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

d1739827-146b-4f7f-b52c-1c509253aa57

DisplayText

-

Read the signed-in user's external authentication methods

Description

-

Allows the app to read the signed-in user's external

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**UserAuthMethod-Email.ReadWrite.All**

ﾉ

**Expand table**

**UserAuthMethod-External.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

d2c4289f-9f95-40da-ad43-

eeb1506f0db7

cbca9646-4c34-4cea-8e54-

9a7088018820

DisplayText

Read all users' external authentication

methods

Read all users' external authentication

methods

Description

Allows the app to read external

authentication methods of all users in

your organization, without a signed-

in user. This does not allow the app

to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

Allows the app to read external

authentication methods of all users in

your organization that the signed-in

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

28c2e8f9-828a-4691-a090-f2f0b7fc07b3

DisplayText

-

Read and write the signed-in user's external authentication

methods

Description

-

Allows the app to read and write the signed-in user's external

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**UserAuthMethod-External.Read.All**

ﾉ

**Expand table**

**UserAuthMethod-External.ReadWrite**

ﾉ

**Expand table**

**UserAuthMethod-External.ReadWrite.All**

**Category**

**Application**

**Delegated**

Identifier

c7a22c2e-5b01-4129-8159-

6c8be2c78f16

9d91805d-0f53-43e3-a0f3-

303ad4f3056f

DisplayText

Read and write all users' external

authentication methods

Read and write all users' external

methods.

Description

Allows the application to read and

write external authentication methods

of all users in your organization,

without a signed-in user. This does

not allow the app to see secret

information like passwords, or to

sign-in or otherwise use the

authentication methods.

Allows the app to read and write

external authentication methods of all

users in your organization that the

signed-in user has access to. This does

not allow the app to see secret

information like passwords, or to sign-

in or otherwise use the authentication

methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

ccd2eb40-8874-44e6-8f96-335908b3cfdb

DisplayText

-

Read the signed-in user's HardwareOATH authentication

methods

Description

-

Allows the app to read the signed-in user's HardwareOATH

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

ﾉ

**Expand table**

**UserAuthMethod-HardwareOATH.Read**

ﾉ

**Expand table**

**UserAuthMethod-HardwareOATH.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

7b544555-7811-49ff-8223-

a56be870e33a

acd68c26-c283-4bf4-8b5c-

200fc179bdd5

DisplayText

Read all users' HardwareOATH

authentication methods

Read all users' HardwareOATH

authentication methods

Description

Allows the app to read

HardwareOATH authentication

methods of all users in your

organization, without a signed-in

user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

Allows the app to read HardwareOATH

authentication methods of all users in

your organization that the signed-in

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

147ca97b-6686-4849-b37e-09d9b5ad45fc

DisplayText

-

Read and write the signed-in user's HardwareOATH

authentication methods

Description

-

Allows the app to read and write the signed-in user's

HardwareOATH authentication methods. This does not allow the

app to see secret information like passwords, or to sign-in or

otherwise use the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

7e9ebcc1-90aa-4471-8051-

480643f2-a162-43c5-a670-

**UserAuthMethod-HardwareOATH.ReadWrite**

ﾉ

**Expand table**

**UserAuthMethod-HardwareOATH.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

e68d6b4e9c89

dc1494fc911b

DisplayText

Read and write all users'

HardwareOATH authentication

methods

Read and write all users'

HardwareOATH methods.

Description

Allows the application to read and

write HardwareOATH authentication

methods of all users in your

organization, without a signed-in

user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

Allows the app to read and write

HardwareOATH authentication

methods of all users in your

organization that the signed-in user

has access to. This does not allow the

app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

f14a567b-3280-4124-95a0-eca86006967e

DisplayText

-

Read the signed-in user's Microsoft Authenticator authentication

methods

Description

-

Allows the app to read the signed-in user's Microsoft

Authenticator authentication methods. This does not allow the

app to see secret information like passwords, or to sign-in or

otherwise use the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

a9c5f16e-e5ca-4e33-89ad-

903fcfc01c23

7b627679-e2fd-4bfd-990e-

989e2914d4e6

**UserAuthMethod-MicrosoftAuthApp.Read**

ﾉ

**Expand table**

**UserAuthMethod-MicrosoftAuthApp.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read all users' Microsoft

authentication methods

Read all users' Microsoft

authentication methods

Description

Allows the app to read Microsoft

authentication methods of all users in

your organization, without a signed-

in user. This does not allow the app

to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

Allows the app to read Microsoft

authentication methods of all users in

your organization that the signed-in

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

9f7dfa0c-eb40-42be-8d45-8af4a9219c6f

DisplayText

-

Read and write the signed-in user's Microsoft Authenticator

authentication methods

Description

-

Allows the app to read and write the signed-in user's Microsoft

Authenticator authentication methods. This does not allow the

app to see secret information like passwords, or to sign-in or

otherwise use the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

c833c349-a1ab-4b6d-94a2-

fa9a8674420c

1b7322b2-5cb3-4f13-928f-

d7ca97c5fba9

DisplayText

Read and write all users' Microsoft

Authentication methods

Read and write all users' Microsoft

Authentication methods.

**UserAuthMethod-MicrosoftAuthApp.ReadWrite**

ﾉ

**Expand table**

**UserAuthMethod-MicrosoftAuthApp.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the application to read and

write Microsoft Authentication

methods of all users in your

organization, without a signed-in

user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

Allows the app to read and write

Microsoft Authentication methods of

all users in your organization that the

signed-in user has access to. This does

not allow the app to see secret

information like passwords, or to sign-

in or otherwise use the authentication

methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

828fcbda-0d26-431d-8bfb-83f217224621

DisplayText

-

Read the signed-in user's passkey authentication methods

Description

-

Allows the app to read the signed-in user's passkey

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

72e00c1d-3e3d-43bb-a0b9-

c435611bb1d2

14195339-1fe4-48a7-a0d3-

a39eb9fd8958

DisplayText

Read all users' passkey authentication

methods

Read all users' passkey authentication

methods

Description

Allows the app to read passkey

authentication methods of all users in

your organization, without a signed-

Allows the app to read passkey

authentication methods of all users in

your organization that the signed-in

**UserAuthMethod-Passkey.Read**

ﾉ

**Expand table**

**UserAuthMethod-Passkey.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

in user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

b2de7db9-10f7-4800-b04c-b5b91e4891d6

DisplayText

-

Read and write the signed-in user's passkey authentication

methods

Description

-

Allows the app to read and write the signed-in user's passkey

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

0400e371-7db1-4338-a269-

96069eb65227

64930478-d0ea-4671-ad72-

fe0d9821df09

DisplayText

Read and write all users' passkey

authentication methods

Read and write all users' passkey

methods.

Description

Allows the application to read and

write passkey authentication methods

of all users in your organization,

without a signed-in user. This does

not allow the app to see secret

information like passwords, or to

Allows the app to read and write

passkey authentication methods of all

users in your organization that the

signed-in user has access to. This does

not allow the app to see secret

information like passwords, or to sign-

**UserAuthMethod-Passkey.ReadWrite**

ﾉ

**Expand table**

**UserAuthMethod-Passkey.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

sign-in or otherwise use the

authentication methods

in or otherwise use the authentication

methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

7f0f82c3-de19-4ddc-810d-a2206d7637fd

DisplayText

-

Read the signed-in user's password authentication methods

Description

-

Allows the app to read the signed-in user's password

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

8d2c17ff-b93d-40d5-9def-

d843680509cb

4f69a4e2-2aa0-43a7-ad6b-

98b4cda1f23f

DisplayText

Read all users' password

authentication methods

Read all users' password

authentication methods

Description

Allows the app to read password

authentication methods of all users in

your organization, without a signed-

in user. This does not allow the app

to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

Allows the app to read password

authentication methods of all users in

your organization that the signed-in

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

No

**UserAuthMethod-Password.Read**

ﾉ

**Expand table**

**UserAuthMethod-Password.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

60cce20d-d41e-4594-b391-84bbf8cc31f3

DisplayText

-

Read and write the signed-in user's password authentication

methods

Description

-

Allows the app to read and write the signed-in user's password

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

f6d38dfd-ec08-4995-8f07-

23e929df0936

7f5b683d-df96-4690-a88d-

6e336ed6dc7c

DisplayText

Read and write all users' password

authentication methods

Read and write all users' password

methods.

Description

Allows the application to read and

write password authentication

methods of all users in your

organization, without a signed-in

user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

Allows the app to read and write

password authentication methods of

all users in your organization that the

signed-in user has access to. This does

not allow the app to see secret

information like passwords, or to sign-

in or otherwise use the authentication

methods.

AdminConsentRequired

Yes

No

**UserAuthMethod-Password.ReadWrite**

ﾉ

**Expand table**

**UserAuthMethod-Password.ReadWrite.All**

ﾉ

**Expand table**

**UserAuthMethod-Phone.Read**

**Category**

**Application**

**Delegated**

Identifier

-

43dab3b9-e8b4-424d-8e13-6a2ad2a625fa

DisplayText

-

Read the signed-in user's phone authentication methods

Description

-

Allows the app to read the signed-in user's phone

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

f529a223-ea70-43ec-b268-

5012de2fbaa2

20cf4ae1-09b9-4d29-a6f8-

43e1820ce60c

DisplayText

Read all users' phone authentication

methods

Read all users' phone authentication

methods

Description

Allows the app to read phone

authentication methods of all users in

your organization, without a signed-

in user. This does not allow the app

to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

Allows the app to read phone

authentication methods of all users in

your organization that the signed-in

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

-

6c4aad61-f76b-46ad-a22c-57d4d3d962af

ﾉ

**Expand table**

**UserAuthMethod-Phone.Read.All**

ﾉ

**Expand table**

**UserAuthMethod-Phone.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

-

Read and write the signed-in user's phone authentication

methods

Description

-

Allows the app to read and write the signed-in user's phone

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

6e85d483-7092-4375-babe-

0a94a8213a58

48c99302-9a24-4f27-a8a7-

acef4debba14

DisplayText

Read and write all users' phone

methods

Read and write all users' phone

methods.

Description

Allows the application to read and

write phone methods of all users in

your organization, without a signed-in

user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

Allows the app to read and write

Phone methods of all users in your

organization that the signed-in user

has access to. This does not allow the

app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

No

**Category**

**Application**

**Delegated**

Identifier

-

9c694582-e8f2-40e2-8353-fb43e2e0f12a

DisplayText

-

Read the signed-in user's platform credential authentication

methods

**UserAuthMethod-Phone.ReadWrite.All**

ﾉ

**Expand table**

**UserAuthMethod-PlatformCred.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

-

Allows the app to read the signed-in user's platform credential

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

07c0b1e4-15bd-442f-834b-

30f8291388d1

5936156c-f89b-4850-997d-

026c4e6ce529

DisplayText

Read all users' platform credentials

methods

Read all users' platform credentials

methods

Description

Allows the app to read platform

credentials methods of all users in

your organization, without a signed-

in user. This does not allow the app

to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

Allows the app to read platform

credentials methods of all users in

your organization that the signed-in

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

70327f81-b953-43c9-92d3-131c74e4beb8

DisplayText

-

Read and write the signed-in user's platform credential

authentication methods

Description

-

Allows the app to read and write the signed-in user's platform

credential authentication methods. This does not allow the app

**UserAuthMethod-PlatformCred.Read.All**

ﾉ

**Expand table**

**UserAuthMethod-PlatformCred.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

to see secret information like passwords, or to sign-in or

otherwise use the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

1a87acf4-a9ca-4576-a974-

452ea265d5f6

cb11bf8c-dde1-4504-b6a5-

31e1562b0749

DisplayText

Read and write all users' platform

credentials methods

Read and write all users' platform

credentials methods.

Description

Allows the application to read and

write platform credentials methods of

all users in your organization, without

a signed-in user. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

Allows the app to read and write

platform credentials methods of all

users in your organization that the

signed-in user has access to. This does

not allow the app to see secret

information like passwords, or to sign-

in or otherwise use the authentication

methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

d6893c31-9187-405c-8dfc-f700c8fc161a

DisplayText

-

Read the signed-in user's QR authentication methods

Description

-

Allows the app to read the signed-in user's QR authentication

methods. This does not allow the app to see secret information

like passwords, or to sign-in or otherwise use the authentication

methods.

**UserAuthMethod-PlatformCred.ReadWrite.All**

ﾉ

**Expand table**

**UserAuthMethod-QR.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

9a45bc50-cddd-4ebe-bd9c-

4f2eacf646ae

e4900dfb-ad17-410d-8ddb-

7aebd8a6af1a

DisplayText

Read all users' QR methods

Read all users' QR methods

Description

Allows the app to read QR

authentication methods of all users in

your organization, without a signed-

in user. This does not allow the app

to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

Allows the app to read QR

authentication methods of all users in

your organization that the signed-in

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

651210da-18ce-4e42-b7db-302ff88e9326

DisplayText

-

Read and write the signed-in user's QR authentication methods

Description

-

Allows the app to read and write the signed-in user's QR

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**UserAuthMethod-QR.Read.All**

ﾉ

**Expand table**

**UserAuthMethod-QR.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

4869299f-18c3-40c8-98f2-

222657e67db1

db39086a-da7d-4cbd-9ac0-

6816f9a80c95

DisplayText

Read and write all users' QR methods

Read and write all users' QR methods.

Description

Allows the application to read and

write QR authentication methods of

all users in your organization, without

a signed-in user. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

Allows the app to read and write QR

authentication methods of all users in

your organization that the signed-in

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

247f2733-6e3d-46ff-a904-f5fd58eb0d97

DisplayText

-

Read the signed-in user's SoftwareOATH authentication

methods

Description

-

Allows the app to read the signed-in user's SoftwareOATH

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**UserAuthMethod-QR.ReadWrite.All**

ﾉ

**Expand table**

**UserAuthMethod-SoftwareOATH.Read**

ﾉ

**Expand table**

**UserAuthMethod-SoftwareOATH.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

a6b423df-a0c8-411d-a809-

a4a5985d2939

3e366fa0-3097-4eb6-8294-

3028f77eea6f

DisplayText

Read all users' SoftwareOATH

methods

Read all users' SoftwareOATH methods

Description

Allows the app to read SoftwareOATH

authentication methods of all users in

your organization, without a signed-

in user. This does not allow the app

to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

Allows the app to read SoftwareOATH

authentication methods of all users in

your organization that the signed-in

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

16721eb3-4493-4ae1-9542-264d9ffe3ce9

DisplayText

-

Read and write the signed-in user's SoftwareOATH

authentication methods

Description

-

Allows the app to read and write the signed-in user's

SoftwareOATH authentication methods. This does not allow the

app to see secret information like passwords, or to sign-in or

otherwise use the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

787442d4-3c6e-4e99-aa95-

8ccca20a48ff

5b34c8b5-2396-4b35-b284-

83fb6a3e73ce

**UserAuthMethod-SoftwareOATH.ReadWrite**

ﾉ

**Expand table**

**UserAuthMethod-SoftwareOATH.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

DisplayText

Read and write all users'

SoftwareOATH methods

Read and write all users'

SoftwareOATH methods.

Description

Allows the application to read and

write SoftwareOATH authentication

methods of all users in your

organization, without a signed-in

user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

Allows the app to read and write

SoftwareOATH authentication

methods of all users in your

organization that the signed-in user

has access to. This does not allow the

app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

84ded88f-26ba-49d6-b776-efec398de692

DisplayText

-

Read the signed-in user's Temporary Access Pass authentication

methods

Description

-

Allows the app to read the signed-in user's Temporary Access

Pass authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

bf82209c-b22b-4747-ac88-

a68be99032cf

6976c635-c9c2-41e6-a21d-

e6913a155273

DisplayText

Read all users' Temporary Access Pass

Read all users' Temporary Access Pass

**UserAuthMethod-TAP.Read**

ﾉ

**Expand table**

**UserAuthMethod-TAP.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

methods

methods

Description

Allows the app to read Temporary

Access Pass authentication methods

of all users in your organization,

without a signed-in user. This does

not allow the app to see secret

information like passwords, or to

sign-in or otherwise use the

authentication methods.

Allows the app to read Temporary

Access Pass authentication methods of

all users in your organization that the

signed-in user has access to. This does

not allow the app to see secret

information like passwords, or to sign-

in or otherwise use the authentication

methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

2424436d-902f-4651-a1c7-b3b93147c960

DisplayText

-

Read and write the signed-in user's Temporary Access Pass

authentication methods

Description

-

Allows the app to read and write the signed-in user's Temporary

Access Pass authentication methods. This does not allow the app

to see secret information like passwords, or to sign-in or

otherwise use the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

627169a8-8c15-451c-861a-

5b80e383de5c

05de4a66-e51a-4312-842a-

30c8094698d2

DisplayText

Read and write all users' Temporary

Access Pass methods

Read and write all users' Temporary

Access Pass methods.

**UserAuthMethod-TAP.ReadWrite**

ﾉ

**Expand table**

**UserAuthMethod-TAP.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the application to read and

write Temporary Access Pass

authentication methods of all users in

your organization, without a signed-in

user. This does not allow the app to

see secret information like passwords,

or to sign-in or otherwise use the

authentication methods.

Allows the app to read and write

Temporary Access Pass authentication

methods of all users in your

organization that the signed-in user

has access to. This does not allow the

app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

efe2b5aa-3a8e-486c-b0be-cc4d185c1b40

DisplayText

-

Read the signed-in user's Windows Hello methods

Description

-

Allows the app to read the signed-in user's Windows Hello

authentication methods. This does not allow the app to see

secret information like passwords, or to sign-in or otherwise use

the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

9b8dd4c7-8cca-4ef5-a34a-

9c2c75fcc934

ff37d46d-b88a-4e0c-85ee-

7e26c37b18eb

DisplayText

Read all users' Windows Hello

methods

Read all users' Windows Hello

methods

Description

Allows the app to read Windows

Hello authentication methods of all

users in your organization, without a

Allows the app to read Windows Hello

authentication methods of all users in

your organization that the signed-in

**UserAuthMethod-WindowsHello.Read**

ﾉ

**Expand table**

**UserAuthMethod-WindowsHello.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

signed-in user. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

user has access to. This does not allow

the app to see secret information like

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

f11e1db9-d419-4a24-b677-792723ffd727

DisplayText

-

Read and write the signed-in user's Windows Hello

authentication methods

Description

-

Allows the app to read and write the signed-in user's Windows

Hello authentication methods. This does not allow the app to

see secret information like passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

f14eee8a-713e-45aa-8223-

2ab74632db1a

13eae17d-aaa4-47b8-aaee-

0eb33c6e2450

DisplayText

Read and write all users' Windows

Hello authentication methods

Read and write all users' Windows

Hello methods.

Description

Allows the application to read and

write Windows Hello authentication

methods of all users in your

organization, without a signed-in user.

This does not allow the app to see

secret information like passwords, or

Allows the app to read and write

Windows Hello authentication

methods of all users in your

organization that the signed-in user

has access to. This does not allow the

app to see secret information like

**UserAuthMethod-WindowsHello.ReadWrite**

ﾉ

**Expand table**

**UserAuthMethod-WindowsHello.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

to sign-in or otherwise use the

authentication methods.

passwords, or to sign-in or otherwise

use the authentication methods.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

61e8a09a-087f-4e36-8c8c-1c77c5228017

DisplayText

-

Read cloud clipboard items

Description

-

Allows the app to read cloud clipboard data on behalf of the

signed-in user.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

4e774092-a092-48d1-90bd-baad67c7eb47

26e2f3e8-b2a1-47fc-9620-

89bb5b042024

DisplayText

Deliver and manage all user's notifications

Deliver and manage user's

notifications

Description

Allows the app to send, read, update and

delete user's notifications, without a

signed-in user.

Allows the app to send, read,

update and delete user's

notifications.

AdminConsentRequired

Yes

No

**UserCloudClipboard.Read**

ﾉ

**Expand table**

**UserNotification.ReadWrite.CreatedByApp**

ﾉ

**Expand table**

**UserShiftPreferences.Read.All**

**Category**

**Application**

**Delegated**

Identifier

de023814-96df-4f53-9376-1e2891ef5a18

-

DisplayText

Read all user shift preferences

-

Description

Allows the app to read all users' shift schedule preferences

without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

d1eec298-80f3-49b0-9efb-d90e224798ac

-

DisplayText

Read and write all user shift preferences

-

Description

Allows the app to manage all users' shift schedule preferences

without a signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

834bcc1c-762f-41b0-bb91-1cdc323ee4bf

DisplayText

-

Read user teamwork settings

Description

-

Allows the app to read the teamwork settings of the signed-in

user.

AdminConsentRequired

-

Yes

ﾉ

**Expand table**

**UserShiftPreferences.ReadWrite.All**

ﾉ

**Expand table**

**UserTeamwork.Read**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

fbcd7ef1-df0d-4e05-bb28-93424a89c6df

-

DisplayText

Read all user teamwork settings

-

Description

Allows the app to read all user teamwork settings without a

signed-in user.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

-

367492fc-594d-4972-a9b5-0d58c622c91c

DisplayText

-

Write app activity to users' timeline

Description

-

Allows the app to report the signed-in user's app activity

information to Microsoft Timeline.

AdminConsentRequired

-

No

**Category**

**Application**

**Delegated**

Identifier

-

77e07bab-1b34-40a5-bb6c-4b197b3f6027

DisplayText

-

Read windows settings for all devices

Description

-

Allows the app to read a user's windows settings which are

stored in cloud and their values on behalf of the signed-in user.

AdminConsentRequired

-

Yes

**UserTeamwork.Read.All**

ﾉ

**Expand table**

**UserTimelineActivity.Write.CreatedByApp**

ﾉ

**Expand table**

**UserWindowsSettings.Read.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

dcb1026d-b7e1-4d31-9f61-6724d5140bf9

DisplayText

-

Read and write windows settings for all devices

Description

-

Allows the app to read and write a user's windows settings

which are stored in cloud and their values on behalf of the

signed-in user.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

e227c591-dd64-4a8a-a033-

816167f7c938

604b2056-41ed-4c56-aad5-

1241d4ef7333

DisplayText

Read Verified Id profiles

Read Verified Id profiles

Description

This role can read Verified Id profiles

in a tenant.

This role can read Verified Id profiles

in a tenant.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

e4a9cb5e-4767-48f8-9029-decf26a54456

DisplayText

-

Read and write Verified Id profiles

Description

-

This role can read and write Verified Id profiles in a tenant.

**UserWindowsSettings.ReadWrite.All**

ﾉ

**Expand table**

**VerifiedId-Profile.Read.All**

ﾉ

**Expand table**

**VerifiedId-Profile.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

-

27470298-d3b8-4b9c-aad4-6334312a3eac

DisplayText

-

Read a user's virtual appointments

Description

-

Allows an application to read virtual appointments for the

signed-in user. Only an organizer or participant user can read

their virtual appointments.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

d4f67ec2-59b5-4bdc-b4af-d78f6f9c1954

-

DisplayText

Read all virtual appointments for users, as authorized by online

meetings application access policy

-

Description

Allows the application to read virtual appointments for all users,

without a signed-in user. The app must also be authorized to

access an individual user's data by the online meetings

application access policy.

-

AdminConsentRequired

Yes

-

**VirtualAppointment.Read**

ﾉ

**Expand table**

**VirtualAppointment.Read.All**

ﾉ

**Expand table**

**VirtualAppointment.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

2ccc2926-a528-4b17-b8bb-860eed29d64c

DisplayText

-

Read and write a user's virtual appointments

Description

-

Allows an application to read and write virtual appointments for

the signed-in user. Only an organizer or participant user can

read and write their virtual appointments.

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

bf46a256-f47d-448f-ab78-f226fff08d40

-

DisplayText

Read-write all virtual appointments for users, as authorized by

online meetings app access policy

-

Description

Allows the application to read and write virtual appointments for

all users, without a signed-in user. The app must also be

authorized to access an individual user's data by the online

meetings application access policy.

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

97e45b36-1250-48e4-bd70-2df6dab7e94a

20d02fff-a0ef-49e7-a46e-

019d4a6523b7

DisplayText

Send notification regarding virtual appointments

as any user

Send notification

regarding virtual

appointments for the

signed-in user

**VirtualAppointment.ReadWrite.All**

ﾉ

**Expand table**

**VirtualAppointmentNotification.Send**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Description

Allows the application to send notification

regarding virtual appointments as any user,

without a signed-in user. The app must also be

authorized to access an individual user's data by

the online meetings application access policy.

Allows an application to

send notifications for

virtual appointments for

the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

-

6b616635-ae58-433a-a918-8c45e4f304dc

DisplayText

-

Read your virtual events

Description

-

Allows the app to read virtual events created by you

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

1dccb351-c4e4-4e09-a8d1-7a9ecbf027cc

-

DisplayText

Read all users' virtual events

-

Description

Allows the app to read all virtual events without a signed-in user.

-

AdminConsentRequired

Yes

-

**VirtualEvent.Read**

ﾉ

**Expand table**

**VirtualEvent.Read.All**

ﾉ

**Expand table**

**VirtualEvent.ReadWrite**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

-

d38d189c-e29b-4344-8b3b-829bfa81380b

DisplayText

-

Read and write your virtual events

Description

-

Allows the app to read and write virtual events for you

AdminConsentRequired

-

Yes

**Category**

**Application**

**Delegated**

Identifier

23211fc1-f9d1-4e8e-8e9e-08a5d0a109bb

-

DisplayText

Read and write anonymous users' virtual event registrations

-

Description

Allows the app to read and write anonymous users' virtual event

registrations, without a signed-in user

-

AdminConsentRequired

Yes

-

**Category**

**Application**

**Delegated**

Identifier

7dd1be58-6e76-4401-bf8d-

31d1e8180d5b

11776c0c-6138-4db3-a668-

ee621bea2555

DisplayText

Read and write all Windows update

deployment settings

Read and write all Windows update

deployment settings

Description

Allows the app to read and write all

Windows update deployment

settings for the organization without

a signed-in user.

Allows the app to read and write all

Windows update deployment settings

for the organization on behalf of the

signed-in user.

AdminConsentRequired

Yes

Yes

**VirtualEventRegistration-Anon.ReadWrite.All**

ﾉ

**Expand table**

**WindowsUpdates.ReadWrite.All**

ﾉ

**Expand table**

**Category**

**Application**

**Delegated**

Identifier

f10b94b9-37d1-4c88-8b7e-

bf75a1152d39

f1ccd5a7-6383-466a-8db8-1a656f7d06fa

DisplayText

Read workforce integrations

Read workforce integrations

Description

Allows the app to read

workforce integrations

without a signed-in user.

Allows the app to read workforce integrations,

to synchronize data from Microsoft Teams

Shifts, on behalf of the signed-in user.

AdminConsentRequired

Yes

Yes

**Category**

**Application**

**Delegated**

Identifier

202bf709-e8e6-478e-bcfd-

5d63c50b68e3

08c4b377-0d23-4a8b-be2a-

23c1c1d88545

DisplayText

Read and write workforce

integrations

Read and write workforce integrations

Description

Allows the app to manage workforce

integrations to synchronize data from

Microsoft Teams Shifts, without a

signed-in user.

Allows the app to manage workforce

integrations, to synchronize data from

Microsoft Teams Shifts, on behalf of

the signed-in user.

AdminConsentRequired

Yes

Yes

Learn more about RSC authorization framework and RSC permissions.

**WorkforceIntegration.Read.All**

ﾉ

**Expand table**

**WorkforceIntegration.ReadWrite.All**

ﾉ

**Expand table**

**Resource-specific consent (RSC) permissions**

ﾉ

**Expand table**

**Name**

**ID**

**Display text**

**Description**

AiEnterpriseInteraction.Read.User

10d712aa-b4cd-

4472-b0ba-

6196e04c344f

Read user AI

enterprise

interactions.

Allows the app to read

user AI enterprise

interactions, without a

signed-in user.

CallAiInsights.Read.Chat

ff9d3910-ca91-

4e7f-843f-

d44ab36a961a

Read all AI

Insights for calls

where the

Teams

application is

installed.

Allows the teams-app

to read all aiInsights for

calls where the Teams-

app is installed, without

a signed-in user.

CallRecordings.Read.Chat

22748df0-bd8c-

4626-aad9-

6dab421b33e4

Read all

recordings of

calls where the

Teams

application is

installed.

Allows the teams-app

to read all recordings

of calls where the

Teams-app is installed,

without a signed-in

user.

Calls.AccessMedia.Chat

e716890c-c30a-

4ac3-a0e3-

551e7d9e8deb

Access media

streams in calls

associated with

this chat or

meeting

Allows the app to

access media streams

in calls associated with

this chat or meeting,

without a signed-in

user.

Calls.JoinGroupCalls.Chat

a01e73f1-94da-

4f6d-9b73-

02e4ea65560b

Join calls

associated with

this chat or

meeting

Allows the app to join

calls associated with

this chat or meeting,

without a signed-in

user.

CallTranscripts.Read.Chat

7990a5df-4c51-

43ea-939c-

3e8b18d6ddad

Read all

transcripts of

calls where the

Teams app is

installed.

Allows the Teams app

to read all transcripts of

calls where the Teams-

app is installed, without

a signed-in user.

Channel.Create.Group

65af85d7-62bb-

4339-a206-

7160fd427454

Create channels

in this team

Allows the app to

create channels in this

team, without a signed-

in user.

Channel.Delete.Group

4432e57d-0983-

4c17-881c-

235c529f96dc

Delete this

team's channels

Allows the app to

delete this team's

channels, without a

signed-in user.

**Name**

**ID**

**Display text**

**Description**

ChannelMeeting.ReadBasic.Group

6c13459c-facc-

4b0a-93cb-

63f0dff28046

Read basic

properties of

the channel

meetings in this

team

Allows the app to read

basic properties, such

as name, schedule,

organizer, join link, and

start or end

notifications, of

channel meetings in

this team, without a

signed-in user.

ChannelMeetingNotification.Send.Group

bbb12bdb-

71e6-4602-9f5e-

b1172c505746

Send

notifications in

all the channel

meetings

associated with

this team

Allows the app to send

notifications inside all

the channel meetings

associated with this

team, without a signed-

in user.

ChannelMeetingParticipant.Read.Group

bd118236-e8f5-

4bec-a62d-

89a623717e05

Read the

participants of

this team's

channel

meetings

Allows the app to read

participant information,

including name, role,

id, joined and left

times, of channel

meetings associated

with this team, without

a signed-in user.

ChannelMeetingRecording.Read.Group

30a40618-9b50-

4764-b62e-

b04023a8f5f3

Read the

recordings of all

channel

meetings

associated with

this team

Allows the app to read

recordings of all the

channel meetings

associated with this

team, without a signed-

in user.

ChannelMeetingTranscript.Read.Group

37e59e88-1a46-

482b-b623-

0a4aa6abdf67

Read the

transcripts of all

channel

meetings

associated with

this team

Allows the app to read

transcripts of all the

channel meetings

associated with this

team, without a signed-

in user.

ChannelMember.Read.Group

7e3614f5-3467-

419c-9c63-

dd0bbd2a88f9

Read the

members of

channels of a

team

Read the members of

channels of a team,

without a signed-in

user

ChannelMember.ReadWrite.Group

1342a0fc-cd33-

4c75-ad65-

d5defcfc7232

Read and write

the members of

Read and write the

members of channels

**Name**

**ID**

**Display text**

**Description**

channels of a

team

of a team, without a

signed-in user

ChannelMessage.Read.Group

19103a54-c397-

4bcd-be5a-

ef111e0406fa

Read this team's

channel

messages

Allows the app to read

this team's channel's

messages, without a

signed-in user.

ChannelMessage.Send.Group

3e38d437-815b-

4368-9f19-

e39dea9a6c7f

Send messages

to this team's

channels

Allows the app to send

messages to this team's

channels, without a

signed-in user.

ChannelSettings.Read.Group

0a7b3084-8d18-

46f5-8aef-

b5b829292c6f

Read the

names,

descriptions,

and settings of

this team's

channels

Allows the app to read

this team's channel

names, channel

descriptions, and

channel settings,

without a signed-in

user.

ChannelSettings.ReadWrite.Group

d057ad03-b27b-

49f7-8219-

e0d4a706da55

Update the

names,

descriptions,

and settings of

this team's

channels

Allows the app to

update and read the

names, descriptions,

and settings of this

team's channels,

without a signed-in

user.

Chat.Manage.Chat

4a14842e-6bb6-

4088-b21a-

7d0a24f835a6

Manage this

chat

Allows the app to

manage the chat, the

chat's members and

grant access to the

chat's data, without a

signed-in user.

Chat.ManageDeletion.Chat

b827a2af-24b2-

4f61-9eb3-

8788e66a0d86

Delete and

recover deleted

chat

Allows the app to

delete and recover

deleted chat, without a

signed-in user.

ChatMember.Read.Chat

e854bbc6-07e3-

45cc-af99-

b6e78fab5b80

Read this chat's

members

Allows the app to read

the members of this

chat, without a signed-

in user.

ChatMessage.Read.Chat

9398c3de-3f6b-

4958-90f3-

5098714ff50c

Read this chat's

messages

Allows the app to read

this chat's messages,

**Name**

**ID**

**Display text**

**Description**

without a signed-in

user.

ChatMessage.Send.Chat

19cbeeb2-02a0-

49d7-95cd-

ab0841beed7f

Send messages

to this chat

Allows the app to send

messages to this chat,

without a signed-in

user.

ChatMessageReadReceipt.Read.Chat

a236cb34-7076-

45a1-9381-

22db8111a3d3

Read the ID of

the last seen

message in this

chat

Allows the app to read

the ID of the last

message seen by the

users in this chat.

ChatSettings.Read.Chat

40d35d7c-9cc3-

4f2d-912b-

464457412a00

Read this chat's

settings

Allows the app to read

this chat's settings,

without a signed-in

user.

ChatSettings.ReadWrite.Chat

ed928a9c-7530-

496a-a624-

4c0a460ab3ed

Read and write

this chat's

settings

Allows the app to read

and write this chat's

settings, without a

signed-in user.

Member.Read.Group

0a8ce3c7-89dd-

46cf-b2c3-

5ef0064437a8

Read this

group's

members

Allows the app to read

the basic profile of this

group's members,

without a signed-in

user.

OnlineMeeting.Read.Chat

f991ed3f-9617-

4d8d-b06c-

d18d9fcbcf2a

Read this

meeting and

subscribe to

meeting call

updates .

Allows the app to read

this meeting and

subscribe to meeting

call updates.

OnlineMeeting.ReadBasic.Chat

eda8d262-4e6e-

4ff6-a7ba-

a2fb50535165

Read basic

properties of

meetings

associated with

this chat

Allows the app to read

basic properties, such

as name, schedule,

organizer, join link, and

start or end

notifications, of

meetings associated

with this chat, without a

signed-in user.

OnlineMeeting.ReadWrite.Chat

93400bb4-2282-

4371-a745-

a86d64c966d0

Manage this

meeting and

subscribe to

Allows the app to

manage this online

meeting, and subscribe

**Name**

**ID**

**Display text**

**Description**

meeting call

updates.

to meeting call

updates.

OnlineMeetingArtifact.Read.Chat

c5d06837-8c0d-

42fc-9e49-

545e3f941261

Read virtual

event artifacts

Read attendance

reports & attendance

records for this webinar

or town hall.

OnlineMeetingNotification.Send.Chat

d9837fe0-9c31-

4faa-8acb-

b10874560161

Send

notifications in

the meetings

associated with

this chat

Allows the app to send

notifications inside

meetings associated

with this chat, without a

signed-in user.

OnlineMeetingParticipant.Read.Chat

6324a770-185c-

4b4f-be13-

2d9a1668e6eb

Read the

participants of

the meetings

associated with

this chat

Allows the app to read

participant information,

including name, role,

id, joined and left

times, of meetings

associated with this

chat, without a signed-

in user.

OnlineMeetingRecording.Read.Chat

d20f0153-08ff-

48a9-b299-

96a8d1131d1d

Read the

recordings of

the meetings

associated with

this chat

Allows the app to read

recordings of the

meetings associated

with this chat, without a

signed-in user.

OnlineMeetingTranscript.Read.Chat

8c477e19-f0f7-

45f9-ae72-

604f77a599e3

Read the

transcripts of

the meetings

associated with

this chat

Allows the app to read

transcripts of the

meetings associated

with this chat, without a

signed-in user.

Owner.Read.Group

70d5316c-9b27-

4057-a650-

3b0fe49002ab

Read this

group's owners

Allows the app to read

the basic profile of this

group's owners,

without a signed-in

user.

Team.Read.Group

41027e3b-d156-

4913-bb0d-

06cbbe931eb7

Read this team's

metadata

Allows the app to read

this team's metadata,

without a signed-in

user.

TeamMember.Read.Group

b8731755-de22-

4604-be08-

93e1e5c2d2d6

Read this team's

members

Allows the app to read

the members of this

**Name**

**ID**

**Display text**

**Description**

team, without a signed-

in user.

TeamsActivity.Send.Chat

119b5846-be45-

44cd-87d7-

bfc566330e11

Send activity

feed

notifications to

users in this

chat

Allows the app to

create new notifications

in the teamwork

activity feeds of the

users in this chat,

without a signed-in

user.

TeamsActivity.Send.Group

d4539c25-0937-

4095-b844-

b97228dd8655

Send activity

feed

notifications to

users in this

team

Allows the app to

create new notifications

in the teamwork

activity feeds of the

users in this team,

without a signed-in

user.

TeamsActivity.Send.User

483c432d-7210-

44e7-a362-

954c0c5e4108

Send activity

feed

notifications to

this user

Allows the app to

create new notifications

in the teamwork

activity feed of this

user, without a signed-

in user.

TeamsAppInstallation.Read.Chat

b60343cd-f77a-

4c4f-8036-

41938b1abd8b

Read which

apps are

installed in this

chat

Allows the app to read

the Teams apps that

are installed in this chat

along with the

permissions granted to

each app, without a

signed-in user.

TeamsAppInstallation.Read.Group

ba4beb29-863b-

4f02-8969-

37a289cd91c0

Read which

apps are

installed in this

team

Allows the app to read

the Teams apps that

are installed in this

team, without a signed-

in user.

TeamsAppInstallation.Read.User

39a4b5e8-1aa6-

4da4-877a-

d2345944028d

Read installed

Teams apps for

a user

Allows the app to read

the Teams apps that

are installed in user's

personal scope, without

a signed-in user. Does

not give the ability to

read application-

specific settings.

**Name**

**ID**

**Display text**

**Description**

TeamSettings.Edit.Group

33f7a028-d012-

4bd9-b40f-

3c970d089bc8

Edit this team's

settings

Allows the app to edit

this team's settings,

without a signed-in

user.

TeamSettings.Read.Group

87909ea6-7b07-

42cf-b3a0-

b8bd8e7072a8

Read this team's

settings

Allows the app to read

this team's settings,

without a signed-in

user.

TeamSettings.ReadWrite.Group

13451d84-ced2-

4d45-9b0d-

98688b90e5bf

Read and write

this team's

settings

Allows the app to read

and write this team's

settings, without a

signed-in user.

TeamsTab.Create.Chat

0029d2bb-fc98-

4712-9310-

69dd5fcc94d5

Create tabs in

this chat

Allows the app to

create tabs in this chat,

without a signed-in

user.

TeamsTab.Create.Group

c4d7203b-1e46-

4c4a-95f9-

862779aa39e1

Create tabs in

this team

Allows the app to

create tabs in this team,

without a signed-in

user.

TeamsTab.Delete.Chat

fa50d890-02fe-

4696-b82b-

110dc7f7382a

Delete this

chat's tabs

Allows the app to

delete this chat's tabs,

without a signed-in

user.

TeamsTab.Delete.Group

cc2e79a6-9a86-

45cc-91c1-

41c15745287e

Delete this

team's tabs

Allows the app to

delete this team's tabs,

without a signed-in

user.

TeamsTab.Read.Chat

aa07ff41-1317-

4f07-8edb-

a1558e9bfc84

Read this chat's

tabs

Allows the app to read

this chat's tabs, without

a signed-in user.

TeamsTab.Read.Group

60d920d0-44e7-

44f4-a811-

1a172a2ea5b3

Read this team's

tabs

Allows the app to read

this team's tabs,

without a signed-in

user.

TeamsTab.ReadWrite.Chat

d583f4d7-57da-

4b2c-9744-

253e9ec3c7be

Manage this

chat's tabs

Allows the app to

manage this chat's

tabs, without a signed-

in user.

**Name**

**ID**

**Display text**

**Description**

TeamsTab.ReadWrite.Group

717ca3a4-bc73-

47f8-b613-

4d43e657fa9c

Manage this

team's tabs

Allows the app to

manage this team's

tabs, without a signed-

in user.

VirtualEvent.Read.Chat

298266a0-fbf7-

4804-b988-

5a54e61566c8

Read virtual

event details

Read information for

this webinars or town

halls, including

schedules, speakers,

and event settings and

webinar registrations.

VirtualEventRegistration-

Anon.ReadWrite.Chat

0e646cc8-6b07-

4030-9a41-

a7db4644b4cc

Manage virtual

event

registrations

Register attendees and

cancel registrations for

this webinar.

Overview of Microsoft Graph permissions

Grant or revoke Microsoft Graph permissions programmatically

**Last updated on 11/17/2025**

**Related content**

**agentIdentityBlueprint resource type**

Namespace: microsoft.graph

An agent identity blueprint serves as a template for creating agent identities within the

Microsoft Entra ID ecosystem.

Inherits from application.

This resource is an open type that allows additional properties beyond those documented here.

**Method**

**Return type**

**Description**

List

agentIdentityBlueprint

collection

Get a list of the agentIdentityBlueprint

objects and their properties.

Create

agentIdentityBlueprint

Create (register) a new

agentIdentityBlueprint.

Get

agentIdentityBlueprint

Read the properties and relationships of

agentIdentityBlueprint object.

Update

agentIdentityBlueprint

Update the properties of an

agentIdentityBlueprint object.

Upsert

agentIdentityBlueprint

Create a new agent identity blueprint if it

doesn't exist, or update the properties of

an existing blueprint.

Delete

None

Delete an agentIdentityBlueprint object.

**Credentials**

Add password

passwordCredential

Add a strong password or secret to an

agent identity blueprint.

） **Important**

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs

in production applications is not supported. To determine whether an API is available in

v1.0, use the **Version** selector.

**Methods**

ﾉ

**Expand table**

**Method**

**Return type**

**Description**

Remove password

passwordCredential

Remove a password or secret from an

agent identity blueprint.

Add key

keyCredential

Add a key credential to an agent identity

blueprint.

Remove key

None

Remove a key credential from an agent

identity blueprint.

List

federatedIdentityCredential

federatedIdentityCredential

collection

Get a list of the federatedIdentityCredential

objects and their properties.

Create

federatedIdentityCredential

federatedIdentityCredential

Create a new federatedIdentityCredential

object.

Get

federatedIdentityCredential

federatedIdentityCredential

Get the properties of a

federatedIdentityCredential object.

Update

federatedIdentityCredential

None

Update the properties of a

federatedIdentityCredential object.

Upsert

federatedIdentityCredential

federatedIdentityCredential

Create a new federatedIdentityCredential if

it doesn't exist, or update the properties of

an existing federatedIdentityCredential

object.

Delete

federatedIdentityCredential

None

Deletes a federatedIdentityCredential

object.

**Deleted items**

List

directoryObject collection

Retrieve a list of recently deleted agent

identities.

Get

directoryObject

Retrieve the properties of a recently

deleted agent identity.

Restore

directoryObject

Restore a recently deleted agent identity.

Permanently delete

None

Permanently delete an agent identity.

**Owners**

List owners

directoryObject collection

Get the owners of this agent identity

blueprint principal.

Add owners

directoryObject

Assign an owner to this agent identity

blueprint principal.

Remove owners

None

Remove an owner from this agent identity

**Method**

**Return type**

**Description**

blueprint principal.

**Sponsors**

List sponsors

directoryObject collection

Get the sponsors for this agent identity

blueprint. Sponsors are users or service

principals who can authorize and manage

the lifecycle of agent identity instances.

Add sponsors

directoryObject

Add sponsors by posting to the sponsors

collection.

Remove sponsors

None

Remove a directoryObject object.

**Verified publisher**

Set

None

Set the verified publisher of an application.

Unset

None

Unset the verified publisher of an

application.

**Property**

**Type**

**Description**

api

apiApplication

Specifies settings for an agent identity blueprint

that implements a web API. Inherited from

application.

appId

String

The unique identifier for the agent identity

blueprint that is assigned by Microsoft Entra ID.

Not nullable. Read-only. Inherited from

application.

appRoles

appRole collection

The collection of roles defined for the agent

identity blueprint. With app role assignments,

these roles can be assigned to users, groups, or

service principals associated with other

**Properties**

） **Important**

While this resource inherits from **application**, some properties are not applicable and

return `null` or default values. These properties are excluded from the table below.

ﾉ

**Expand table**

**Property**

**Type**

**Description**

applications. Not nullable. Inherited from

application.

certification

certification

Specifies the certification status of the agent

identity blueprint. Inherited from application.

createdByAppId

String

The unique identifier of the application that

created this agent identity blueprint. Set internally

by Microsoft Entra ID. Read-only. Inherited from

application.

createdDateTime

DateTimeOffset

The date and time the agent identity blueprint was

registered. The DateTimeOffset type represents

date and time information using ISO 8601 format

and is always in UTC time. Read-only. Inherited

from application.

createdByAppId

String

The **appId** (called **Application (client) ID** on the

Microsoft Entra admin center) of the application

that created this agent identity blueprint. Set

internally by Microsoft Entra ID. Read-only.

Inherited from application.

description

String

Free text field to provide a description of the

agent identity blueprint to end users. The

maximum allowed size is 1,024 characters.

Inherited from application.

disabledByMicrosoftStatus

String

Specifies whether Microsoft has disabled the

registered agent identity blueprint. Possible values

are: `null` (default value), `NotDisabled` , and

`DisabledDueToViolationOfServicesAgreement`

(reasons may include suspicious, abusive, or

malicious activity, or a violation of the Microsoft

Services Agreement). Inherited from application.

displayName

String

The display name for the agent identity blueprint.

Maximum length is 256 characters. Inherited from

application.

groupMembershipClaims

String

Configures the `groups` claim issued in a user or

OAuth 2.0 access token that the agent identity

blueprint expects. To set this attribute, use one of

the following string values: `None` , `SecurityGroup`

(for security groups and Microsoft Entra roles),

`All` (this gets all security groups, distribution

groups, and Microsoft Entra directory roles that

the signed-in user is a member of). Inherited from

application.

**Property**

**Type**

**Description**

id

String

Unique identifier for the agent identity blueprint

object. This property is referred to as **Object ID** in

the Microsoft Entra admin center. Key. Not

nullable. Read-only. Inherited from

directoryObject.

identifierUris

String collection

Also known as App ID URI, this value is set when

an agent identity blueprint is used as a resource

app. The identifierUris acts as the prefix for the

scopes you reference in your API's code, and it

must be globally unique across Microsoft Entra ID.

Not nullable. Inherited from application.

info

informationalUrl

Basic profile information of the agent identity

blueprint, such as it's marketing, support, terms of

service, and privacy statement URLs. The terms of

service and privacy statement are surfaced to

users through the user consent experience.

Inherited from application.

keyCredentials

keyCredential

collection

The collection of key credentials associated with

the agent identity blueprint. Not nullable.

Inherited from application.

optionalClaims

optionalClaims

Application developers can configure optional

claims in their Microsoft Entra agent identity

blueprints to specify the claims that are sent to

their application by the Microsoft security token

service. Inherited from application.

passwordCredentials

passwordCredential

collection

The collection of password credentials associated

with the agent identity blueprint. Not nullable.

Inherited from application.

You can also add passwords after creating the

agent identity blueprint by calling the Add

password API.

publisherDomain

String

The verified publisher domain for the agent

identity blueprint. Read-only. Inherited from

application.

serviceManagementReference

String

References application or service contact

information from a Service or Asset Management

database. Nullable. Inherited from application.

signInAudience

String

Specifies the Microsoft accounts that are

supported for the current agent identity blueprint.

The possible values are: `AzureADMyOrg` (default),

**Property**

**Type**

**Description**

`AzureADMultipleOrgs` ,

`AzureADandPersonalMicrosoftAccount` , and

`PersonalMicrosoftAccount` . Inherited from

application.

tags

String collection

Custom strings that can be used to categorize and

identify the agent identity blueprint. Not nullable.

Inherited from application.

tokenEncryptionKeyId

Guid

Specifies the keyId of a public key from the

keyCredentials collection. When configured,

Microsoft Entra ID encrypts all the tokens it emits

by using the key this property points to. Inherited

from application.

uniqueName

String

The unique identifier that can be assigned to an

agent identity blueprint and used as an alternate

key. Immutable. Read-only. Inherited from

application.

verifiedPublisher

verifiedPublisher

Specifies the verified publisher of the agent

identity blueprint. Inherited from application.

web

webApplication

Specifies settings for a web application. Inherited

from application.

**Relationship**

**Type**

**Description**

appManagementPolicies

appManagementPolicy

collection

The appManagementPolicy applied to this

agent identity blueprint. Inherited from

microsoft.graph.application

federatedIdentityCredentials

federatedIdentityCredential

collection

Federated identities for agent identity

blueprints. Inherited from

microsoft.graph.application

owners

directoryObject collection

Directory objects that are owners of this

agent identity blueprint. The owners are a

set of nonadmin users or service principals

allowed to modify this object. Read-only.

Nullable. Inherited from

microsoft.graph.application

**Relationships**

ﾉ

**Expand table**

**Relationship**

**Type**

**Description**

sponsors

directoryObject collection

The sponsors for this agent identity

blueprint. Sponsors are users or groups

who can authorize and manage the lifecycle

of agent identity instances.

The following JSON representation shows the resource type. Only a subset of all properties are

returned by default. All other properties can only be retrieved using `$select` .

JSON

**JSON representation**

`{`

`  ``"@odata.type"` `: ``"#microsoft.graph.agentIdentityBlueprint"` `,`

`  ``"id"` `: ``"String (identifier)"` `,`

`  ``"appId"` `: ``"String"` `,`

`  ``"identifierUris"` `: [` `"String"` `],`

`  ``"createdByAppId"` `: ``"String"` `,`

`  ``"createdDateTime"` `: ``"String (timestamp)"` `,`

`  ``"description"` `: ``"String"` `,`

`  ``"disabledByMicrosoftStatus"` `: ``"String"` `,`

`  ``"displayName"` `: ``"String"` `,`

`  ``"groupMembershipClaims"` `: ``"String"` `,`

`  ``"publisherDomain"` `: ``"String"` `,`

`  ``"signInAudience"` `: ``"String"` `,`

`  ``"tags"` `: [` `"String"` `],`

`  ``"tokenEncryptionKeyId"` `: ``"Guid"` `,`

`  ``"uniqueName"` `: ``"String"` `,`

`  ``"serviceManagementReference"` `: ``"String"` `,`

`  ``"certification"` `: {`

`    ``"@odata.type"` `: ``"microsoft.graph.certification"`

`  },`

`  ``"optionalClaims"` `: {`

`    ``"@odata.type"` `: ``"microsoft.graph.optionalClaims"`

`  },`

`  ``"api"` `: {`

`    ``"@odata.type"` `: ``"microsoft.graph.apiApplication"`

`  },`

`  ``"appRoles"` `: [`

`    {`

`      ``"@odata.type"` `: ``"microsoft.graph.appRole"`

`    }`

`  ],`

`  ``"info"` `: {`

`    ``"@odata.type"` `: ``"microsoft.graph.informationalUrl"`

`  },`

`  ``"keyCredentials"` `: [`

`    {`

`      ``"@odata.type"` `: ``"microsoft.graph.keyCredential"`

**Last updated on 11/17/2025**

`    }`

`  ],`

`  ``"passwordCredentials"` `: [`

`    {`

`      ``"@odata.type"` `: ``"microsoft.graph.passwordCredential"`

`    }`

`  ],`

`  ``"verifiedPublisher"` `: {`

`    ``"@odata.type"` `: ``"microsoft.graph.verifiedPublisher"`

`  },`

`  ``"web"` `: {`

`    ``"@odata.type"` `: ``"microsoft.graph.webApplication"`

`  }`

`}`

**agentIdentityBlueprintPrincipal resource**

**type**

Namespace: microsoft.graph

Represents an agent identity blueprint principal in a tenant. An agent identity blueprint

principal is instantiated from an agentIdentityBlueprintPrincipal object and is used to create

agent identities within a Microsoft Entra ID tenant, and perform various identity management

operations that affect all agent identities created.

Inherits from servicePrincipal.

This resource is an open type that allows additional properties beyond those documented here.

**Method**

**Return type**

**Description**

List

agentIdentityBlueprintPrincipal

collection

Get a list of the

agentIdentityBlueprintPrincipal objects and

their properties.

Create

agentIdentityBlueprintPrincipal

Create a new

agentIdentityBlueprintPrincipal object.

Get

agentIdentityBlueprintPrincipal

Read the properties and relationships of

agentIdentityBlueprintPrincipal object.

Update

agentIdentityBlueprintPrincipal

Update the properties of an

agentIdentityBlueprintPrincipal object.

Delete

None

Delete an agentIdentityBlueprintPrincipal

object.

**App role assignments**

） **Important**

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs

in production applications is not supported. To determine whether an API is available in

v1.0, use the **Version** selector.

**Methods**

ﾉ

**Expand table**

**Method**

**Return type**

**Description**

List appRoleAssignedTo

appRoleAssignment collection

Get the users, groups, and agent identities

assigned app roles for this agent identity

blueprint principal.

Add appRoleAssignedTo

appRoleAssignment

Assign an app role for this agent identity

blueprint principal to a user, group, or

service principal.

Remove

appRoleAssignedTo

None

Remove an app role assignment for this

agent identity blueprint principal from a

user, group, or service principal.

List appRoleAssignments

appRoleAssignment collection

Get the app roles that this agent identity

blueprint principal is assigned.

Add appRoleAssignment

appRoleAssignment

Assign an app role to this agent identity

blueprint principal.

Remove

appRoleAssignment

None

Remove an app role assignment from this

agent identity blueprint principal.

**Delegated permission**

**grants**

List

oauth2PermissionGrants

oAuth2PermissionGrant

collection

Get the delegated permission grants

authorizing this agent identity blueprint

principal to access an API on behalf of a

signed-in user.

**Deleted items**

List

directoryObject collection

Retrieve a list of recently deleted agent

identities.

Get

directoryObject

Retrieve the properties of a recently

deleted agent identity.

Restore

directoryObject

Restore a recently deleted agent identity.

Permanently delete

None

Permanently delete an agent identity.

**Directory objects**

List ownedObjects

directoryObject collection

Get directory objects owned by this agent

identity blueprint principal.

List createdObjects

directoryObject collection

Get directory objects created by this agent

identity blueprint principal.

**Memberships**

**Method**

**Return type**

**Description**

List memberOf

directoryObject collection

Get the groups that this agent identity

blueprint principal is a direct member of.

**Owners**

List owners

directoryObject collection

Get the owners of this agent identity

blueprint principal.

Add owners

None

Assign an owner to this agent identity

blueprint principal.

Remove owners

None

Remove an owner from this agent identity

blueprint principal.

**Sponsors**

List sponsors

directoryObject collection

Get the sponsors for this agent identity

blueprint principal.

Add sponsors

directoryObject

Add sponsors by posting to the sponsors

collection.

Remove sponsors

None

Remove a directoryObject object.

**Property**

**Type**

**Description**

accountEnabled

Boolean

`true` if the agent identity blueprint principal account

is enabled; otherwise, `false` . If set to `false` , then no

users are able to sign in to this app, even if they're

assigned to it. Inherited from servicePrincipal.

appDescription

String

The description exposed by the associated agent

identity blueprint. Inherited from servicePrincipal.

appDisplayName

String

The display name exposed by the associated agent

identity blueprint. Maximum length is 256 characters.

**Properties**

） **Important**

While this resource inherits from **servicePrincipal**, some properties are not applicable and

return `null` or default values. These properties are excluded from the table below.

ﾉ

**Expand table**

**Property**

**Type**

**Description**

Inherited from servicePrincipal.

appId

String

The **appId** of the associated agent identity blueprint.

Alternate key. Inherited from servicePrincipal.

appOwnerOrganizationId

Guid

Contains the tenant ID where the agent identity

blueprint is registered. This is applicable only to agent

identity blueprint principals backed by applications.

Inherited from servicePrincipal.

appRoleAssignmentRequired

Boolean

Specifies whether users or other service principals

need to be granted an app role assignment for this

agent identity blueprint principal before users can

sign in or apps can get tokens. The default value is

`false` . Not nullable. Inherited from servicePrincipal.

appRoles

appRole

collection

The roles exposed by the agent identity blueprint,

which this agent identity blueprint principal

represents. For more information, see the **appRoles**

property definition on the application entity. Not

nullable. Inherited from servicePrincipal.

createdByAppId

String

The **appId** (called **Application (client) ID** on the

Microsoft Entra admin center) of the application that

created this agent identity blueprint principal. Set

internally by Microsoft Entra ID. Read-only. Inherited

from servicePrincipal.

disabledByMicrosoftStatus

String

Specifies whether Microsoft has disabled the

registered agent identity blueprint. Possible values are:

`null` (default value), `NotDisabled` , and

`DisabledDueToViolationOfServicesAgreement` (reasons

may include suspicious, abusive, or malicious activity,

or a violation of the Microsoft Services Agreement).

Inherited from servicePrincipal.

displayName

String

The display name for the agent identity blueprint

principal. Inherited from servicePrincipal.

id

String

The unique identifier for the agent identity blueprint

principal. Inherited from entity. Key. Not nullable.

Read-only.

info

informationalUrl

Basic profile information of the acquired application

such as app's marketing, support, terms of service and

privacy statement URLs. The terms of service and

privacy statement are surfaced to users through the

user consent experience. Inherited from

servicePrincipal.

**Property**

**Type**

**Description**

publishedPermissionScopes

permissionScope

collection

The delegated permissions exposed by the

application. For more information, see the

**oauth2PermissionScopes** property on the agent

identity blueprint entity's **api** property. Not nullable.

Inherited from servicePrincipal.

publisherName

String

The name of the Microsoft Entra tenant that published

the application. Inherited from servicePrincipal.

servicePrincipalNames

String collection

Contains the list of **identifiersUris**, copied over from

the associated agent identity blueprint. More values

can be added to hybrid agent identity blueprint. These

values can be used to identify the permissions

exposed by this app within Microsoft Entra ID. Not

nullable. **Property blocked on Agent Identity**

**Blueprint Principal.** Inherited from servicePrincipal.

servicePrincipalType

String

Identifies if the agent identity blueprint principal

represents an application. This is set by Microsoft

Entra ID internally. For an agent identity blueprint

principal that represents an application this is set as

**Application**. Inherited from servicePrincipal.

signInAudience

String

Specifies the Microsoft accounts that are supported

for the current agent identity blueprint. Read-only.

Supported values are: `AzureADMyOrg` ,

`AzureADMultipleOrgs` ,

`AzureADandPersonalMicrosoftAccount` , and

`PersonalMicrosoftAccount` . Inherited from

servicePrincipal.

tags

String collection

Custom strings that can be used to categorize and

identify the agent identity blueprint principal. Not

nullable. The value is the union of strings set here and

on the associated agent identity blueprint entity's **tags**

property. Inherited from servicePrincipal.

verifiedPublisher

verifiedPublisher

Specifies the verified publisher of the application

that's linked to this agent identity blueprint principal.

Inherited from servicePrincipal.

**Relationships**

ﾉ

**Expand table**

**Relationship**

**Type**

**Description**

appManagementPolicies

appManagementPolicy

collection

The appManagementPolicy applied to this agent

identity blueprint principal. Inherited from

microsoft.graph.servicePrincipal

appRoleAssignedTo

appRoleAssignment

collection

App role assignments for this agent identity

blueprint principal, granted to users, groups, and

other service principals. Supports `$expand` .

Inherited from microsoft.graph.servicePrincipal

appRoleAssignments

appRoleAssignment

collection

App role assignment for another app or service,

granted to this agent identity blueprint principal.

Supports `$expand` . Inherited from

microsoft.graph.servicePrincipal

createdObjects

directoryObject

collection

Directory objects created by this agent identity

blueprint principal. Read-only. Nullable. Inherited

from microsoft.graph.servicePrincipal

memberOf

directoryObject

collection

Roles that this agent identity blueprint principal is a

member of. HTTP Methods: GET Read-only.

Nullable. Supports `$expand` . Inherited from

microsoft.graph.servicePrincipal

oauth2PermissionGrants

oAuth2PermissionGrant

collection

Delegated permission grants authorizing this agent

identity blueprint principal to access an API on

behalf of a signed-in user. Read-only. Nullable.

Inherited from microsoft.graph.servicePrincipal

ownedObjects

directoryObject

collection

Directory objects that are owned by this agent

identity blueprint principal. Read-only. Nullable.

Supports `$expand` and `$filter` ( ` /$count eq 0` ,

`/$count ne 0` , `/$count eq 1` , `/$count ne 1` ).

Inherited from microsoft.graph.servicePrincipal

owners

directoryObject

collection

Directory objects that are owners of this agent

identity blueprint principal. The owners are a set of

nonadmin users or servicePrincipals who are

allowed to modify this object. Supports `$expand`

and `$filter` ( ` /$count eq 0` , `/$count ne 0` , `/$count`

`eq 1` , `/$count ne 1` ). Inherited from

microsoft.graph.servicePrincipal

sponsors

directoryObject

collection

The sponsors for this agent identity blueprint

principal. Sponsors are users or service principals

who can authorize and manage the lifecycle of

agent identity instances.

The following JSON representation shows the resource type. Only a subset of all properties are

returned by default. All other properties can only be retrieved using `$select` .

JSON

**Last updated on 11/17/2025**

**JSON representation**

`{`

`  ``"@odata.type"` `: ``"#microsoft.graph.agentIdentityBlueprintPrincipal"` `,`

`  ``"id"` `: ``"String (identifier)"` `,`

`  ``"accountEnabled"` `: ``"Boolean"` `,`

`  ``"createdByAppId"` `: ``"String"` `,`

`  ``"appDescription"` `: ``"String"` `,`

`  ``"appDisplayName"` `: ``"String"` `,`

`  ``"appId"` `: ``"String"` `,`

`  ``"appOwnerOrganizationId"` `: ``"Guid"` `,`

`  ``"appRoleAssignmentRequired"` `: ``"Boolean"` `,`

`  ``"disabledByMicrosoftStatus"` `: ``"String"` `,`

`  ``"displayName"` `: ``"String"` `,`

`  ``"publisherName"` `: ``"String"` `,`

`  ``"servicePrincipalNames"` `: [`

`    ``"String"`

`  ],`

`  ``"servicePrincipalType"` `: ``"String"` `,`

`  ``"signInAudience"` `: ``"String"` `,`

`  ``"tags"` `: [`

`    ``"String"`

`  ],`

`  ``"appRoles"` `: [`

`    {`

`      ``"@odata.type"` `: ``"microsoft.graph.appRole"`

`    }`

`  ],`

`  ``"info"` `: {`

`    ``"@odata.type"` `: ``"microsoft.graph.informationalUrl"`

`  },`

`  ``"publishedPermissionScopes"` `: [`

`    {`

`      ``"@odata.type"` `: ``"microsoft.graph.permissionScope"`

`    }`

`  ],`

`  ``"verifiedPublisher"` `: {`

`    ``"@odata.type"` `: ``"microsoft.graph.verifiedPublisher"`

`  }`

`}`

**agentIdentity resource type**

Namespace: microsoft.graph

Represents an agent identity in an Entra ID directory. An agent identity is an account used by

AI agents to authenticate within the Microsoft Entra ID ecosystem.

Inherits from servicePrincipal.

This resource is an open type that allows additional properties beyond those documented here.

**Method**

**Return type**

**Description**

List

agentidentity collection

Get a list of the agentidentity objects and their

properties.

Create

agentidentity

Create a new agentidentity object.

Get

agentIdentity

Read the properties and relationships of

agentIdentity object.

Update

agentIdentity

Update the properties of an agentIdentity object.

**App role assignments**

List appRoleAssignedTo

appRoleAssignment

collection

Get the users, groups, and agent identities

assigned app roles for this agent identity.

List appRoleAssignments

appRoleAssignment

collection

Get the app roles that this agent identity is

assigned.

Create

appRoleAssignment

appRoleAssignment

Create a new appRoleAssignment object.

Delete

appRoleAssignment

appRoleAssignment

Delete an existing appRoleAssignment object.

） **Important**

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs

in production applications is not supported. To determine whether an API is available in

v1.0, use the **Version** selector.

**Methods**

ﾉ

**Expand table**

**Method**

**Return type**

**Description**

**Delegated permission**

**grants**

List

oauth2PermissionGrants

oAuth2PermissionGrant

collection

Get the delegated permission grants authorizing

this agent identity to access an API on behalf of a

signed-in user.

**Deleted items**

List

directoryObject collection

Retrieve a list of recently deleted agent identities.

Get

directoryObject

Retrieve the properties of a recently deleted

agent identity.

Restore

directoryObject

Restore a recently deleted agent identity.

Permanently delete

None

Permanently delete an agent identity.

**Directory objects**

List ownedObjects

directoryObject collection

Get directory objects owned by this agent

identity.

**Memberships**

List direct memberships

directoryObject collection

Get the groups that this agent identity is a direct

member of.

List transitive

memberships

directoryObject collection

Get the groups that this agent identity is a

member of. This operation is transitive and

includes the groups that this agent identity is a

nested member of.

**Owners**

List owners

directoryObject collection

Get the owners of this agent identity.

Add owners

directoryObject

Add owners by posting to the owners collection.

Remove owners

None

Remove a directoryObject object.

**Sponsors**

List sponsors

directoryObject collection

Get the sponsors for this agent identity.

Add sponsors

directoryObject

Add sponsors by posting to the sponsors

collection.

Remove sponsors

None

Remove a directoryObject object.

**Property**

**Type**

**Description**

odata.type

String

`#microsoft.graph.agentIdentity` .

Distinguishes this object as an agent

identity. Can be used to identify this object

as an agent identity, instead of another kind

of service principal.

accountEnabled

Boolean

`true` if the agent identity account is

enabled; otherwise, `false` . If set to `false` ,

then no users are able to sign in to this app,

even if they're assigned to it. Inherited from

servicePrincipal.

agentIdentityBlueprintId

String

The **appId** of the agent identity blueprint

that defines the configuration for this agent

identity.

customSecurityAttributes

customSecurityAttributeValue

An open complex type that holds the value

of a custom security attribute that is

assigned to a directory object. Nullable.

Returned only on `$select` . Inherited from

servicePrincipal.

createdByAppId

String

The **appId** of the application used to create

the agent identity. Set internally by

Microsoft Entra ID. Read-only. Inherited

from servicePrincipal.

createdDateTime

DateTimeOffset

The date and time the agent identity was

created. Read-only. Inherited from

servicePrincipal.

disabledByMicrosoftStatus

String

Specifies whether Microsoft has disabled the

registered Agent Identity Blueprint. Possible

values are: `null` (default value),

`NotDisabled` , and

`DisabledDueToViolationOfServicesAgreement`

(reasons may include suspicious, abusive, or

malicious activity, or a violation of the

**Properties**

） **Important**

While this resource inherits from **servicePrincipal**, some properties are not applicable.

ﾉ

**Expand table**

**Property**

**Type**

**Description**

Microsoft Services Agreement). Inherited

from servicePrincipal.

displayName

String

The display name for the agent identity.

Inherited from servicePrincipal.

id

String

The unique identifier for the agent identity.

Inherited from directoryObject. Key. Not

nullable. Read-only. Inherited from entity.

servicePrincipalType

String

Set to **ServiceIdentity** for all agent identities.

Inherited from servicePrincipal.

tags

String collection

Custom strings that can be used to

categorize and identify the agent identity.

Not nullable. The value is the union of

strings set here and on the associated Agent

Identity Blueprint entity's **tags** property.

Inherited from servicePrincipal.

**Relationship**

**Type**

**Description**

appRoleAssignedTo

appRoleAssignment

collection

App role assignments for this app or service,

granted to users, groups, and other agent identities.

Supports `$expand` . Inherited from

microsoft.graph.servicePrincipal

appRoleAssignments

appRoleAssignment

collection

App role assignment for another app or service,

granted to this agent identity. Supports `$expand` .

Inherited from microsoft.graph.servicePrincipal

createdObjects

directoryObject

collection

Directory objects created by this agent identity.

Read-only. Nullable. Inherited from

microsoft.graph.servicePrincipal

memberOf

directoryObject

collection

Roles that this agent identity is a member of. HTTP

Methods: GET Read-only. Nullable. Supports

`$expand` . Inherited from

microsoft.graph.servicePrincipal

oauth2PermissionGrants

oAuth2PermissionGrant

collection

Delegated permission grants authorizing this agent

identity to access an API on behalf of a signed-in

**Relationships**

ﾉ

**Expand table**

**Relationship**

**Type**

**Description**

user. Read-only. Nullable. Inherited from

microsoft.graph.servicePrincipal

ownedObjects

directoryObject

collection

Directory objects that are owned by this agent

identity. Read-only. Nullable. Supports `$expand` and

`$filter` ( ` /$count eq 0` , `/$count ne 0` , `/$count eq`

`1` , `/$count ne 1` ). Inherited from

microsoft.graph.servicePrincipal

owners

directoryObject

collection

Directory objects that are owners of this agent

identity. The owners are a set of nonadmin users or

agent identities who are allowed to modify this

object. Supports `$expand` and `$filter` ( ` /$count eq`

`0` , `/$count ne 0` , `/$count eq 1` , `/$count ne 1` ).

Inherited from microsoft.graph.servicePrincipal

sponsors

directoryObject

collection

The sponsors for this agent identity.

The following JSON representation shows the resource type. Only a subset of all properties are

returned by default. All other properties can only be retrieved using $select.

JSON

**Last updated on 11/17/2025**

**JSON representation**

`{`

`  ``"@odata.type"` `: ``"#microsoft.graph.agentIdentity"` `,`

`  ``"id"` `: ``"String (identifier)"` `,`

`  ``"accountEnabled"` `: ``"Boolean"` `,`

`  ``"agentIdentityBlueprintId"` `: ``"String"` `,`

`  ``"createdByAppId"` `: ``"String"` `,`

`  ``"createdDateTime"` `: ``"String (timestamp)"` `,`

`  ``"disabledByMicrosoftStatus"` `: ``"String"` `,`

`  ``"displayName"` `: ``"String"` `,`

`  ``"servicePrincipalType"` `: ``"String"` `,`

`  ``"tags"` `: [`

`    ``"String"`

`  ]`

`}`

**Microsoft Entra Agent ID preview: Known**

**issues and gaps**

This article lists limitations, issues, and feature gaps observed in the preview. You can always

return to this article for the most up to date known issues. These items can change or be

resolved without notice. Microsoft Entra Agent ID is subject to its standard preview terms and

conditions.

The following known issues and gaps relate to agent identities and agent identity blueprints.

Microsoft Graph APIs support various relationships involving agent identities and agent

identity blueprints, such as `/ownedObjects` , `/deletedItems` , `/owners` , and more. There's no way

to filter these queries to return only Agent IDs. To use the existing APIs documented in

Microsoft Graph reference docs and perform client side filtering, use the `odata.type` property

to filter results to Agent IDs.

The following known issues and gaps relate to agent users.

When an agent identity blueprint or agent identity is deleted, any agent users created using

that blueprint or identity remain in the tenant. They aren't shown as disabled or deleted,

though they can't authenticate. Delete any orphaned agent users via Microsoft Entra admin

center, Microsoft Graph APIs, or scripting tools.

The following known issues and gaps relate to roles and permissions for managing agent

identities.

**Agent identities and agent identity blueprints**

**Agent IDs in Graph API relationships**

**Agent users**

**Clean up agent users**

**Roles and permissions for agent identity**

**management**

**Global Reader can't list agent identities**

When querying Microsoft Graph APIs to list agent identities using the endpoint `GET`

`https://graph.microsoft.com/beta/servicePrincipals/graph.agentIdentity` , users assigned the

Global Reader role receive a `403 Unauthorized` response. Use the endpoint `GET`

`https://graph.microsoft.com/beta/servicePrincipals` instead to make the query.

There's currently no viable delegated permission for creating agent identities. Implementers

must use application permissions to create agent identities.

When creating, updating, and deleting Agent IDs, clients can use delegated permissions like

_AgentIdentityBlueprint.Create_ and _AgentIdentityBlueprintPrincipal.EnableDisable.All_. However, if

the client has been granted the delegated permission _Directory.AccessAsUser.All_, the client's

permission to create and modify Agent IDs are ignored. This can cause Microsoft Graph

requests to fail with `403 Unauthorized` , even though the client and user have the appropriate

permissions. The work-around here's to remove the _Directory.AccessAsUser.All_ permission from

the client, request new access tokens, and retry the request.

You can't include actions for management of agent identities in Microsoft Entra ID custom role

definitions. Use built-in roles _Agent ID Administrator_ and _Agent ID Developer_ for all

management of Agent IDs.

You can't add agent identities, agent identity blueprints, and agent identity blueprint principals

to administrative units. Use the `owners` property of Agent IDs to limit the set of users who can

manage these objects.

The _Agent ID Administrator_ role can't update photos for agent users. Use the _User_

_Administrator_ role to update photos for agent users.

**Delegated permissions for agent identity creation**

**Directory.AccessAsUser.All causes other permissions to be**

**ignored**

**Custom roles**

**Administrative units**

**Updating photos for agent users**

**Microsoft Entra admin center**

The following known issues and gaps relate to the Microsoft Entra admin center.

You can't create or edit agent identity blueprints through the Microsoft Entra admin center or

the Azure portal. To create agent identity blueprints, follow the documentation to create and

edit blueprint configuration using Microsoft Graph APIs and PowerShell.

The following known issues and gaps relate to authentication protocols.

Agent IDs can't sign-in to Microsoft Entra ID's sign-in pages. This means they can't single-sign

on to websites and web apps using the OpenID Connect or SAML protocols. Use available web

APIs to integrate agents with workplace apps and services.

The following known issues and gaps relate to consent and permissions.

The Microsoft Entra ID admin consent workflow doesn't work properly for permissions

requested by Agent IDs. Users can contact their Microsoft Entra ID tenant admins to request

permissions be granted to an Agent ID.

You can't grant Microsoft Entra ID application permissions (app roles) to agent identity

blueprint principals. Grant application permissions to individual agent identities instead.

You can't assign Microsoft Entra ID app roles where the target resource of the role assignment

is an agent identity. Assign app roles using an agent identity blueprint principal as the target

resource.

**No agent identity blueprint management**

**Authentication protocols**

**Single-Sign-On to web apps**

**Consent and permissions**

**Admin consent workflow (ACW)**

**Application permissions for agent identity blueprints**

**App role assignment to agent identity**

User consents that are blocked by risk-based step-up have no mention of "risky" in the UX.

There's no workaround for this. Risk-based step-up is still enforced.

The following known issues and gaps relate to Microsoft Entra ID administration.

You can't add agent identities and agent users to Microsoft Entra ID groups with dynamic

membership. Add Agent IDs to security groups with fixed membership.

The following known issues and gaps relate to monitoring and logs.

Audit logs don't distinguish Agent IDs from other identities:

Operations on agent identities, agent identity blueprints, and agent identity blueprint

principals are logged in the _ApplicationManagement_ category.

Operations on agent users are logged in the _User Management_ category.

Operations initiated by agent identities appear as service principals in audit logs.

Operations initiated by agent users appear as users in audit logs.

The workarounds for these limitations are:

Use the object IDs provided in audit logs to query Microsoft Graph and determine the

entity type.

Use the Microsoft Entra sign-in logs correlation ID to locate the identity of the actor or

subject involved in the auditable activity.

The Microsoft Graph activity logs don't distinguish Agent IDs from other identities:

Requests from agent identities are logged as applications, with the agent identity

included in the _appID_ column.

**Consents blocked by risk-based step-up**

**Microsoft Entra ID administration**

**Dynamic groups**

**Monitoring and logs**

**Audit logs**

**Microsoft Graph activity logs**

Requests from agent users are logged as users, with the `agentUser` ID in the _UserID_

column.

The workaround here's to join with the Microsoft Entra sign-in logs to determine the entity

type.

No known issues.

The following known issues and gaps relate to performance and scale.

When using the Microsoft Graph APIs to create Agent IDs, attempts to create multiple entities

in quick sequence might fail with errors like `400 Bad Request: Object with id {id} not found` .

Retrying the request might not succeed for several minutes. Examples include:

Create agent identity blueprint, quickly create blueprint principal.

Create agent identity blueprint, quickly add credential.

Create agent identity blueprint principal, then use blueprint to create agent identity.

Create agent identity, quickly create agent user.

These sequences of requests often fail when using MS Graph application permissions to

authorize the requests. Use delegated permissions where possible. Add retry logic to your

requests with exponential backoff and a reasonable timeout.

The following known issues and gaps relate to product integrations.

Agents built using Copilot Studio must opt in to Agent IDs in the agent's environment settings.

Only custom engine agents are supported at this time. Custom engine agents currently use

Agent IDs for authenticating to the channels where they're published. Agent IDs aren't

currently used for authentication to connectors or tools in Copilot Studio.

**Security and compliance**

**Performance and scale**

**Delays in multiple creation requests**

**Product integrations**

**Copilot Studio agents**

Agent ID scenarios introduce extra complexity when using MSAL due to the need to manage

Federated Identity Credentials (FIC). For .NET developers, Microsoft recommends using

Microsoft.Identity.Web.AgentIdentities

, which provides a streamlined experience for Agent

IDs. For non-.NET implementations, use the Microsoft Entra SDK for agent ID, designed to

simplify Agent ID integration across other languages.

If you encounter an unlisted issue, report an issue using aka.ms/agentidfeedback

.

**Last updated on 11/18/2025**

**Libraries and SDKs**

**Reporting new issues**

