**Tell us about your PDF experience.**

**Microsoft Entra SDK for AgentID: Overview**

The Microsoft Entra SDK for AgentID is a containerized web service that handles token

acquisition, validation, and secure downstream API calls. It runs as a companion container

alongside your application, allowing you to offload identity logic to a dedicated service. By

centralizing identity operations in the Microsoft Entra SDK for AgentID, you eliminate the need

to embed complex token management logic in each service, reducing code duplication and

potential security vulnerabilities.

If you're building with Kubernetes, containerized services with Docker, or modern microservices

on Azure, the Microsoft Entra SDK for AgentID provides a standardized way to handle

authentication and authorization in cloud-native applications.

The Microsoft Entra SDK for AgentID communicates with your application through a HTTP API

for authentication and authorization, providing consistent integration patterns regardless of

your technology stack. Instead of embedding identity logic directly in your application code,

the Microsoft Entra SDK for AgentID handles token management, validation, and API calls

through standard HTTP requests.

This approach enables polyglot microservices architectures where different services can be

written in Python, Node.js, Go, Java, and others while maintaining consistent authentication

patterns.

The typical architecture is as follows:

_Client Application → Your Web API → Microsoft Entra SDK for AgentID → Microsoft Entra ID_

For the latest container image and version tags, see the Container Image to get started.

Ensure your Microsoft Entra SDK for AgentID deployment follows best practices for secure

operation. The SDK must run in a containerized environment with restricted network access, to

**What is the Microsoft Entra SDK for AgentID?**

７ **Note**

The Microsoft Entra SDK for AgentID is currently in preview. Check the **GitHub releases**

for latest available tags.

**Security**

prevent unauthorized access. Exposing the SDK API publicly can lead to security vulnerabilities,

such as unauthorized token acquisition.

Consult Security Best Practices to ensure best practices for network, credential, and runtime

security recommendations.

To get started with the Microsoft Entra SDK for AgentID, the following steps are recommended:

1\. **Choose your deployment** \- Select Kubernetes, Docker, or AKS

2\. **Configure settings** \- Set up environment variables

3\. **Pick a scenario** \- Follow a guided example

4\. **Deploy to production** \- Review security best practices

The architecture separates identity concerns from business logic, providing the following

benefits:

**Benefit**

**Description**

**Multiple Language**

**Support**

Call via HTTP from Python, Node.js, Go, Java, and others

**Centralized Security**

**config**

One place for identity configuration, token management and credential

management

**Container Native**

Built for Kubernetes, Docker, AKS and other modern deployments

**Zero Trust Ready**

Integrates with managed identity and proof-of-possession tokens - keeping

sensitive data out of your application code

Ｕ **Caution**

The the SDK API must not be publicly accessible. It should only be reachable by

applications within the same trust boundary (e.g., same pod or virtual network) to prevent

unauthorized token acquisition.

**Quick Start**

**Key benefits**

ﾉ

**Expand table**

**Scenario**

**Use Microsoft Entra SDK for AgentID**

**Use Microsoft.Identity.Web**

**Language Support**

Multiple languages (Python, Node.js, Go,

Java, etc.)

.NET only

**Deployment Model**

Containers (Kubernetes, Docker, AKS)

Any deployment model

**Identity Patterns**

Consistent patterns across all services

Deep .NET framework

integration

**Agent Identity**

Available in all supported languages

.NET only

**Token Validation**

Available in all supported languages

.NET only

**Security Model**

Secrets and tokens isolated from application

code

Integrated with application

**Performance**

Additional network hop required

Direct in-process calls

**Framework**

**Integration**

HTTP API integration

Native .NET integration

**Containerization**

Designed for containerized environments

Works with or without

containers

See Comparison with Microsoft.Identity.Web for detailed guidance on choosing between the

two approaches.

The Microsoft Entra SDK for AgentID validates both access tokens and ID tokens issued by

Microsoft Entra ID, verifying their signatures against Microsoft Entra ID's public keys, checking

expiration times, and ensuring the tokens are intended for your application. Once validated,

you can extract user claims, roles, and scopes to make informed authorization decisions within

your application logic.

**On-Behalf-Of OAuth 2.0 flow** \- Delegate user context to downstream APIs

**Client Credentials** \- Application-to-application authentication

**When to use the Microsoft Entra SDK for AgentID**

**or Microsoft.Identity.Web**

ﾉ

**Expand table**

**Token validation**

**Token Acquisition / Authorization header creation**

**Managed Identity** \- Native Azure service authentication

**Agent Identity** \- Autonomous or delegated agent patterns

Acquire and attach tokens automatically

Optional request overrides (scopes, method, headers)

Signed HTTP Requests (PoP/SHR) support

The following guides are comprehensive step-by-step tutorials with practical code examples

demonstrating how to integrate the Microsoft Entra SDK for AgentID into your applications.

Each scenario provides complete request/response examples, code snippets, and

implementation patterns tailored for different programming languages and frameworks.

**Scenario**

**Description**

**Validate Authorization**

**Header**

Extract claims from bearer tokens for access control and custom

authorization middleware

**Obtain Authorization**

**Header**

Acquire tokens for calling downstream APIs securely

**Call Downstream API**

Make HTTP calls to protected APIs with automatic token attachment for

multi-language microservices

**Use Managed Identity**

Authenticate as an Azure service for calling Microsoft Graph or other

Azure services

**Implement Long-Running**

**OBO Flow**

Handle user context over extended operations with token refresh and

On-Behalf-Of delegation

**Use Signed HTTP Requests**

Implement proof-of-possession security with PoP tokens

**Agent Autonomous Batch**

**Processing**

Process batch jobs with autonomous agent identity

**Integrate from TypeScript**

Use the Microsoft Entra SDK for AgentID from Node.js/Express/NestJS

applications

**Integrate from Python**

Use the Microsoft Entra SDK for AgentID from Flask/FastAPI/Django

applications

**Downstream API calls**

**Scenarios & Tutorials**

ﾉ

**Expand table**

A typical flow where your client calls a Web API, the API delegates identity operations to the

Microsoft Entra SDK for AgentID via HTTP endpoints. The SDK validates inbound tokens using

the `/Validate` endpoint, acquires tokens using `/AuthorizationHeader` and

`/AuthorizationHeaderUnauthenticated` , and can directly invoke downstream APIs using

`/DownstreamApi` and `/DownstreamApiUnauthenticated` .

It interacts with Microsoft Entra ID for token issuance and Open ID Connect metadata retrieval,

with architecture demonstrated in the following snippet:

mermaid

The following resources provide comprehensive guidance and help with troubleshooting issues

and answers to common questions.

**Resource**

**Description**

**Agent Identities**

Learn about autonomous and delegated agent patterns for advanced scenarios

**Architecture patterns**

`%%{init: {`

`  "theme": "base",`

`  "themeVariables": {`

`    "background": "#121212",`

`    "primaryColor": "#1E1E1E",`

`    "primaryBorderColor": "#FFFFFF",`

`    "primaryTextColor": "#FFFFFF",`

`    "textColor": "#FFFFFF",`

`    "lineColor": "#FFFFFF",`

`    "labelBackground": "#000000"`

`  }`

`}}%%`

`flowchart LR`

`    classDef dnode fill:#1E1E1E,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF`

`    linkStyle default stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF`

`    client[Client Application]:::dnode -->| Bearer over HTTP | webapi[Web `

`API]:::dnode`

`    subgraph Pod / Host`

`        webapi -->|"/Validate<br/>/AuthorizationHeader/{name}`

`<br/>/DownstreamApi/{name}"| sidecar[Microsoft Entra SDK for AgentID]:::dnode`

`    end`

`    sidecar -->|Token validation & acquisition| entra[Microsoft Entra ID]:::dnode`

**Support and resources**

ﾉ

**Expand table**

**Resource**

**Description**

**API Reference**

Complete endpoint documentation with request/response formats, query parameters,

and error codes

**Troubleshooting**

Common issues and step-by-step solutions for deployment and runtime problems

**FAQ**

Frequently asked questions covering configuration, security, and integration topics

For additional help:

Report issues on Microsoft-identity-web repository

Check Microsoft Entra ID troubleshooting guides

Microsoft Entra ID documentation

Microsoft Identity Platform documentation

Microsoft Identity Web repository

Kubernetes documentation

Docker documentation

**Last updated on 11/12/2025**

**Additional resources**

**Comparison: Microsoft Entra SDK for**

**AgentID vs. In-Process**

**Microsoft.Identity.Web**

This guide helps you identify the differences between the Microsoft Entra SDK for AgentID and

the in-process Microsoft.Identity.Web library for handling authentication in your applications.

The Microsoft.Identity.Web library integrates directly into .NET applications for maximum

performance, while the Microsoft Entra SDK for AgentID runs as a separate container and

supports any programming language via HTTP APIs, and choosing the correct approach

depends on your application's architecture, language, and deployment environment.

The fundamental difference lies in **where authentication logic executes**. Microsoft.Identity.Web

runs within your application process, while the Microsoft Entra SDK for AgentID operates as an

independent service alongside your application. This architectural choice impacts factors such

as development workflow and operational complexity.

**Aspect**

**Microsoft.Identity.Web (In-Process)**

**Microsoft Entra SDK for AgentID (Out-of-**

**Process)**

**Process**

**Boundary**

Shares the same process, memory, and

lifecycle as your application, enabling

direct method calls and shared

configuration

Maintains complete isolation,

communicating only through HTTP APIs and

managing its own resources independently

**Language**

**Coupling**

Tightly couples your authentication

strategy to .NET, requiring C# experience

and .NET runtime everywhere you need

authentication

Decouples authentication from your

application's technology stack, exposing a

language-agnostic HTTP interface that

works equally well with Python, Node.js, Go,

or any HTTP-capable language

**Deployment**

**Model**

Deploys as NuGet packages embedded in

your application binary, creating a

monolithic deployment unit

Deploys as a separate container image,

enabling independent versioning, scaling,

and updates of authentication logic without

impacting your application code

**Architectural differences**

ﾉ

**Expand table**

**Microsoft.Identity.Web (In-Process)**

This code snippet shows how Microsoft.Identity.Web integrates directly into an ASP.NET Core

application:

C#

This code snippet demonstrates how to call the Microsoft Entra SDK for AgentID from a

Node.js application using HTTP. The call to the SDK's `/DownstreamApi` endpoint handles token

acquisition and downstream API calls, including passing the incoming token for OBO flows in

the `Authorization` header:

TypeScript

`// Startup configuration`

`services.AddMicrosoftIdentityWebApiAuthentication(Configuration)`

`    .EnableTokenAcquisitionToCallDownstreamApi()`

`    .AddDownstreamApi(` `"Graph"` `, Configuration.GetSection(` `"DownstreamApis:Graph"` `))`

`    .AddInMemoryTokenCaches();`

`// Usage in controller`

`public`  ` `  `class`  ` `  `MyController` ` : ` `ControllerBase`

`{`

`    ` `private`  ` `  `readonly` ` IDownstreamApi _downstreamApi;`

`    `

`    ` `public`  ` `  `MyController` `(IDownstreamApi downstreamApi)`

`    {`

`        _downstreamApi = downstreamApi;`

`    }`

`    `

`    ` `public`  ` `  `async` ` Task<ActionResult> ` `GetUserData` `()`

`    {`

`        ` `var` ` user = ` `await` ` _downstreamApi.GetForUserAsync<User>(` `"Graph"` `, `

`            options => options.RelativePath = ``"me"` `);`

`        ` `return` ` Ok(user);`

`    }`

`}`

**Microsoft Entra SDK for AgentID (Out-of-Process)**

`// Configuration`

`const` ` SidecarUrl = process.env.SIDECAR_URL || ``"http://localhost:5000"` `;`

`// Usage in application`

`async`  ` `  `function`  ` `  `getUserData` `(incomingToken: ` `string` `) {`

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${SidecarUrl}` ``/DownstreamApi/Graph?optionsOverride.RelativePath=me` `` `,`

`    {`

`      headers: {`

`        ``'Authorization'` `: ` `` `Bearer `` `${incomingToken}`  `` ` ``

`      }`

`    }`

**Feature**

**Microsoft.Identity.Web**

**Microsoft Entra SDK for AgentID**

**Language Support**

C# / .NET only

Any language (HTTP)

**Deployment**

In-process library

Separate container

**Token Acquisition**

✅ Direct MSAL.NET

✅ Via HTTP API

**Token Caching**

✅ In-memory, ✅ distributed

✅ In-memory, ❌distributed

**OBO Flow**

✅ Native support

✅ Via HTTP endpoint

**Client Credentials**

✅ Native support

✅ Via HTTP endpoint

**Managed Identity**

✅ Direct support

✅ Direct support

**Agent Identities**

✅ Via extensions

✅ Query parameters

**Token Validation**

✅ Middleware

✅ /Validate endpoint

**Downstream API**

✅ IDownstreamApi

✅ /DownstreamApi endpoint

**Microsoft Graph**

✅ Graph SDK integration

⚠Via DownstreamApi

**Performance**

⚡ In-process (fastest)

🔄 HTTP overhead

**Configuration**

`appsettings.json` and code

`appsettings.json` and Environment variables

**Debugging**

✅ Standard .NET debugging

⚠Container debugging

**Hot Reload**

✅ .NET Hot Reload

❌ Container restart

**Package Updates**

📦 NuGet packages

🐳 Container images

**License**

MIT

MIT

`  );`

`  `

`  ` `const` ` result = ` `await` ` response.json();`

`  ` `return`  ` `  `JSON` `.parse(result.content);`

`}`

**Feature Comparison**

ﾉ

**Expand table**

**When to Use Each Approach**

Deciding between Microsoft.Identity.Web and the Microsoft Entra SDK for AgentID depends on

your application's requirements, architecture, and deployment strategy. Depending on your

needs, one approach may be more suitable than the other, and the following guidelines could

help you make an informed decision.

**Scenario**

**Microsoft.Identity.Web (In-**

**Process)**

**Microsoft Entra SDK for AgentID (Out-**

**of-Process)**

**Application Stack**

.NET applications exclusively

• ASP.NET Core Web APIs

• ASP.NET Core Web Apps

• .NET Worker Services

• Blazor applications

• Daemon apps

Multi-language microservices

• Node.js, Python, Go, Java services

• Polyglot architectures

• Non-.NET services

• Legacy systems integration

**Performance**

**Requirements**

Performance is critical

• High-throughput scenarios

• Latency-sensitive operations

• Every millisecond counts

Can tolerate HTTP overhead

• ~1-5ms additional latency acceptable

• Throughput not bottlenecked by auth

**Integration Needs**

Deep integration required

• Custom MSAL.NET configuration

• Direct access to MSAL features

• Advanced token cache

strategies

Standardized integration

• HTTP API sufficient

• Consistent auth patterns across services

**Development**

**Experience**

Rapid development

• Quick prototyping

• Hot reload for development

• Standard .NET debugging

Container-based development

• Container restart for changes

• Container debugging required

**Team & Architecture**

Single-language stack

• Team expertise in C#/.NET

• No multi-language

requirements

Technology diversity

• Mix of frameworks and languages

• Polyglot team structure

**Deployment Model**

Monolithic deployments

• Single application deployment

• Traditional hosting models

Containerized deployments

• Kubernetes environments

• Docker Compose setups

• Service mesh architectures

**Operations**

Coupled auth updates

• Auth changes require app

rebuild

• Shared lifecycle with application

Operational benefits

• Independent scaling of auth logic

• Separate auth updates from app code

• Centralized monitoring of auth

ﾉ

**Expand table**

In certain scenarios, you may want to migrate an existing .NET application using

Microsoft.Identity.Web to leverage the Microsoft Entra SDK for AgentID for authentication. The

reasons for migration could include adopting a multi-language architecture, standardizing

authentication across services, or moving to a containerized deployment model.

Careful consideration and planning is required before you do so. This section provides a high-

level migration path with code examples to help you transition your application.

First you'll need to add the SDK container to your pod:

YAML

**Migration Guidance**

**Migrating from Microsoft.Identity.Web to Microsoft Entra SDK**

**for AgentID**

Ｕ **Caution**

Microsoft doesn't recommend that you move from Microsoft.Identity.Web to the

Microsoft Entra SDK for AgentID, but if you chose to do so, the following are

demonstrations of similar concepts in other languages and frameworks.

**Step 1: Deploy SDK Container**

`# Before: Single ASP.NET Core container`

`containers:`

`- name:`  ` `  `app`

`  image:`  ` `  `myregistry/myapp:latest`

`# After: App + Microsoft Entra SDK for AgentID`

`containers:`

`- name:`  ` `  `app`

`  image:`  ` `  `myregistry/myapp:latest`

`  env:`

`  - name:`  ` `  `SIDECAR_URL`

`    value:` ` ` `"http://localhost:5000"`

`- name:`  ` `  `sidecar`

`  image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`  env:`

`  - name:`  ` `  `AzureAd__TenantId`

`    value:` ` ` `"your-tenant-id"`

`  - name:`  ` `  `AzureAd__ClientId`

`    value:` ` ` `"your-client-id"`

Next, you'll need to transfer your configuration from `appsettings.json` to environment

variables:

**Before (appsettings.json)**

JSON

**After (Kubernetes ConfigMap / Environment Variables)**

YAML

Locate all instances of in-process calls to Microsoft.Identity.Web and replace them with HTTP

calls to the Microsoft Entra SDK for AgentID endpoints:

**Before (C# with IDownstreamApi)**:

C#

**Step 2: Migrate configuration**

`{`

`  ``"AzureAd"` `: {`

`    ``"Instance"` `: ``"https://login.microsoftonline.com/"` `,`

`    ``"TenantId"` `: ``"your-tenant-id"` `,`

`    ``"ClientId"` `: ``"your-client-id"`

`  },`

`  ``"DownstreamApis"` `: {`

`    ``"Graph"` `: {`

`      ``"BaseUrl"` `: ``"https://graph.microsoft.com/v1.0"` `,`

`      ``"Scopes"` `: ``"User.Read Mail.Read"` `, `

`      ``"RelativePath"` `: ``"/me"`

`    }`

`  }`

`}`

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `ConfigMap`

`metadata:`

`  name:`  ` `  `sidecar-config`

`data:`

`  AzureAd__Instance:` ` ` `"https://login.microsoftonline.com/"`

`  AzureAd__TenantId:` ` ` `"your-tenant-id"`

`  AzureAd__ClientId:` ` ` `"your-client-id"`

`  DownstreamApis__Graph__BaseUrl:` ` ` `"https://graph.microsoft.com/v1.0"`

`  DownstreamApis__Graph__Scopes:` ` ` `"User.Read Mail.Read"`

`  DownstreamApis__Graph__RelativePath:` ` ` `"/me"`

**Step 3: Update Application Code**

**After (Any language with HTTP client)**:

In the following snippet, we can see calls to the Microsoft Entra SDK for AgentID using the

`/DownstreamApi` endpoint to get user data. Examples are provided in C# and TypeScript.

C#

`public`  ` `  `class`  ` `  `UserController` ` : ` `ControllerBase`

`{`

`    ` `private`  ` `  `readonly` ` IDownstreamApi _downstreamApi;`

`    `

`    ` `public`  ` `  `UserController` `(IDownstreamApi downstreamApi)`

`    {`

`        _downstreamApi = downstreamApi;`

`    }`

`    `

`    [`  `HttpGet` `]`

`    ` `public`  ` `  `async` ` Task<ActionResult<User>> GetMe()`

`    {`

`        ` `var` ` user = ` `await` ` _downstreamApi.GetForUserAsync<User>(`

`            ``"Graph"` `,`

`            options => options.RelativePath = ``"me"`

`        );`

`        ` `return` ` Ok(user);`

`    }`

`}`

`public`  ` `  `class`  ` `  `UserController` ` : ` `ControllerBase`

`{`

`    ` `private`  ` `  `readonly` ` HttpClient _httpClient;`

`    ` `private`  ` `  `readonly`  ` `  `string` ` _SidecarUrl;`

`    `

`    ` `public`  ` `  `UserController` `(IHttpClientFactory httpClientFactory, IConfiguration `

`config)`

`    {`

`        _httpClient = httpClientFactory.CreateClient();`

`        _SidecarUrl = config[` `"SIDECAR_URL"` `];`

`    }`

`    `

`    [`  `HttpGet` `]`

`    ` `public`  ` `  `async` ` Task<ActionResult<User>> GetMe()`

`    {`

`        ` `var` ` inboundAuthorizationHeader = `

`Request.Headers[` `"Authorization"` `].ToString();`

`        ``// this validates the inbound authorization header and calls the downstream `

`API.`

`        ``// If you don't call a downstream API, Do validate the inbound authorization `

`header `

`        ``// (calling the /Validate endpoint)`

`        ` `var` ` request = ` `new` ` HttpRequestMessage(`

`            HttpMethod.Get,`

`            ` `$"` `{_SidecarUrl}` `/DownstreamApi/Graph?optionsOverride.RelativePath=me"`

The same logic can be implemented in TypeScript as follows:

TypeScript

Once the previous steps have been completed, you can tidy your application by removing the

NuGet packages used by Microsoft.Identity.Web from your project:

XML

If you still want to validate tokens in your app, you do not need to fully remove the original

authentication configuration, although you could delegate validation entirely to the Microsoft

Entra SDK for AgentID.

`        );`

`        request.Headers.Add(` `"Authorization"` `, inboundAuthorizationHeader);`

`        `

`        ` `var` ` response = ` `await` ` _httpClient.SendAsync(request);`

`        ` `var` ` result = ` `await` ` response.Content.ReadFromJsonAsync<SidecarResponse>();`

`        ` `var` ` user = JsonSerializer.Deserialize<User>(result.Content);`

`        ` `return` ` Ok(user);`

`    }`

`}`

**TypeScript**

`export`  ` `  `async`  ` `  `function`  ` `  `getMe` `(incomingToken: ` `string` `): ` `Promise`  `<`  `User`  `> {`

`  ` `const` ` SidecarUrl = process.env.SIDECAR_URL!;`

`  `

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${SidecarUrl}` ``/DownstreamApi/Graph?optionsOverride.RelativePath=me` `` `,`

`    {`

`      headers: {`

`        ``'Authorization'` `: incomingToken`

`      }`

`    }`

`  );`

`  `

`  ` `const` ` result = ` `await` ` response.json();`

`  ` `return`  ` `  `JSON` `.parse(result.content) ` `as` ` User;`

`}`

**Step 4: Remove Microsoft.Identity.Web dependencies**

`<!-- Remove these from .csproj -->`

`<PackageReference ` `Include`  `=` `"Microsoft.Identity.Web"`  ` `  `Version`  `=` `"..."` ` />`

`<PackageReference ` `Include`  `=` `"Microsoft.Identity.Web.MicrosoftGraph"`  ` `  `Version`  `=` `"..."` ` />`

`<PackageReference ` `Include`  `=` `"Microsoft.Identity.Web.DownstreamApi"`  ` `  `Version`  `=` `"..."` ` />`

C#

1\. **Unit Tests**: Update tests to mock HTTP calls to the SDK

2\. **Integration Tests**: Test SDK communication in staging

3\. **Performance Tests**: Measure HTTP overhead impact

4\. **Security Tests**: Validate token handling and network policies

The Microsoft Entra SDK for AgentID introduces HTTP communication overhead:

**Performance**

**Factor**

**Impact**

**Mitigation Strategy**

**Latency**

~1-5ms per request for localhost

communication

Use HTTP/2 to reduce connection overhead

**Throughput**

Limited by HTTP connection pooling

Implement connection pooling to reuse

HTTP connections

**Memory**

Additional container memory

overhead

Ensure adequate SDK resource allocation

**Request**

**Efficiency**

Multiple round trips for complex

operations

Batch requests to combine multiple

operations when possible

**Token**

**Performance**

Repeated token acquisition overhead

Leverage SDK's token cache for optimal

performance

Using Microsoft.Identity.Web has minimal overhead since it runs within the same process as

your application, providing native method calls with microsecond latency and shared process

`// Remove from Program.cs or Startup.cs`

`services.AddMicrosoftIdentityWebApiAuthentication(Configuration)`

`    .EnableTokenAcquisitionToCallDownstreamApi()`

`    .AddDownstreamApi(` `"Graph"` `, Configuration.GetSection(` `"DownstreamApis:Graph"` `))`

`    .AddInMemoryTokenCaches();`

**Step 5: Test and Validate**

**Performance Considerations**

**SDK Overhead**

ﾉ

**Expand table**

**In-Process Performance**

memory without HTTP limitations. When performance is critical, in-process integration is the

optimal choice, but the Microsoft Entra SDK for AgentID's flexibility and language-agnostic

design may outweigh the performance trade-offs in many scenarios.

The following are some performance and cost comparisons for in-process usage and Microsoft

Entra SDK for AgentID (Out-of-Process) usage:

**Cost Factor**

**Microsoft.Identity.Web (In-Process)**

**Microsoft Entra SDK for AgentID (Out-**

**of-Process)**

**Compute**

Minimal additional CPU/memory in

application process

Additional container resources per pod

**Network**

No additional overhead

Minimal (localhost communication)

**Storage**

NuGet package size (~10MB)

Container image storage

**Management**

No additional overhead

Container orchestration overhead

For 10 replicas with 128Mi/100m SDK configuration:

**Resource**

**In-Process**

**Microsoft Entra SDK for AgentID**

**Memory**

~0MB additional

10 × 128Mi = 1.28GB

**CPU**

~0% additional

10 × 100m = 1 core

**Storage**

~10MB per deployment

Container image size per node

**Aspect**

**Microsoft.Identity.Web**

**Microsoft Entra SDK for AgentID**

**Updates**

NuGet package updates

Container image updates

**Cost Considerations**

ﾉ

**Expand table**

**Cost Example**

ﾉ

**Expand table**

**Support and Maintenance**

ﾉ

**Expand table**

**Aspect**

**Microsoft.Identity.Web**

**Microsoft Entra SDK for AgentID**

**Breaking Changes**

Via package versioning

Via container tags

**Bug Fixes**

Compile-time integration

Runtime container updates

**Security Patches**

Rebuild application

Redeploy container

**Documentation**

Extensive .NET docs

This documentation

**Community**

Large .NET community

Growing community

You can combine both approaches within the same architecture: use Microsoft.Identity.Web for

.NET services that require maximum performance, while leveraging the Microsoft Entra SDK for

AgentID for non-.NET services or when you need language-agnostic authentication patterns.

This hybrid strategy allows you to optimize performance where critical while maintaining

consistency and flexibility across your entire service ecosystem.

An example architecture would be as follows:

mermaid

Installation Guide \- Deploy the Microsoft Entra SDK for AgentID

Configuration Reference \- Configure the SDK

Scenarios \- Practical examples

**Hybrid Approach**

`graph TB`

`    subgraph cluster["Kubernetes Cluster"]`

`        subgraph netpod["<b>.NET API Pod</b>"]`

`            netapi["<b>.NET API</b><br/>(Microsoft.Identity.Web)"]`

`            style netapi fill:#0078d4,stroke:#005a9e,stroke-width:2px,color:#fff`

`        end`

`        subgraph nodepod["<b>Node.js API Pod</b>"]`

`            nodeapi["<b>Node.js API</b>"]`

`            sidecar["<b>Microsoft Entra SDK for AgentID</b>"]`

`            style nodeapi fill:#68a063,stroke:#4a7c45,stroke-width:2px,color:#fff`

`            style sidecar fill:#f2711c,stroke:#d85e10,stroke-width:2px,color:#fff`

`        end`

`    end`

`    style cluster fill:#f0f0f0,stroke:#333,stroke-width:3px`

`    style netpod fill:#e8f4f8,stroke:#0078d4,stroke-width:2px`

`    style nodepod fill:#e8f4e8,stroke:#68a063,stroke-width:2px`

**Next Steps**

Microsoft.Identity.Web Documentation

\- Learn about in-process library

**Last updated on 11/14/2025**

**Installation guide: Deploy the Microsoft**

**Entra SDK for AgentID**

The Microsoft Entra SDK for AgentID is a ready-to-deploy containerized authentication service

that streamlines secure token acquisition for your applications. This installation guide provides

step-by-step instructions for deploying the SDK container across Kubernetes, Docker, and

Azure environments, eliminating the need to embed sensitive credentials directly in your

application code.

Access to Microsoft Container Registry (MCR)

Container runtime (Docker, Kubernetes, or container service)

Register a new app in the Microsoft Entra admin center

, configured for _Accounts in this_

_organizational directory only_. Refer to Register an application for more details. Record the

following values from the application **Overview** page for later use:

Application (client) ID

Directory (tenant) ID

Credentials for the application:

Client Secret or Certificate stored securely (e.g., Azure Key Vault)

For Azure deployments: Azure CLI or access to Azure portal

The Microsoft Entra SDK for AgentID is distributed as a container image from the MCR.

`latest` \- Latest stable release

`<version>` \- Specific versions (e.g., `1.0.0` )

`<version>-preview` \- Preview releases

**Prerequisites**

**Container Image**

`mcr.microsoft.com/entra-sdk/auth-sidecar:<tag>`

**Version Tags**

７ **Note**

The Microsoft Entra SDK for AgentID is designed to run as a companion container alongside

your application. This allows your application to offload token acquisition and management to

the SDK via HTTP calls, and keeps sensitive credentials out of your application code. The

following are common deployment patterns and should be adapted to your specific

environment.

Deploy the Microsoft Entra SDK for AgentID in the same pod as your application container for

secure pod-local communication. This pattern ensures the authentication service runs

alongside your app, enabling fast HTTP-based token acquisition while keeping credentials

isolated from your application code:

YAML

The container image is currently in preview. Check the **GitHub releases**

for latest version

tags.

**Deployment patterns**

**Kubernetes pattern**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `Pod`

`metadata:`

`  ``# Your application container`

`  name:`  ` `  `myapp`

`spec:`

`  containers:`

`  - name:`  ` `  `app`

`    image:`  ` `  `myregistry/myapp:latest`

`    ports:`

`    - containerPort:` ` 8080`

`    env:`

`    - name:`  ` `  `SIDECAR_URL`

`      value:` ` ` `"http://localhost:5000"`

`  ``# Microsoft Entra SDK for AgentID container`

`  - name:`  ` `  `sidecar`

`    image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`    ports:`

`    - containerPort:` ` 5000`

`    env:`

`    - name:`  ` `  `AzureAd__TenantId`

`      value:` ` ` `"your-tenant-id"`

`    - name:`  ` `  `AzureAd__ClientId`

`      value:` ` ` `"your-client-id"`

`    - name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`      value:` ` ` `"KeyVault"`

`    - name:`  ` `  `AzureAd__ClientCredentials__0__KeyVaultUrl`

See Kubernetes on Azure tutorial - Prepare an application for Azure Kubernetes Service (AKS) if

you want to target Azure Kubernetes Services. This pattern uses a Deployment resource to

manage application and Microsoft Entra SDK for AgentID containers, allowing for scaling and

updates. The deployment also handles health checks and resource allocation, ensuring secure

operation in production environments:

YAML

`      value:` ` ` `"https://your-keyvault.vault.azure.net"`

`    - name:`  ` `  `AzureAd__ClientCredentials__0__KeyVaultCertificateName`

`      value:` ` ` `"your-cert-name"`

**Kubernetes Deployment**

`apiVersion:`  ` `  `apps/v1`

`kind:`  ` `  `Deployment`

`metadata:`

`  name:`  ` `  `myapp-deployment`

`spec:`

`  replicas:` ` 3`

`  selector:`

`    matchLabels:`

`      app:`  ` `  `myapp`

`  template:`

`    metadata:`

`      labels:`

`        app:`  ` `  `myapp`

`    spec:`

`      serviceAccountName:`  ` `  `myapp-sa`

`      containers:`

`      - name:`  ` `  `app`

`        image:`  ` `  `myregistry/myapp:latest`

`        ports:`

`        - containerPort:` ` 8080`

`        env:`

`        - name:`  ` `  `SIDECAR_URL`

`          value:` ` ` `"http://localhost:5000"`

`        resources:`

`          requests:`

`            memory:` ` ` `"256Mi"`

`            cpu:` ` ` `"250m"`

`          limits:`

`            memory:` ` ` `"512Mi"`

`            cpu:` ` ` `"500m"`

`      `

`      - name:`  ` `  `sidecar`

`        image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`        ports:`

`        - containerPort:` ` 5000`

`        env:`

`        - name:`  ` `  `AzureAd__TenantId`

When working in a Docker environment, you can use Docker Compose to define and run multi-

container applications. The following example demonstrates how to set up the Microsoft Entra

SDK for AgentID alongside your application container in a local development environment:

YAML

`          valueFrom:`

`            configMapKeyRef:`

`              name:`  ` `  `app-config`

`              key:`  ` `  `tenant-id`

`        - name:`  ` `  `AzureAd__ClientId`

`          valueFrom:`

`            configMapKeyRef:`

`              name:`  ` `  `app-config`

`              key:`  ` `  `client-id`

`        - name:`  ` `  `AzureAd__Instance`

`          value:` ` ` `"https://login.microsoftonline.com/"`

`        resources:`

`          requests:`

`            memory:` ` ` `"128Mi"`

`            cpu:` ` ` `"100m"`

`          limits:`

`            memory:` ` ` `"256Mi"`

`            cpu:` ` ` `"250m"`

`        livenessProbe:`

`          httpGet:`

`            path:` ` ` `/health`

`            port:` ` 5000`

`          initialDelaySeconds:` ` 10`

`          periodSeconds:` ` 10`

`        readinessProbe:`

`          httpGet:`

`            path:` ` ` `/health`

`            port:` ` 5000`

`          initialDelaySeconds:` ` 5`

`          periodSeconds:` ` 5`

**Docker Compose**

`version:` ` ` `'3.8'`

`services:`

`  app:`

`    image:`  ` `  `myregistry/myapp:latest`

`    ports:`

`      -` ` ` `"8080:8080"`

`    ` `en` ` ` `-`  ` `  `sidecar`  ` `  `environment:`

`      -`  ` `  `AzureAd__TenantId=${TENANT_ID}`

`      -`  ` `  `AzureAd__ClientId=${CLIENT_ID}`

`      -`  ` `  `AzureAd__ClientCredentials__0__SourceType=ClientSecret`

`      -`  ` `  `AzureAd__ClientCredentials__0__ClientSecret=${CLIENT_SECRET}`

`    networks:`

When deploying to AKS, you can use Azure Managed Identity to authenticate the Microsoft

Entra SDK for AgentID without storing credentials in configuration. First you'll need to enable

Azure AD Workload Identity on your AKS cluster and create a federated identity credential for

your managed identity. Then configure the SDK to use the managed identity for authentication.

Create a managed identity and assign it appropriate permissions

Bash

Grant the managed identity permissions to access downstream APIs:

Bash

`      -`  ` `  `app-network`

`networks:`

`  app-network:`

`    driver:`  ` `  `bridge`

**Azure Kubernetes Service (AKS) with Managed**

**Identity**

**Step 1: Create Managed Identity**

`# Create managed identity`

`az identity create \`

`  --resource-group myResourceGroup \`

`  --name myapp-identity`

`# Get the identity details`

`IDENTITY_CLIENT_ID=$(az identity show \`

`  --resource-group myResourceGroup \`

`  --name myapp-identity \`

`  --query clientId -o tsv)`

`IDENTITY_OBJECT_ID=$(az identity show \`

`  --resource-group myResourceGroup \`

`  --name myapp-identity \`

`  --query principalId -o tsv)`

**Step 2: Assign permissions**

`# Example: Grant permission to call Microsoft Graph`

`az ad app permission add \`

`  --id $IDENTITY_CLIENT_ID \`

Create a service account with workload identity federation:

Bash

In the following deployment example, the Microsoft Entra SDK for AgentID is configured to use

Azure AD Workload Identity for authentication using file-based token projection. The

`SignedAssertionFilePath` credential type reads the token from the file projected by the

workload identity webhook:

YAML

`  --api 00000003-0000-0000-c000-000000000000 \`

`  --api-permissions e1fe6dd8-ba31-4d61-89e7-88639da4683d=Scope`

**Step 3: Configure Workload Identity**

`export` ` AKS_OIDC_ISSUER=$(az aks show \`

`  --resource-group myResourceGroup \`

`  --name myAKSCluster \`

`  --query ``"oidcIssuerProfile.issuerUrl"` ` -o tsv)`

`az identity federated-credential create \`

`  --name myapp-federated-identity \`

`  --identity-name myapp-identity \`

`  --resource-group myResourceGroup \`

`  --issuer $AKS_OIDC_ISSUER \`

`  --subject system:serviceaccount:default:myapp-sa`

**Step 4: Deploy with Workload Identity**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `ServiceAccount`

`metadata:`

`  name:`  ` `  `myapp-sa`

`  namespace:`  ` `  `default`

`  annotations:`

`    ` `azure.workload.identity/client-id:` ` ` `"<MANAGED_IDENTITY_CLIENT_ID>"`

`---`

`apiVersion:`  ` `  `apps/v1`

`kind:`  ` `  `Deployment`

`metadata:`

`  name:`  ` `  `myapp-deployment`

`spec:`

`  template:`

`    metadata:`

`      labels:`

`        ` `azure.workload.identity/use:` ` ` `"true"`

`    spec:`

**Note**: The workload identity webhook automatically projects the federated token to

`/var/run/secrets/azure/tokens/azure-identity-token` or an environment variable when the

pod has the required label and service account annotation.

Correct network configuration is essential to ensure secure communication between the

Microsoft Entra SDK for AgentID and external services while restricting unauthorized access.

Proper configuration prevents security vulnerabilities and ensures reliable connectivity to

Microsoft Entra ID endpoints. Use the following guidelines to configure network access for the

SDK, depending on your deployment environment.

To configure the Microsoft Entra SDK for AgentID for internal pod-local communication only,

set the endpoint URL in your application to point to `localhost` or `127.0.0.1` , depending on

your environment:

YAML

`      serviceAccountName:`  ` `  `myapp-sa`

`      containers:`

`      - name:`  ` `  `app`

`        image:`  ` `  `myregistry/myapp:latest`

`        env:`

`        - name:`  ` `  `SIDECAR_URL`

`          value:` ` ` `"http://localhost:5000"`

`      `

`      - name:`  ` `  `sidecar`

`        image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`        ports:`

`        - containerPort:` ` 5000`

`        env:`

`        - name:`  ` `  `AzureAd__TenantId`

`          value:` ` ` `"your-tenant-id"`

`        - name:`  ` `  `AzureAd__ClientId`

`          value:` ` ` `"<MANAGED_IDENTITY_CLIENT_ID>"`

`        `

`        ``# Workload Identity credentials - uses file-based token projection`

`        - name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`          value:` ` ` `"SignedAssertionFilePath"`

**Network configuration**

**Internal communication only**

`containers:`

`- name:`  ` `  `sidecar`

`  env:`

`  - name:`  ` `  `Kestrel__Endpoints__Http__Url`

`    value:` ` ` `"http://127.0.0.1:5000"` ` ` `# Same pod, localhost communication`

To further restrict network access, consider implementing Kubernetes Network Policies to limit

traffic to and from the SDK container:

YAML

The Microsoft Entra SDK for AgentID exposes a `/health` endpoint for liveness and readiness

probes, ensuring the container is running safely. Configure your deployment to include these

probes:

Ｕ **Caution**

Never expose the Microsoft Entra SDK for AgentID externally via LoadBalancer or Ingress.

It should only be accessible from your application container.

**Network Policies**

`apiVersion:`  ` `  `networking.k8s.io/v1`

`kind:`  ` `  `NetworkPolicy`

`metadata:`

`  name:`  ` `  `sidecar-network-policy`

`spec:`

`  podSelector:`

`    matchLabels:`

`      app:`  ` `  `myapp`

`  policyTypes:`

`  -`  ` `  `Ingress`

`  -`  ` `  `Egress`

`  ingress:`

`  ``# No external ingress rules - only pod-local communication`

`  egress:`

`  - to:`

`    - namespaceSelector:`

`        matchLabels:`

`          name:`  ` `  `kube-system`

`    ports:`

`    - protocol:`  ` `  `TCP`

`      port:` ` 53  ``# DNS`

`  - to:`

`    - podSelector:` ` ` `{}`

`  - to:`

`    ``# Allow outbound to Microsoft Entra ID`

`    ports:`

`    - protocol:`  ` `  `TCP`

`      port:` ` 443`

**Health Checks**

YAML

The recommended resource allocations are as follows, but ensure to adjust based on token

acquisition frequency, number of configured downstream APIs and cache size requirements:

**Resource Profile**

**Memory**

**CPU**

**Minimum**

128Mi

100m

**Recommended**

256Mi

250m

**High Traffic**

512Mi

500m

The Microsoft Entra SDK for AgentID is designed to scale with your application:

1\. **Stateless Design**: Each SDK instance maintains its own token cache

2\. **Horizontal Scaling**: Scale by adding more application pods (each with its own SDK

instance)

3\. **Cache Warming**: Consider implementing cache warming strategies for high-traffic

scenarios

Common issues that you may encounter could be due to invalid configuration values, network

connectivity to Microsoft Entra ID, or missing credentials or certificates. Ensure the managed

`livenessProbe:`

`  httpGet:`

`    path:` ` ` `/health`

`    port:` ` 5000`

`  initialDelaySeconds:` ` 10`

`  periodSeconds:` ` 10`

`readinessProbe:`

`  httpGet:`

`    path:` ` ` `/health`

`    port:` ` 5000`

`  initialDelaySeconds:` ` 5`

`  periodSeconds:` ` 5`

**Resource Requirements**

ﾉ

**Expand table**

**Scaling Considerations**

**Troubleshooting Deployment**

identity or service principal has the correct application permissions, admin consent granted (if

required), and correct role assignments.

The following are some common troubleshooting steps that can help resolve deployment

issues:

Check container logs:

Bash

Verify the Microsoft Entra SDK for AgentID is responding:

Bash

For more detailed steps on troubleshooting, please refer to the Troubleshooting guide.

Configure settings \- Set up identity configuration

Review endpoints \- Explore the HTTP API

Security best practices \- Harden your deployment

Choose a scenario \- Start with a guided example

**Last updated on 11/14/2025**

**Container Won't Start**

`kubectl logs <pod-name> -c sidecar`

**Health Check Failures**

`kubectl ` `exec` ` <pod-name> -c sidecar -- curl http://localhost:5000/health`

**Next Steps**

**Configuration reference: Microsoft Entra**

**SDK for AgentID settings**

This guide provides configuration options for the Microsoft Entra SDK for AgentID, a

containerized authentication service that handles token acquisition and management for

applications in containerized environments. The SDK simplifies identity integration by

managing Microsoft Entra ID authentication, on-behalf-of (OBO) token flows, and downstream

API calls without requiring applications to embed authentication libraries directly.

While this guide focuses on Kubernetes deployment patterns, the SDK can be deployed in any

containerized environment including Docker, Azure Container Instances, and other container

orchestration platforms.

If you're deploying to Azure Kubernetes Service (AKS), setting up development environments,

or configuring production workloads, this reference covers configuration patterns, credential

types, and environment variables needed to secure your applications with Microsoft Entra ID.

The Microsoft Entra SDK for AgentID is configured using configuration sources following

ASP.NET Core conventions. Configuration values can be provided via multiple methods,

including:

Environment variables (recommended for Kubernetes)

Entra ID configuration - `appsettings.json` file attached to the container, or embedded in

the yaml file.

Command-line arguments

Azure App Configuration or Key Vault (for advanced scenarios)

Microsoft Entra SDK for AgentID deployments require core Entra ID settings to authenticate

incoming tokens and acquire tokens for downstream APIs. Use the appropriate client

credentials in the following YAML format, typically as environment variables, to ensure secure

authentication.

First, configure the core Entra ID settings for the SDK to authenticate incoming tokens and

acquire tokens for downstream APIs.

**Configuration overview**

**Core Entra ID settings**

**Required configuration**

YAML

**Key**

**Description**

**Required**

**Default**

`AzureAd__Instance`

Microsoft Entra authority URL

No

`https://login.microsoftonline.com/`

`AzureAd__TenantId`

Your Microsoft Entra tenant ID

Yes

-

`AzureAd__ClientId`

Application (client) ID

Yes

-

`AzureAd__Audience`

Expected audience in incoming

tokens

No

`api://{ClientId}`

`AzureAd__Scopes`

Required scopes for incoming

tokens (space-separated)

No

-

The Microsoft Entra SDK for AgentID supports multiple client credential types for

authenticating with Microsoft Entra ID when acquiring tokens for downstream APIs. Choose the

credential type that best fits your deployment environment and security requirements, and

ensure that the configuration you choose is appropriate for your scenario.

Each credential type serves different scenarios:

`env:`

`- name:`  ` `  `AzureAd__Instance`

`  value:` ` ` `"https://login.microsoftonline.com/"`

`- name:`  ` `  `AzureAd__TenantId`

`  value:` ` ` `"<your-tenant-id>"`

`- name:`  ` `  `AzureAd__ClientId`

`  value:` ` ` `"<your-client-id>"`

ﾉ

**Expand table**

７ **Note**

The expected audience value depends on your app registration's

**requestedAccessTokenVersion**:

**Version 2**: Use the `{ClientId}` value directly

**Version 1** or **null**: Use the App ID URI (typically `api://{ClientId}` unless you

customized it)

**Client credentials configuration**

**Client Secret**: Simple setup for development and testing (not recommended for

production)

**Key Vault Certificate**: Production environments with centralized certificate management

**File Certificate**: When certificates are mounted as files (e.g., via Kubernetes secrets)

**Certificate Store**: Windows environments with certificate stores

**Workload Identity for Containers**: Recommended for AKS, using Azure AD Workload

Identity with file-based token projection

**Managed Identity for VMs/App Services**: Azure Virtual Machines and App Services with

system or user-assigned managed identities (not for containers)

Configure one or more credential sources in the following YAML format:

This configuration sets up Entra ID authentication using a client secret for service-to-service

authentication.

YAML

This configuration sets up Entra ID authentication using a certificate stored in Azure Key Vault.

YAML

This configuration sets up Entra ID authentication using a certificate stored as a file.

YAML

**Client Secret**

`- name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`  value:` ` ` `"ClientSecret"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__ClientSecret`

`  value:` ` ` `"<your-client-secret>"`

**Certificate from Key Vault**

`- name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`  value:` ` ` `"KeyVault"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__KeyVaultUrl`

`  value:` ` ` `"https://<your-keyvault>.vault.azure.net"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__KeyVaultCertificateName`

`  value:` ` ` `"<certificate-name>"`

**Certificate from file**

This configuration sets up Entra ID authentication using a certificate from the local certificate

store.

YAML

This configuration sets up Entra ID authentication using Azure AD Workload Identity for

containerized deployments (AKS). This is the recommended approach for container-based

scenarios as it uses file-based token projection.

YAML

**Note**: The token file path `/var/run/secrets/azure/tokens/azure-identity-token` or an

environment variable is automatically projected by the Azure Workload Identity webhook when

your pod is properly configured with the service account annotation and pod label. See Using

Managed Identity for complete setup instructions.

For classic Azure Managed Identity scenarios on Virtual Machines or App Services (not

containers), use `SignedAssertionFromManagedIdentity` :

YAML

`- name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`  value:` ` ` `"Path"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__CertificateDiskPath`

`  value:` ` ` `"/path/to/certificate.pfx"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__CertificatePassword`

`  value:` ` ` `"<certificate-password>"`

**Certificate from store**

`- name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`  value:` ` ` `"StoreWithThumbprint"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__CertificateStorePath`

`  value:` ` ` `"CurrentUser/My"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__CertificateThumbprint`

`  value:` ` ` `"<thumbprint>"`

**Workload Identity for containers (recommended for AKS)**

`- name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`  value:` ` ` `"SignedAssertionFilePath"`

**Managed Identity for VMs and App Services**

**Important**: Do not use `SignedAssertionFromManagedIdentity` for containerized environments

(Kubernetes, AKS, Docker). For AKS, use `SignedAssertionFilePath` as shown above. For

Kubernetes and Docker, use client certificates. For details see https://aka.ms/idweb/client-

credentials

For complete details on all credential configuration options and their usage, see the

CredentialDescription specification

in the microsoft-identity-abstractions-for-dotnet

repository.

Configure multiple credentials with priority-based selection:

YAML

The Microsoft Entra SDK for AgentID evaluates credentials in numerical order (0, 1, 2, etc.) and

uses the first credential that successfully authenticates.

`- name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`  value:` ` ` `"SignedAssertionFromManagedIdentity"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__ManagedIdentityClientId`

`  value:` ` ` `"<managed-identity-client-id>"`

**Additional Resources**

**Credentials priority**

`# First priority - Key Vault certificate`

`- name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`  value:` ` ` `"KeyVault"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__KeyVaultUrl`

`  value:` ` ` `"https://prod-keyvault.vault.azure.net"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__KeyVaultCertificateName`

`  value:` ` ` `"prod-cert"`

`# Second priority - Client secret (fallback)`

`- name:`  ` `  `AzureAd__ClientCredentials__1__SourceType`

`  value:` ` ` `"ClientSecret"`

`- name:`  ` `  `AzureAd__ClientCredentials__1__ClientSecret`

`  valueFrom:`

`    secretKeyRef:`

`      name:`  ` `  `app-secrets`

`      key:`  ` `  `client-secret`

**Downstream APIs configuration**

Configure downstream APIs that your application needs to call using on-behalf-of (OBO) token

flows. The Microsoft Entra SDK for AgentID manages token acquisition and provides

authentication headers for these API calls. Each downstream API requires a unique

configuration name and specific parameters for token acquisition and HTTP request handling.

Define each downstream API with its base URL, required scopes, and optional parameters. The

SDK will automatically handle token acquisition using the incoming user token and provide the

appropriate authorization headers for your application's API calls.

YAML

**Key Pattern**

**Description**

**Required**

`DownstreamApis__<Name>__BaseUrl`

Base URL of the API

Yes

`DownstreamApis__<Name>__Scopes`

Space-separated scopes to request

Yes

`DownstreamApis__<Name>__HttpMethod`

Default HTTP method

No (GET)

`DownstreamApis__<Name>__RelativePath`

Default relative path

No

`DownstreamApis__<Name>__RequestAppToken`

Use app token instead of OBO

No (false)

Fine-tune token acquisition behavior:

YAML

`- name:`  ` `  `DownstreamApis__Graph__BaseUrl`

`  value:` ` ` `"https://graph.microsoft.com/v1.0"`

`- name:`  ` `  `DownstreamApis__Graph__Scopes`

`  value:` ` ` `"User.Read Mail.Read"`

`- name:`  ` `  `DownstreamApis__Graph__RelativePath`

`  value:` ` ` `"/me"`

`- name:`  ` `  `DownstreamApis__MyApi__BaseUrl`

`  value:` ` ` `"https://api.contoso.com"`

`- name:`  ` `  `DownstreamApis__MyApi__Scopes`

`  value:` ` ` `"api://myapi/.default"`

ﾉ

**Expand table**

**Token acquisition options**

`- name:`  ` `  `DownstreamApis__Graph__AcquireTokenOptions__Tenant`

`  value:` ` ` `"<specific-tenant-id>"`

`- name:`  ` `  `DownstreamApis__Graph__AcquireTokenOptions__AuthenticationScheme`

`  value:` ` ` `"Bearer"`

Enable Signed HTTP Requests for enhanced security:

YAML

Configure logging levels:

YAML

YAML

All token acquisition endpoints accept query parameters to override configuration:

Bash

`- name:`  ` `  `DownstreamApis__Graph__AcquireTokenOptions__CorrelationId`

`  value:` ` ` `"<correlation-id>"`

**Signed HTTP Request (SHR) configuration**

`- name:`  ` `  `DownstreamApis__SecureApi__AcquireTokenOptions__PopPublicKey`

`  value:` ` ` `"<base64-encoded-public-key>"`

`- name:`  ` `  `DownstreamApis__SecureApi__AcquireTokenOptions__PopClaims`

`  value:` ` ` `'{"custom_claim": "value"}'`

**Logging configuration**

`- name:`  ` `  `Logging__LogLevel__Default`

`  value:` ` ` `"Information"`

`- name:`  ` `  `Logging__LogLevel__Microsoft.Identity.Web`

`  value:` ` ` `"Debug"`

`- name:`  ` `  `Logging__LogLevel__Microsoft.AspNetCore`

`  value:` ` ` `"Warning"`

**ASP.NET Core settings**

`- name:`  ` `  `ASPNETCORE_ENVIRONMENT`

`  value:` ` ` `"Production"`

`- name:`  ` `  `ASPNETCORE_URLS`

`  value:` ` ` `"http://+:5000"`

**Per-Request configuration overrides**

Specify agent identity at request time:

Bash

**Important Rules:**

`AgentUsername` and `AgentUserId` require `AgentIdentity`

`AgentUsername` and `AgentUserId` are mutually exclusive

See Agent Identities for detailed semantics.

The following provides a production-ready example showing how to deploy the SDK with

proper separation of configuration and secrets. This example demonstrates configuring

`# Override scopes`

`GET /AuthorizationHeader/Graph?`

`optionsOverride.Scopes=User.Read&optionsOverride.Scopes=Mail.Read`

`# Request app token instead of OBO`

`GET /AuthorizationHeader/Graph?optionsOverride.RequestAppToken=`  `true`

`GET /AuthorizationHeaderUnauthenticated/Graph?optionsOverride.RequestAppToken=`  `true`

`# Override tenant`

`GET /AuthorizationHeader/Graph?optionsOverride.AcquireTokenOptions.Tenant=<tenant-`

`id>`

`# Override relative path`

`GET /DownstreamApi/Graph?optionsOverride.RelativePath=me/messages`

`# Enable SHR for this request`

`GET /AuthorizationHeader/Graph?optionsOverride.AcquireTokenOptions.PopPublicKey=`

`<base64-key>`

**Agent Identity Overrides**

`# Autonomous agent`

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-client-id>`

`# Autonomous agent with specific agent user identity (by username)`

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-client-`

`id>&AgentUsername=user@contoso.com`

`# Autonomous agent with specific agent user identity (by object ID)`

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-client-id>&AgentUserId=<user-`

`object-id>`

**Complete configuration example**

multiple downstream APIs, using Kubernetes ConfigMaps for non-sensitive settings, storing

credentials securely in Secrets, and applying environment-specific configurations for secure

deployment.

This pattern follows Kubernetes best practices by separating configuration data from sensitive

credentials, enabling effective management of different environments while maintaining

security.

The ConfigMap stores non-sensitive configuration settings for the SDK, including Entra ID

settings, downstream APIs, and logging levels.

YAML

The Secret stores sensitive credentials, such as client secrets, separately from the ConfigMap.

YAML

**Kubernetes ConfigMap**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `ConfigMap`

`metadata:`

`  name:`  ` `  `sidecar-config`

`data:`

`  ASPNETCORE_ENVIRONMENT:` ` ` `"Production"`

`  ASPNETCORE_URLS:` ` ` `"http://+:5000"`

`  `

`  AzureAd__Instance:` ` ` `"https://login.microsoftonline.com/"`

`  AzureAd__TenantId:` ` ` `"common"`

`  AzureAd__ClientId:` ` ` `"your-app-client-id"`

`  AzureAd__Scopes:` ` ` `"access_as_user"`

`  `

`  DownstreamApis__Graph__BaseUrl:` ` ` `"https://graph.microsoft.com/v1.0"`

`  DownstreamApis__Graph__Scopes:` ` ` `"User.Read Mail.Read"`

`  `

`  DownstreamApis__MyApi__BaseUrl:` ` ` `"https://api.contoso.com"`

`  DownstreamApis__MyApi__Scopes:` ` ` `"api://myapi/.default"`

`  `

`  Logging__LogLevel__Default:` ` ` `"Information"`

`  ` `Logging__LogLevel__Microsoft.Identity.Web:` ` ` `"Debug"`

**Kubernetes secret**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `Secret`

`metadata:`

`  name:`  ` `  `sidecar-secrets`

`type:`  ` `  `Opaque`

The Deployment mounts both the ConfigMap and Secret into the SDK container, ensuring that

configuration and credentials are properly separated.

YAML

Configure environment-specific settings to tailor security, logging, and tenant isolation for your

deployment environments. Each environment requires different configuration approaches to

balance development efficiency, staging validation, and production security requirements.

YAML

`stringData:`

`  AzureAd__ClientCredentials__0__ClientSecret:` ` ` `"your-client-secret"`

**Deployment with ConfigMap and secret**

`apiVersion:`  ` `  `apps/v1`

`kind:`  ` `  `Deployment`

`metadata:`

`  name:`  ` `  `myapp`

`spec:`

`  template:`

`    spec:`

`      containers:`

`      - name:`  ` `  `sidecar`

`        image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`        envFrom:`

`        - configMapRef:`

`            name:`  ` `  `sidecar-config`

`        - secretRef:`

`            name:`  ` `  `sidecar-secrets`

**Environment-specific configuration**

**Development**

`- name:`  ` `  `ASPNETCORE_ENVIRONMENT`

`  value:` ` ` `"Development"`

`- name:`  ` `  `Logging__LogLevel__Default`

`  value:` ` ` `"Debug"`

`- name:`  ` `  `AzureAd__TenantId`

`  value:` ` ` `"<dev-tenant-id>"`

**Staging**

YAML

YAML

The Microsoft Entra SDK for AgentID validates configuration at startup and logs errors for:

Missing required settings ( ` TenantId` , `ClientId` )

Invalid credential configurations

Malformed downstream API definitions

Invalid URLs or scope formats

Check container logs for validation messages:

Bash

1\. **Use Secrets for Credentials**: Store client secrets and certificates in Kubernetes Secrets or

Azure Key Vault. See also https://aka.ms/msidweb/client-credentials

2\. **Separate Configuration per Environment**: Use ConfigMaps to manage environment-

specific settings

`- name:`  ` `  `ASPNETCORE_ENVIRONMENT`

`  value:` ` ` `"Staging"`

`- name:`  ` `  `Logging__LogLevel__Default`

`  value:` ` ` `"Information"`

`- name:`  ` `  `AzureAd__TenantId`

`  value:` ` ` `"<staging-tenant-id>"`

**Production**

`- name:`  ` `  `ASPNETCORE_ENVIRONMENT`

`  value:` ` ` `"Production"`

`- name:`  ` `  `Logging__LogLevel__Default`

`  value:` ` ` `"Warning"`

`- name:`  ` `  `Logging__LogLevel__Microsoft.Identity.Web`

`  value:` ` ` `"Information"`

`- name:`  ` `  `AzureAd__TenantId`

`  value:` ` ` `"<prod-tenant-id>"`

`- name:`  ` `  `ApplicationInsights__ConnectionString`

`  value:` ` ` `"<app-insights-connection>"`

**Validation**

`kubectl logs <pod-name> -c sidecar`

**Best practices**

3\. **Enable Appropriate Logging**: Use Debug logging in development, Information/Warning

in production

4\. **Configure Health Checks**: Ensure health check endpoints are properly configured

5\. **Use Workload Identity for Containers**: For containerized deployments (AKS), prefer Azure

AD Workload Identity with `SignedAssertionFilePath` over client secrets for enhanced

security

6\. **Use Managed Identity for VMs/App Services**: For Azure VMs and App Services, use

system or user-assigned managed identities

7\. **Validate at Deploy Time**: Test configuration in staging before production deployment

Agent Identities

Endpoints Reference

Security Best Practices

Troubleshooting

**Last updated on 11/14/2025**

**See Also**

**Agent Identities: Autonomous and**

**Interactive Agent Patterns**

Agent identities enable sophisticated authentication scenarios where an agent application acts

autonomously or on behalf of users. Using agent identities with the Microsoft Entra SDK for

AgentID allows for both autonomous agents operating in their own context and interactive

agents acting on behalf of users. To facilitate these scenarios, the SDK supports specific query

parameters to specify agent identities and user contexts.

For comprehensive agent identity platform documentation, see Agentic identity platform

documentation.

Agent identities support two primary patterns:

**Autonomous Agent**: The agent operates in its own application context

**Interactive Agent**: An interactive agent operates on behalf of a user

The SDK accepts three optional query parameters:

`AgentIdentity` \- GUID of the agent identity

`AgentUsername` \- User principal name (UPN) for specific user

`AgentUserId` \- User object ID (OID) for specific user, as an alternative to UPN

If both `AgentUsername` and `AgentUserId` are present, though validation will prevent this, the

implementation gives precedence to username:

_AgentUsername > AgentUserId_

However, providing both `AgentUsername` and `AgentUserId` should be **avoided** and will result in

a validation error in strict validation mode.

Before configuring agent identities in your application, you must set up the necessary

components in Microsoft Entra ID. To register a new application in Microsoft Entra ID tenant,

refer to Register an application for more details.

**Overview**

**Precedence Rules**

**Microsoft Entra ID Configuration**

1\. **Agent Application Registration**:

Register the parent agent application in Microsoft Entra ID

Configure API permissions for downstream APIs

Set up client credentials (FIC+MSI or certificate or secret)

2\. **Agent Identity Configuration**:

Create agent identities using the agent blueprint

Assign necessary permissions to agent identities

3\. **Application Permissions**:

Grant application permissions for autonomous scenarios

Grant delegated permissions for user delegation scenarios

Ensure admin consent is provided where required

For detailed step-by-step instructions on configuring agent identities in Microsoft Entra ID, see

the Agentic identity platform documentation

Ensuring correct usage of agent identity parameters is crucial for successful authentication. The

following rules govern the use of `AgentIdentity` , `AgentUsername` , and `AgentUserId` parameters

and should be followed to avoid validation errors that are returned by the SDK.

`AgentUsername` or `AgentUserId` must be paired with `AgentIdentity` .

If you specify `AgentUsername` or `AgentUserId` without `AgentIdentity` , the request will fail with a

validation error.

Bash

**Prerequisites for Agent Identities**

**Semantic Rules**

**Rule 1: AgentIdentity Requirement**

`# INVALID - AgentUsername without AgentIdentity`

`GET /AuthorizationHeader/Graph?AgentUsername=user@contoso.com`

`# VALID - AgentUsername with AgentIdentity`

`GET /AuthorizationHeader/Graph?AgentIdentity=agent-client-`

`id&AgentUsername=user@contoso.com`

`AgentUsername` and `AgentUserId` are mutually exclusive parameters.

You cannot specify both `AgentUsername` and `AgentUserId` in the same request. If both are

provided, the request will fail with a validation error.

Bash

The combination of parameters determines the authentication pattern:

**Parameters**

**Pattern**

**Description**

`AgentIdentity` only

**Autonomous**

**Agent**

Acquires application token for the agent identity

`AgentIdentity` +

`AgentUsername`

**Interactive Agent**

Acquires user token for the specified user (by UPN)

`AgentIdentity` \+ `AgentUserId`

**Interactive Agent**

Acquires user token for the specified user (by

Object ID)

**Examples**:

Bash

**Rule 2: Mutual Exclusivity**

`# INVALID - Both AgentUsername and AgentUserId specified`

`GET /AuthorizationHeader/Graph?AgentIdentity=agent-`

`id&AgentUsername=user@contoso.com&AgentUserId=user-oid`

`# VALID - Only AgentUsername`

`GET /AuthorizationHeader/Graph?AgentIdentity=agent-id&AgentUsername=user@contoso.com`

`# VALID - Only AgentUserId`

`GET /AuthorizationHeader/Graph?AgentIdentity=agent-id&AgentUserId=user-object-id`

**Rule 3: Autonomous vs Interactive**

ﾉ

**Expand table**

`# Autonomous agent - application context`

`GET /AuthorizationHeader/Graph?AgentIdentity=agent-id`

`# Interactive agent - user context by username`

`GET /AuthorizationHeader/Graph?AgentIdentity=agent-id&AgentUsername=user@contoso.com`

`# Interactive agent - user context by user ID`

`GET /AuthorizationHeader/Graph?AgentIdentity=agent-id&AgentUserId=user-object-id`

For each usage pattern, the combination of parameters determines the authentication flow and

the type of token acquired.

The agent application operates independently in its own application context, acquiring

application tokens.

**Scenario**: A batch processing service that processes files autonomously.

Bash

**Token Characteristics**:

Token type: Application token

Subject ( ` sub` ): Agent application's object ID

Token issued for the agent's identity

**Permissions**: Application permissions assigned to agent identity

**Use Cases**:

Automated batch processing

Background tasks

System-to-system operations

Scheduled jobs without user context

The agent operates on behalf of a specific user identified by their UPN.

**Scenario**: An AI assistant acting on behalf of a user in a chat application.

Bash

**Token Characteristics**:

Token type: User token

**Usage Patterns**

**Pattern 1: Autonomous Agent**

`GET /AuthorizationHeader/Graph?AgentIdentity=12345678-1234-1234-1234-123456789012`

**Pattern 2: Autonomous User Agent (by Username)**

`GET /AuthorizationHeader/Graph?AgentIdentity=12345678-1234-1234-1234-`

`123456789012&AgentUsername=alice@contoso.com`

Subject ( ` sub` ): User's Object ID

Agent identity facet included in token claims

**Permissions**: Interactive permissions scoped to user

**Use Cases**:

Interactive agent applications

AI assistants with user delegation

User-scoped automation

Personalized workflows

The agent operates on behalf of a specific user identified by their Object ID.

**Scenario**: A workflow engine processing user-specific tasks using stored user IDs.

Bash

**Token Characteristics**:

Token type: User token

Subject ( ` sub` ): User's Object ID

Agent identity facet included in token claims

**Permissions**: Interactive permissions scoped to user

**Use Cases**:

Long-running workflows with stored user identifiers

Batch operations on behalf of multiple users

Systems using Object IDs for user reference

An agent web API receives a user token, validates it, and makes delegated calls on behalf of

that user.

**Scenario**: A web API acting as an interactive agent validating incoming user tokens and making

delegated calls to downstream services.

**Pattern 3: Autonomous User Agent (by Object ID)**

`GET /AuthorizationHeader/Graph?AgentIdentity=12345678-1234-1234-1234-`

`123456789012&AgentUserId=87654321-4321-4321-4321-210987654321`

**Pattern 4: Interactive Agent (acting on behalf of the user**

**calling it)**

**Flow**:

1\. Agent web API receives user token from the calling application

2\. Validates token via the `/Validate` endpoint

3\. Acquires tokens for downstream APIs by calling `/AuthorizationHeader` with only the

`AgentIdentity` and the incoming Authorization header

Bash

**Token Characteristics**:

Token type: User token (OBO flow)

Subject ( ` sub` ): Original user's Object ID

Agent acts as intermediary for user

**Permissions**: Interactive permissions scoped to the user

**Use Cases**:

Web APIs that act as agents

Interactive agent services

Agent-based middleware that delegates to downstream APIs

Services that validate and forward user context

When no agent parameters are provided, the SDK uses the incoming token's identity.

**Scenario**: Standard on-behalf-of (OBO) flow without agent identities.

Bash

**Token Characteristics**:

Token type: Depends on incoming token and configuration

Uses standard OBO or client credentials flow

`# Step 1: Validate incoming user token`

`GET /Validate`

`Authorization: Bearer <user-token>`

`# Step 2: Get authorization header on behalf of the user`

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-client-id>`

`Authorization: Bearer <user-token>`

**Pattern 5: Regular Request (No Agent)**

`GET /AuthorizationHeader/Graph`

`Authorization: Bearer <user-token>`

No agent identity facets

The following code snippets demonstrate how to implement the different agent identity

patterns using various programming languages, and how to interact with the SDK endpoints.

The code demonstrates how to handle out of process calls to the SDK to acquire authorization

headers for downstream API calls.

TypeScript

Python

**Code Examples**

**TypeScript: Autonomous Agent**

`const` ` sidecarUrl = ``"http://localhost:5000"` `;`

`const` ` agentId = ``"12345678-1234-1234-1234-123456789012"` `;`

`async`  ` `  `function`  ` `  `runBatchJob` `() {`

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${sidecarUrl}` `/AuthorizationHeader/Graph?AgentIdentity=`  `${agentId}`  `` ` `` `,`

`    {`

`      headers: {`

`        ``'Authorization'` `: ``'Bearer system-token'`

`      }`

`    }`

`  );`

`  `

`  ` `const` ` { authorizationHeader } = ` `await` ` response.json();`

`  ``// Use authorizationHeader for downstream API calls`

`}`

**Python: Agent with User Identity**

`import` ` requests`

`sidecar_url = ``"http://localhost:5000"`

`agent_id = ``"12345678-1234-1234-1234-123456789012"`

`user_email = ``"alice@contoso.com"`

`response = requests.get(`

`    ` `f"` `{sidecar_url}` `/AuthorizationHeader/Graph"` `,`

`    params={`

`        ``"AgentIdentity"` `: agent_id,`

`        ``"AgentUsername"` `: user_email`

`    },`

`    headers={` `"Authorization"` `: ` `f"Bearer ``{system_token}` `"` `}`

`)`

TypeScript

C#

`token = response.json()[` `"authorizationHeader"` `]`

**TypeScript: Interactive Agent**

`async`  ` `  `function`  ` `  `delegateCall` `(userToken: ` `string` `) {`

`  ``// Validate incoming token`

`  ` `const` ` validation = ` `await` ` fetch(`

`    ` `` ` ``  `${sidecarUrl}` ``/Validate` `` `,`

`    {`

`      headers: { ``'Authorization'` `: ` `` `Bearer `` `${userToken}`  `` ` `` ` }`

`    }`

`  );`

`  `

`  ` `const` ` claims = ` `await` ` validation.json();`

`  `

`  ``// Call downstream API on behalf of user`

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${sidecarUrl}` ``/DownstreamApi/Graph` `` `,`

`    {`

`      headers: { ``'Authorization'` `: ` `` `Bearer `` `${userToken}`  `` ` `` ` }`

`    }`

`  );`

`  `

`  ` `return`  ` `  `await` ` response.json();`

`}`

**C# with HttpClient**

`using` ` System.Net.Http;`

`var` ` httpClient = ` `new` ` HttpClient();`

`// Autonomous agent`

`var` ` autonomousUrl = ` `$"http://localhost:5000/AuthorizationHeader/Graph"` ` +`

`    ` `$"?AgentIdentity=` `{agentClientId}` `"` `;`

`var` ` response = ` `await` ` httpClient.GetAsync(autonomousUrl);`

`// Delegated agent with username`

`var` ` delegatedUrl = ` `$"http://localhost:5000/AuthorizationHeader/Graph"` ` +`

`    ` `$"?AgentIdentity=` `{agentClientId}` `"` ` +`

`    ` `$"&AgentUsername=` `{Uri.EscapeDataString(userPrincipalName)}` `"` `;`

`response = ` `await` ` httpClient.GetAsync(delegatedUrl);`

`// Delegated agent with user ID`

`var` ` delegatedByIdUrl = ` `$"http://localhost:5000/AuthorizationHeader/Graph"` ` +`

When agent identity parameters are misconfigured or used incorrectly, the SDK returns

validation errors. Below are common error scenarios and their corresponding responses. For

more details on error handling, see the Troubleshooting Guide.

**Request**:

Bash

**Response**:

JSON

**Request**:

Bash

**Response**:

JSON

`    ` `$"?AgentIdentity=` `{agentClientId}` `"` ` +`

`    ` `$"&AgentUserId=` `{userObjectId}` `"` `;`

`response = ` `await` ` httpClient.GetAsync(delegatedByIdUrl);`

**Error Scenarios**

**Missing AgentIdentity with AgentUsername**

`GET /AuthorizationHeader/Graph?AgentUsername=user@contoso.com`

`{`

`  ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.1"` `,`

`  ``"title"` `: ``"Bad Request"` `,`

`  ``"status"` `: 400,`

`  ``"detail"` `: ``"AgentUsername requires AgentIdentity to be specified"`

`}`

**Both AgentUsername and AgentUserId Specified**

`GET /AuthorizationHeader/Graph?AgentIdentity=agent-`

`id&AgentUsername=user@contoso.com&AgentUserId=user-oid`

`{`

`  ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.1"` `,`

`  ``"title"` `: ``"Bad Request"` `,`

**Request**:

Bash

**Response**:

JSON

1\. **Validate Input**: Always validate agent identity parameters before making requests

2\. **Use Object IDs When Available**: Object IDs are more stable

3\. **Implement Proper Error Handling**: Handle agent identity validation errors gracefully

4\. **Secure Agent Credentials**: Protect agent identity client IDs and credentials

5\. **Audit Agent Operations**: Log and monitor agent identity usage for security and

compliance

6\. **Test Both Patterns**: Validate both autonomous and delegated scenarios in your tests

7\. **Document Intent**: Clearly document which agent pattern is appropriate for each use case

Endpoints Reference

Configuration Reference

Scenario: Agent Autonomous Batch Processing

Agentic Identity Platform

`  ``"status"` `: 400,`

`  ``"detail"` `: ``"AgentUsername and AgentUserId are mutually exclusive"`

`}`

**Invalid AgentUserId Format**

`GET /AuthorizationHeader/Graph?AgentIdentity=agent-id&AgentUserId=invalid-guid`

`{`

`  ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.1"` `,`

`  ``"title"` `: ``"Bad Request"` `,`

`  ``"status"` `: 400,`

`  ``"detail"` `: ``"AgentUserId must be a valid GUID"`

`}`

**Best Practices**

**See Also**

**Last updated on 11/14/2025**

**Sign in users and call downstream APIs**

**with the Microsoft Entra SDK for AgentID**

**in Python**

In this quickstart, you use a sample web app to learn how to sign in users or agents and call

downstream APIs by using its own identity. The sample app uses the Microsoft Entra SDK for

AgentID to validate user tokens for delegated access and uses application identity for service-

to-service communication with downstream APIs like Microsoft Graph.

Install the UV package manager

. UV is a fast Python package installer and resolver

written in Rust.

Install Docker Desktop

.

An Azure account with an active subscription. If you don't already have one, Create an

account for free

.

This Azure account must have permissions to manage applications. Any of the following

Microsoft Entra roles include the required permissions:

Application Administrator

Application Developer

A workforce tenant. You can use your Default Directory or set up a new tenant.

To complete the rest of the quickstart, you need to first register an application in Microsoft

Entra ID.

Follow these steps to create the app registration:

1\. Sign in to the Microsoft Entra admin center

as at least an Application Developer.

2\. If you have access to multiple tenants, use the **Settings** icon

![](./assets/output_51_1.png)

in the top menu to switch

to the tenant in which you want to register the application.

**Prerequisites**

**Create and configure your Microsoft Entra**

**application**

**Create application registration**

3\. Browse to **Entra ID** \> **App registrations** and select **New registration**.

4\. Enter a meaningful **Name** for your app, such as _identity-client-app_. App users see this

name, and you can change it at any time. You can have multiple app registrations with the

same name.

5\. Under **Supported account types**, specify who can use the application. Select **Accounts in**

**this organizational directory only** for most applications. Refer to the table for more

information on each option.

**Supported account types**

**Description**

**Accounts in this**

**organizational directory only**

For _single-tenant_ apps for use only by users (or guests) in _your_

tenant.

**Accounts in any**

**organizational directory**

For _multitenant_ apps and you want users in _any_ Microsoft Entra

tenant to be able to use your application. Ideal for software-as-a-

service (SaaS) applications that you intend to provide to multiple

organizations.

**Accounts in any**

**organizational directory and**

**personal Microsoft accounts**

For _multitenant_ apps that support both organizational and

personal Microsoft accounts (for example, Skype, Xbox, Live,

Hotmail).

**Personal Microsoft accounts**

For apps used only by personal Microsoft accounts (for example,

Skype, Xbox, Live, Hotmail).

6\. Select **Register** to complete the app registration.

ﾉ

**Expand table**

![](./assets/output_53_1.png)

7\. The application's **Overview** page is displayed. Record the following values from the

application Overview page for later use:

Application (client) ID

Directory (tenant) ID

![](./assets/output_53_2.png)

The Python sample app uses interactive authentication with a browser-based sign-in flow.

Configure a redirect URI to handle the authentication response:

1\. In your app registration, under **Manage**, select **Authentication**.

2\. Select **Add a platform**.

3\. Select **Mobile and desktop applications**.

4\. Under **Custom redirect URIs**, enter `http://localhost` .

5\. Select **Configure**.

The Microsoft Entra SDK for AgentID uses client credentials to authenticate and get tokens for

downstream APIs. For local development and testing, use a self-signed certificate for

authentication.

Run PowerShell as an administrator and use the following commands to generate a self-signed

certificate:

PowerShell

**Add a redirect URI**

**Add client credentials**

**Generate a self-signed certificate**

`# Generate a self-signed certificate`

`$cert = ` `New-SelfSignedCertificate` `` ` ``

`   `` -Subject` ` ` `"CN=AgentID-Client-Certificate"` `` ` ``

`   `` -CertStoreLocation` ` ` `"Cert:\CurrentUser\My"` `` ` ``

`   `` -KeyExportPolicy` `` Exportable ` ``

`   `` -KeySpec` `` Signature ` ``

`   `` -KeyLength` `` 2048 ` ``

`   `` -KeyAlgorithm` `` RSA ` ``

`   `` -HashAlgorithm` `` SHA256 ` ``

`   `` -NotAfter` ` (`  `Get-Date` `).AddDays(7)`

`# Export public key (CER) for upload to Azure`

`$cerPath = ``"agentid-client-certificate.cer"`

`Export-Certificate` ` -Cert` ` $cert` ` -FilePath` ` $cerPath`

`# Export private key (PFX) for the Agent ID SDK container`

`$pfxPath = ``"agentid-client-certificate.pfx"`

`$certPassword = ` `ConvertTo-SecureString` ` -String` ` ` `"YourSecurePassword123!"` ` -Force -`

`AsPlainText`

`Export-PfxCertificate` ` -Cert` ` $cert` ` -FilePath` ` $pfxPath` ` -Password` ` $certPassword`

`Write-Host` ` ` `"Certificate generated successfully!"`

Record the certificate thumbprint displayed in the PowerShell output. You need it to verify the

certificate in the Microsoft Entra admin center matches the one installed locally.

Follow these steps to upload the `.cer` file created in your current directory to the Microsoft

Entra admin center:

1\. Open your app registration in the Microsoft Entra admin center

2\. Under **Manage**, select **Certificates & secrets**.

3\. In the **Certificates** tab, select **Upload certificate**.

4\. Select the `.cer` file you generated (for example, `agentid-client-cert.cer` ).

5\. Provide a description (for example, "AgentID Local Development Certificate").

6\. Select **Add**.

7\. Record the certificate **Thumbprint** displayed (it should match the one from your

certificate generation).

Follow these steps to configure delegated permissions to Microsoft Graph. With these

permissions, your client application can perform operations on behalf of the signed-in user,

such as reading their email.

1\. In your app registration, under **Manage**, select **API permissions** \> **Add a permission** >

**Microsoft Graph**.

2\. Select **Delegated permissions**. Microsoft Graph exposes many permissions, with the most

commonly used shown at the top of the list.

3\. Under **Select permissions**, select and add **User.Read**.

`Write-Host` ` ` `"CER file (public key): $cerPath"`

`Write-Host` ` ` `"PFX file (private key): $pfxPath"`

`Write-Host` ` ` `"Certificate Thumbprint: $($cert.Thumbprint)"`

`Write-Host` ` ` `"Certificate Password: YourSecurePassword123!"`

**Upload the certificate to Microsoft Entra ID**

７ **Note**

For production environments, use certificates issued by a trusted Certificate Authority (CA)

and store them in Azure Key Vault with managed identity access. Use self-signed

certificates only for local development and testing.

**Configure API permissions**

**Configure application permissions**

To test application-only flows where the AgentID SDK calls APIs by using its own identity

(without a user context), configure application permissions:

1\. From the **API permissions** page, select **Add a permission** \> **Microsoft Graph**.

2\. Select **Application permissions**.

3\. Under **Select permissions**, search for and select **User.Read.All**.

4\. Select **Add permissions**.

5\. Select **Grant admin consent for \[Your Tenant\]** and confirm.

To call the AgentID SDK's `/validate` endpoint with tokens issued specifically for your

application (using the `api://<application-client-id>/access_as_user` scope), you **must**

complete this step. If you're only testing Microsoft Graph scenarios with delegated

permissions, you can skip this section. Follow these steps to expose an API containing the

required scopes:

1\. Under **Manage**, select **Expose an API**.

2\. At the top of the page, select **Add** next to **Application ID URI**. This value defaults to

`api://<application-client-id>` . The App ID URI acts as the prefix for the scopes you'll

reference in your API's code, and it must be globally unique. Select **Save**.

3\. Select **Add a scope** as shown:

７ **Note**

Application permissions require administrator consent. Without this step, the application-

only endpoints in the testing section fail.

**Expose an API (for token validation testing)**

![](./assets/output_57_1.png)

4\. Next, specify the scope's attributes in the **Add a scope** pane, as follows:

**Scope name**: `access_as_user`

**Who can consent**: Admins and users

**Admin consent display name**: Access the AgentID SDK as user

**Admin consent description**: Allow access to AgentID SDK APIs as the signed-in user

**State**: Enabled

5\. Select **Add scope**.

The Microsoft Entra SDK for AgentID is a containerized web service that handles token

acquisition, validation, and secure downstream API calls. It runs as a companion container

alongside your application, allowing you to offload identity logic to a dedicated service.

The AgentID SDK requires a configuration file to connect to your Microsoft Entra application.

Create a new directory for your configuration and create an `appsettings.json` file:

**Start the Microsoft Entra SDK for AgentID**

**Create a configuration file**

PowerShell

Open `appsettings.json` in your preferred text editor and add the following configuration,

replacing the placeholder values with your Microsoft Entra application details:

JSON

The AgentID SDK is available as a prebuilt container image from the Microsoft Container

Registry (MCR)

. Before pulling the container image, verify that Docker Desktop is running. If

Docker isn't running, open Docker Desktop and wait for the status to show "Docker Desktop is

running".

`# Create a directory for the AgentID SDK configuration`

`New-Item` ` -ItemType` ` Directory` ` -Path` ` ` `"agentid-config"` ` -Force`

`cd ` `agentid-config`

`# Create the appsettings.json file`

`New-Item` ` -ItemType` ` File` ` -Path` ` ` `"appsettings.json"`

`{`

`    ``"AzureAd"` `: {`

`        ``"Instance"` `: ``"https://login.microsoftonline.com/"` `,`

`        ``"TenantId"` `: ``"YOUR_TENANT_ID_HERE"` `,`

`        ``"ClientId"` `: ``"YOUR_CLIENT_ID_HERE"` `,`

`        ``"ClientCredentials"` `: [`

`            {`

`                ``"SourceType"` `: ``"Path"` `,`

`                ``"CertificateStorePath"` `: ``"agentid-client-certificate.pfx"` `,`

`                ``"CertificateDistinguishedName"` `: ``"YourSecurePassword123!"`

`            }`

`        ]`

`    },`

`    ``"DownstreamApis"` `: {`

`        ``"me"` `: {`

`            ``"BaseUrl"` `: ``"https://graph.microsoft.com/v1.0/"` `,`

`            ``"RelativePath"` `: ``"me"` `,`

`            ``"Scopes"` `: [ ``"User.Read"` ` ]`

`        }`

`    },`

`    ``"Logging"` `: {`

`        ``"LogLevel"` `: {`

`            ``"Default"` `: ``"Information"` `,`

`            ``"Microsoft.AspNetCore"` `: ``"Warning"`

`        }`

`    },`

`    ``"AllowedHosts"` `: ``"*"`

`}`

**Pull and run the AgentID SDK container**

Navigate to your configuration directory and run the following commands:

PowerShell

You can manage the Agent ID SDK container by using the following Docker commands:

**View container logs**: `docker logs agentid-sdk`

**View real-time logs**: `docker logs -f agentid-sdk`

**Stop the container**: `docker stop agentid-sdk`

**Start the container again**: `docker start agentid-sdk`

**Remove the container**: `docker rm agentid-sdk`

You can verify whether the AgentID SDK container is running correctly by calling the health

check endpoint, ` /healthz` :

PowerShell

`# Navigate to your config directory`

`cd ` `agentid-config`

`# Pull the AgentID SDK container image from MCR`

`docker pull mcr.microsoft.com/`  `entra-sdk` `/`  `auth-sidecar` `:1.0.0-rc.2-azurelinux3.0-`

`distroless`

`# Run the container`

`docker run` ` -d` `` ` ``

`   `` --name`  ` `  `agentid-sdk` `` ` ``

`   `` -p` `` 5178:8080 ` ``

`   `` -e` `` ASPNETCORE_ENVIRONMENT=Development ` ``

`    mcr.microsoft.com/`  `entra-sdk` `/`  `auth-sidecar` `:1.0.0-rc.2-azurelinux3.0-distroless`

`# Copy configuration files into the container`

`docker cp appsettings.json ` `agentid-sdk` `:/app/appsettings.json`

`docker cp ` `agentid-client` `-certificate.pfx ` `agentid-sdk` `:/app/`  `agentid-client` `-`

`certificate.pfx`

`# Restart the container to apply the configuration`

`docker restart ` `agentid-sdk`

７ **Note**

For Windows hosts, use the Windows container variant: `mcr.microsoft.com/entra-`

`sdk/auth-sidecar:1.0.0-rc.2-windows`

**Verify that the container is running**

This endpoint returns `Healthy` , which confirms the AgentID SDK is running correctly and ready

to handle requests. Don't terminate the AgentID SDK while testing. The container must

continue running in the background for all authentication and API calls from the Python app to

work.

The Python sample app demonstrates how to use the Microsoft Entra SDK for AgentID for

authentication and API calls. The AgentID SDK runs as a local web service and acts as an

authentication proxy. It validates user tokens and calls downstream APIs like Microsoft Graph

on your behalf.

The sample includes Python scripts that show two authentication patterns:

**Delegated permissions**: The AgentID SDK validates your user token and calls APIs on

behalf of the signed-in user.

**Application permissions**: The AgentID SDK uses its own identity to call APIs without a

user context.

This approach centralizes token management and API access in a single service that your

applications can consume through simple HTTP requests.

Download the Python sample app

and extract it to a local directory. Alternatively, clone the

repository by opening a command prompt, navigating to your desired project location, and

running the following command:

PowerShell

The sample app contains the following Python scripts:

`get_token.py` – Acquires user access tokens through the Microsoft Authentication Library

(MSAL).

`main.py` – Command-line interface that calls the AgentID SDK endpoints and displays

JSON responses.

`Invoke-RestMethod` ` -Uri` ` ` `"http://localhost:5178/healthz"` ` -ErrorAction` ` SilentlyContinue`

**Run the Python sample app**

**Clone or download the Python sample app**

`git clone https://github.com/AzureAD/`  `microsoft-identity` `-web.git`

`cd ` `microsoft-identity` `-web/tests/DevApps/SidecarAdapter/python`

`MicrosoftIdentityWebSidecarClient.py` – HTTP client wrapper for the AgentID SDK's

`/Validate` , `/AuthorizationHeader` , and `/DownstreamApi` endpoints.

The Python scripts use the parameter `me` when calling AgentID SDK endpoints. This parameter

references the downstream API configuration named "me" in the AgentID SDKs

`appsettings.json` :

JSON

When you call an AgentID SDK endpoint with the `me` parameter, the SDK uses the base URL

and relative path from the configuration to construct the full API endpoint, requests the

specified scopes, and calls the Microsoft Graph `/me` endpoint to retrieve the signed-in user's

profile. You can add additional downstream API configurations to `appsettings.json` with

different names and endpoints to call additional APIs.

This quickstart demonstrates a three-tier authentication pattern:

1\. **User authentication**: You acquire a user access token by using MSAL for Python. This

token proves the user's identity.

2\. **Token validation**: The AgentID SDK validates the user token to ensure it's authentic and

issued for your application.

3\. **Token exchange**: The AgentID SDK uses the On-Behalf-Of (OBO) flow to exchange the

user token for a new token scoped to Microsoft Graph, then calls the API.

For application-only scenarios, the AgentID SDK bypasses user authentication and uses its own

client credentials to acquire tokens directly. The SDK centralizes this authentication logic, so

your Python application only needs to make simple HTTP requests without managing complex

OAuth flows.

`"DownstreamApis"` `: {`

`    ``"me"` `: {`

`        ``"BaseUrl"` `: ``"https://graph.microsoft.com/v1.0/"` `,`

`        ``"RelativePath"` `: ``"me"` `,`

`        ``"Scopes"` `: [ ``"User.Read"` ` ]`

`    }`

`}`

**Test interaction between the Microsoft Entra SDK**

**for AgentID and the Python app**

**Acquire a user access token**

Before testing the AgentID SDK endpoints, obtain a valid access token. The `get_token.py` script

uses MSAL for Python to acquire tokens interactively through a browser-based sign-in flow.

**Token scopes and audiences:**

The scope you request determines the token's audience ( ` aud` claim), which must match the

endpoint you're calling:

**For token validation testing**, use `api://<client-id>/access_as_user` to test the

`/validate` endpoint

**For Microsoft Graph testing**, acquire a new token with `User.Read` scope to test

`/authorizationheader` and `/downstreamapi` endpoints

Use the following commands to set your configuration variables and acquire a token:

PowerShell

When you run the acquire token command, the script initiates an interactive browser-based

sign-in flow. This browser authentication only occurs on the first run. After successful

authentication, the token is cached locally for subsequent use. The access token is then printed

to the console and stored in the `$token` PowerShell variable for use in subsequent commands.

After you get a valid user token, you can test the AgentID SDK core endpoints. These

operations use delegated permissions, so the SDK acts on behalf of the signed-in user.

First, set the SDK's base URL:

`# Set your configuration`

`$clientId = ``"YOUR_CLIENT_ID_HERE"`

`$tenantId = ``"YOUR_TENANT_ID_HERE"`

`$authority = ``"https://login.microsoftonline.com/$tenantId"`

`# For testing AgentID SDK APIs (if you exposed the API)`

`$scope = ``"api://$clientId/access_as_user"`

`# Or for testing Microsoft Graph directly`

`# $scope = "User.Read"`

`# Acquire token`

`$token = uv run` ` --with` ` msal get_token.py` ` --client-id` ` $clientId` ` --authority` ` `

`$authority` ` --scope` ` $scope`

**Test the Microsoft Entra SDK for AgentID endpoints with**

**delegated permissions**

PowerShell

The `/validate` endpoint requires a token issued specifically for your application by using the

`api://<client-id>/access_as_user` scope. Before you test token validation, ensure you

complete the steps in the "Expose an API" section. Use the following command to call the

`/validate` endpoint.

PowerShell

**Expected response:**

The `/validate` endpoint checks that the token is valid and extracts claims information:

JSON

This response confirms that:

The token format is correct (Bearer token)

The token is issued by the expected authority

The audience ( ` aud` ) matches your application

User identity claims are present and valid

The `/authorizationheader` endpoint retrieves a properly formatted authorization header for

calling downstream APIs:

`$side_car_url = ``"http://localhost:5178"`

**1\. Validate the user token**

`uv run` ` --with` ` requests main.py` ` --base-url` ` $side_car_url` ` --authorization-header` ` `

`"Bearer $token"` ` validate`

`{`

`  ``"protocol"` `: ``"Bearer"` `,`

`  ``"token"` `: ``"eyJ0eXAiOiJKV1QiLCJub25jZSI6..."` `,`

`  ``"claims"` `: {`

`    ``"aud"` `: ``"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"` `,`

`    ``"iss"` `: ``"https://login.microsoftonline.com/..."` `,`

`    ``"name"` `: ``"Your Name"` `,`

`    ``"upn"` `: ``"your.email@domain.com"`

`  }`

`}`

**2\. Get an authorization header for Microsoft Graph**

PowerShell

This endpoint:

Validates the incoming user token

Acquires a new token for Microsoft Graph on behalf of the user

Returns the formatted authorization header

The `/downstreamapi` endpoint calls Microsoft Graph directly and returns the response:

PowerShell

**Expected response:**

JSON

The `me` parameter corresponds to the downstream API configuration you defined in

`appsettings.json` . The AgentID SDK:

1\. Validates your user token

2\. Acquires a new token for Microsoft Graph by using the on-behalf-of (OBO) flow

3\. Calls the `/me` endpoint on Microsoft Graph

4\. Returns the user profile data

`uv run` ` --with` ` requests main.py` ` --base-url` ` $side_car_url` ` --authorization-header` ` `

`"Bearer $token"`  ` `  `get-auth` `-header me`

**3\. Call Microsoft Graph through the Microsoft Entra SDK for AgentID**

`uv run` ` --with` ` requests main.py` ` --base-url` ` $side_car_url` ` --authorization-header` ` `

`"Bearer $token"`  ` `  `invoke-downstream` ` me`

`{`

`  ``"statusCode"` `: 200,`

`  ``"headers"` `: {...},`

`  ``"content"` `: {`

`    ``"displayName"` `: ``"Your Name"` `,`

`    ``"mail"` `: ``"your.email@domain.com"` `,`

`    ``"userPrincipalName"` `: ``"your.email@domain.com"`

`  }`

`}`

**4\. Override default scopes and supply a request body**

You can customize API calls by overriding the default scopes configured in `appsettings.json` or

by providing a request body for write operations.

PowerShell

This approach is useful when:

Testing different permission levels. For example, you can specify different scopes like --

scope `User.Read Mail.Read` to request additional permissions

The downstream API requires scopes not configured by default

You need to request additional permissions dynamically

When calling APIs that require a request body (such as creating or updating resources),

you add the optional `--body-file` parameter used for POST/PUT operations

The Microsoft Entra SDK for AgentID also supports application-only flows. In these flows, the

AgentID SDK uses its own app identity instead of acting on behalf of a user. These endpoints

don't require a user authorization header.

Use this endpoint to retrieve an authorization header for calling Microsoft Graph with the

AgentID SDK's own identity:

PowerShell

This endpoint:

`uv run` ` --with` ` requests main.py` ` --base-url` ` $side_car_url` ` --authorization-header` ` `

`"Bearer $token"` ` --scope` ` <scopes> ` `invoke-downstream` ` <`  `api-name`  `>` ` --body-file` ` <`  `path-to` `-`

`file>`

**Test application-only endpoints**

７ **Note**

Application-only flows require that your app registration has **application permissions**

(such as `User.Read.All` ) in Microsoft Entra ID, not just delegated permissions. An

administrator must grant consent to these permissions before you can test these

endpoints.

**Get authorization header without user context**

`uv run` ` --with` ` requests main.py` ` --base-url` ` $side_car_url ` `get-auth` `-`  `header-unauth` ` me`

Uses the AgentID SDK's client credentials (app identity) to authenticate.

Acquires an app-only access token for Microsoft Graph

Returns the authorization header

Use this endpoint to call Microsoft Graph directly by using the AgentID SDK identity:

PowerShell

This example demonstrates service-to-service communication where:

No user is involved in the authentication flow

The AgentID SDK authenticates by using its own client ID and certificate

The API call uses application permissions, not delegated permissions

This pattern is ideal for background services, batch processing, or automated tasks

The validation response provides detailed information about the token:

**Field**

**Description**

`protocol`

The authentication scheme (always "Bearer" for OAuth 2.0 tokens)

`token`

The original access token (truncated in examples)

`claims`

Key-value pairs extracted from the token's payload

`claims.aud`

The intended audience (your client ID)

`claims.iss`

The token issuer (Microsoft Entra ID)

`claims.name`

The display name of the signed-in user

`claims.upn`

User Principal Name (email address)

**Call Microsoft Graph without user context**

`uv run` ` --with` ` requests main.py` ` --base-url` ` $side_car_url ` `invoke-downstream` `-unauth me`

**Understand the responses**

**Token validation response structure**

ﾉ

**Expand table**

**Microsoft Graph call response structure**

**Field**

**Description**

`statusCode`

HTTP status code from Microsoft Graph (200 = success)

`headers`

Response headers from the API call

`content`

The actual data returned by Microsoft Graph

`content.displayName`

User's display name in the directory

`content.mail`

User's email address

`content.userPrincipalName`

User's UPN

If you encounter errors when testing the Microsoft Entra SDK for AgentID endpoints, check the

following solutions to common issues:

**Issue**

**Solution**

**"Connection refused"**

**errors**

Verify the AgentID SDK container is running: `docker ps -a` . If the container status

shows "Exited", check the logs: `docker logs agentid-sdk` . Restart the container:

`docker start agentid-sdk` and test the health endpoint: `Invoke-RestMethod -Uri`

`"http://localhost:5178/healthz"` .

**Container returns**

**500 Internal Server**

**Error**

View container logs for detailed errors: `docker logs agentid-sdk` . Common

causes: invalid JSON in `appsettings.json` , incorrect certificate path, wrong

certificate password, or missing TenantId/ClientId values.

**Certificate not found**

**errors**

Ensure the PFX file was copied correctly: `docker exec agentid-sdk ls -la`

`/app/agentid-client-certificate.pfx` . If missing, copy it again: `docker cp`

`agentid-client-certificate.pfx agentid-sdk:/app/agentid-client-`

`certificate.pfx` and restart: `docker restart agentid-sdk` .

**"Invalid token" or**

**"Audience validation**

**failed" errors**

Ensure your token's audience ( ` aud` claim) matches your client ID. For the

`/validate` endpoint, use the `api://<client-id>/access_as_user` scope. For

Microsoft Graph calls, use `User.Read` . Clear the token cache: `Remove-Item -Path`

`"$env:USERPROFILE\.msal_token_cache.bin" -ErrorAction SilentlyContinue` .

**appsettings.json not**

**loading**

Verify the file was copied into the container: `docker exec agentid-sdk cat`

`/app/appsettings.json` . Ensure the JSON is valid (no comments, proper syntax). If

the file is missing or incorrect, copy it again and restart the container.

ﾉ

**Expand table**

**Troubleshooting common issues**

ﾉ

**Expand table**

**Issue**

**Solution**

**Container won't start**

**after configuration**

**changes**

Stop and remove the container: `docker stop agentid-sdk && docker rm agentid-`

`sdk` . Run the container again with updated configuration files following the "Pull

and run the AgentID SDK container" section.

**Agent identities**: Learn how to use the Microsoft Entra SDK for AgentID with service

principals and managed identities by testing with `--agent-identity` and `--agent-`

`username` parameters

**Custom APIs**: Add more downstream API configurations to `appsettings.json` to call your

own protected APIs

**Production deployment**: Configure the Microsoft Entra SDK for AgentID to use managed

identities instead of certificates

**Last updated on 11/12/2025**

**Next steps**

**Sign in users and call downstream APIs**

**with the Microsoft Entra SDK for AgentID**

**in TypeScript**

In this quickstart, you use a sample web app to learn how to sign in users or agents and call

downstream APIs by using its own identity. The sample app uses the Microsoft Entra SDK for

AgentID to validate user tokens for delegated access and uses application identity for service-

to-service communication with downstream APIs like Microsoft Graph.

Install Node.js 18.x

or later.

Install Docker Desktop

.

An Azure account with an active subscription. If you don't already have one, Create an

account for free

.

This Azure account must have permissions to manage applications. Any of the following

Microsoft Entra roles include the required permissions:

Application Administrator

Application Developer

A workforce tenant. You can use your Default Directory or set up a new tenant.

To complete the rest of the quickstart, you need to first register an application in Microsoft

Entra ID.

Follow these steps to create the app registration:

1\. Sign in to the Microsoft Entra admin center

as at least an Application Developer.

2\. If you have access to multiple tenants, use the **Settings** icon

![](./assets/output_69_1.png)

in the top menu to switch

to the tenant in which you want to register the application.

**Prerequisites**

**Create and configure your Microsoft Entra**

**application**

**Create application registration**

3\. Browse to **Entra ID** \> **App registrations** and select **New registration**.

4\. Enter a meaningful **Name** for your app, such as _identity-client-app_. App users see this

name, and you can change it at any time. You can have multiple app registrations with the

same name.

5\. Under **Supported account types**, specify who can use the application. Select **Accounts in**

**this organizational directory only** for most applications. Refer to the table for more

information on each option.

**Supported account types**

**Description**

**Accounts in this**

**organizational directory only**

For _single-tenant_ apps for use only by users (or guests) in _your_

tenant.

**Accounts in any**

**organizational directory**

For _multitenant_ apps and you want users in _any_ Microsoft Entra

tenant to be able to use your application. Ideal for software-as-a-

service (SaaS) applications that you intend to provide to multiple

organizations.

**Accounts in any**

**organizational directory and**

**personal Microsoft accounts**

For _multitenant_ apps that support both organizational and

personal Microsoft accounts (for example, Skype, Xbox, Live,

Hotmail).

**Personal Microsoft accounts**

For apps used only by personal Microsoft accounts (for example,

Skype, Xbox, Live, Hotmail).

6\. Select **Register** to complete the app registration.

ﾉ

**Expand table**

![](./assets/output_71_1.png)

7\. The application's **Overview** page is displayed. Record the following values from the

application Overview page for later use:

Application (client) ID

Directory (tenant) ID

![](./assets/output_71_2.png)

The TypeScript sample app uses interactive authentication with a browser-based sign-in flow.

Configure a redirect URI to handle the authentication response:

1\. In your app registration, under **Manage**, select **Authentication**.

2\. Select **Add a platform**.

3\. Select **Mobile and desktop applications**.

4\. Under **Custom redirect URIs**, enter `http://localhost` .

5\. Select **Configure**.

The Microsoft Entra SDK for AgentID uses client credentials to authenticate and acquire tokens

for downstream APIs. For local development and testing, use a self-signed certificate for

authentication.

Run PowerShell as an administrator and use the following commands to generate a self-signed

certificate:

PowerShell

**Add a redirect URI**

**Add client credentials**

**Generate a self-signed certificate**

`# Generate a self-signed certificate`

`$cert = ` `New-SelfSignedCertificate` `` ` ``

`   `` -Subject` ` ` `"CN=AgentID-Client-Certificate"` `` ` ``

`   `` -CertStoreLocation` ` ` `"Cert:\CurrentUser\My"` `` ` ``

`   `` -KeyExportPolicy` `` Exportable ` ``

`   `` -KeySpec` `` Signature ` ``

`   `` -KeyLength` `` 2048 ` ``

`   `` -KeyAlgorithm` `` RSA ` ``

`   `` -HashAlgorithm` `` SHA256 ` ``

`   `` -NotAfter` ` (`  `Get-Date` `).AddDays(7)`

`# Export public key (CER) for upload to Azure`

`$cerPath = ``"agentid-client-certificate.cer"`

`Export-Certificate` ` -Cert` ` $cert` ` -FilePath` ` $cerPath`

`# Export private key (PFX) for the Agent ID SDK container`

`$pfxPath = ``"agentid-client-certificate.pfx"`

`$certPassword = ` `ConvertTo-SecureString` ` -String` ` ` `"YourSecurePassword123!"` ` -Force -`

`AsPlainText`

`Export-PfxCertificate` ` -Cert` ` $cert` ` -FilePath` ` $pfxPath` ` -Password` ` $certPassword`

`Write-Host` ` ` `"Certificate generated successfully!"`

Record the certificate thumbprint displayed in the PowerShell output. You need it to verify the

certificate in the Microsoft Entra admin center matches the one installed locally.

Follow these steps to upload the `.cer` file created in your current directory to the Microsoft

Entra admin center:

1\. Open your app registration in the Microsoft Entra admin center

2\. Under **Manage**, select **Certificates & secrets**.

3\. In the **Certificates** tab, select **Upload certificate**.

4\. Select the `.cer` file you generated (for example, `agentid-client-cert.cer` ).

5\. Provide a description (for example, "AgentID Local Development Certificate").

6\. Select **Add**.

7\. Record the certificate **Thumbprint** displayed (it should match the one from your

certificate generation).

Follow these steps to configure delegated permissions to Microsoft Graph. With these

permissions, your client application can perform operations on behalf of the signed-in user,

such as reading their email.

1\. In your app registration, under **Manage**, select **API permissions** \> **Add a permission** >

**Microsoft Graph**.

2\. Select **Delegated permissions**. Microsoft Graph exposes many permissions, with the most

commonly used shown at the top of the list.

3\. Under **Select permissions**, select and add **User.Read**.

`Write-Host` ` ` `"CER file (public key): $cerPath"`

`Write-Host` ` ` `"PFX file (private key): $pfxPath"`

`Write-Host` ` ` `"Certificate Thumbprint: $($cert.Thumbprint)"`

`Write-Host` ` ` `"Certificate Password: YourSecurePassword123!"`

**Upload the certificate to Microsoft Entra ID**

７ **Note**

For production environments, use certificates issued by a trusted Certificate Authority (CA)

and store them in Azure Key Vault with managed identity access. Self-signed certificates

should only be used for local development and testing.

**Configure API permissions**

**Configure application permissions**

To test application-only flows where the AgentID SDK calls APIs by using its own identity

(without a user context), configure application permissions:

1\. From the **API permissions** page, select **Add a permission** \> **Microsoft Graph**.

2\. Select **Application permissions**.

3\. Under **Select permissions**, search for and select **User.Read.All**.

4\. Select **Add permissions**.

5\. Select **Grant admin consent for \[Your Tenant\]** and confirm.

To call the AgentID SDK's `/validate` endpoint with tokens issued specifically for your

application (using the `api://<application-client-id>/access_as_user` scope), you **must**

complete this step. If you're only testing Microsoft Graph scenarios with delegated

permissions, you can skip this section. Follow these steps to expose an API containing the

required scopes:

1\. Under **Manage**, select **Expose an API**.

2\. At the top of the page, select **Add** next to **Application ID URI**. This value defaults to

`api://<application-client-id>` . The App ID URI acts as the prefix for the scopes you'll

reference in your API's code, and it must be globally unique. Select **Save**.

3\. Select **Add a scope** as shown:

７ **Note**

Application permissions require administrator consent. Without this step, the application-

only endpoints in the testing section fail.

**Expose an API (for token validation testing)**

![](./assets/output_75_1.png)

4\. Next, specify the scope's attributes in the **Add a scope** pane, as follows:

**Scope name**: `access_as_user`

**Who can consent**: Admins and users

**Admin consent display name**: Access the AgentID SDK as user

**Admin consent description**: Allow access to AgentID SDK APIs as the signed-in user

**State**: Enabled

5\. Select **Add scope**.

The Microsoft Entra SDK for AgentID is a containerized web service that handles token

acquisition, validation, and secure downstream API calls. It runs as a companion container

alongside your application, allowing you to offload identity logic to a dedicated service.

The AgentID SDK requires a configuration file to connect to your Microsoft Entra application.

Create a new directory for your configuration and create an `appsettings.json` file:

**Start the Microsoft Entra SDK for AgentID**

**Create a configuration file**

PowerShell

Open `appsettings.json` in your preferred text editor and add the following configuration,

replacing the placeholder values with your Microsoft Entra application details:

JSON

The AgentID SDK is available as a prebuilt container image from the Microsoft Container

Registry (MCR)

. Before pulling the container image, verify that Docker Desktop is running. If

Docker isn't running, open Docker Desktop and wait for the status to show "Docker Desktop is

running".

`# Create a directory for the AgentID SDK configuration`

`New-Item` ` -ItemType` ` Directory` ` -Path` ` ` `"agentid-config"` ` -Force`

`cd ` `agentid-config`

`# Create the appsettings.json file`

`New-Item` ` -ItemType` ` File` ` -Path` ` ` `"appsettings.json"`

`{`

`    ``"AzureAd"` `: {`

`        ``"Instance"` `: ``"https://login.microsoftonline.com/"` `,`

`        ``"TenantId"` `: ``"YOUR_TENANT_ID_HERE"` `,`

`        ``"ClientId"` `: ``"YOUR_CLIENT_ID_HERE"` `,`

`        ``"ClientCredentials"` `: [`

`            {`

`                ``"SourceType"` `: ``"Path"` `,`

`                ``"CertificateStorePath"` `: ``"agentid-client-certificate.pfx"` `,`

`                ``"CertificateDistinguishedName"` `: ``"YourSecurePassword123!"`

`            }`

`        ]`

`    },`

`    ``"DownstreamApis"` `: {`

`        ``"me"` `: {`

`            ``"BaseUrl"` `: ``"https://graph.microsoft.com/v1.0/"` `,`

`            ``"RelativePath"` `: ``"me"` `,`

`            ``"Scopes"` `: [ ``"User.Read"` ` ]`

`        }`

`    },`

`    ``"Logging"` `: {`

`        ``"LogLevel"` `: {`

`            ``"Default"` `: ``"Information"` `,`

`            ``"Microsoft.AspNetCore"` `: ``"Warning"`

`        }`

`    },`

`    ``"AllowedHosts"` `: ``"*"`

`}`

**Pull and run the AgentID SDK container**

Navigate to your configuration directory and run the following commands:

PowerShell

You can manage the Agent ID SDK container by using the following Docker commands:

**View container logs**: `docker logs agentid-sdk`

**View real-time logs**: `docker logs -f agentid-sdk`

**Stop the container**: `docker stop agentid-sdk`

**Start the container again**: `docker start agentid-sdk`

**Remove the container**: `docker rm agentid-sdk`

You can verify whether the AgentID SDK container is running correctly by calling the health

check endpoint, ` /healthz` :

PowerShell

`# Navigate to your config directory`

`cd ` `agentid-config`

`# Pull the AgentID SDK container image from MCR`

`docker pull mcr.microsoft.com/`  `entra-sdk` `/`  `auth-sidecar` `:1.0.0-rc.2-azurelinux3.0-`

`distroless`

`# Run the container`

`docker run` ` -d` `` ` ``

`   `` --name`  ` `  `agentid-sdk` `` ` ``

`   `` -p` `` 5178:8080 ` ``

`   `` -e` `` ASPNETCORE_ENVIRONMENT=Development ` ``

`    mcr.microsoft.com/`  `entra-sdk` `/`  `auth-sidecar` `:1.0.0-rc.2-azurelinux3.0-distroless`

`# Copy configuration files into the container`

`docker cp appsettings.json ` `agentid-sdk` `:/app/appsettings.json`

`docker cp ` `agentid-client` `-certificate.pfx ` `agentid-sdk` `:/app/`  `agentid-client` `-`

`certificate.pfx`

`# Restart the container to apply the configuration`

`docker restart ` `agentid-sdk`

７ **Note**

For Windows hosts, use the Windows container variant: `mcr.microsoft.com/entra-`

`sdk/auth-sidecar:1.0.0-rc.2-windows`

**Verify that the container is running**

This endpoint returns `Healthy` , which confirms the AgentID SDK is running correctly and ready

to handle requests. Don't terminate the AgentID SDK while testing. The container must

continue running in the background for all authentication and API calls from the TypeScript

sample app to work.

The TypeScript sample app demonstrates how to use the Microsoft Entra SDK for AgentID to

validate user tokens. The app is an Express.js server that validates incoming requests through

the AgentID SDK. The AgentID SDK can also call downstream APIs like Microsoft Graph on your

behalf.

Download the TypeScript sample app

and extract it to a local directory. Alternatively, clone

the repository by opening a command prompt, navigating to your desired project location, and

running the following command:

PowerShell

After cloning the repo, navigate to the TypeScript sample app:

PowerShell

The TypeScript sample app consists of three main files that work together to demonstrate

authentication patterns with the Microsoft Entra SDK for AgentID.

**sidecar.ts**: Provides the `SidecarClient` class, which is a TypeScript client that communicates

with the AgentID SDK container. It sends bearer tokens to the AgentID SDK's `/Validate`

endpoint, receives back the validated token along with user claims, and handles token

validation errors.

**app.ts**: An Express.js web server that authenticates all incoming requests. It extracts bearer

tokens from the authorization header and validates them using `SidecarClient` . If validation

fails, the server returns a 401 Unauthorized response. When validation succeeds, it attaches the

`Invoke-RestMethod` ` -Uri` ` ` `"http://localhost:5178/healthz"` ` -ErrorAction` ` SilentlyContinue`

**Run the TypeScript sample app**

**Clone or download the sample app**

`git clone https://github.com/AzureAD/`  `microsoft-identity` `-web.git`

`cd ` `microsoft-identity` `-web/tests/DevApps/SidecarAdapter/typescript`

user's claims to the request object via `req.sidecarValidation` , for use in downstream route

handlers.

**sidecar.test.ts**: Contains automated integration tests that verify the complete authentication

flow. The test suite starts by launching the Express server, then uses MSAL Node to perform

interactive browser authentication and acquire an access token with the required scopes. It

then makes an HTTP request to the server with the acquired token and verifies that the

AgentID SDK validates the token correctly before returning the expected user claims.

Navigate to the TypeScript sample directory and install the required packages:

PowerShell

Before running the sample app, configure it with your application details as follows:

1\. Open `sidecar.test.ts` and update the client ID, tenant ID, and scopes to match your app

registration.

2\. Create a `.env` file in the `typescript` directory for environment variables:

PowerShell

Add the following configuration to `.env` :

env

Start the TypeScript sample app by running `npm start` . The server starts on

`http://localhost:5555` and is ready to accept authenticated requests. You should see output

**Install dependencies**

`cd d:\SDKs\`  `microsoft-identity` `-web\tests\DevApps\SidecarAdapter\typescript`

`npm install`

**Configure the sample app**

`# Create .env file`

`New-Item` ` -ItemType` ` File` ` -Path` ` ` `".env"` ` -Force`

`PORT=5555`

`SIDECAR_BASE_URL=http://localhost:5178`

**Start the Express server**

similar to:

Keep this terminal window open. The Express server must continue running to handle test

requests in the next section.

Now that both the AgentID SDK container and the Express server are running, you can test the

authentication and API call scenarios.

This scenario shows how to sign in a user, acquire a token, and call the Express server with that

token.

The sample includes an automated test that acquires a user token by using MSAL. Open a **new**

PowerShell window (keep the Express server running) and run:

PowerShell

This command runs the integration test that:

1\. Opens a browser window for interactive authentication

2\. Acquires an access token with the `api://<your-client-id>/access_as_user` scope

3\. Calls the Express server with the token

4\. Checks that the AgentID SDK validates the token successfully

On the first run, you're prompted to sign in with your Microsoft Entra credentials. The browser

window opens automatically. After successful authentication, you can close the browser.

`Server listening on port 5555`

`Sidecar base URL: http://localhost:5178`

**Test the TypeScript sample app**

**Test with user-delegated permissions**

**Acquire a user token**

`cd d:\SDKs\`  `microsoft-identity` `-web\tests\DevApps\SidecarAdapter\typescript`

`npm test`

**Manual testing with curl**

If you prefer manual testing, you can acquire a token and call the Express server directly:

PowerShell

The expected response is:

JSON

This scenario demonstrates how to call downstream APIs by using the application's own

identity without user context.

From your PowerShell window, call the AgentID SDK directly to test application-only flow:

PowerShell

This endpoint:

1\. Authenticates by using the application's certificate (configured in `appsettings.json` )

2\. Acquires an app-only access token for Microsoft Graph

3\. Calls the Graph API `/me` endpoint

4\. Returns the service principal information

`# First, get a token (you'll need to implement token acquisition or extract from `

`test output)`

`$token = ``"YOUR_ACCESS_TOKEN_HERE"`

`# Call the Express server`

`Invoke-RestMethod` ` -Uri` ` ` `"http://localhost:5555/api/protected"` `` ` ``

`   `` -Headers` ` @{ Authorization = ``"Bearer $token"` `` } ` ``

`   `` -Method` ` Get`

`message                                                  protocol token          `

`claims`

`-------                                                  -------- -----          ---`

`---`

`Request authenticated via Microsoft Identity Web Sidecar Bearer   ***redacted*** `

`@{aud=api://` `"Your client ID"` `; iss=https://sts.win…`

**Test application-only authentication**

`# Call Microsoft Graph using application identity`

`Invoke-RestMethod` ` -Uri` ` ` `"http://localhost:5178/DownstreamApiUnauthenticated/me"` `` ` ``

`   `` -Method` ` Get`

７ **Note**

You can test custom downstream API configurations by adding them to the AgentID SDK's

`appsettings.json` :

JSON

Then restart the AgentID SDK container and test the new endpoint:

PowerShell

**Agent identities**: Learn how to use the Microsoft Entra SDK for AgentID with service

principals and managed identities by testing with `--agent-identity` and `--agent-`

`username` parameters

**Custom APIs**: Add more downstream API configurations to `appsettings.json` to call your

own protected APIs

**Production deployment**: Configure the Microsoft Entra SDK for AgentID to use managed

identities instead of certificates

This scenario requires the `User.Read.All` application permission with admin consent

(configured earlier in the quickstart).

**Test custom downstream API calls**

`"DownstreamApis"` `: {`

`    ``"me"` `: {`

`        ``"BaseUrl"` `: ``"https://graph.microsoft.com/v1.0/"` `,`

`        ``"RelativePath"` `: ``"me"` `,`

`        ``"Scopes"` `: [ ``"User.Read"` ` ]`

`    },`

`    ``"users"` `: {`

`        ``"BaseUrl"` `: ``"https://graph.microsoft.com/v1.0/"` `,`

`        ``"RelativePath"` `: ``"users"` `,`

`        ``"Scopes"` `: [ ``"User.Read.All"` ` ]`

`    }`

`}`

`# Restart container to reload configuration`

`docker restart ` `agentid-sdk`

`# Test the new endpoint`

`Invoke-RestMethod` ` -Uri` ` ` `"http://localhost:5178/DownstreamApiUnauthenticated/users"` `` ` ``

`   `` -Method` ` Get`

**Next steps**

**Last updated on 11/13/2025**

**Scenario: Call a downstream API**

Use the Microsoft Entra SDK for AgentID to handle both token acquisition and HTTP

communication in a single operation. The SDK exchanges your incoming token for one scoped

to the downstream API, then makes the HTTP call and returns the response. This guide shows

you how to configure downstream APIs, implement calls in TypeScript and Python, handle

different HTTP methods, and manage errors with retries.

An Azure account with an active subscription. Create an account for free

.

**Microsoft Entra SDK for AgentID** deployed and running in your environment. See

Installation Guide for setup instructions.

**Downstream API configured** in the SDK with the base URL and required scopes for the

APIs you want to call.

**Bearer tokens from authenticated clients** \- Your application receives tokens from client

applications that you'll forward to the SDK.

**Appropriate permissions in Microsoft Entra ID** \- Your account must have permissions to

register applications and grant API permissions.

Configure the downstream API in your Microsoft Entra SDK for AgentID environment settings:

YAML

The configuration specifies:

**BaseUrl**: The root endpoint of your downstream API

**Scopes**: The permissions required for accessing the downstream API

**Prerequisites**

**Configuration**

`env:`

`- name:`  ` `  `DownstreamApis__Graph__BaseUrl`

`  value:` ` ` `"https://graph.microsoft.com/v1.0"`

`- name:`  ` `  `DownstreamApis__Graph__Scopes__0`

`  value:` ` ` `"User.Read"`

`- name:`  ` `  `DownstreamApis__Graph__Scopes__1`

`  value:` ` ` `"Mail.Read"`

**TypeScript/Node.js**

The following examples show how to call downstream APIs from TypeScript and Node.js

applications. The code demonstrates both a reusable function and integration with Express.js.

TypeScript

`interface` ` DownstreamApiResponse {`

`  statusCode: ` `number` `;`

`  headers: Record<`  `string` `, ` `string`  `>;`

`  content: ` `string` `;`

`}`

`async`  ` `  `function`  ` `  `callDownstreamApi` `(`

`  incomingToken: ` `string` `,`

`  serviceName: ` `string` `,`

`  relativePath: ` `string` `,`

`  method: ` `string` ` = 'GET',`

`  body?: ` `any`

`): ` `Promise`  `<`  `any`  `> {`

`  ` `const` ` sdkUrl = process.env.ENTRA_SDK_URL || ``'http://localhost:5000'` `;`

`  `

`  ` `const` ` url = ` `new` ` URL(`  `` ` ``  `${sdkUrl}` `/DownstreamApi/`  `${serviceName}`  `` ` `` `);`

`  url.searchParams.append(` `'optionsOverride.RelativePath'` `, relativePath);`

`  ` `if` ` (method !== ``'GET'` `) {`

`    url.searchParams.append(` `'optionsOverride.HttpMethod'` `, method);`

`  }`

`  `

`  ` `const` ` requestOptions: ` `any` ` = {`

`    method: method,`

`    headers: {`

`      ``'Authorization'` `: incomingToken`

`    }`

`  };`

`  `

`  ` `if` ` (body) {`

`    requestOptions.headers[` `'Content-Type'` `] = ``'application/json'` `;`

`    requestOptions.body = ` `JSON` `.stringify(body);`

`  }`

`  `

`  ` `const` ` response = ` `await` ` fetch(url.toString(), requestOptions);`

`  `

`  ` `if` ` (!response.ok) {`

`    ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `SDK error: `` `${response.statusText}`  `` ` `` `);`

`  }`

`  `

`  ` `const` ` data = ` `await` ` response.json() ` `as` ` DownstreamApiResponse;`

`  `

`  ` `if` ` (data.statusCode >= 400) {`

`    ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `API error `` `${data.statusCode}` `: ` `${data.content}`  `` ` `` `);`

`  }`

`  `

`  ` `return`  ` `  `JSON` `.parse(data.content);`

`}`

`// Usage examples`

The following example demonstrates how to integrate these functions into an Express.js

application using middleware and route handlers:

JavaScript

`async`  ` `  `function`  ` `  `getUserProfile` `(incomingToken: ` `string` `) {`

`  ` `return`  ` `  `await` ` callDownstreamApi(incomingToken, ``'Graph'` `, ``'me'` `);`

`}`

`async`  ` `  `function`  ` `  `listEmails` `(incomingToken: ` `string` `) {`

`  ` `return`  ` `  `await` ` callDownstreamApi(`

`    incomingToken,`

`    ``'Graph'` `,`

`    ``'me/messages?$top=10&$select=subject,from,receivedDateTime'`

`  );`

`}`

`async`  ` `  `function`  ` `  `sendEmail` `(incomingToken: ` `string` `, message: ` `any` `) {`

`  ` `return`  ` `  `await` ` callDownstreamApi(`

`    incomingToken,`

`    ``'Graph'` `,`

`    ``'me/sendMail'` `,`

`    ``'POST'` `,`

`    { message }`

`  );`

`}`

`// Express.js API example`

`import` ` express ` `from` ` ` `'express'` `;`

`const` ` app = express();`

`app.use(express.json());`

`app.get(` `'/api/profile'` `, ` `async` ` (req, res) => {`

`  ` `try` ` {`

`    ` `const` ` incomingToken = req.headers.authorization;`

`    ` `if` ` (!incomingToken) {`

`      ` `return` ` res.status(401).json({ ` `error` `: ``'No authorization token'` ` });`

`    }`

`    `

`    ` `const` ` profile = ` `await` ` getUserProfile(incomingToken);`

`    res.json(profile);`

`  } ` `catch` ` (error) {`

`    ` `console` `.error(` `'Error:'` `, error);`

`    res.status(500).json({ ` `error` `: ``'Failed to fetch profile'` ` });`

`  }`

`});`

`app.get(` `'/api/messages'` `, ` `async` ` (req, res) => {`

`  ` `try` ` {`

`    ` `const` ` incomingToken = req.headers.authorization;`

`    ` `if` ` (!incomingToken) {`

`      ` `return` ` res.status(401).json({ ` `error` `: ``'No authorization token'` ` });`

The following examples show how to call downstream APIs from Python applications using the

requests library and Flask for HTTP handling:

Python

`    }`

`    `

`    ` `const` ` messages = ` `await` ` listEmails(incomingToken);`

`    res.json(messages);`

`  } ` `catch` ` (error) {`

`    ` `console` `.error(` `'Error:'` `, error);`

`    res.status(500).json({ ` `error` `: ``'Failed to fetch messages'` ` });`

`  }`

`});`

`app.post(` `'/api/messages/send'` `, ` `async` ` (req, res) => {`

`  ` `try` ` {`

`    ` `const` ` incomingToken = req.headers.authorization;`

`    ` `if` ` (!incomingToken) {`

`      ` `return` ` res.status(401).json({ ` `error` `: ``'No authorization token'` ` });`

`    }`

`    `

`    ` `const` ` message = req.body;`

`    ` `await` ` sendEmail(incomingToken, message);`

`    res.json({ ` `success` `: ` `true` ` });`

`  } ` `catch` ` (error) {`

`    ` `console` `.error(` `'Error:'` `, error);`

`    res.status(500).json({ ` `error` `: ``'Failed to send message'` ` });`

`  }`

`});`

`app.listen(8080, () => {`

`  ` `console` `.log(` `'Server running on port 8080'` `);`

`});`

**Python**

`import` ` os`

`import` ` json`

`import` ` requests`

`from` ` typing ` `import` ` Dict, Any, Optional`

`def`  ` `  `call_downstream_api` `(`

`    incoming_token: str,`

`    service_name: str,`

`    relative_path: str,`

`    method: str = ``'GET'` `,`

`    body: Optional[Dict[str, Any]] = None`

`) -> Any:`

`    ``"""Call a downstream API via the Microsoft Entra SDK for AgentID."""`

`    sdk_url = os.getenv(` `'ENTRA_SDK_URL'` `, ``'http://localhost:5000'` `)`

`    `

If you want to integrate these functions into a Flask application, you can use the following

example:

`    params = {`

`        ``'optionsOverride.RelativePath'` `: relative_path`

`    }`

`    `

`    ` `if` ` method != ``'GET'` `:`

`        params[` `'optionsOverride.HttpMethod'` `] = method`

`    `

`    headers = {` `'Authorization'` `: incoming_token}`

`    json_body = ` `None`

`    `

`    ` `if` ` body:`

`        headers[` `'Content-Type'` `] = ``'application/json'`

`        json_body = body`

`    `

`    response = requests.request(`

`        method,`

`        ` `f"` `{sdk_url}` `/DownstreamApi/` `{service_name}` `"` `,`

`        params=params,`

`        headers=headers,`

`        json=json_body`

`    )`

`    `

`    ` `if`  ` `  `not` ` response.ok:`

`        ` `raise` ` Exception(`  `f"SDK error: ``{response.text}` `"` `)`

`    `

`    data = response.json()`

`    `

`    ` `if` ` data[` `'statusCode'` `] >= 400:`

`        ` `raise` ` Exception(`  `f"API error ``{data[` `'statusCode'` `]}` `: ``{data[` `'content'` `]}` `"` `)`

`    `

`    ` `return` ` json.loads(data[` `'content'` `])`

`# Usage examples`

`def`  ` `  `get_user_profile` `(incoming_token: str) -> Dict[str, Any]:`

`    ` `return` ` call_downstream_api(incoming_token, ``'Graph'` `, ``'me'` `)`

`def`  ` `  `list_emails` `(incoming_token: str) -> Dict[str, Any]:`

`    ` `return` ` call_downstream_api(`

`        incoming_token,`

`        ``'Graph'` `,`

`        ``'me/messages?$top=10&$select=subject,from,receivedDateTime'`

`    )`

`def`  ` `  `send_email` `(incoming_token: str, message: Dict[str, Any]) -> ` `None` `:`

`    call_downstream_api(`

`        incoming_token,`

`        ``'Graph'` `,`

`        ``'me/sendMail'` `,`

`        ``'POST'` `,`

`        {` `'message'` `: message}`

`    )`

Python

`# Flask API example`

`from` ` flask ` `import` ` Flask, request, jsonify`

`app = Flask(__name__)`

`@app.route('/api/profile')`

`def`  ` `  `profile` `():`

`    incoming_token = request.headers.get(` `'Authorization'` `)`

`    ` `if`  ` `  `not` ` incoming_token:`

`        ` `return` ` jsonify({` `'error'` `: ``'No authorization token'` `}), 401`

`    `

`    ` `try` `:`

`        profile_data = get_user_profile(incoming_token)`

`        ` `return` ` jsonify(profile_data)`

`    ` `except` ` Exception ` `as` ` e:`

`        print(`  `f"Error: ``{e}` `"` `)`

`        ` `return` ` jsonify({` `'error'` `: ``'Failed to fetch profile'` `}), 500`

`@app.route('/api/messages')`

`def`  ` `  `messages` `():`

`    incoming_token = request.headers.get(` `'Authorization'` `)`

`    ` `if`  ` `  `not` ` incoming_token:`

`        ` `return` ` jsonify({` `'error'` `: ``'No authorization token'` `}), 401`

`    `

`    ` `try` `:`

`        messages_data = list_emails(incoming_token)`

`        ` `return` ` jsonify(messages_data)`

`    ` `except` ` Exception ` `as` ` e:`

`        print(`  `f"Error: ``{e}` `"` `)`

`        ` `return` ` jsonify({` `'error'` `: ``'Failed to fetch messages'` `}), 500`

`@app.route('/api/messages/send', methods=['POST'])`

`def`  ` `  `send_message` `():`

`    incoming_token = request.headers.get(` `'Authorization'` `)`

`    ` `if`  ` `  `not` ` incoming_token:`

`        ` `return` ` jsonify({` `'error'` `: ``'No authorization token'` `}), 401`

`    `

`    ` `try` `:`

`        message = request.json`

`        send_email(incoming_token, message)`

`        ` `return` ` jsonify({` `'success'` `: ` `True` `})`

`    ` `except` ` Exception ` `as` ` e:`

`        print(`  `f"Error: ``{e}` `"` `)`

`        ` `return` ` jsonify({` `'error'` `: ``'Failed to send message'` `}), 500`

`if` ` __name__ == ``'__main__'` `:`

`    app.run(port=8080)`

**POST/PUT/PATCH requests**

The `/DownstreamApi` endpoint supports modification operations by passing the HTTP method

and request body. Use these patterns when you need to create, update, or delete resources in

the downstream API.

TypeScript

TypeScript

**Creating resources**

`// POST example - Create a calendar event`

`async`  ` `  `function`  ` `  `createEvent` `(incomingToken: ` `string` `, event: ` `any` `) {`

`  ` `return`  ` `  `await` ` callDownstreamApi(`

`    incomingToken,`

`    ``'Graph'` `,`

`    ``'me/events'` `,`

`    ``'POST'` `,`

`    event`

`  );`

`}`

`// Usage`

`const` ` newEvent = {`

`  subject: ``"Team Meeting"` `,`

`  start: {`

`    dateTime: ``"2024-01-15T14:00:00"` `,`

`    timeZone: ``"Pacific Standard Time"`

`  },`

`  end: {`

`    dateTime: ``"2024-01-15T15:00:00"` `,`

`    timeZone: ``"Pacific Standard Time"`

`  }`

`};`

`const` ` createdEvent = ` `await` ` createEvent(incomingToken, newEvent);`

**Updating resources**

`// PATCH example - Update user profile`

`async`  ` `  `function`  ` `  `updateProfile` `(incomingToken: ` `string` `, updates: ` `any` `) {`

`  ` `return`  ` `  `await` ` callDownstreamApi(`

`    incomingToken,`

`    ``'Graph'` `,`

`    ``'me'` `,`

`    ``'PATCH'` `,`

`    updates`

`  );`

`}`

`// Usage`

The following scenarios demonstrate advanced configurations for specialized use cases.

Add custom headers to the downstream API request:

TypeScript

Request different scopes than the default configured scopes:

TypeScript

Use agent identity to call APIs with application permissions:

TypeScript

`await` ` updateProfile(incomingToken, {`

`  mobilePhone: ``"+1 555 0100"` `,`

`  officeLocation: ``"Building 2, Room 201"`

`});`

**Advanced scenarios**

**Custom headers**

`const` ` url = ` `new` ` URL(`  `` ` ``  `${sdkUrl}` ``/DownstreamApi/MyApi` `` `);`

`url.searchParams.append(` `'optionsOverride.RelativePath'` `, ``'items'` `);`

`url.searchParams.append(` `'optionsOverride.CustomHeader.X-Custom-Header'` `, ``'custom-`

`value'` `);`

`url.searchParams.append(` `'optionsOverride.CustomHeader.X-Request-Id'` `, requestId);`

**Override scopes**

`const` ` url = ` `new` ` URL(`  `` ` ``  `${sdkUrl}` ``/DownstreamApi/Graph` `` `);`

`url.searchParams.append(` `'optionsOverride.RelativePath'` `, ``'me'` `);`

`url.searchParams.append(` `'optionsOverride.Scopes'` `, ``'User.ReadWrite'` `);`

`url.searchParams.append(` `'optionsOverride.Scopes'` `, ``'Mail.Send'` `);`

**With agent identity**

`const` ` url = ` `new` ` URL(`  `` ` ``  `${sdkUrl}` ``/DownstreamApi/Graph` `` `);`

`url.searchParams.append(` `'optionsOverride.RelativePath'` `, ``'users'` `);`

`url.searchParams.append(` `'AgentIdentity'` `, agentClientId);`

`url.searchParams.append(` `'AgentUsername'` `, ``'admin@contoso.com'` `);`

Implement retry logic with exponential backoff to handle transient failures gracefully:

TypeScript

The Microsoft Entra SDK for AgentID provides two approaches for calling downstream APIs.

Use this comparison to determine which approach best fits your needs.

**Error handling**

`async`  ` `  `function`  ` `  `callDownstreamApiWithRetry` `(`

`  incomingToken: ` `string` `,`

`  serviceName: ` `string` `,`

`  relativePath: ` `string` `,`

`  method: ` `string` ` = 'GET',`

`  body?: ` `any` `,`

`  maxRetries: ` `number` ` = 3`

`): ` `Promise`  `<`  `any`  `> {`

`  ` `let` ` lastError: ` `Error` `;`

`  `

`  ` `for` ` (`  `let` ` attempt = 1; attempt <= maxRetries; attempt++) {`

`    ` `try` ` {`

`      ` `return`  ` `  `await` ` callDownstreamApi(`

`        incomingToken,`

`        serviceName,`

`        relativePath,`

`        method,`

`        body`

`      );`

`    } ` `catch` ` (error) {`

`      lastError = error ` `as`  ` `  `Error` `;`

`      `

`      ``// Don't retry on client errors (4xx)`

`      ` `if` ` (error.message.includes(` `'API error 4'` `)) {`

`        ` `throw` ` error;`

`      }`

`      `

`      ``// Retry on server errors (5xx) or network errors`

`      ` `if` ` (attempt < maxRetries) {`

`        ` `const` ` delay = ` `Math` `.pow(2, attempt) * 100;`

`        ` `await`  ` `  `new`  ` `  `Promise` `(resolve => setTimeout(resolve, delay));`

`      }`

`    }`

`  }`

`  `

`  ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `Failed after `` `${maxRetries}` ` retries: ` `${lastError!.message}`  `` ` `` `);`

`}`

**Comparison with AuthorizationHeader approach**

**Capability**

**/DownstreamApi**

**/AuthorizationHeader**

Token Acquisition

✅ Handled by SDK

✅ Handled by SDK

HTTP Request

✅ Handled by SDK

❌ Your responsibility

Response Parsing

⚠Wrapped in JSON

✅ Direct HTTP response

Custom Headers

⚠Via query parameters

✅ Full HTTP control

Request Body

✅ Forwarded automatically

✅ Full control

Error Handling

⚠SDK-wrapped errors

✅ Standard HTTP errors

**Use Case**

**Recommendation**

**Best For**

Standard REST API calls with

conventional patterns

`/DownstreamApi`

GET, POST, PUT, PATCH, DELETE

operations; reducing boilerplate

Complex HTTP clients requiring

custom configuration

`/AuthorizationHeader`

Specialized request/response handling;

fine-grained control

Direct access to HTTP error codes

and headers needed

`/AuthorizationHeader`

Applications needing low-level HTTP

behavior control

Simplicity and quick integration

prioritized

`/DownstreamApi`

Applications prioritizing simplicity over

low-level control

1\. **Reuse HTTP clients**: Create once and reuse to avoid connection overhead

2\. **Implement error handling**: Add retry logic for transient failures with exponential backoff

3\. **Check status codes**: Always verify the status code before parsing response content

4\. **Set timeouts**: Configure appropriate request timeouts to prevent hanging requests

5\. **Include correlation IDs**: Log all requests with unique identifiers for end-to-end tracing

6\. **Validate input**: Sanitize and validate data before sending to downstream APIs

7\. **Monitor performance**: Track API call latency and failure rates for observability

**Capabilities comparison**

ﾉ

**Expand table**

**When to use each approach**

ﾉ

**Expand table**

**Best practices**

Ready to integrate downstream API calls into your application?

1\. Integrate from TypeScript \- Full Node.js and Express.js integration examples

2\. Integrate from Python \- Flask and FastAPI integration examples

3\. Review Security \- Learn security hardening best practices for API calls

**Last updated on 11/14/2025**

**Next steps**

**Scenario: Obtain an Authorization Header**

Exchange incoming bearer tokens for authorization headers scoped to downstream APIs using

the Microsoft Entra SDK for AgentID's `/AuthorizationHeader` endpoint. This approach gives you

full control over HTTP requests while delegating token acquisition to the SDK.

An Azure account with an active subscription. Create an account for free

.

**Microsoft Entra SDK for AgentID** deployed and running in your environment. See

Installation Guide for setup instructions.

**Downstream API configured** in the SDK with the base URL and required scopes for token

exchange.

**Bearer tokens from authenticated clients** \- Your application receives tokens from client

applications that you'll exchange for downstream API tokens.

**Appropriate permissions in Microsoft Entra ID** \- Your account must have permissions to

register applications and grant API permissions.

Configure the downstream API in your Microsoft Entra SDK for AgentID with the base URL,

required scopes, and optional relative path:

YAML

Create a TypeScript function to call the Microsoft Entra SDK for AgentID and obtain an

authorization header. You can then use this header with your HTTP client to call downstream

APIs:

TypeScript

**Prerequisites**

**Configuration**

`env:`

`- name:`  ` `  `DownstreamApis__Graph__BaseUrl`

`  value:` ` ` `"https://graph.microsoft.com/v1.0"`

`- name:`  ` `  `DownstreamApis__Graph__Scopes`

`  value:` ` ` `"User.Read Mail.Read"`

**TypeScript/Node.js**

`import` ` fetch ` `from` ` ` `'node-fetch'` `;`

`interface` ` AuthHeaderResponse {`

The following example demonstrates how to integrate this function into an Express.js

application using middleware and route handlers:

JavaScript

`  authorizationHeader: ` `string` `;`

`}`

`async`  ` `  `function`  ` `  `getAuthorizationHeader` `(`

`  incomingToken: ` `string` `,`

`  serviceName: ` `string`

`): ` `Promise`  `<`  `string`  `> {`

`  ` `const` ` sidecarUrl = process.env.SIDECAR_URL || ``'http://localhost:5000'` `;`

`  `

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${sidecarUrl}` `/AuthorizationHeader/`  `${serviceName}`  `` ` `` `,`

`    {`

`      headers: {`

`        ``'Authorization'` `: incomingToken`

`      }`

`    }`

`  );`

`  `

`  ` `if` ` (!response.ok) {`

`    ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `Failed to get authorization header: `` `${response.statusText}`  `` ` `` `);`

`  }`

`  `

`  ` `const` ` data = ` `await` ` response.json() ` `as` ` AuthHeaderResponse;`

`  ` `return` ` data.authorizationHeader;`

`}`

`// Usage example`

`async`  ` `  `function`  ` `  `getUserProfile` `(incomingToken: ` `string` `) {`

`  ``// Get authorization header for Microsoft Graph`

`  ` `const` ` authHeader = ` `await` ` getAuthorizationHeader(incomingToken, ``'Graph'` `);`

`  `

`  ``// Use the authorization header to call Microsoft Graph`

`  ` `const` ` graphResponse = ` `await` ` fetch(`

`    ``'https://graph.microsoft.com/v1.0/me'` `,`

`    {`

`      headers: {`

`        ``'Authorization'` `: authHeader`

`      }`

`    }`

`  );`

`  `

`  ` `return`  ` `  `await` ` graphResponse.json();`

`}`

`// Express.js middleware example`

`import` ` express ` `from` ` ` `'express'` `;`

`const` ` app = express();`

The following snippet demonstrates a Python function that calls the Microsoft Entra SDK for

AgentID and obtains an authorization header.

Python

`app.get(` `'/api/profile'` `, ` `async` ` (req, res) => {`

`  ` `try` ` {`

`    ` `const` ` incomingToken = req.headers.authorization;`

`    ` `if` ` (!incomingToken) {`

`      ` `return` ` res.status(401).json({ ` `error` `: ``'No authorization token provided'` ` });`

`    }`

`    `

`    ` `const` ` profile = ` `await` ` getUserProfile(incomingToken);`

`    res.json(profile);`

`  } ` `catch` ` (error) {`

`    ` `console` `.error(` `'Error fetching profile:'` `, error);`

`    res.status(500).json({ ` `error` `: ``'Failed to fetch profile'` ` });`

`  }`

`});`

**Python**

`import` ` os`

`import` ` requests`

`from` ` typing ` `import` ` Dict, Any`

`def`  ` `  `get_authorization_header` `(incoming_token: str, service_name: str) -> str:`

`    ``"""Get an authorization header from the SDK."""`

`    sidecar_url = os.getenv(` `'SIDECAR_URL'` `, ``'http://localhost:5000'` `)`

`    `

`    response = requests.get(`

`        ` `f"` `{sidecar_url}` `/AuthorizationHeader/` `{service_name}` `"` `,`

`        headers={` `'Authorization'` `: incoming_token}`

`    )`

`    `

`    ` `if`  ` `  `not` ` response.ok:`

`        ` `raise` ` Exception(`  `f"Failed to get authorization header: ``{response.text}` `"` `)`

`    `

`    data = response.json()`

`    ` `return` ` data[` `'authorizationHeader'` `]`

`def`  ` `  `get_user_profile` `(incoming_token: str) -> Dict[str, Any]:`

`    ``"""Get user profile from Microsoft Graph."""`

`    ``# Get authorization header for Microsoft Graph`

`    auth_header = get_authorization_header(incoming_token, ``'Graph'` `)`

`    `

`    ``# Use the authorization header to call Microsoft Graph`

`    graph_response = requests.get(`

`        ``'https://graph.microsoft.com/v1.0/me'` `,`

`        headers={` `'Authorization'` `: auth_header}`

`    )`

If you want to integrate this function into a Flask application, you can use the following

example:

Python

The following demonstrates a Go function to call the Microsoft Entra SDK for AgentID and

obtain an authorization header. This implementation shows how to parse JSON responses and

use the header:

Go

`    `

`    ` `if`  ` `  `not` ` graph_response.ok:`

`        ` `raise` ` Exception(`  `f"Graph API error: ``{graph_response.text}` `"` `)`

`    `

`    ` `return` ` graph_response.json()`

`from` ` flask ` `import` ` Flask, request, jsonify`

`app = Flask(__name__)`

`@app.route('/api/profile')`

`def`  ` `  `profile` `():`

`    incoming_token = request.headers.get(` `'Authorization'` `)`

`    ` `if`  ` `  `not` ` incoming_token:`

`        ` `return` ` jsonify({` `'error'` `: ``'No authorization token provided'` `}), 401`

`    `

`    ` `try` `:`

`        profile_data = get_user_profile(incoming_token)`

`        ` `return` ` jsonify(profile_data)`

`    ` `except` ` Exception ` `as` ` e:`

`        print(`  `f"Error fetching profile: ``{e}` `"` `)`

`        ` `return` ` jsonify({` `'error'` `: ``'Failed to fetch profile'` `}), 500`

`if` ` __name__ == ``'__main__'` `:`

`    app.run(port=8080)`

**Go**

`package` ` main`

`import` ` (`

`    ``"encoding/json"`

`    ``"fmt"`

`    ``"io"`

`    ``"net/http"`

`    ``"os"`

`)`

`type` ` AuthHeaderResponse ` `struct` ` {`

`    AuthorizationHeader ` `string`  ` `  `` `json:"authorizationHeader"` ``

`}`

`type` ` UserProfile ` `struct` ` {`

`    DisplayName ` `string`  ` `  `` `json:"displayName"` ``

`    Mail        ` `string`  ` `  `` `json:"mail"` ``

`    UserPrincipalName ` `string`  ` `  `` `json:"userPrincipalName"` ``

`}`

`func`  ` `  `getAuthorizationHeader` `(incomingToken, serviceName ` `string` `) (`  `string` `, error) {`

`    sidecarURL := os.Getenv(` `"SIDECAR_URL"` `)`

`    ` `if` ` sidecarURL == ``""` ` {`

`        sidecarURL = ``"http://localhost:5000"`

`    }`

`    `

`    url := fmt.Sprintf(` `"%s/AuthorizationHeader/%s"` `, sidecarURL, serviceName)`

`    `

`    req, err := http.NewRequest(` `"GET"` `, url, ` `nil` `)`

`    ` `if` ` err != ` `nil` ` {`

`        ` `return` ` ` `""` `, err`

`    }`

`    `

`    req.Header.Set(` `"Authorization"` `, incomingToken)`

`    `

`    client := &http.Client{}`

`    resp, err := client.Do(req)`

`    ` `if` ` err != ` `nil` ` {`

`        ` `return` ` ` `""` `, err`

`    }`

`    ` `defer` ` resp.Body.Close()`

`    `

`    ` `if` ` resp.StatusCode != http.StatusOK {`

`        body, _ := io.ReadAll(resp.Body)`

`        ` `return` ` ` `""` `, fmt.Errorf(` `"failed to get authorization header: %s"` `, `

`string` `(body))`

`    }`

`    `

`    ` `var` ` authResp AuthHeaderResponse`

`    ` `if` ` err := json.NewDecoder(resp.Body).Decode(&authResp); err != ` `nil` ` {`

`        ` `return` ` ` `""` `, err`

`    }`

`    `

`    ` `return` ` authResp.AuthorizationHeader, ` `nil`

`}`

`func`  ` `  `getUserProfile` `(incomingToken ` `string` `) (*UserProfile, error) {`

`    ``// Get authorization header for Microsoft Graph`

`    authHeader, err := getAuthorizationHeader(incomingToken, ``"Graph"` `)`

`    ` `if` ` err != ` `nil` ` {`

`        ` `return`  ` `  `nil` `, err`

`    }`

`    `

`    ``// Use the authorization header to call Microsoft Graph`

`    req, err := http.NewRequest(` `"GET"` `, ``"https://graph.microsoft.com/v1.0/me"` `, ` `nil` `)`

`    ` `if` ` err != ` `nil` ` {`

`        ` `return`  ` `  `nil` `, err`

`    }`

`    `

`    req.Header.Set(` `"Authorization"` `, authHeader)`

`    `

`    client := &http.Client{}`

`    resp, err := client.Do(req)`

`    ` `if` ` err != ` `nil` ` {`

`        ` `return`  ` `  `nil` `, err`

`    }`

`    ` `defer` ` resp.Body.Close()`

`    `

`    ` `if` ` resp.StatusCode != http.StatusOK {`

`        body, _ := io.ReadAll(resp.Body)`

`        ` `return`  ` `  `nil` `, fmt.Errorf(` `"Graph API error: %s"` `, ` `string` `(body))`

`    }`

`    `

`    ` `var` ` profile UserProfile`

`    ` `if` ` err := json.NewDecoder(resp.Body).Decode(&profile); err != ` `nil` ` {`

`        ` `return`  ` `  `nil` `, err`

`    }`

`    `

`    ` `return` ` &profile, ` `nil`

`}`

`// HTTP handler example`

`func`  ` `  `profileHandler` `(w http.ResponseWriter, r *http.Request) {`

`    incomingToken := r.Header.Get(` `"Authorization"` `)`

`    ` `if` ` incomingToken == ``""` ` {`

`        http.Error(w, ``"No authorization token provided"` `, http.StatusUnauthorized)`

`        ` `return`

`    }`

`    `

`    profile, err := getUserProfile(incomingToken)`

`    ` `if` ` err != ` `nil` ` {`

`        fmt.Printf(` `"Error fetching profile: %v\n"` `, err)`

`        http.Error(w, ``"Failed to fetch profile"` `, http.StatusInternalServerError)`

`        ` `return`

`    }`

`    `

`    w.Header().Set(` `"Content-Type"` `, ``"application/json"` `)`

`    json.NewEncoder(w).Encode(profile)`

`}`

`func`  ` `  `main` `() {`

`    http.HandleFunc(` `"/api/profile"` `, profileHandler)`

`    fmt.Println(` `"Server starting on :8080"` `)`

`    http.ListenAndServe(` `":8080"` `, ` `nil` `)`

`}`

**C# implementation**

Create a C# class to call the Microsoft Entra SDK for AgentID and obtain an authorization

header. This implementation uses ASP.NET Core's dependency injection:

C#

`using` ` System;`

`using` ` System.Net.Http;`

`using` ` System.Net.Http.Json;`

`using` ` System.Threading.Tasks;`

`using` ` Microsoft.AspNetCore.Mvc;`

`public`  ` `  `class`  ` `  `SidecarClient`

`{`

`    ` `private`  ` `  `readonly` ` HttpClient _httpClient;`

`    ` `private`  ` `  `readonly`  ` `  `string` ` _sidecarUrl;`

`    `

`    ` `public`  ` `  `SidecarClient` `(IHttpClientFactory httpClientFactory, IConfiguration `

`config)`

`    {`

`        _httpClient = httpClientFactory.CreateClient();`

`        _sidecarUrl = config[` `"SIDECAR_URL"` `] ?? ``"http://localhost:5000"` `;`

`    }`

`    `

`    ` `public`  ` `  `async` ` Task<`  `string`  `> ` `GetAuthorizationHeaderAsync` `(`

`        ` `string` ` incomingAuthorizationHeader, `

`        ` `string` ` serviceName)`

`    {`

`        ` `var` ` request = ` `new` ` HttpRequestMessage(`

`            HttpMethod.Get,`

`            ` `$"` `{_sidecarUrl}` `/AuthorizationHeader/` `{serviceName}` `"`

`        );`

`        `

`        request.Headers.Add(` `"Authorization"` `, incomingAuthorizationHeader);`

`        `

`        ` `var` ` response = ` `await` ` _httpClient.SendAsync(request);`

`        response.EnsureSuccessStatusCode();`

`        `

`        ` `var` ` result = ` `await` ` response.Content.ReadFromJsonAsync<AuthHeaderResponse>();`

`        ` `return` ` result.AuthorizationHeader;`

`    }`

`}`

`public`  ` `  `record`  ` `  `AuthHeaderResponse` `(`  `string` ` AuthorizationHeader);`

`public`  ` `  `record`  ` `  `UserProfile` `(`  `string` ` DisplayName, ` `string` ` Mail, ` `string` ` `

`UserPrincipalName);`

`// Controller example`

`[`  `ApiController` `]`

`[`  `Route(` `"api/[controller]"` `)` `]`

`public`  ` `  `class`  ` `  `ProfileController` ` : ` `ControllerBase`

`{`

`    ` `private`  ` `  `readonly` ` SidecarClient _sidecarClient;`

`    ` `private`  ` `  `readonly` ` HttpClient _httpClient;`

The Microsoft Entra SDK for AgentID supports several advanced patterns through query

parameters:

`    `

`    ` `public`  ` `  `ProfileController` `(SidecarClient sidecarClient, IHttpClientFactory `

`httpClientFactory)`

`    {`

`        _sidecarClient = sidecarClient;`

`        _httpClient = httpClientFactory.CreateClient();`

`    }`

`    `

`    [`  `HttpGet` `]`

`    ` `public`  ` `  `async` ` Task<ActionResult<UserProfile>> GetProfile()`

`    {`

`        ` `var` ` incomingToken = Request.Headers[` `"Authorization"` `].ToString();`

`        ` `if` ` (`  `string` `.IsNullOrEmpty(incomingToken))`

`        {`

`            ` `return` ` Unauthorized(` `"No authorization token provided"` `);`

`        }`

`        `

`        ` `try`

`        {`

`            ``// Get authorization header for Microsoft Graph`

`            ` `var` ` authHeader = ` `await` ` _sidecarClient.GetAuthorizationHeaderAsync(`

`                incomingToken, `

`                ``"Graph"`

`            );`

`            `

`            ``// Use the authorization header to call Microsoft Graph`

`            ` `var` ` request = ` `new` ` HttpRequestMessage(`

`                HttpMethod.Get,`

`                ``"https://graph.microsoft.com/v1.0/me"`

`            );`

`            request.Headers.Add(` `"Authorization"` `, authHeader);`

`            `

`            ` `var` ` response = ` `await` ` _httpClient.SendAsync(request);`

`            response.EnsureSuccessStatusCode();`

`            `

`            ` `var` ` profile = ` `await` ` response.Content.ReadFromJsonAsync<UserProfile>();`

`            ` `return` ` Ok(profile);`

`        }`

`        catch (Exception ex)`

`        {`

`            ` `return` ` StatusCode(500, ` `$"Failed to fetch profile: ``{ex.Message}` `"` `);`

`        }`

`    }`

`}`

**Advanced scenarios**

**Override scopes**

Request specific scopes different from configuration:

TypeScript

Override tenant for specific user:

TypeScript

Request an application token instead of OBO:

TypeScript

Use agent identity for delegation:

TypeScript

`const` ` response = ` `await` ` fetch(`

`  ` `` ` ``  `${sidecarUrl}` ``/AuthorizationHeader/Graph?` `` ` +`

`  ` `` `optionsOverride.Scopes=User.Read&` `` ` +`

`  ` `` `optionsOverride.Scopes=Mail.Send` `` `,`

`  {`

`    headers: { ``'Authorization'` `: incomingToken }`

`  }`

`);`

**Multi-tenant support**

`const` ` response = ` `await` ` fetch(`

`  ` `` ` ``  `${sidecarUrl}` ``/AuthorizationHeader/Graph?` `` ` +`

`  ` `` `optionsOverride.AcquireTokenOptions.Tenant=``  `${userTenantId}`  `` ` `` `,`

`  {`

`    headers: { ``'Authorization'` `: incomingToken }`

`  }`

`);`

**Request application token**

`const` ` response = ` `await` ` fetch(`

`  ` `` ` ``  `${sidecarUrl}` ``/AuthorizationHeader/Graph?` `` ` +`

`  ` `` `optionsOverride.RequestAppToken=true` `` `,`

`  {`

`    headers: { ``'Authorization'` `: incomingToken }`

`  }`

`);`

**With agent identity**

Implement proper error handling when calling the Microsoft Entra SDK for AgentID to

distinguish between transient and permanent failures:

Implement retry logic with exponential backoff for transient failures:

TypeScript

`const` ` response = ` `await` ` fetch(`

`  ` `` ` ``  `${sidecarUrl}` ``/AuthorizationHeader/Graph?` `` ` +`

`  ` `` `AgentIdentity=``  `${agentClientId}` ``&` `` ` +`

`  ` `` `AgentUsername=``  `${`  `encodeURIComponent` `(userPrincipalName)}`  `` ` `` `,`

`  {`

`    headers: { ``'Authorization'` `: incomingToken }`

`  }`

`);`

**Error handling**

**Handle transient errors**

`async`  ` `  `function`  ` `  `getAuthorizationHeaderWithRetry` `(`

`  incomingToken: ` `string` `,`

`  serviceName: ` `string` `,`

`  maxRetries = 3`

`): ` `Promise`  `<`  `string`  `> {`

`  ` `let` ` lastError: ` `Error` `;`

`  `

`  ` `for` ` (`  `let` ` attempt = 1; attempt <= maxRetries; attempt++) {`

`    ` `try` ` {`

`      ` `const` ` response = ` `await` ` fetch(`

`        ` `` ` ``  `${sidecarUrl}` `/AuthorizationHeader/`  `${serviceName}`  `` ` `` `,`

`        {`

`          headers: { ``'Authorization'` `: incomingToken }`

`        }`

`      );`

`      `

`      ` `if` ` (response.ok) {`

`        ` `const` ` data = ` `await` ` response.json();`

`        ` `return` ` data.authorizationHeader;`

`      }`

`      `

`      ``// Don't retry on 4xx errors (client errors)`

`      ` `if` ` (response.status >= 400 && response.status < 500) {`

`        ` `const` ` error = ` `await` ` response.json();`

`        ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `Client error: `` `${error.detail || response.statusText}`  `` ` `` `);`

`      }`

`      `

`      ``// Retry on 5xx errors (server errors)`

`      lastError = ` `new`  ` `  `Error` `(`  `` `Server error: `` `${response.statusText}`  `` ` `` `);`

`      `

When obtaining authorization headers from the Microsoft Entra SDK for AgentID, follow these

practices:

**Reuse HTTP Clients**: Create a single HTTP client instance and reuse it across requests

rather than creating new clients per call. This improves performance and enables

connection pooling.

**Handle Errors Gracefully**: Implement retry logic for transient failures (5xx errors) but fail

immediately on client errors (4xx responses) that indicate configuration problems.

**Set Appropriate Timeouts**: Configure timeouts for SDK calls based on expected latency.

This prevents your application from hanging if the SDK is unresponsive.

**Cache Authorization Headers**: Cache returned headers for their lifetime to reduce

unnecessary calls to the SDK. Respect the token's expiration time when caching.

**Log Correlation IDs**: Include correlation IDs from SDK responses in your logs to enable

request tracing across system boundaries.

**Validate Responses**: Always check response status codes and validate that required fields

are present before using the authorization header.

Call Downstream API

Use Managed Identity

Implement Long-Running OBO

`      ` `if` ` (attempt < maxRetries) {`

`        ``// Exponential backoff`

`        ` `await`  ` `  `new`  ` `  `Promise` `(resolve => `

`          setTimeout(resolve, ` `Math` `.pow(2, attempt) * 100)`

`        );`

`      }`

`    } ` `catch` ` (error) {`

`      lastError = error ` `as`  ` `  `Error` `;`

`      ` `if` ` (attempt < maxRetries) {`

`        ` `await`  ` `  `new`  ` `  `Promise` `(resolve => `

`          setTimeout(resolve, ` `Math` `.pow(2, attempt) * 100)`

`        );`

`      }`

`    }`

`  }`

`  `

`  ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `Failed after `` `${maxRetries}` ` retries: ` `${lastError.message}`  `` ` `` `);`

`}`

**Best practices**

**Next steps**

**Last updated on 11/14/2025**

**Scenario: Validate an Authorization Header**

Validate incoming bearer tokens by forwarding them to the Microsoft Entra SDK for AgentID's

`/Validate` endpoint, then extract the returned claims to make authorization decisions. This

guide shows you how to implement token validation middleware and make authorization

decisions based on scopes or roles.

An Azure account with an active subscription. Create an account for free

.

**Microsoft Entra SDK for AgentID** deployed and running with network access from your

application. See Installation Guide for setup instructions.

**Registered application in Microsoft Entra ID** \- Register a new app in the Microsoft Entra

admin center

, configured for _Accounts in this organizational directory only_. Refer to

Register an application for more details. Record the following values from the application

**Overview** page:

Application (client) ID

Directory (tenant) ID

Configure an **App ID URI** in the **Expose an API** section (used as the audience for token

validation)

**Bearer tokens from authenticated clients** \- Your application must receive tokens from

client applications through OAuth 2.0 flows.

**Appropriate permissions in Microsoft Entra ID** \- Your account must have permissions to

register applications and configure authentication settings.

To validate tokens for your API, configure the Microsoft Entra SDK for AgentID with your

Microsoft Entra ID tenant information.

YAML

**Prerequisites**

**Configuration**

`env:`

`- name:`  ` `  `AzureAd__Instance`

`  value:` ` ` `"https://login.microsoftonline.com/"`

`- name:`  ` `  `AzureAd__TenantId`

`  value:` ` ` `"your-tenant-id"`

`- name:`  ` `  `AzureAd__ClientId`

`  value:` ` ` `"your-api-client-id"`

`- name:`  ` `  `AzureAd__Audience`

`  value:` ` ` `"api://your-api-id"`

The following implementation shows how to create a token validation middleware that

integrates with the Microsoft Entra SDK for AgentID using TypeScript or JavaScript. This

middleware checks every incoming request for a valid bearer token and extracts claims for use

in your route handlers:

TypeScript

The following snippet demonstrates how to use the `validateToken` function in an Express.js

middleware to protect API endpoints:

JavaScript

**TypeScript/Node.js**

`import` ` fetch ` `from` ` ` `'node-fetch'` `;`

`interface` ` ValidateResponse {`

`  protocol: ` `string` `;`

`  token: ` `string` `;`

`  claims: {`

`    aud: ` `string` `;`

`    iss: ` `string` `;`

`    oid: ` `string` `;`

`    sub: ` `string` `;`

`    tid: ` `string` `;`

`    upn?: ` `string` `;`

`    scp?: ` `string` `;`

`    roles?: ` `string` `[];`

`    [key: ` `string` `]: ` `any` `;`

`  };`

`}`

`async`  ` `  `function`  ` `  `validateToken` `(authorizationHeader: ` `string` `): ` `Promise`  `<`  `ValidateResponse`  `> `

`{`

`  ` `const` ` sidecarUrl = process.env.SIDECAR_URL || ``'http://localhost:5000'` `;`

`  `

`  ` `const` ` response = ` `await` ` fetch(`  `` ` ``  `${sidecarUrl}` ``/Validate` `` `, {`

`    headers: {`

`      ``'Authorization'` `: authorizationHeader`

`    }`

`  });`

`  `

`  ` `if` ` (!response.ok) {`

`    ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `Token validation failed: `` `${response.statusText}`  `` ` `` `);`

`  }`

`  `

`  ` `return`  ` `  `await` ` response.json() ` `as` ` ValidateResponse;`

`}`

`// Express.js middleware example`

`import` ` express ` `from` ` ` `'express'` `;`

`const` ` app = express();`

`// Token validation middleware`

`async`  ` `  `function`  ` `  `requireAuth` `(req, res, next) {`

`  ` `const` ` authHeader = req.headers.authorization;`

`  `

`  ` `if` ` (!authHeader) {`

`    ` `return` ` res.status(401).json({ ` `error` `: ``'No authorization token provided'` ` });`

`  }`

`  `

`  ` `try` ` {`

`    ` `const` ` validation = ` `await` ` validateToken(authHeader);`

`    `

`    ``// Attach claims to request object`

`    req.user = {`

`      ` `id` `: validation.claims.oid,`

`      ` `upn` `: validation.claims.upn,`

`      ` `tenantId` `: validation.claims.tid,`

`      ` `scopes` `: validation.claims.scp?.split(` `' '` `) || [],`

`      ` `roles` `: validation.claims.roles || [],`

`      ` `claims` `: validation.claims`

`    };`

`    `

`    next();`

`  } ` `catch` ` (error) {`

`    ` `console` `.error(` `'Token validation failed:'` `, error);`

`    ` `return` ` res.status(401).json({ ` `error` `: ``'Invalid token'` ` });`

`  }`

`}`

`// Protected endpoint`

`app.get(` `'/api/protected'` `, requireAuth, (req, res) => {`

`  res.json({`

`    ` `message` `: ``'Access granted'` `,`

`    ` `user` `: {`

`      ` `id` `: req.user.id,`

`      ` `upn` `: req.user.upn`

`    }`

`  });`

`});`

`// Scope-based authorization`

`app.get(` `'/api/admin'` `, requireAuth, (req, res) => {`

`  ` `if` ` (!req.user.roles.includes(` `'Admin'` `)) {`

`    ` `return` ` res.status(403).json({ ` `error` `: ``'Insufficient permissions'` ` });`

`  }`

`  `

`  res.json({ ` `message` `: ``'Admin access granted'` ` });`

`});`

`app.listen(8080);`

The following Python snippet uses Flask decorators to wrap route handlers with token

validation. This decorator extracts the bearer token from the Authorization header, validates it

with the Microsoft Entra SDK for AgentID, and makes the claims available in your route:

Python

**Python**

`import` ` os`

`import` ` requests`

`from` ` flask ` `import` ` Flask, request, jsonify`

`from` ` functools ` `import` ` wraps`

`app = Flask(__name__)`

`def`  ` `  `validate_token` `(authorization_header: str) -> dict:`

`    ``"""Validate token using the SDK."""`

`    sidecar_url = os.getenv(` `'SIDECAR_URL'` `, ``'http://localhost:5000'` `)`

`    `

`    response = requests.get(`

`        ` `f"` `{sidecar_url}` `/Validate"` `,`

`        headers={` `'Authorization'` `: authorization_header}`

`    )`

`    `

`    ` `if`  ` `  `not` ` response.ok:`

`        ` `raise` ` Exception(`  `f"Token validation failed: ``{response.text}` `"` `)`

`    `

`    ` `return` ` response.json()`

`# Token validation decorator`

`def`  ` `  `require_auth` `(f):`

`    @wraps(f)`

`    ` `def`  ` `  `decorated_function` `(*args, **kwargs):`

`        auth_header = request.headers.get(` `'Authorization'` `)`

`        `

`        ` `if`  ` `  `not` ` auth_header:`

`            ` `return` ` jsonify({` `'error'` `: ``'No authorization token provided'` `}), 401`

`        `

`        ` `try` `:`

`            validation = validate_token(auth_header)`

`            `

`            ``# Attach user info to Flask's g object`

`            ` `from` ` flask ` `import` ` g`

`            g.user = {`

`                ``'id'` `: validation[` `'claims'` `][` `'oid'` `],`

`                ``'upn'` `: validation[` `'claims'` `].get(` `'upn'` `),`

`                ``'tenant_id'` `: validation[` `'claims'` `][` `'tid'` `],`

`                ``'scopes'` `: validation[` `'claims'` `].get(` `'scp'` `, ``''` `).split(` `' '` `),`

`                ``'roles'` `: validation[` `'claims'` `].get(` `'roles'` `, []),`

`                ``'claims'` `: validation[` `'claims'` `]`

`            }`

`            `

The following Go implementation demonstrates token validation using the standard HTTP

handler pattern. This middleware approach extracts bearer tokens from the Authorization

header, validates them with the Microsoft Entra SDK for AgentID, and stores user information

in request headers for use in downstream handlers:

Go

`            ` `return` ` f(*args, **kwargs)`

`        ` `except` ` Exception ` `as` ` e:`

`            print(`  `f"Token validation failed: ``{e}` `"` `)`

`            ` `return` ` jsonify({` `'error'` `: ``'Invalid token'` `}), 401`

`    `

`    ` `return` ` decorated_function`

`# Protected endpoint`

`@app.route('/api/protected')`

`@require_auth`

`def`  ` `  `protected` `():`

`    ` `from` ` flask ` `import` ` g`

`    ` `return` ` jsonify({`

`        ``'message'` `: ``'Access granted'` `,`

`        ``'user'` `: {`

`            ``'id'` `: g.user[` `'id'` `],`

`            ``'upn'` `: g.user[` `'upn'` `]`

`        }`

`    })`

`# Role-based authorization`

`@app.route('/api/admin')`

`@require_auth`

`def`  ` `  `admin` `():`

`    ` `from` ` flask ` `import` ` g`

`    ` `if` ` ` `'Admin'`  ` `  `not`  ` `  `in` ` g.user[` `'roles'` `]:`

`        ` `return` ` jsonify({` `'error'` `: ``'Insufficient permissions'` `}), 403`

`    `

`    ` `return` ` jsonify({` `'message'` `: ``'Admin access granted'` `})`

`if` ` __name__ == ``'__main__'` `:`

`    app.run(port=8080)`

**Go**

`package` ` main`

`import` ` (`

`    ``"encoding/json"`

`    ``"fmt"`

`    ``"net/http"`

`    ``"os"`

`    ``"strings"`

`)`

`type` ` ValidateResponse ` `struct` ` {`

`    Protocol ` `string`  `                 `  `` `json:"protocol"` ``

`    Token    ` `string`  `                 `  `` `json:"token"` ``

`    Claims   ` `map` `[`  `string` `]`  `interface` `{} ` `` `json:"claims"` ``

`}`

`type` ` User ` `struct` ` {`

`    ID       ` `string`

`    UPN      ` `string`

`    TenantID ` `string`

`    Scopes   []`  `string`

`    Roles    []`  `string`

`    Claims   ` `map` `[`  `string` `]`  `interface` `{}`

`}`

`func`  ` `  `validateToken` `(authHeader ` `string` `) (*ValidateResponse, error) {`

`    sidecarURL := os.Getenv(` `"SIDECAR_URL"` `)`

`    ` `if` ` sidecarURL == ``""` ` {`

`        sidecarURL = ``"http://localhost:5000"`

`    }`

`    `

`    req, err := http.NewRequest(` `"GET"` `, fmt.Sprintf(` `"%s/Validate"` `, sidecarURL), ` `nil` `)`

`    ` `if` ` err != ` `nil` ` {`

`        ` `return`  ` `  `nil` `, err`

`    }`

`    `

`    req.Header.Set(` `"Authorization"` `, authHeader)`

`    `

`    client := &http.Client{}`

`    resp, err := client.Do(req)`

`    ` `if` ` err != ` `nil` ` {`

`        ` `return`  ` `  `nil` `, err`

`    }`

`    ` `defer` ` resp.Body.Close()`

`    `

`    ` `if` ` resp.StatusCode != http.StatusOK {`

`        ` `return`  ` `  `nil` `, fmt.Errorf(` `"token validation failed: %s"` `, resp.Status)`

`    }`

`    `

`    ` `var` ` validation ValidateResponse`

`    ` `if` ` err := json.NewDecoder(resp.Body).Decode(&validation); err != ` `nil` ` {`

`        ` `return`  ` `  `nil` `, err`

`    }`

`    `

`    ` `return` ` &validation, ` `nil`

`}`

`// Middleware for token validation`

`func`  ` `  `requireAuth` `(next http.HandlerFunc) ` `http` `.`  `HandlerFunc` ` {`

`    ` `return`  ` `  `func` `(w http.ResponseWriter, r *http.Request) {`

`        authHeader := r.Header.Get(` `"Authorization"` `)`

`        `

`        ` `if` ` authHeader == ``""` ` {`

`            http.Error(w, ``"No authorization token provided"` `, `

`http.StatusUnauthorized)`

`            ` `return`

`        }`

`        `

`        validation, err := validateToken(authHeader)`

`        ` `if` ` err != ` `nil` ` {`

`            http.Error(w, ``"Invalid token"` `, http.StatusUnauthorized)`

`            ` `return`

`        }`

`        `

`        ``// Extract user information from claims`

`        user := &User{`

`            ID:       validation.Claims[` `"oid"` `].(`  `string` `),`

`            TenantID: validation.Claims[` `"tid"` `].(`  `string` `),`

`            Claims:   validation.Claims,`

`        }`

`        `

`        ` `if` ` upn, ok := validation.Claims[` `"upn"` `].(`  `string` `); ok {`

`            user.UPN = upn`

`        }`

`        `

`        ` `if` ` scp, ok := validation.Claims[` `"scp"` `].(`  `string` `); ok {`

`            user.Scopes = strings.Split(scp, ``" "` `)`

`        }`

`        `

`        ` `if` ` roles, ok := validation.Claims[` `"roles"` `].([]`  `interface` `{}); ok {`

`            ` `for` ` _, role := ` `range` ` roles {`

`                user.Roles = ` `append` `(user.Roles, role.(`  `string` `))`

`            }`

`        }`

`        `

`        ``// Store user in context (simplified - use context.Context in production)`

`        r.Header.Set(` `"X-User-ID"` `, user.ID)`

`        r.Header.Set(` `"X-User-UPN"` `, user.UPN)`

`        `

`        next(w, r)`

`    }`

`}`

`func`  ` `  `protectedHandler` `(w http.ResponseWriter, r *http.Request) {`

`    w.Header().Set(` `"Content-Type"` `, ``"application/json"` `)`

`    json.NewEncoder(w).Encode(`  `map` `[`  `string` `]`  `interface` `{}{`

`        ``"message"` `: ``"Access granted"` `,`

`        ``"user"` `: ` `map` `[`  `string` `]`  `string` `{`

`            ``"id"` `:  r.Header.Get(` `"X-User-ID"` `),`

`            ``"upn"` `: r.Header.Get(` `"X-User-UPN"` `),`

`        },`

`    })`

`}`

`func`  ` `  `main` `() {`

`    http.HandleFunc(` `"/api/protected"` `, requireAuth(protectedHandler))`

`    `

`    fmt.Println(` `"Server starting on :8080"` `)`

The following C# implementation demonstrates token validation using ASP.NET Core

middleware. This approach uses dependency injection to access the token validation service,

extracts bearer tokens from the Authorization header, validates them with the Microsoft Entra

SDK for AgentID, and stores user claims in the HttpContext for use in controllers:

C#

`    http.ListenAndServe(` `":8080"` `, ` `nil` `)`

`}`

**C#**

`using` ` Microsoft.AspNetCore.Mvc;`

`using` ` System.Net.Http;`

`using` ` System.Net.Http.Json;`

`using` ` System.Text.Json;`

`public`  ` `  `class`  ` `  `ValidateResponse`

`{`

`    ` `public`  ` `  `string` ` Protocol { ` `get` `; ` `set` `; }`

`    ` `public`  ` `  `string` ` Token { ` `get` `; ` `set` `; }`

`    ` `public` ` JsonElement Claims { ` `get` `; ` `set` `; }`

`}`

`public`  ` `  `class`  ` `  `TokenValidationService`

`{`

`    ` `private`  ` `  `readonly` ` HttpClient _httpClient;`

`    ` `private`  ` `  `readonly`  ` `  `string` ` _sidecarUrl;`

`    `

`    ` `public`  ` `  `TokenValidationService` `(IHttpClientFactory httpClientFactory, `

`IConfiguration config)`

`    {`

`        _httpClient = httpClientFactory.CreateClient();`

`        _sidecarUrl = config[` `"SIDECAR_URL"` `] ?? ``"http://localhost:5000"` `;`

`    }`

`    `

`    ` `public`  ` `  `async` ` Task<ValidateResponse> ` `ValidateTokenAsync` `(`  `string` ` `

`authorizationHeader)`

`    {`

`        ` `var` ` request = ` `new` ` HttpRequestMessage(HttpMethod.Get, ` `$"`

`{_sidecarUrl}` `/Validate"` `);`

`        request.Headers.Add(` `"Authorization"` `, authorizationHeader);`

`        `

`        ` `var` ` response = ` `await` ` _httpClient.SendAsync(request);`

`        response.EnsureSuccessStatusCode();`

`        `

`        ` `return`  ` `  `await` ` response.Content.ReadFromJsonAsync<ValidateResponse>();`

`    }`

`}`

`// Middleware example`

`public`  ` `  `class`  ` `  `TokenValidationMiddleware`

`{`

`    ` `private`  ` `  `readonly` ` RequestDelegate _next;`

`    ` `private`  ` `  `readonly` ` TokenValidationService _validationService;`

`    `

`    ` `public`  ` `  `TokenValidationMiddleware` `(RequestDelegate next, TokenValidationService `

`validationService)`

`    {`

`        _next = next;`

`        _validationService = validationService;`

`    }`

`    `

`    ` `public`  ` `  `async` ` Task ` `InvokeAsync` `(HttpContext context)`

`    {`

`        ` `var` ` authHeader = context.Request.Headers[` `"Authorization"` `].ToString();`

`        `

`        ` `if` ` (`  `string` `.IsNullOrEmpty(authHeader))`

`        {`

`            context.Response.StatusCode = 401;`

`            ` `await` ` context.Response.WriteAsJsonAsync(`  `new` ` { error = ``"No authorization `

`token"` ` });`

`            ` `return` `;`

`        }`

`        `

`        ` `try`

`        {`

`            ` `var` ` validation = ` `await` ` `

`_validationService.ValidateTokenAsync(authHeader);`

`            `

`            ``// Store claims in HttpContext.Items for use in controllers`

`            context.Items[` `"UserClaims"` `] = validation.Claims;`

`            context.Items[` `"UserId"` `] = `

`validation.Claims.GetProperty(` `"oid"` `).GetString();`

`            `

`            ` `await` ` _next(context);`

`        }`

`        catch (Exception ex)`

`        {`

`            context.Response.StatusCode = 401;`

`            ` `await` ` context.Response.WriteAsJsonAsync(`  `new` ` { error = ``"Invalid token"` ` `

`});`

`        }`

`    }`

`}`

`// Controller example`

`[`  `ApiController` `]`

`[`  `Route(` `"api"` `)` `]`

`public`  ` `  `class`  ` `  `ProtectedController` ` : ` `ControllerBase`

`{`

`    [`  `HttpGet(` `"protected"` `)` `]`

`    ` `public` ` IActionResult ` `GetProtected` `()`

`    {`

`        ` `var` ` userId = HttpContext.Items[` `"UserId"` `] ` `as`  ` `  `string` `;`

`        `

After validating a token, you can extract the claims to make authorization decisions in your

application. The `/Validate` endpoint returns a claims object with the following information:

JSON

**Common claims include:**

`oid` : Object identifier (unique user ID) in your Microsoft Entra ID tenant

`upn` : User principal name (typically email format)

`tid` : Tenant ID where the user belongs

`scp` : Delegated scopes the user granted to your application

`roles` : Application roles assigned to the user

The following examples show how to extract specific claims from the validation response:

**User Identity**:

TypeScript

**Scopes and Roles**:

`        ` `return` ` Ok(`  `new`

`        {`

`            message = ``"Access granted"` `,`

`            user = ` `new` ` { id = userId }`

`        });`

`    }`

`}`

**Extracting specific claims**

`{`

`  ``"protocol"` `: ``"Bearer"` `,`

`  ``"claims"` `: {`

`    ``"oid"` `: ``"user-object-id"` `,`

`    ``"upn"` `: ``"user@contoso.com"` `,`

`    ``"tid"` `: ``"tenant-id"` `,`

`    ``"scp"` `: ``"User.Read Mail.Read"` `,`

`    ``"roles"` `: [` `"Admin"` `]`

`  }`

`}`

`// Extract user identity`

`const` ` userId = validation.claims.oid;  ``// Object ID`

`const` ` userPrincipalName = validation.claims.upn;  ``// User Principal Name`

`const` ` tenantId = validation.claims.tid;  ``// Tenant ID`

TypeScript

After validating tokens, you can enforce authorization based on either delegated scopes

(permissions granted by the user) or application roles (assigned by your tenant administrator).

Choose the pattern that matches your authorization model:

Check if the user token includes required scopes before granting access:

TypeScript

`// Extract scopes (delegated permissions)`

`const` ` scopes = validation.claims.scp?.split(` `' '` `) || [];`

`// Check for specific scope`

`if` ` (scopes.includes(` `'User.Read'` `)) {`

`  ``// Allow access`

`}`

`// Extract roles (application permissions)`

`const` ` roles = validation.claims.roles || [];`

`// Check for specific role`

`if` ` (roles.includes(` `'Admin'` `)) {`

`  ``// Allow admin access`

`}`

**Authorization patterns**

**Scope-based authorization**

`function`  ` `  `requireScopes` `(requiredScopes: ` `string` `[]) {`

`  ` `return`  ` `  `async` ` (req, res, next) => {`

`    ` `const` ` validation = ` `await` ` validateToken(req.headers.authorization);`

`    ` `const` ` userScopes = validation.claims.scp?.split(` `' '` `) || [];`

`    ` `const` ` hasAllScopes = requiredScopes.every(s => userScopes.includes(s));`

`    `

`    ` `if` ` (!hasAllScopes) {`

`      ` `return` ` res.status(403).json({ error: ``'Insufficient scopes'` ` });`

`    }`

`    next();`

`  };`

`}`

`app.get(` `'/api/mail'` `, requireScopes([` `'Mail.Read'` `]), (req, res) => {`

`  res.json({ message: ``'Mail access granted'` ` });`

`});`

**Role-based authorization**

Check if the user has required application roles:

TypeScript

Token validation can fail for several reasons: the token may be expired, invalid, or missing

required scopes. Implement error handling that distinguishes between different failure

scenarios so you can respond appropriately:

TypeScript

`function`  ` `  `requireRoles` `(requiredRoles: ` `string` `[]) {`

`  ` `return`  ` `  `async` ` (req, res, next) => {`

`    ` `const` ` validation = ` `await` ` validateToken(req.headers.authorization);`

`    ` `const` ` userRoles = validation.claims.roles || [];`

`    ` `const` ` hasRole = requiredRoles.some(r => userRoles.includes(r));`

`    `

`    ` `if` ` (!hasRole) {`

`      ` `return` ` res.status(403).json({ error: ``'Insufficient permissions'` ` });`

`    }`

`    next();`

`  };`

`}`

`app.delete(` `'/api/resource'` `, requireRoles([` `'Admin'` `]), (req, res) => {`

`  res.json({ message: ``'Resource deleted'` ` });`

`});`

**Error handling**

`async`  ` `  `function`  ` `  `validateTokenSafely` `(authHeader: ` `string` `): ` `Promise`  `<`  `ValidateResponse` ` | `

`null`  `> {`

`  ` `try` ` {`

`    ` `return`  ` `  `await` ` validateToken(authHeader);`

`  } ` `catch` ` (error) {`

`    ` `if` ` (error.message.includes(` `'401'` `)) {`

`      ` `console` `.error(` `'Token is invalid or expired'` `);`

`    } ` `else`  ` `  `if` ` (error.message.includes(` `'403'` `)) {`

`      ` `console` `.error(` `'Token missing required scopes'` `);`

`    } ` `else` ` {`

`      ` `console` `.error(` `'Token validation error:'` `, error.message);`

`    }`

`    ` `return`  ` `  `null` `;`

`  }`

`}`

**Common Validation Errors**

**Error**

**Cause**

**Solution**

401 Unauthorized

Invalid or expired token

Request new token from client

403 Forbidden

Missing required scopes

Update scope configuration or token request

400 Bad Request

Malformed authorization header

Check header format: `******`

The `/Validate` endpoint returns:

JSON

1\. **Validate Early**: Validate tokens at the API gateway or entry point

2\. **Check Scopes**: Always verify token has required scopes for the operation

3\. **Log Failures**: Log validation failures for security monitoring

4\. **Handle Errors**: Provide clear error messages for debugging

5\. **Use Middleware**: Implement validation as middleware for consistency

6\. **Secure SDK**: Ensure the SDK is only accessible from your application

ﾉ

**Expand table**

**Response Structure**

`{`

`  ``"protocol"` `: ``"Bearer"` `,`

`  ``"token"` `: ``"******"` `,`

`  ``"claims"` `: {`

`    ``"aud"` `: ``"api://your-api-id"` `,`

`    ``"iss"` `: ``"https://sts.windows.net/tenant-id/"` `,`

`    ``"iat"` `: 1234567890,`

`    ``"nbf"` `: 1234567890,`

`    ``"exp"` `: 1234571490,`

`    ``"oid"` `: ``"user-object-id"` `,`

`    ``"sub"` `: ``"subject"` `,`

`    ``"tid"` `: ``"tenant-id"` `,`

`    ``"upn"` `: ``"user@contoso.com"` `,`

`    ``"scp"` `: ``"User.Read Mail.Read"` `,`

`    ``"roles"` `: [` `"Admin"` `]`

`  }`

`}`

**Best Practices**

**Next steps**

After validating tokens, you may need to:

Obtain tokens for downstream APIs

Call downstream APIs directly

Implement agent identities

**Last updated on 11/14/2025**

**Scenario: Using the Microsoft Entra SDK for**

**AgentID from TypeScript**

Create a TypeScript/Node.js client library that integrates with the Microsoft Entra SDK for

AgentID to obtain tokens and call downstream APIs. Then integrate this client into Express.js or

NestJS applications to handle authenticated API requests.

An Azure account with an active subscription. Create an account for free

.

**Node.js** (version 14 or later) with npm installed on your development machine.

**Microsoft Entra SDK for AgentID** deployed and running in your environment. See

Installation Guide for setup instructions.

**Downstream APIs configured** in the SDK with base URLs and required scopes.

**Appropriate permissions in Microsoft Entra ID** \- Your account must have permissions to

register applications and grant API permissions.

Before creating your client library, install the required dependencies for making HTTP requests:

Bash

Create a reusable client class that wraps HTTP calls to the Microsoft Entra SDK for AgentID. This

class handles token forwarding, request configuration, and error handling:

TypeScript

**Prerequisites**

**Setup**

`npm install node-fetch`

`npm install --save-dev @types/node-fetch`

**Client library implementation**

`// sidecar-client.ts`

`import` ` fetch ` `from` ` ` `'node-fetch'` `;`

`export`  ` `  `interface` ` SidecarConfig {`

`  baseUrl: ` `string` `;`

`  timeout?: ` `number` `;`

`}`

`export`  ` `  `class` ` SidecarClient {`

`  ` `private` ` readonly baseUrl: ` `string` `;`

`  ` `private` ` readonly timeout: ` `number` `;`

`  `

`  ` `constructor` `(config: SidecarConfig) {`

`    ` `this` `.baseUrl = config.baseUrl || process.env.SIDECAR_URL || `

`'http://localhost:5000'` `;`

`    ` `this` `.timeout = config.timeout || 10000;`

`  }`

`  `

`  ` `async` ` getAuthorizationHeader(`

`    incomingToken: ` `string` `,`

`    serviceName: ` `string` `,`

`    options?: {`

`      scopes?: ` `string` `[];`

`      tenant?: ` `string` `;`

`      agentIdentity?: ` `string` `;`

`      agentUsername?: ` `string` `;`

`    }`

`  ): ` `Promise`  `<`  `string`  `> {`

`    ` `const` ` url = ` `new` ` URL(`  `` ` ``  `${`  `this` `.baseUrl}` `/AuthorizationHeader/`  `${serviceName}`  `` ` `` `);`

`    `

`    ` `if` ` (options?.scopes) {`

`      options.scopes.forEach(scope => `

`        url.searchParams.append(` `'optionsOverride.Scopes'` `, scope)`

`      );`

`    }`

`    `

`    ` `if` ` (options?.tenant) {`

`      url.searchParams.append(` `'optionsOverride.AcquireTokenOptions.Tenant'` `, `

`options.tenant);`

`    }`

`    `

`    ` `if` ` (options?.agentIdentity) {`

`      url.searchParams.append(` `'AgentIdentity'` `, options.agentIdentity);`

`      ` `if` ` (options.agentUsername) {`

`        url.searchParams.append(` `'AgentUsername'` `, options.agentUsername);`

`      }`

`    }`

`    `

`    ` `const` ` response = ` `await` ` fetch(url.toString(), {`

`      headers: { ``'Authorization'` `: incomingToken },`

`      signal: AbortSignal.timeout(`  `this` `.timeout)`

`    });`

`    `

`    ` `if` ` (!response.ok) {`

`      ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `SDK error: `` `${response.statusText}`  `` ` `` `);`

`    }`

`    `

`    ` `const` ` data = ` `await` ` response.json();`

`    ` `return` ` data.authorizationHeader;`

`  }`

`  `

`  ` `async` ` callDownstreamApi<T>(`

`    incomingToken: ` `string` `,`

`    serviceName: ` `string` `,`

`    relativePath: ` `string` `,`

`    options?: {`

`      method?: ` `string` `;`

`      body?: ` `any` `;`

`      scopes?: ` `string` `[];`

`    }`

`  ): ` `Promise`  `<T> {`

`    ` `const` ` url = ` `new` ` URL(`  `` ` ``  `${`  `this` `.baseUrl}` `/DownstreamApi/`  `${serviceName}`  `` ` `` `);`

`    url.searchParams.append(` `'optionsOverride.RelativePath'` `, relativePath);`

`    `

`    ` `if` ` (options?.method && options.method !== ``'GET'` `) {`

`      url.searchParams.append(` `'optionsOverride.HttpMethod'` `, options.method);`

`    }`

`    `

`    ` `if` ` (options?.scopes) {`

`      options.scopes.forEach(scope => `

`        url.searchParams.append(` `'optionsOverride.Scopes'` `, scope)`

`      );`

`    }`

`    `

`    ` `const` ` fetchOptions: ` `any` ` = {`

`      method: options?.method || ``'GET'` `,`

`      headers: { ``'Authorization'` `: incomingToken },`

`      signal: AbortSignal.timeout(`  `this` `.timeout)`

`    };`

`    `

`    ` `if` ` (options?.body) {`

`      fetchOptions.headers[` `'Content-Type'` `] = ``'application/json'` `;`

`      fetchOptions.body = ` `JSON` `.stringify(options.body);`

`    }`

`    `

`    ` `const` ` response = ` `await` ` fetch(url.toString(), fetchOptions);`

`    `

`    ` `if` ` (!response.ok) {`

`      ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `SDK error: `` `${response.statusText}`  `` ` `` `);`

`    }`

`    `

`    ` `const` ` data = ` `await` ` response.json();`

`    `

`    ` `if` ` (data.statusCode >= 400) {`

`      ` `throw`  ` `  `new`  ` `  `Error` `(`  `` `API error `` `${data.statusCode}` `: ` `${data.content}`  `` ` `` `);`

`    }`

`    `

`    ` `return`  ` `  `JSON` `.parse(data.content) ` `as` ` T;`

`  }`

`}`

`// Usage`

`const` ` sidecar = ` `new` ` SidecarClient({ baseUrl: ``'http://localhost:5000'` ` });`

`// Get authorization header`

`const` ` authHeader = ` `await` ` sidecar.getAuthorizationHeader(token, ``'Graph'` `);`

`// Call API`

`interface` ` UserProfile {`

Integrate the client library into an Express.js application by creating middleware to extract the

incoming token and route handlers that call downstream APIs:

TypeScript

`  displayName: ` `string` `;`

`  mail: ` `string` `;`

`  userPrincipalName: ` `string` `;`

`}`

`const` ` profile = ` `await` ` sidecar.callDownstreamApi<UserProfile>(`

`  token,`

`  ``'Graph'` `,`

`  ``'me'`

`);`

**Express.js integration**

`import` ` express ` `from` ` ` `'express'` `;`

`import` ` { SidecarClient } ` `from` ` ` `'./sidecar-client'` `;`

`const` ` app = express();`

`app.use(express.json());`

`const` ` sidecar = ` `new` ` SidecarClient({ baseUrl: process.env.SIDECAR_URL! });`

`// Middleware to extract token`

`app.use((req, res, next) => {`

`  ` `const` ` token = req.headers.authorization;`

`  ` `if` ` (!token && !req.path.startsWith(` `'/health'` `)) {`

`    ` `return` ` res.status(401).json({ error: ``'No authorization token'` ` });`

`  }`

`  req.userToken = token;`

`  next();`

`});`

`// Routes`

`app.get(` `'/api/profile'` `, ` `async` ` (req, res) => {`

`  ` `try` ` {`

`    ` `const` ` profile = ` `await` ` sidecar.callDownstreamApi(`

`      req.userToken,`

`      ``'Graph'` `,`

`      ``'me'`

`    );`

`    res.json(profile);`

`  } ` `catch` ` (error) {`

`    res.status(500).json({ error: error.message });`

`  }`

`});`

`app.get(` `'/api/messages'` `, ` `async` ` (req, res) => {`

`  ` `try` ` {`

For NestJS applications, create a service that wraps the client library. This service can be

injected into controllers to handle authenticated requests:

TypeScript

`    ` `const` ` messages = ` `await` ` sidecar.callDownstreamApi(`

`      req.userToken,`

`      ``'Graph'` `,`

`      ``'me/messages?$top=10'`

`    );`

`    res.json(messages);`

`  } ` `catch` ` (error) {`

`    res.status(500).json({ error: error.message });`

`  }`

`});`

`app.listen(8080, () => {`

`  ` `console` `.log(` `'Server running on port 8080'` `);`

`});`

**NestJS integration**

`import` ` { Injectable } ` `from` ` ` `'@nestjs/common'` `;`

`import` ` { SidecarClient } ` `from` ` ` `'./sidecar-client'` `;`

`@Injectable` `()`

`export`  ` `  `class` ` GraphService {`

`  ` `private` ` readonly sidecar: SidecarClient;`

`  `

`  ` `constructor` `() {`

`    ` `this` `.sidecar = ` `new` ` SidecarClient({ `

`      baseUrl: process.env.SIDECAR_URL! `

`    });`

`  }`

`  `

`  ` `async` ` getUserProfile(token: ` `string` `) {`

`    ` `return`  ` `  `await`  ` `  `this` `.sidecar.callDownstreamApi(`

`      token,`

`      ``'Graph'` `,`

`      ``'me'`

`    );`

`  }`

`  `

`  ` `async` ` getUserMessages(token: ` `string` `, top: ` `number` ` = 10) {`

`    ` `return`  ` `  `await`  ` `  `this` `.sidecar.callDownstreamApi(`

`      token,`

`      ``'Graph'` `,`

`      ` `` `me/messages?$top=``  `${top}`  `` ` ``

`    );`

`  }`

`}`

When using the Microsoft Entra SDK for AgentID from TypeScript, follow these practices to

build reliable and maintainable applications:

**Reuse Client Instance**: Create a single `SidecarClient` instance and reuse it throughout

your application rather than creating new instances per request. This improves

performance and resource usage.

**Set Appropriate Timeouts**: Configure request timeouts based on your downstream API

latency. This prevents your application from hanging indefinitely if the SDK or

downstream service is slow.

**Implement Error Handling**: Add proper error handling and retry logic, especially for

transient failures. Distinguish between client errors (4xx) and server errors (5xx) to

determine appropriate responses.

**Use TypeScript Interfaces**: Define TypeScript interfaces for API responses to ensure type

safety and catch errors at compile time rather than runtime.

**Enable Connection Pooling**: Use HTTP agents to enable connection reuse across

requests, which reduces overhead and improves throughput.

Using from Python

Managed Identity patterns

Start with a scenario:

Call Downstream API

Obtain Authorization Header

Validate Authorization Header

**Last updated on 11/14/2025**

**Best practices**

**Other language guides**

**Next steps**

**Scenario: Using the Microsoft Entra SDK for**

**AgentID from Python**

Create a Python client library that integrates with the Microsoft Entra SDK for AgentID to

obtain tokens and call downstream APIs. Then integrate this client into Flask, FastAPI, or

Django applications to handle authenticated requests.

An Azure account with an active subscription. Create an account for free

.

**Python** (version 3.7 or later) with pip installed on your development machine.

**Microsoft Entra SDK for AgentID** deployed and running in your environment. See

Installation Guide for setup instructions.

**Downstream APIs configured** in the SDK with base URLs and required scopes.

**Appropriate permissions in Microsoft Entra ID** \- Your account must have permissions to

register applications and grant API permissions.

Before creating your client library, install the required dependency for making HTTP requests:

Bash

Create a reusable client class that wraps HTTP calls to the Microsoft Entra SDK for AgentID. This

class handles token forwarding, request configuration, and error handling:

Python

**Prerequisites**

**Setup**

`pip install requests`

**Client library implementation**

`# sidecar_client.py`

`import` ` os`

`import` ` json`

`import` ` requests`

`from` ` typing ` `import` ` Dict, Any, Optional, List`

`from` ` urllib.parse ` `import` ` urlencode`

`class`  ` `  `SidecarClient` `:`

`    ``"""Client for interacting with the Microsoft Entra SDK for AgentID."""`

`    `

`    ` `def` ` ` `__init__` `(self, base_url: Optional[str] = None, timeout: int = 10):`

`        self.base_url = base_url ` `or` ` os.getenv(` `'SIDECAR_URL'` `, `

`'http://localhost:5000'` `)`

`        self.timeout = timeout`

`    `

`    ` `def`  ` `  `get_authorization_header` `(`

`        self,`

`        incoming_token: str,`

`        service_name: str,`

`        scopes: Optional[List[str]] = None,`

`        tenant: Optional[str] = None,`

`        agent_identity: Optional[str] = None,`

`        agent_username: Optional[str] = None`

`    ) -> str:`

`        ``"""Get authorization header from the SDK."""`

`        params = {}`

`        `

`        ` `if` ` scopes:`

`            params[` `'optionsOverride.Scopes'` `] = scopes`

`        `

`        ` `if` ` tenant:`

`            params[` `'optionsOverride.AcquireTokenOptions.Tenant'` `] = tenant`

`        `

`        ` `if` ` agent_identity:`

`            params[` `'AgentIdentity'` `] = agent_identity`

`            ` `if` ` agent_username:`

`                params[` `'AgentUsername'` `] = agent_username`

`        `

`        response = requests.get(`

`            ` `f"` `{self.base_url}` `/AuthorizationHeader/` `{service_name}` `"` `,`

`            params=params,`

`            headers={` `'Authorization'` `: incoming_token},`

`            timeout=self.timeout`

`        )`

`        `

`        response.raise_for_status()`

`        data = response.json()`

`        ` `return` ` data[` `'authorizationHeader'` `]`

`    `

`    ` `def`  ` `  `call_downstream_api` `(`

`        self,`

`        incoming_token: str,`

`        service_name: str,`

`        relative_path: str,`

`        method: str = ``'GET'` `,`

`        body: Optional[Dict[str, Any]] = None,`

`        scopes: Optional[List[str]] = None`

`    ) -> Any:`

`        ``"""Call downstream API via the SDK."""`

`        params = {` `'optionsOverride.RelativePath'` `: relative_path}`

`        `

`        ` `if` ` method != ``'GET'` `:`

`            params[` `'optionsOverride.HttpMethod'` `] = method`

`        `

`        ` `if` ` scopes:`

Integrate the client library into a Flask application by extracting the incoming token in a helper

function and using it in route handlers to call downstream APIs:

Python

`            params[` `'optionsOverride.Scopes'` `] = scopes`

`        `

`        headers = {` `'Authorization'` `: incoming_token}`

`        json_body = ` `None`

`        `

`        ` `if` ` body:`

`            headers[` `'Content-Type'` `] = ``'application/json'`

`            json_body = body`

`        `

`        response = requests.request(`

`            method,`

`            ` `f"` `{self.base_url}` `/DownstreamApi/` `{service_name}` `"` `,`

`            params=params,`

`            headers=headers,`

`            json=json_body,`

`            timeout=self.timeout`

`        )`

`        `

`        response.raise_for_status()`

`        data = response.json()`

`        `

`        ` `if` ` data[` `'statusCode'` `] >= 400:`

`            ` `raise` ` Exception(`  `f"API error ``{data[` `'statusCode'` `]}` `: ``{data[` `'content'` `]}` `"` `)`

`        `

`        ` `return` ` json.loads(data[` `'content'` `])`

`# Usage`

`sidecar = SidecarClient(base_url=` `'http://localhost:5000'` `)`

`# Get authorization header`

`auth_header = sidecar.get_authorization_header(token, ``'Graph'` `)`

`# Call API`

`profile = sidecar.call_downstream_api(token, ``'Graph'` `, ``'me'` `)`

**Flask integration**

`from` ` flask ` `import` ` Flask, request, jsonify`

`from` ` sidecar_client ` `import` ` SidecarClient`

`app = Flask(__name__)`

`sidecar = SidecarClient()`

`def`  ` `  `get_token` `():`

`    ``"""Extract token from request."""`

`    token = request.headers.get(` `'Authorization'` `)`

`    ` `if`  ` `  `not` ` token:`

`        ` `raise` ` ValueError(` `'No authorization token provided'` `)`

`    ` `return` ` token`

`@app.route('/api/profile')`

`def`  ` `  `profile` `():`

`    ` `try` `:`

`        token = get_token()`

`        profile_data = sidecar.call_downstream_api(`

`            token,`

`            ``'Graph'` `,`

`            ``'me'`

`        )`

`        ` `return` ` jsonify(profile_data)`

`    ` `except` ` ValueError ` `as` ` e:`

`        ` `return` ` jsonify({` `'error'` `: str(e)}), 401`

`    ` `except` ` Exception ` `as` ` e:`

`        ` `return` ` jsonify({` `'error'` `: str(e)}), 500`

`@app.route('/api/messages')`

`def`  ` `  `messages` `():`

`    ` `try` `:`

`        token = get_token()`

`        messages_data = sidecar.call_downstream_api(`

`            token,`

`            ``'Graph'` `,`

`            ``'me/messages?$top=10'`

`        )`

`        ` `return` ` jsonify(messages_data)`

`    ` `except` ` ValueError ` `as` ` e:`

`        ` `return` ` jsonify({` `'error'` `: str(e)}), 401`

`    ` `except` ` Exception ` `as` ` e:`

`        ` `return` ` jsonify({` `'error'` `: str(e)}), 500`

`@app.route('/api/messages/send', methods=['POST'])`

`def`  ` `  `send_message` `():`

`    ` `try` `:`

`        token = get_token()`

`        message = request.json`

`        `

`        result = sidecar.call_downstream_api(`

`            token,`

`            ``'Graph'` `,`

`            ``'me/sendMail'` `,`

`            method=` `'POST'` `,`

`            body={` `'message'` `: message}`

`        )`

`        `

`        ` `return` ` jsonify({` `'success'` `: ` `True` `, ``'result'` `: result})`

`    ` `except` ` ValueError ` `as` ` e:`

`        ` `return` ` jsonify({` `'error'` `: str(e)}), 401`

`    ` `except` ` Exception ` `as` ` e:`

`        ` `return` ` jsonify({` `'error'` `: str(e)}), 500`

`if` ` __name__ == ``'__main__'` `:`

`    app.run(host=` `'0.0.0.0'` `, port=8080)`

For FastAPI applications, use the dependency injection system with the `Header` dependency to

extract and validate the authorization token before passing it to route handlers:

Python

For Django applications, create view classes that extract the authorization token from request

headers and use it to call downstream APIs:

Python

**FastAPI integration**

`from` ` fastapi ` `import` ` FastAPI, Header, HTTPException`

`from` ` sidecar_client ` `import` ` SidecarClient`

`from` ` typing ` `import` ` Optional`

`app = FastAPI()`

`sidecar = SidecarClient()`

`async`  ` `  `def`  ` `  `get_token` `(authorization: Optional[str] = Header(None)):`

`    ` `if`  ` `  `not` ` authorization:`

`        ` `raise` ` HTTPException(status_code=401, detail=` `"No authorization token"` `)`

`    ` `return` ` authorization`

`@app.get("/api/profile")`

`async`  ` `  `def`  ` `  `get_profile` `(token: str = Depends(get_token)):`

`    ` `try` `:`

`        ` `return` ` sidecar.call_downstream_api(token, ``'Graph'` `, ``'me'` `)`

`    ` `except` ` Exception ` `as` ` e:`

`        ` `raise` ` HTTPException(status_code=500, detail=str(e))`

`@app.get("/api/messages")`

`async`  ` `  `def`  ` `  `get_messages` `(token: str = Depends(get_token)):`

`    ` `try` `:`

`        ` `return` ` sidecar.call_downstream_api(`

`            token,`

`            ``'Graph'` `,`

`            ``'me/messages?$top=10'`

`        )`

`    ` `except` ` Exception ` `as` ` e:`

`        ` `raise` ` HTTPException(status_code=500, detail=str(e))`

**Django integration**

`# views.py`

`from` ` django.http ` `import` ` JsonResponse`

`from` ` django.views ` `import` ` View`

For improved performance and resilience, use a `requests.Session` object with retry logic. This

approach enables automatic retries for transient failures and connection pooling to reduce

overhead:

Python

`from` ` sidecar_client ` `import` ` SidecarClient`

`sidecar = SidecarClient()`

`class`  ` `  `ProfileView` `(View):`

`    ` `def`  ` `  `get` `(self, request):`

`        token = request.META.get(` `'HTTP_AUTHORIZATION'` `)`

`        ` `if`  ` `  `not` ` token:`

`            ` `return` ` JsonResponse({` `'error'` `: ``'No authorization token'` `}, status=401)`

`        `

`        ` `try` `:`

`            profile = sidecar.call_downstream_api(token, ``'Graph'` `, ``'me'` `)`

`            ` `return` ` JsonResponse(profile)`

`        ` `except` ` Exception ` `as` ` e:`

`            ` `return` ` JsonResponse({` `'error'` `: str(e)}, status=500)`

`class`  ` `  `MessagesView` `(View):`

`    ` `def`  ` `  `get` `(self, request):`

`        token = request.META.get(` `'HTTP_AUTHORIZATION'` `)`

`        ` `if`  ` `  `not` ` token:`

`            ` `return` ` JsonResponse({` `'error'` `: ``'No authorization token'` `}, status=401)`

`        `

`        ` `try` `:`

`            messages = sidecar.call_downstream_api(`

`                token,`

`                ``'Graph'` `,`

`                ``'me/messages?$top=10'`

`            )`

`            ` `return` ` JsonResponse(messages)`

`        ` `except` ` Exception ` `as` ` e:`

`            ` `return` ` JsonResponse({` `'error'` `: str(e)}, status=500)`

**Advanced: using requests.Session**

`import` ` requests`

`from` ` requests.adapters ` `import` ` HTTPAdapter`

`from` ` requests.packages.urllib3.util.retry ` `import` ` Retry`

`class`  ` `  `SidecarClient` `:`

`    ` `def` ` ` `__init__` `(self, base_url: Optional[str] = None):`

`        self.base_url = base_url ` `or` ` os.getenv(` `'SIDECAR_URL'` `, `

`'http://localhost:5000'` `)`

`        `

`        ``# Configure session with retry logic`

`        self.session = requests.Session()`

When using the Microsoft Entra SDK for AgentID from Python, follow these practices to build

reliable and maintainable applications:

**Reuse Client Instance**: Create a single `SidecarClient` instance and reuse it throughout

your application rather than creating new instances per request. This improves

performance and resource usage.

**Set Appropriate Timeouts**: Configure request timeouts based on your downstream API

latency. This prevents your application from hanging indefinitely if the SDK or

downstream service is slow.

**Implement Error Handling**: Add proper error handling and retry logic, especially for

transient failures. Distinguish between client errors (4xx) and server errors (5xx) to

determine appropriate responses.

**Use Type Hints**: Add type hints to function parameters and return values for better code

clarity and to catch errors at development time.

**Enable Connection Pooling**: Use a `requests.Session` object for connection reuse across

requests, which reduces overhead and improves throughput for multiple API calls.

Using from TypeScript

Managed Identity patterns

Start with a scenario:

Call Downstream API

`        retry = Retry(`

`            total=3,`

`            backoff_factor=0.3,`

`            status_forcelist=[500, 502, 503, 504]`

`        )`

`        adapter = HTTPAdapter(max_retries=retry)`

`        self.session.mount(` `'http://'` `, adapter)`

`        self.session.mount(` `'https://'` `, adapter)`

`    `

`    ` `def`  ` `  `call_downstream_api` `(self, token, service_name, relative_path, **kwargs):`

`        ``# Use self.session instead of requests`

`        response = self.session.get(...)`

`        ` `return` ` response`

**Best practices**

**Other language guides**

**Next steps**

Obtain Authorization Header

Validate Authorization Header

**Last updated on 11/14/2025**

**Scenario: Using Managed Identity**

Use Azure AD Workload Identity to authenticate pods in Azure Kubernetes Service (AKS) to the

Microsoft Entra SDK for AgentID without storing credentials. The SDK automatically acquires

tokens using your pod's managed identity, eliminating the need for client secrets or

certificates, keeping your application secure.

An Azure account with an active subscription. Create an account for free

.

**Azure Kubernetes Service (AKS) cluster** with OIDC issuer and workload identity enabled.

See Quickstart: Deploy an AKS cluster.

**Microsoft Entra SDK for AgentID** container image available and ready to deploy. See

Installation Guide for setup instructions.

**Appropriate permissions in Microsoft Entra ID** \- Your account must have permissions to

create and manage managed identities, create federated identity credentials, and grant

application permissions.

**kubectl access** to your AKS cluster for deploying pods and creating Kubernetes resources.

Follow these steps to configure Azure Managed Identity with the Microsoft Entra SDK for

AgentID:

To enable workload identity, create or update your AKS cluster with OIDC issuer and workload

identity support:

Bash

） **Important**

For AKS, Azure AD Workload Identity uses **file-based token projection** with the

`SignedAssertionFilePath` credential type. The workload identity webhook automatically

projects the token to `/var/run/secrets/azure/tokens/azure-identity-token` in your pod.

This is different from classic managed identity on VMs or App Services, which uses the

`SignedAssertionFromManagedIdentity` credential type.

**Prerequisites**

**Setup steps**

**1\. Enable Workload Identity on AKS**

Next, you need to create a managed identity in Azure that your AKS pods will use to

authenticate to the Microsoft Entra SDK for AgentID:

Bash

Grant the managed identity the necessary API permissions to access downstream APIs via the

Microsoft Entra SDK for AgentID:

Bash

`# Create or update AKS cluster with workload identity`

`az aks create \`

`  --resource-group myResourceGroup \`

`  --name myAKSCluster \`

`  --`  `enable` `-oidc-issuer \`

`  --`  `enable` `-workload-identity`

`# Get OIDC issuer URL`

`export` ` AKS_OIDC_ISSUER=$(az aks show \`

`  --resource-group myResourceGroup \`

`  --name myAKSCluster \`

`  --query ``"oidcIssuerProfile.issuerUrl"` ` -o tsv)`

**2\. Create Managed Identity**

`# Create managed identity`

`az identity create \`

`  --resource-group myResourceGroup \`

`  --name myapp-identity`

`# Get identity details`

`export` ` IDENTITY_CLIENT_ID=$(az identity show \`

`  --resource-group myResourceGroup \`

`  --name myapp-identity \`

`  --query clientId -o tsv)`

`export` ` IDENTITY_OBJECT_ID=$(az identity show \`

`  --resource-group myResourceGroup \`

`  --name myapp-identity \`

`  --query principalId -o tsv)`

**3\. Grant Permissions**

`# Grant Microsoft Graph permissions`

`az ad app permission add \`

`  --id $IDENTITY_CLIENT_ID \`

`  --api 00000003-0000-0000-c000-000000000000 \`

`  --api-permissions e1fe6dd8-ba31-4d61-89e7-88639da4683d=Scope  ``# User.Read`

Create a federated identity credential to link the AKS workload identity with the managed

identity:

Bash

Finally, create a Kubernetes service account annotated with the managed identity client ID:

YAML

Once created, you can apply the service account configuration with kubectl:

Bash

Deploy the Microsoft Entra SDK for AgentID alongside your application in a Kubernetes pod.

The SDK automatically uses workload identity when configured:

`# Grant admin consent`

`az ad app permission admin-consent --id $IDENTITY_CLIENT_ID`

**4\. Create Federated Identity Credential**

`# Create federated credential for Kubernetes service account`

`az identity federated-credential create \`

`  --name myapp-federated-identity \`

`  --identity-name myapp-identity \`

`  --resource-group myResourceGroup \`

`  --issuer $AKS_OIDC_ISSUER \`

`  --subject system:serviceaccount:default:myapp-sa`

**5\. Create Kubernetes Service Account**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `ServiceAccount`

`metadata:`

`  name:`  ` `  `myapp-sa`

`  namespace:`  ` `  `default`

`  annotations:`

`    ` `azure.workload.identity/client-id:` ` ` `"<MANAGED_IDENTITY_CLIENT_ID>"`

`kubectl apply -f serviceaccount.yaml`

**Deployment configuration**

**Complete pod configuration**

YAML

`apiVersion:`  ` `  `apps/v1`

`kind:`  ` `  `Deployment`

`metadata:`

`  name:`  ` `  `myapp`

`  namespace:`  ` `  `default`

`spec:`

`  replicas:` ` 3`

`  selector:`

`    matchLabels:`

`      app:`  ` `  `myapp`

`  template:`

`    metadata:`

`      labels:`

`        app:`  ` `  `myapp`

`        ` `azure.workload.identity/use:` ` ` `"true"` `  ` `# Required for workload identity`

`    spec:`

`      serviceAccountName:`  ` `  `myapp-sa`

`      containers:`

`      ``# Application container`

`      - name:`  ` `  `app`

`        image:`  ` `  `myregistry/myapp:latest`

`        ports:`

`        - containerPort:` ` 8080`

`        env:`

`        - name:`  ` `  `SIDECAR_URL`

`          value:` ` ` `"http://localhost:5000"`

`        resources:`

`          requests:`

`            memory:` ` ` `"256Mi"`

`            cpu:` ` ` `"250m"`

`          limits:`

`            memory:` ` ` `"512Mi"`

`            cpu:` ` ` `"500m"`

`      `

`      ``# SDK container`

`      - name:`  ` `  `sidecar`

`        image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`        ports:`

`        - containerPort:` ` 5000`

`        env:`

`        ``# Azure AD Configuration`

`        - name:`  ` `  `AzureAd__Instance`

`          value:` ` ` `"https://login.microsoftonline.com/"`

`        - name:`  ` `  `AzureAd__TenantId`

`          value:` ` ` `"common"` `  ` `# Or specific tenant ID`

`        - name:`  ` `  `AzureAd__ClientId`

`          value:` ` ` `"<MANAGED_IDENTITY_CLIENT_ID>"`

`        `

`        ``# Client Credentials - Use SignedAssertionFilePath for workload identity`

`        - name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`          value:` ` ` `"SignedAssertionFilePath"`

`        `

`        ``# Downstream API Configuration`

When you configure a pod with the Azure Workload Identity label

( ` azure.workload.identity/use: "true"` ) and a properly annotated service account, the Azure

Workload Identity webhook automatically:

1\. **Injects environment variables** into the pod:

`AZURE_CLIENT_ID` \- The managed identity client ID from the service account

annotation

`AZURE_TENANT_ID` \- The tenant ID

`AZURE_FEDERATED_TOKEN_FILE` \- Path to the projected token file

( ` /var/run/secrets/azure/tokens/azure-identity-token` )

2\. **Projects the token file** as a volume mount at `/var/run/secrets/azure/tokens/azure-`

`identity-token`

`        - name:`  ` `  `DownstreamApis__Graph__BaseUrl`

`          value:` ` ` `"https://graph.microsoft.com/v1.0"`

`        - name:`  ` `  `DownstreamApis__Graph__Scopes`

`          value:` ` ` `"User.Read Mail.Read"`

`        `

`        ``# Logging`

`        - name:`  ` `  `Logging__LogLevel__Default`

`          value:` ` ` `"Information"`

`        - name:`  ` `  `Logging__LogLevel__Microsoft.Identity.Web`

`          value:` ` ` `"Information"`

`        `

`        resources:`

`          requests:`

`            memory:` ` ` `"128Mi"`

`            cpu:` ` ` `"100m"`

`          limits:`

`            memory:` ` ` `"256Mi"`

`            cpu:` ` ` `"250m"`

`        `

`        livenessProbe:`

`          httpGet:`

`            path:` ` ` `/healthz`

`            port:` ` 5000`

`          initialDelaySeconds:` ` 10`

`          periodSeconds:` ` 10`

`        `

`        readinessProbe:`

`          httpGet:`

`            path:` ` ` `/healthz`

`            port:` ` 5000`

`          initialDelaySeconds:` ` 5`

`          periodSeconds:` ` 5`

**How Workload Identity Token Projection Works**

3\. **Automatically refreshes** the token before it expires

The SDK uses the `SignedAssertionFilePath` credential type to read the token from this

projected file location. This approach is specific to containerized workload identity and differs

from classic managed identity on VMs or App Services.

Verify that workload identity is properly configured and that the Microsoft Entra SDK for

AgentID can acquire tokens by using the following steps:

Verify pod labels and service account configuration using kubectl commands:

Bash

Check that Azure workload identity environment variables are correctly set in the pod:

Bash

**Verification**

**Test workload identity**

`# Check pod labels`

`kubectl get pod -l app=myapp -o yaml | grep -A 5 ``"labels:"`

`# Verify service account`

`kubectl get pod -l app=myapp -o yaml | grep serviceAccountName`

`# Check SDK logs`

`kubectl logs -l app=myapp -c sidecar`

`# Test token acquisition`

`kubectl ` `exec` ` -it $(kubectl get pod -l app=myapp -o name | head -1) -c app -- \`

`  curl -H ``"Authorization: Bearer <test-token>"` ` \`

`  http://localhost:5000/AuthorizationHeader/Graph`

**Verify environment variables**

`# Check identity environment variables in pod`

`kubectl ` `exec` ` -it $(kubectl get pod -l app=myapp -o name | head -1) -c sidecar -- env `

`| grep AZURE`

`# You should see:`

`# AZURE_CLIENT_ID=<managed-identity-client-id>`

`# AZURE_TENANT_ID=<tenant-id>`

`# AZURE_FEDERATED_TOKEN_FILE=/var/run/secrets/azure/tokens/azure-identity-token`

Since the Microsoft Entra SDK for AgentID automatically handles all token acquisition using the

pod's managed identity, your application code can remain unchanged. The following example

demonstrates calling a downstream API without any authentication logic:

TypeScript

Manage different authentication approaches across development and production

environments:

Use client secret for local development - ensure you store secrets securely, and do not commit

them to source control:

YAML

**Application code**

`// TypeScript example`

`async`  ` `  `function`  ` `  `getUserProfile` `(incomingToken: ` `string` `) {`

`  ` `const` ` sidecarUrl = process.env.SIDECAR_URL!;`

`  `

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${sidecarUrl}` ``/DownstreamApi/Graph?optionsOverride.RelativePath=me` `` `,`

`    {`

`      method: ``'POST'` `,`

`      headers: {`

`        ``'Authorization'` `: incomingToken`

`      }`

`    }`

`  );`

`  `

`  ` `const` ` result = ` `await` ` response.json();`

`  ` `return`  ` `  `JSON` `.parse(result.content);`

`}`

**Multiple environments**

**Development**

`# dev-secrets.yaml (local only, not committed)`

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `Secret`

`metadata:`

`  name:`  ` `  `sidecar-secrets-dev`

`type:`  ` `  `Opaque`

`stringData:`

`  AzureAd__ClientCredentials__0__SourceType:` ` ` `"ClientSecret"`

`  AzureAd__ClientCredentials__0__ClientSecret:` ` ` `"<dev-client-secret>"`

Use workload identity in production for secure, credential-free authentication:

YAML

Diagnose and resolve common issues with workload identity and the Microsoft Entra SDK for

AgentID:

Check pod events and logs to identify startup failures:

Bash

Common issues:

Missing service account annotation with the managed identity client ID

Missing pod label `azure.workload.identity/use: "true"`

Incorrect or mismatched client ID in service account annotation

Bash

Common issues:

**Production**

`# prod-serviceaccount.yaml`

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `ServiceAccount`

`metadata:`

`  name:`  ` `  `myapp-sa-prod`

`  annotations:`

`    ` `azure.workload.identity/client-id:` ` ` `"<prod-managed-identity-client-id>"`

**Troubleshooting**

**Pod fails to start**

`# Check pod events`

`kubectl describe pod -l app=myapp`

`# Check SDK logs`

`kubectl logs -l app=myapp -c sidecar`

**Token acquisition fails**

`# Check logs for AADSTS errors`

`kubectl logs -l app=myapp -c sidecar | grep AADSTS`

Federated credential OIDC issuer URL does not match cluster's issuer URL exactly

Subject pattern mismatch (should be `system:serviceaccount:<namespace>:<service-`

`account>` )

Managed identity lacks required permissions or admin consent not granted

Service account not properly labeled or annotated

Verify the workload identity webhook is configured and pods are properly mutated:

Bash

Follow these practices for security and operational excellence with managed identity:

**Separate Identities per Environment**: Use different managed identities for development,

staging, and production to limit blast radius if any identity is compromised.

**Apply Least Privilege**: Grant only required permissions to each managed identity and

regularly audit to revoke unnecessary access.

**Enable Diagnostic Logging**: Configure Azure AD audit logs and SDK diagnostic logging

to monitor identity usage and detect suspicious patterns.

**Review Permissions Regularly**: Periodically validate that granted permissions remain

necessary for your application.

**Maintain Documentation**: Document all permissions granted to each managed identity

and their business justification.

**Test in Staging**: Verify workload identity configuration in a staging environment before

production deployment.

**Apply Proper Labels**: Use consistent Kubernetes labels ( ` azure.workload.identity/use:`

`"true"` ) for managed identity pods to simplify operations.

Managed identity eliminates the need to manage client secrets or certificates, automatically

renews tokens, provides complete audit trails in Azure AD, integrates seamlessly with Azure

RBAC, and enhances your security posture by reducing credential exposure risks.

**Environment variables not set**

`# Verify workload identity webhook is running`

`kubectl get pods -n kube-system | grep azure-workload-identity-webhook`

`# Check pod mutation`

`kubectl get pod -l app=myapp -o yaml | grep -A 10 ``"env:"`

**Best practices**

Compare managed identity with alternative authentication approaches:

**Method**

**Security**

**Complexity**

**Maintenance**

**Workload Identity**

⭐⭐⭐⭐⭐

⭐⭐⭐

⭐⭐⭐⭐⭐

Certificate (Key Vault)

⭐⭐⭐⭐

⭐⭐⭐

⭐⭐⭐⭐

Certificate (Kubernetes Secret)

⭐⭐⭐

⭐⭐

⭐⭐⭐

Client Secret

⭐⭐

⭐

⭐⭐

**Workload Identity** offers the highest security rating due to token-based authentication with no

shared secrets, moderate operational complexity for setup and configuration, and minimal

ongoing maintenance compared to other approaches.

After setting up managed identity:

Call Downstream APIs

Implement OBO Flows

Review Security

**Last updated on 11/14/2025**

**Comparison with other methods**

ﾉ

**Expand table**

**Next steps**

**Scenario: Long-Running On-Behalf-Of**

**(OBO)**

Implement long-running operations that extend beyond a user's token lifetime by

automatically refreshing tokens using the Microsoft Entra SDK for AgentID. This guide shows

you how to store user context, implement background processing, and handle token

expiration.

An Azure account with an active subscription. Create an account for free

.

**Microsoft Entra SDK for AgentID** deployed and running with refresh token support

enabled. See Installation Guide for setup instructions.

**Registered application in Microsoft Entra ID** \- Register a new app in the Microsoft Entra

admin center

. Refer to Register an application for details. Record:

Application (client) ID

Directory (tenant) ID

Configure an **App ID URI** in the **Expose an API** section

Grant API permissions for downstream services (e.g., Microsoft Graph permissions for

tasks or reports your batch job accesses)

Enable **Allow public client flows** if using device flow or similar patterns

**Downstream APIs configured** in the SDK with appropriate scopes for long-running

operations.

**Storage mechanism** (database, cache, or message queue) to store user context during

long-running background operations.

**Appropriate permissions in Microsoft Entra ID** \- Your account must have permissions to

configure OBO flows and grant API permissions.

Configure longer refresh token lifetime in Microsoft Entra ID:

Bash

**Prerequisites**

**Configuration**

`# Set refresh token lifetime (via Microsoft Graph PowerShell)`

`Connect-MgGraph -Scopes ``"Policy.Read.All"` `, `

`"Policy.ReadWrite.ApplicationConfiguration"`

`# Create token lifetime policy (example: 90 days)`

`$params = @{`

`    Definition = @(`

`        ``'{"TokenLifetimePolicy":`

Long-running OBO scenarios require three key components: storing user context when the

operation starts, processing in the background, and handling token refresh automatically.

Store the user's identity and tokens when initiating the operation:

TypeScript

`{"Version":1,"AccessTokenLifetime":"1:00:00","RefreshTokenMaxInactiveTime":"90.00:00`

`:00","RefreshTokenMaxAge":"90.00:00:00"}}'`

`    )`

`    DisplayName = ``"LongRunningOBOPolicy"`

`    IsOrganizationDefault = $false`

`}`

`New-MgPolicyTokenLifetimePolicy -BodyParameter $params`

**Implementation pattern**

**Store user context**

`// When user initiates long-running task`

`interface` ` UserContext {`

`  userId: ` `string` `;`

`  userPrincipalName: ` `string` `;`

`  originalToken: ` `string` `;`

`  taskId: ` `string` `;`

`  createdAt: ` `Date` `;`

`}`

`async`  ` `  `function`  ` `  `initiateLongRunningTask` `(incomingToken: ` `string` `): ` `Promise`  `<`  `string`  `> {`

`  ``// Extract user information from token`

`  ` `const` ` tokenClaims = ValidateToken(incomingToken);`

`  `

`  ` `const` ` taskId = generateTaskId();`

`  `

`  ``// Store user context`

`  ` `const` ` userContext: UserContext = {`

`    userId: tokenClaims.oid,`

`    userPrincipalName: tokenClaims.upn,`

`    originalToken: incomingToken,`

`    taskId: taskId,`

`    createdAt: ` `new`  ` `  `Date` `()`

`  };`

`  `

`  ` `await` ` storeUserContext(taskId, userContext);`

`  `

`  ``// Start background process`

`  ` `await` ` queueBackgroundTask(taskId);`

`  `

Process the queued task using the stored user context:

TypeScript

`  ` `return` ` taskId;`

`}`

**Background processing**

`async`  ` `  `function`  ` `  `processLongRunningTask` `(taskId: ` `string` `) {`

`  ``// Retrieve user context`

`  ` `const` ` userContext = ` `await` ` getUserContext(taskId);`

`  `

`  ``// Use stored token with the SDK - refresh handled automatically`

`  ` `try` ` {`

`    ``// Step 1: Process data`

`    ` `const` ` data = ` `await` ` fetchData(userContext.originalToken);`

`    `

`    ``// Step 2: Generate report (may take hours)`

`    ` `const` ` report = ` `await` ` generateReport(data);`

`    `

`    ``// Step 3: Upload to user's OneDrive`

`    ` `await` ` uploadToOneDrive(userContext.originalToken, report);`

`    `

`    ``// Step 4: Send notification`

`    ` `await` ` sendNotification(userContext.originalToken, userContext.userId);`

`    `

`    ` `await` ` markTaskComplete(taskId);`

`  } ` `catch` ` (error) {`

`    ``// Handle token expiration`

`    ` `if` ` (isTokenExpiredError(error)) {`

`      ` `await` ` markTaskFailed(taskId, ``'User token expired and could not be refreshed'` `);`

`    } ` `else` ` {`

`      ` `await` ` markTaskFailed(taskId, error.message);`

`    }`

`  }`

`}`

`async`  ` `  `function`  ` `  `uploadToOneDrive` `(token: ` `string` `, report: Buffer) {`

`  ``// SDK automatically handles token refresh`

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${sidecarUrl}` `/DownstreamApi/Graph?`

``optionsOverride.RelativePath=me/drive/root:/reports/report.pdf:/content` `` `,`

`    {`

`      method: ``'PUT'` `,`

`      headers: {`

`        ``'Authorization'` `: token,`

`        ``'Content-Type'` `: ``'application/pdf'`

`      },`

`      body: report`

`    }`

`  );`

Automatically refresh tokens before expiration:

TypeScript

The following example demonstrates a long-running task processor in Python using Flask or

FastAPI:

Python

`  `

`  ` `return`  ` `  `await` ` response.json();`

`}`

**Periodic token refresh**

`// Proactively refresh tokens before expiration`

`async`  ` `  `function`  ` `  `refreshTokenPeriodically` `(taskId: ` `string` `) {`

`  ` `const` ` userContext = ` `await` ` getUserContext(taskId);`

`  `

`  ``// Call SDK to refresh token`

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${sidecarUrl}` ``/AuthorizationHeader/Graph` `` `,`

`    {`

`      headers: {`

`        ``'Authorization'` `: userContext.originalToken`

`      }`

`    }`

`  );`

`  `

`  ` `if` ` (response.ok) {`

`    ` `const` ` data = ` `await` ` response.json();`

`    ``// Extract new token`

`    ` `const` ` newToken = data.authorizationHeader;`

`    `

`    ``// Update stored context`

`    userContext.originalToken = newToken;`

`    ` `await` ` updateUserContext(taskId, userContext);`

`  }`

`}`

**Python example**

`import` ` asyncio`

`from` ` datetime ` `import` ` datetime, timedelta`

`import` ` requests`

`import` ` os`

`class`  ` `  `LongRunningTaskProcessor` `:`

`    ` `def` ` ` `__init__` `(self, sidecar_url: str):`

When calling APIs through the SDK, implement retry logic to handle transient errors, including

token expiration:

TypeScript

`        self.sidecar_url = sidecar_url`

`    `

`    ` `async`  ` `  `def`  ` `  `process_task` `(self, task_id: str, user_token: str):`

`        ``"""Process a long-running task using the user's token."""`

`        ` `try` `:`

`            ``# Step 1: Fetch data`

`            data = ` `await` ` self.fetch_data(user_token)`

`            `

`            ``# Step 2: Process (may take hours)`

`            ` `await` ` asyncio.sleep(3600)  ``# Simulate long processing`

`            result = ` `await` ` self.process_data(data)`

`            `

`            ``# Step 3: Upload result`

`            ` `await` ` self.upload_result(user_token, result)`

`            `

`            ``# Step 4: Notify user`

`            ` `await` ` self.notify_user(user_token, task_id)`

`            `

`        ` `except` ` Exception ` `as` ` e:`

`            print(`  `f"Task ``{task_id}` ` failed: ``{e}` `"` `)`

`            ``# Handle failure`

`    `

`    ` `async`  ` `  `def`  ` `  `fetch_data` `(self, token: str):`

`        ``"""Fetch data from API - token refresh handled by the SDK."""`

`        response = requests.get(`

`            ` `f"` `{self.sidecar_url}` `/DownstreamApi/Graph"` `,`

`            params={` `'optionsOverride.RelativePath'` `: ``'me/messages'` `},`

`            headers={` `'Authorization'` `: token}`

`        )`

`        response.raise_for_status()`

`        ` `return` ` response.json()`

`    `

`    ` `async`  ` `  `def`  ` `  `upload_result` `(self, token: str, result):`

`        ``"""Upload result to user's OneDrive."""`

`        response = requests.put(`

`            ` `f"` `{self.sidecar_url}` `/DownstreamApi/Graph"` `,`

`            params={` `'optionsOverride.RelativePath'` `: `

`'me/drive/root:/results/output.json:/content'` `},`

`            headers={` `'Authorization'` `: token},`

`            json=result`

`        )`

`        response.raise_for_status()`

**Token Expiration Handling**

`async`  ` `  `function`  ` `  `callApiWithRetry` `(`

`  token: ` `string` `,`

**Practice**

**Benefit**

**Store minimal context**

Only persist essential user information needed to complete the operation

**Encrypt stored tokens**

Protect tokens at rest using encryption to prevent unauthorized access

**Secure key**

**management**

Use secure key management practices for encryption keys

**Set context expiration**

Implement time limits on stored user contexts to avoid indefinite storage

**Access control**

Restrict access to stored user contexts to authorized processes only

**Handle refresh failures**

Detect when refresh tokens expire and notify users appropriately

**Monitor token usage**

Track refresh token consumption to understand token lifetime and usage

patterns

**Audit logging**

Log all token usage and long-running operations for compliance and

troubleshooting

**User consent**

Obtain and document user consent for long-running operations before

beginning

**Revocation support**

Allow users to cancel long-running operations and revoke token access

**Notify users**

Keep users informed of long-running task status, especially if operations fail

**Implement cleanup**

Remove completed task contexts from storage to prevent accumulation

`  apiCall: (token: ` `string` `) => ` `Promise`  `<`  `any`  `>,`

`  maxRetries: ` `number` ` = 3`

`): ` `Promise`  `<`  `any`  `> {`

`  ` `for` ` (`  `let` ` attempt = 1; attempt <= maxRetries; attempt++) {`

`    ` `try` ` {`

`      ` `return`  ` `  `await` ` apiCall(token);`

`    } ` `catch` ` (error) {`

`      ` `if` ` (attempt < maxRetries) {`

`        ``// Wait and retry`

`        ` `await`  ` `  `new`  ` `  `Promise` `(resolve => setTimeout(resolve, 1000 * attempt));`

`        ` `continue` `;`

`      }`

`      ` `throw` ` error;`

`    }`

`  }`

`}`

**Best practices and security**

ﾉ

**Expand table**

**Refresh token lifetime**: Refresh tokens have a maximum lifetime (typically 90 days),

limiting how long operations can run

**User consent revocation**: Users can revoke consent at any time, causing operations to fail

**Conditional access changes**: Administrators may change conditional access policies

during processing

**MFA interruptions**: Multi-factor authentication requirements may prevent token refresh

**Session termination**: User sessions may be terminated by administrators or security

policies

Ready to implement long-running OBO operations?

1\. Implement Agent Batch Processing \- Autonomous workflows for scheduled tasks

2\. Use Managed Identity \- For system-level operations without user context

3\. Review Security \- Token security and storage best practices

**Last updated on 11/14/2025**

**Limitations**

**Next steps**

**Scenario: Signed HTTP Requests (SHR)**

Use Signed HTTP Requests (SHR) with the Microsoft Entra SDK for AgentID to implement

proof-of-possession (PoP) token security. PoP tokens cryptographically bind tokens to a public

key, preventing token theft and replay attacks when calling downstream APIs.

An Azure account with an active subscription. Create an account for free

.

**Microsoft Entra SDK for AgentID** deployed and running with proof-of-possession

support enabled. See Installation Guide for setup instructions.

**RSA key pair** \- Generate a public/private key pair for cryptographic signing. The public

key is configured in the SDK, while the private key remains secure in your application.

**Downstream API supporting PoP tokens** \- The target API must validate proof-of-

possession tokens and verify signatures using the public key.

**Appropriate permissions in Microsoft Entra ID** \- Your account must have permissions to

register applications and configure PoP settings.

Before implementing PoP tokens, generate an RSA key pair. The private key remains in your

application for signing requests, while the public key is configured in the Microsoft Entra SDK

for AgentID:

Bash

Configure the Microsoft Entra SDK for AgentID with your RSA public key and downstream API

settings. Store sensitive keys in secure configuration stores:

**Prerequisites**

**Generate key pair**

`# Generate RSA private key`

`openssl genrsa -out private.pem 2048`

`# Extract public key`

`openssl rsa -`  `in` ` private.pem -pubout -out public.pem`

`# Base64 encode public key for configuration`

`base64 -w 0 public.pem > public.pem.b64`

`# View base64-encoded key`

`cat public.pem.b64`

**Configuration**

YAML

To use PoP tokens in your application, request a PoP token from the Microsoft Entra SDK for

AgentID by specifying your public key, then include it in API requests:

TypeScript

**SDK configuration**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `Secret`

`metadata:`

`  name:`  ` `  `shr-keys`

`type:`  ` `  `Opaque`

`data:`

`  public-key:`  ` `  `<base64-encoded-public-key>`

`---`

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `ConfigMap`

`metadata:`

`  name:`  ` `  `sidecar-config`

`data:`

`  ``# ... other configuration ...`

`  DownstreamApis__SecureApi__BaseUrl:` ` ` `"https://api.contoso.com"`

`  DownstreamApis__SecureApi__Scopes:` ` ` `"api://secureapi/.default"`

`  DownstreamApis__SecureApi__AcquireTokenOptions__PopPublicKey:` ` ` `"<base64-public-`

`key>"`

**Usage examples**

**TypeScript**

`// Request PoP token`

`async`  ` `  `function`  ` `  `getPopToken` `(incomingToken: ` `string` `, publicKey: ` `string` `): `

`Promise`  `<`  `string`  `> {`

`  ` `const` ` sidecarUrl = process.env.SIDECAR_URL!;`

`  `

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${sidecarUrl}` ``/AuthorizationHeader/SecureApi?` `` ` +`

`    `

`` `optionsOverride.AcquireTokenOptions.PopPublicKey=``  `${`  `encodeURIComponent` `(publicKey)}`  `` ` `` `,`

`    {`

`      headers: {`

`        ``'Authorization'` `: incomingToken`

`      }`

`    }`

`  );`

`  `

Python

`  ` `const` ` data = ` `await` ` response.json();`

`  ` `return` ` data.authorizationHeader; ``// Returns "PoP <pop-token>"`

`}`

`// Use PoP token with signed request`

`async`  ` `  `function`  ` `  `callSecureApi` `(incomingToken: ` `string` `, publicKey: ` `string` `, privateKey: `

`string` `) {`

`  ``// Get PoP token from the SDK`

`  ` `const` ` popToken = ` `await` ` getPopToken(incomingToken, publicKey);`

`  `

`  ``// Make request to API with PoP token`

`  ` `const` ` response = ` `await` ` fetch(` `'https://api.contoso.com/secure/data'` `, {`

`    headers: {`

`      ``'Authorization'` `: popToken`

`    }`

`  });`

`  `

`  ` `return`  ` `  `await` ` response.json();`

`}`

**Python**

`import` ` base64`

`import` ` requests`

`import` ` os`

`def`  ` `  `get_pop_token` `(incoming_token: str, public_key: str) -> str:`

`    ``"""Get a PoP token from the SDK."""`

`    sidecar_url = os.getenv(` `'SIDECAR_URL'` `, ``'http://localhost:5000'` `)`

`    `

`    response = requests.get(`

`        ` `f"` `{sidecar_url}` `/AuthorizationHeader/SecureApi"` `,`

`        params={`

`            ``'optionsOverride.AcquireTokenOptions.PopPublicKey'` `: public_key`

`        },`

`        headers={` `'Authorization'` `: incoming_token}`

`    )`

`    `

`    response.raise_for_status()`

`    data = response.json()`

`    ` `return` ` data[` `'authorizationHeader'` `]`

`def`  ` `  `call_secure_api` `(incoming_token: str, public_key_b64: str):`

`    ``"""Call API with PoP token."""`

`    pop_token = get_pop_token(incoming_token, public_key_b64)`

`    `

`    response = requests.get(`

`        ``'https://api.contoso.com/secure/data'` `,`

`        headers={` `'Authorization'` `: pop_token}`

`    )`

You can override PoP settings on a per-request basis by specifying different public keys for

different APIs or scopes:

TypeScript

Implement secure key management practices to protect your RSA keys and enable key rotation

when needed:

Store RSA keys securely using Kubernetes Secrets:

YAML

`    `

`    ` `return` ` response.json()`

**Per-request SHR**

`// Enable SHR for specific request`

`const` ` response = ` `await` ` fetch(`

`  ` `` ` ``  `${sidecarUrl}` ``/AuthorizationHeader/Graph?` `` ` +`

`  `

`` `optionsOverride.AcquireTokenOptions.PopPublicKey=``  `${`  `encodeURIComponent` `(publicKey)}`  `` ` `` `,`

`  {`

`    headers: { ``'Authorization'` `: incomingToken }`

`  }`

`);`

**Key management**

**Secure key storage**

`# Store keys in Kubernetes Secret`

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `Secret`

`metadata:`

`  name:`  ` `  `shr-keys`

`type:`  ` `  `Opaque`

`data:`

`  public-key:`  ` `  `<base64-encoded-public-key>`

`  private-key:`  ` `  `<base64-encoded-private-key>`

`---`

`# Mount keys in application`

`volumes:`

`- name:`  ` `  `shr-keys`

`  secret:`

`    secretName:`  ` `  `shr-keys`

Rotate signing keys periodically using OpenSSL and update configurations:

Bash

The downstream API must validate the PoP token to ensure it's correctly signed and bound to

the request:

1\. Verify JWT signature using the public key extracted from the token

2\. Validate standard JWT claims (issuer, audience, expiration)

3\. Verify the `cnf` claim contains the expected public key

4\. Validate that the HTTP request signature matches using the key from the `cnf` claim

Implementing Signed HTTP Requests with proof-of-possession tokens provides several security

advantages:

`    defaultMode:` ` 0400`

`containers:`

`- name:`  ` `  `app`

`  volumeMounts:`

`  - name:`  ` `  `shr-keys`

`    mountPath:` ` ` `/keys`

`    readOnly:`  ` `  `true`

**Key rotation**

`#!/bin/bash`

`# Script to rotate SHR keys`

`# Generate new key pair`

`openssl genrsa -out private-new.pem 2048`

`openssl rsa -`  `in` ` private-new.pem -pubout -out public-new.pem`

`base64 -w 0 public-new.pem > public-new.pem.b64`

`# Update Kubernetes secret`

`kubectl create secret generic shr-keys-new \`

`  --from-file=public-key=public-new.pem.b64 \`

`  --from-file=private-key=private-new.pem \`

`  --dry-run=client -o yaml | kubectl apply -f -`

`# Update deployment to use new keys`

`kubectl rollout restart deployment myapp`

**Validating PoP tokens**

**Benefits**

**Token Binding**: Each token is cryptographically bound to a specific public key, preventing

unauthorized use even if intercepted.

**Replay Prevention**: An attacker cannot replay a captured token without possessing the

corresponding private key.

**Enhanced Security**: Provides protection against token theft, especially important for

sensitive operations and high-security environments.

**Proof of Possession**: Cryptographically proves that the client holds the private key

corresponding to the token.

When implementing Signed HTTP Requests, follow these practices to maintain security and

operational reliability:

**Secure Private Keys**: Never expose private keys in logs, configuration files, or code

repositories. Store them securely using key vaults or configuration management systems.

**Rotate Keys Regularly**: Implement a key rotation schedule to minimize the impact of

potential key compromise. Update both the SDK and downstream APIs during rotation.

**Use Per-API Keys**: Use different key pairs for different APIs or security zones to limit the

impact if one key is compromised.

**Monitor Usage**: Audit and monitor PoP token usage to detect suspicious patterns or

unauthorized access attempts.

**Test Thoroughly**: Verify that PoP token validation works correctly before deploying to

production, ensuring both signature validation and request binding checks pass.

After implementing PoP tokens:

Review Security

Configure the Microsoft Entra SDK for AgentID

Troubleshoot Issues

**Last updated on 11/14/2025**

**Best practices**

**Next steps**

**Scenario: Agent Autonomous Batch**

**Processing**

Implement autonomous batch processing using agent identities to perform operations without

user context. This scenario enables batch processing of large data volumes, scheduled tasks via

cron jobs, background operations outside user sessions, and secure service-to-system

workflows. This guide shows you how to configure the Microsoft Entra SDK for AgentID and

implement common patterns like scheduled jobs and queue-based processing.

An Azure account with an active subscription. Create an account for free

.

**Microsoft Entra SDK for AgentID** deployed in your environment with agent identity

support enabled. See Installation Guide for setup instructions.

**Registered application in Microsoft Entra ID** \- Register a new app in the Microsoft Entra

admin center

for your batch service. Refer to Register an application for details. Record:

Application (client) ID

Directory (tenant) ID

Create a client secret or certificate for authentication

Configure application permissions for the downstream APIs your batch job will access

(e.g., Microsoft Graph permissions)

**Appropriate permissions in Microsoft Entra ID** \- Your account must have permissions to

register applications, configure agent identities, and grant application permissions.

**Access to downstream APIs** \- Target APIs (such as Microsoft Graph) must be accessible

and configured with the required scopes for your batch operations.

For details on creating agent identities and configuring federated identity credentials, see the

Microsoft agent identity platform documentation.

When setting up an agent identity for batch processing:

1\. **Federated Identity Credentials**: Configure workload identity federation to allow your

application to obtain tokens without storing secrets

2\. **Application Permissions**: Grant the agent identity only the Microsoft Graph API

permissions (or other downstream API permissions) that the batch operation requires

**Prerequisites**

**Agent identity setup**

**Key configuration requirements**

3\. **Environment Variables**: Set `ENTRA_SDK_URL` to point to your running Microsoft Entra SDK

for AgentID instance, and store the agent `CLIENT_ID` for use in your batch processing

code

4\. **Token Scope**: Ensure the Microsoft Entra SDK for AgentID is configured to request tokens

in the service principal's context, not on behalf of a user

The following code snippets demonstrate how to implement autonomous batch processing

with agent identities. The key principle is to pass the agent identity to the Microsoft Entra SDK

for AgentID and request an application token instead of a user-delegated token.

Request an application token using the agent identity to process batch operations:

TypeScript

**Implementation**

**TypeScript**

`async`  ` `  `function`  ` `  `processBatchWithAgent` `(`

`  incomingToken: ` `string` `,`

`  agentIdentity: ` `string`

`) {`

`  ` `const` ` sdkUrl = process.env.ENTRA_SDK_URL!;`

`  `

`  ``// Get users list using agent identity (autonomous)`

`  ` `const` ` response = ` `await` ` fetch(`

`    ` `` ` ``  `${sdkUrl}` ``/DownstreamApi/Graph?` `` ` +`

`    ` `` `AgentIdentity=``  `${agentIdentity}` ``&` `` ` +`

`    ` `` `optionsOverride.RelativePath=users&` `` ` +`

`    ` `` `optionsOverride.RequestAppToken=true` `` `,`

`    {`

`      headers: {`

`        ``'Authorization'` `: incomingToken`

`      }`

`    }`

`  );`

`  `

`  ` `const` ` result = ` `await` ` response.json();`

`  ` `const` ` users = ` `JSON` `.parse(result.content);`

`  `

`  ``// Process each user`

`  ` `for` ` (`  `const` ` user of users.value) {`

`    ` `await` ` processUser(user);`

`  }`

`}`

`async`  ` `  `function`  ` `  `scheduledReportGeneration` `() {`

`  ` `const` ` agentIdentity = process.env.AGENT_CLIENT_ID!;`

Here's the equivalent implementation in Python using the requests library:

Python

Different scenarios call for different batch processing approaches. The following code snippets

provide patterns for the most common implementations that leverage agent identities.

`  ` `const` ` token = ` `await` ` getSystemToken();`

`  `

`  ``// Generate reports for all departments`

`  ` `const` ` departments = ` `await` ` getDepartments(token, agentIdentity);`

`  `

`  ` `for` ` (`  `const` ` dept of departments) {`

`    ` `await` ` generateDepartmentReport(token, agentIdentity, dept);`

`  }`

`}`

**Python**

`import` ` requests`

`import` ` os`

`import` ` json`

`def`  ` `  `process_batch_with_agent` `(incoming_token: str, agent_identity: str):`

`    ``"""Process batch using autonomous agent."""`

`    sdk_url = os.getenv(` `'ENTRA_SDK_URL'` `, ``'http://localhost:5000'` `)`

`    `

`    ``# Get users using agent identity`

`    response = requests.get(`

`        ` `f"` `{sdk_url}` `/DownstreamApi/Graph"` `,`

`        params={`

`            ``'AgentIdentity'` `: agent_identity,`

`            ``'optionsOverride.RelativePath'` `: ``'users'` `,`

`            ``'optionsOverride.RequestAppToken'` `: ``'true'`

`        },`

`        headers={` `'Authorization'` `: incoming_token}`

`    )`

`    `

`    result = response.json()`

`    users = json.loads(result[` `'content'` `])`

`    `

`    ``# Process each user`

`    ` `for` ` user ` `in` ` users[` `'value'` `]:`

`        process_user(user)`

**Batch processing patterns**

**Scheduled job**

Use scheduled jobs when you need to run batch operations at specific times:

TypeScript

Use queue-based processing when batch items arrive asynchronously or unpredictably:

TypeScript

1\. **Use application permissions**: Grant only the application permissions required for the

batch operation, following the principle of least privilege

`// Cron-based batch processor`

`import` ` cron ` `from` ` ` `'node-cron'` `;`

`// Run every day at 2 AM`

`cron.schedule(` `'0 2 * * *'` `, ` `async` ` () => {`

`  ` `console` `.log(` `'Starting nightly batch process'` `);`

`  `

`  ` `try` ` {`

`    ` `await` ` runAutonomousBatch(`

`      process.env.AGENT_CLIENT_ID!`

`    );`

`    ` `console` `.log(` `'Batch completed successfully'` `);`

`  } ` `catch` ` (error) {`

`    ` `console` `.error(` `'Batch failed:'` `, error);`

`  }`

`});`

**Queue-based processing**

`// Process messages from queue`

`async`  ` `  `function`  ` `  `processQueueMessages` `(queueClient, agentIdentity: ` `string` `) {`

`  ` `while` ` (`  `true` `) {`

`    ` `const` ` messages = ` `await` ` queueClient.receiveMessages(10);`

`    `

`    ` `for` ` (`  `const` ` message of messages) {`

`      ` `try` ` {`

`        ` `await` ` processMessage(message, agentIdentity);`

`        ` `await` ` queueClient.deleteMessage(message);`

`      } ` `catch` ` (error) {`

`        ` `console` `.error(` `'Message processing failed:'` `, error);`

`      }`

`    }`

`    `

`    ` `await` ` sleep(5000);`

`  }`

`}`

**Best practices**

2\. **Implement retry logic**: Handle transient failures with exponential backoff to improve

reliability

3\. **Monitor progress**: Track batch job progress and log key metrics to enable

troubleshooting and performance analysis

4\. **Limit scope**: Request only the necessary permissions for each operation

5\. **Audit operations**: Log all agent actions with details about what was processed and by

which agent

6\. **Handle throttling**: Respect API rate limits and implement appropriate backoff strategies

Ready to deploy batch processing with agent identities? Follow these guides:

1\. Configure Agent Identities \- Learn how to set up and manage agent identity

configurations

2\. Review Security \- Understand agent security patterns and best practices for protecting

your batch operations

3\. Troubleshoot Issues \- Resolve common issues with agent-based batch processing

**Last updated on 11/18/2025**

**Next steps**

**Security Best Practices: Hardening the**

**Microsoft Entra SDK for AgentID**

This guide provides comprehensive security configuration and hardening best practices for

safely deploying and operating the Microsoft Entra SDK for AgentID in production

environments. It covers essential security controls including network isolation, credential

management, token validation, runtime security, and monitoring to ensure your SDK

deployment follows security best practices.

The Microsoft Entra SDK for AgentID is designed with security in mind, but its safety depends

on proper configuration and deployment practices. Follow these best practices to ensure a

secure deployment:

Network isolation is critical for protecting authentication operations. The Microsoft Entra SDK

for AgentID must run within trusted boundaries with strict access controls and comprehensive

traffic filtering. This includes localhost-only binding, pod-internal communication, and network

policies that prevent unauthorized access to authentication endpoints.

Ｕ **Caution**

The Microsoft Entra SDK for AgentID API must **never** be publicly accessible. It should only

be reachable by applications within the same trust boundary (e.g., same pod, same virtual

network). By default the allowed hosts is localhost. Exposing this API publicly can enable

**unauthorized token acquisition**, which is a critical security risk. Also note that all the

applications within the same trust boundary wil have access to this API. Ensure that every

applicaiton in that boundary is trusted and property secured.

**Is it safe to run the SDK?**

Run only in containerized environments

＂

Restrict access to localhost/pod-internal only

＂

Use Kubernetes Network Policies

＂

Store credentials securely (Key Vault, Secrets)

＂

Run as non-root user

＂

Enable audit logging

＂

**Network Security**

**Restrict SDK Access**

Configure Kestrel to listen only on localhost only to prevent external network access to

authentication endpoints:

YAML

Alternatively, use Kestrel's host filtering with AllowedHosts to restrict access:

YAML

Configure your application to communicate with the Microsoft Entra SDK for AgentID via

localhost to ensure traffic remains within the same pod and doesn't traverse the network:

YAML

Never expose via LoadBalancer or Ingress (this would allow unauthorized token acquisition

from outside the trusted boundary):

YAML

`containers:`

`- name:`  ` `  `sidecar`

`  image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`  env:`

`  - name:`  ` `  `Kestrel__Endpoints__Http__Url`

`    value:` ` ` `"http://127.0.0.1:5000"`

`containers:`

`- name:`  ` `  `sidecar`

`  image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`  env:`

`  - name:`  ` `  `AllowedHosts`

`    value:` ` ` `"localhost;127.0.0.1"`

**Use Pod-Local Communication**

`containers:`

`- name:`  ` `  `app`

`  env:`

`  - name:`  ` `  `SIDECAR_URL`

`    value:` ` ` `"http://localhost:5000"` ` ` `# Pod-local communication only`

`# WRONG - exposes Microsoft Entra SDK for AgentID publicly`

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `Service`

`metadata:`

`  name:`  ` `  `sidecar-service`

`spec:`

`  type:`  ` `  `LoadBalancer` ` ` `# Exposes SDK publicly - INSECURE`

Secure credential management is fundamental for SDK security. Use managed identities

whenever possible to eliminate secrets, and follow the principle of least privilege when

configuring authentication credentials.

Use Azure AD Workload Identity for containerized deployments (AKS) to eliminate secrets

entirely and ensure secure credential management with file-based token projection:

YAML

`  selector:`

`    app:`  ` `  `myapp`

`  ports:`

`  - port:` ` 5000`

**Credential Management**

**Prefer Workload Identity for Containers**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `ServiceAccount`

`metadata:`

`  name:`  ` `  `myapp-sa`

`  annotations:`

`    ` `azure.workload.identity/client-id:` ` ` `"<managed-identity-client-id>"`

`---`

`apiVersion:`  ` `  `apps/v1`

`kind:`  ` `  `Deployment`

`metadata:`

`  name:`  ` `  `myapp`

`spec:`

`  template:`

`    metadata:`

`      labels:`

`        ` `azure.workload.identity/use:` ` ` `"true"`

`    spec:`

`      serviceAccountName:`  ` `  `myapp-sa`

`      containers:`

`      - name:`  ` `  `sidecar`

`        image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`        env:`

`        - name:`  ` `  `AzureAd__ClientId`

`          value:` ` ` `"<web-api-client-id>"`

`        `

`        ``# Workload Identity credentials - uses file-based token projection`

`        - name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`          value:` ` ` `"SignedAssertionFilePath"`

**Benefits**: Workload identity eliminates the need to store or rotate secrets while providing

automatic credential management, Azure RBAC integration, and a full audit trail. The token is

automatically projected to the pod by the workload identity webhook, and the SDK reads it

using the `SignedAssertionFilePath` credential type. This approach significantly reduces security

risks and operational overhead compared to traditional secret-based authentication.

**Note**: For Azure VMs and App Services (non-containerized environments), use system or user-

assigned managed identities with the `SignedAssertionFromManagedIdentity` credential type

instead. For more information, see Use Managed Identity.

Prefer certificates for authentication when client secrets cannot be avoided. Certificates provide

stronger security than client secrets because they use public-key cryptography and are more

difficult to extract or misuse. Store certificates in Azure Key Vault for centralized management

and automatic renewal:

YAML

**Benefits**: Azure Key Vault provides centralized certificate management with automated

rotation, access policies, and comprehensive auditing, while ensuring certificates are never

embedded in container images. For more information, see Use Certificates for Authentication.

Kubernetes Secrets is suitable option for storing client secrets if managed identities or

certificates are not an option, although ensure secrets are encrypted at rest and access is

tightly controlled:

YAML

**Use Certificates Over Secrets**

`- name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`  value:` ` ` `"KeyVault"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__KeyVaultUrl`

`  value:` ` ` `"https://your-keyvault.vault.azure.net"`

`- name:`  ` `  `AzureAd__ClientCredentials__0__KeyVaultCertificateName`

`  value:` ` ` `"your-cert-name"`

**Store Secrets Securely**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `Secret`

`metadata:`

`  name:`  ` `  `app-cert`

`type:`  ` `  `Opaque`

`data:`

`  ` `certificate.pfx:`  ` `  `<base64-encoded-pfx>`

If client secrets must be used, implement additional security measures to minimize risk. Client

secrets are less secure than managed identities or certificates, so they require extra protection

including short expiration periods, secure storage with encryption at rest, restricted access

through RBAC, and frequent rotation schedules. Never store secrets in container images or

environment variables visible in deployment manifests:

YAML

`  ` `certificate.password:`  ` `  `<base64-encoded-password>`

`---`

`containers:`

`- name:`  ` `  `sidecar`

`  volumeMounts:`

`  - name:`  ` `  `cert-volume`

`    mountPath:` ` ` `/certs`

`    readOnly:`  ` `  `true`

`  env:`

`  - name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`    value:` ` ` `"Path"`

`  - name:`  ` `  `AzureAd__ClientCredentials__0__CertificateDiskPath`

`    value:` ` ` `"/certs/certificate.pfx"`

`  - name:`  ` `  `AzureAd__ClientCredentials__0__CertificatePassword`

`    valueFrom:`

`      secretKeyRef:`

`        name:`  ` `  `app-cert`

`        key:`  ` `  `certificate.password`

`volumes:`

`- name:`  ` `  `cert-volume`

`  secret:`

`    secretName:`  ` `  `app-cert`

`    items:`

`    - key:`  ` `  `certificate.pfx`

`      path:`  ` `  `certificate.pfx`

`    defaultMode:` ` 0400  ``# Read-only for owner`

**Client Secrets (Avoid if possible)**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `Secret`

`metadata:`

`  name:`  ` `  `app-secrets`

`type:`  ` `  `Opaque`

`stringData:`

`  client-secret:` ` ` `"<your-client-secret>"`

`---`

`containers:`

`- name:`  ` `  `sidecar`

`  env:`

Token security ensures that only valid, appropriately-scoped tokens are accepted and

processed by the SDK. Implement token validation, scope requirements, and audience checks

to prevent unauthorized access and limit token misuse.

Require specific scopes for incoming tokens (space separated):

YAML

Configure expected audience for token validation:

YAML

`  - name:`  ` `  `AzureAd__ClientCredentials__0__SourceType`

`    value:` ` ` `"ClientSecret"`

`  - name:`  ` `  `AzureAd__ClientCredentials__0__ClientSecret`

`    valueFrom:`

`      secretKeyRef:`

`        name:`  ` `  `app-secrets`

`        key:`  ` `  `client-secret`

Ｕ **Caution**

Never commit secrets to source control. Use external secret management (Azure Key

Vault, Sealed Secrets, etc.).

**Token Security**

**Enable Scope Validation**

`- name:`  ` `  `AzureAd__Scopes`

`  value:` ` ` `"access_as_user"`

**Set Appropriate Audience**

`- name:`  ` `  `AzureAd__Audience`

`  value:` ` ` `"api://your-api-id"`

７ **Note**

The expected audience value depends on your app registration's

**requestedAccessTokenVersion**:

Always call `/Validate` before accepting user tokens:

Bash

Runtime security controls protect the SDK container from modification, privilege escalation,

and unauthorized capability access. Configure the container to run with minimal privileges and

read-only filesystems to reduce the attack surface.

Prevent modification of container filesystem:

YAML

Enforce security standards:

YAML

**Version 2**: Use the `{ClientId}` value directly

**Version 1** or **null**: Use the App ID URI (typically `api://{ClientId}` unless you

customized it)

**Validate Tokens Before Use**

`GET /Validate`

`Authorization: Bearer <user-token>`

**Runtime Security**

**Read-Only Root Filesystem**

`securityContext:`

`  readOnlyRootFilesystem:`  ` `  `true`

**Pod Security Policy**

`apiVersion:`  ` `  `policy/v1beta1`

`kind:`  ` `  `PodSecurityPolicy`

`metadata:`

`  name:`  ` `  `sidecar-psp`

`spec:`

`  privileged:`  ` `  `false`

`  allowPrivilegeEscalation:`  ` `  `false`

`  requiredDropCapabilities:`

`  -`  ` `  `ALL`

Effective logging and monitoring enable you to detect anomalies, troubleshoot issues, and

maintain audit trails for compliance. Configure appropriate logging levels for your environment

and implement health probes to ensure the SDK operates as expected.

Production environment:

YAML

Development environment (verbose):

YAML

Configure liveness and readiness probes:

YAML

`  runAsUser:`

`    rule:` ` ` `'MustRunAsNonRoot'`

`  seLinux:`

`    rule:` ` ` `'MustRunAs'`

`  fsGroup:`

`    rule:` ` ` `'MustRunAs'`

`  readOnlyRootFilesystem:`  ` `  `true`

**Logging and Monitoring**

**Configure Appropriate Logging**

`- name:`  ` `  `Logging__LogLevel__Default`

`  value:` ` ` `"Warning"`

`- name:`  ` `  `Logging__LogLevel__Microsoft.Identity.Web`

`  value:` ` ` `"Information"`

`- name:`  ` `  `Logging__LogLevel__Default`

`  value:` ` ` `"Debug"`

`- name:`  ` `  `ASPNETCORE_ENVIRONMENT`

`  value:` ` ` `"Development"`

**Enable Health Monitoring**

`livenessProbe:`

`  httpGet:`

`    path:` ` ` `/health`

`    port:` ` 5000`

`  initialDelaySeconds:` ` 10`

`  periodSeconds:` ` 10`

Use this comprehensive checklist to ensure your SDK deployment follows all recommended

security practices across network, credentials, tokens, runtime, and monitoring dimensions.

Network:

\[ \] SDK listens only on localhost/127.0.0.1

\[ \] Never exposed via LoadBalancer or Ingress

\[ \] Network policies restrict external access

\[ \] HTTPS/TLS for external communication

Credentials:

\[ \] Use Workload Identity for containers (AKS, Kubernetes, Docker) with

`SignedAssertionFilePath`

\[ \] Use Managed Identity for VMs/App Services with `SignedAssertionFromManagedIdentity`

\[ \] Prefer certificates over secrets

\[ \] Secrets stored in secure management system

\[ \] Regular credential rotation

Tokens:

\[ \] Scope validation enabled

\[ \] Audience validation configured

\[ \] Tokens validated before use

Runtime:

\[ \] Container runs as non-root

\[ \] Read-only root filesystem

\[ \] Security context applied

\[ \] Resource limits set

Monitoring:

`  failureThreshold:` ` 3`

`readinessProbe:`

`  httpGet:`

`    path:` ` ` `/health`

`    port:` ` 5000`

`  initialDelaySeconds:` ` 5`

`  periodSeconds:` ` 5`

`  failureThreshold:` ` 3`

**Best Practices Checklist**

\[ \] Appropriate logging configured

\[ \] Health checks enabled

\[ \] Audit logging enabled

\[ \] Alerts configured

Reference implementations demonstrate how to combine multiple security controls into

cohesive deployment patterns. These patterns serve as templates for production deployments

in various threat models.

YAML

**Common Security Patterns**

**High-Security Deployment**

`apiVersion:`  ` `  `v1`

`kind:`  ` `  `ServiceAccount`

`metadata:`

`  name:`  ` `  `secure-app-sa`

`  annotations:`

`    ` `azure.workload.identity/client-id:` ` ` `"<managed-identity-id>"`

`---`

`apiVersion:`  ` `  `apps/v1`

`kind:`  ` `  `Deployment`

`metadata:`

`  name:`  ` `  `secure-app`

`spec:`

`  template:`

`    metadata:`

`      labels:`

`        ` `azure.workload.identity/use:` ` ` `"true"`

`    spec:`

`      serviceAccountName:`  ` `  `secure-app-sa`

`      securityContext:`

`        fsGroup:` ` 2000`

`      containers:`

`      - name:`  ` `  `sidecar`

`        image:`  ` `  `mcr.microsoft.com/entra-sdk/auth-sidecar:1.0.0`

`        ports:`

`        - containerPort:` ` 5000`

`        env:`

`        - name:`  ` `  `Kestrel__Endpoints__Http__Url`

`          value:` ` ` `"http://127.0.0.1:5000"`

`        - name:`  ` `  `AzureAd__TenantId`

`          valueFrom:`

`            configMapKeyRef:`

`              name:`  ` `  `app-config`

`              key:`  ` `  `tenant-id`

Rotating credentials reduces the window of opportunity for attackers if credentials are leaked

or compromised. The rotation frequency depends on the credential type and your

organization's security policy:

**Client secrets**: Every 90 days (recommended)

**Certificates**: Before expiration, typically every 1-2 years

**Keys for Signed HTTP Requests (SHR)**: Follow your organization's security policy

**Implementation guidance**: Use Azure Key Vault with automated rotation capabilities or

integrate external secret managers (such as Sealed Secrets) into your deployment pipeline. This

minimizes manual intervention and ensures consistent rotation schedules.

If you suspect that credentials have been compromised, follow these steps immediately to

contain the incident and prevent unauthorized access:

1\. **Revoke compromised credentials in Microsoft Entra ID** \- Remove the credentials from

the application registration to block their use immediately.

2\. **Generate new credentials** \- Create new client secrets or certificates in Microsoft Entra ID

to replace the compromised ones.

`        - name:`  ` `  `AzureAd__ClientId`

`          value:` ` ` `"<managed-identity-client-id>"`

`        securityContext:`

`          runAsNonRoot:`  ` `  `true`

`          runAsUser:` ` 1000`

`          readOnlyRootFilesystem:`  ` `  `true`

`          allowPrivilegeEscalation:`  ` `  `false`

`          capabilities:`

`            drop:`

`            -`  ` `  `ALL`

`        resources:`

`          requests:`

`            memory:` ` ` `"128Mi"`

`            cpu:` ` ` `"100m"`

`          limits:`

`            memory:` ` ` `"256Mi"`

`            cpu:` ` ` `"250m"`

`        livenessProbe:`

`          httpGet:`

`            path:` ` ` `/health`

`            port:` ` 5000`

`          initialDelaySeconds:` ` 10`

`          periodSeconds:` ` 10`

**Rotate credentials regularly**

**Respond to compromised credentials**

3\. **Update your secrets management system** \- Store the new credentials in Kubernetes

Secrets or Azure Key Vault with appropriate access controls.

4\. **Redeploy SDK containers** \- Update your deployments to use the new credentials,

ensuring all running instances pick up the changes.

5\. **Review access logs** \- Check Azure Monitor and Kubernetes audit logs for signs of

unauthorized token requests or suspicious activity during the compromise window.

6\. **Document the incident** \- Record details of the incident (when discovered, how it

happened, what was accessed) and follow your organization's incident response

procedures to prevent recurrence.

Installation Guide

Configuration Reference

Endpoints Reference

Troubleshooting

**Last updated on 11/14/2025**

**See Also**

**Endpoints Reference: Microsoft Entra SDK for**

**AgentID HTTP API**

This document provides complete reference for the HTTP endpoints exposed by the Microsoft Entra SDK for AgentID.

**OpenAPI specification**: Available at `/openapi/v1.json` (development environment) and in the repository:

https://github.com/AzureAD/microsoft-identity-

web/blob/master/src/Microsoft.Identity.Web.Sidecar/OpenAPI/Microsoft.Identity.Web.AgentID.json

Use it to:

Generate client code

Validate requests

Discover available endpoints

**Endpoint**

**Method(s)**

**Purpose**

**Auth**

**Required**

`/Validate`

GET

Validate an inbound bearer token and return claims

Yes

`/AuthorizationHeader/{serviceName}`

GET

Validate inbound token (if present) and acquire an

authorization header for a downstream API

Yes

`/AuthorizationHeaderUnauthenticated/{serviceName}`

GET

Acquire an authorization header (app or agent

identity) with no inbound user token

Yes

`/DownstreamApi/{serviceName}`

GET, POST, PUT,

PATCH, DELETE

Validate inbound token (if present) and call

downstream API with automatic token acquisition

Yes

`/DownstreamApiUnauthenticated/{serviceName}`

GET, POST, PUT,

PATCH, DELETE

Call downstream API (app or agent identity only)

Yes

`/healthz`

GET

Health probe (liveness/readiness)

No

`/openapi/v1.json`

GET

OpenAPI 3.0 document

No (Dev

only)

All token acquisition and validation endpoints require a bearer token in the `Authorization` header unless explicitly marked

unauthenticated:

HTTP

Tokens are validated against configured Microsoft Entra ID settings (tenant, audience, issuer, scopes if enabled).

**API Specification**

**Endpoint Overview**

ﾉ

**Expand table**

**Authentication**

`GET /AuthorizationHeader/Graph`

`Authorization` `: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

`/Validate`

Validates the inbound bearer token and returns its claims.

HTTP

JSON

JSON

JSON

Acquires an access token for the configured downstream API and returns it as an authorization header value. If a user bearer

token is provided inbound, OBO (delegated) is used; otherwise app context patterns apply (if enabled).

**Request**

`GET` ` ` `/Validate` ` HTTP/1.1`

`Authorization` `: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

**Successful Response (200)**

`{`

`  ``"protocol"` `: ``"Bearer"` `,`

`  ``"token"` `: ``"eyJ0eXAiOiJKV1QiLCJhbGc..."` `,`

`  ``"claims"` `: {`

`    ``"aud"` `: ``"api://your-api-id"` `,`

`    ``"iss"` `: ``"https://sts.windows.net/tenant-id/"` `,`

`    ``"iat"` `: 1234567890,`

`    ``"nbf"` `: 1234567890,`

`    ``"exp"` `: 1234571490,`

`    ``"acr"` `: ``"1"` `,`

`    ``"appid"` `: ``"client-id"` `,`

`    ``"appidacr"` `: ``"1"` `,`

`    ``"idp"` `: ``"https://sts.windows.net/tenant-id/"` `,`

`    ``"oid"` `: ``"user-object-id"` `,`

`    ``"tid"` `: ``"tenant-id"` `,`

`    ``"scp"` `: ``"access_as_user"` `,`

`    ``"sub"` `: ``"subject"` `,`

`    ``"ver"` `: ``"1.0"`

`  }`

`}`

**Error Examples**

`// 400 Bad Request - No token`

`{`

`  ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.1"` `,`

`  ``"title"` `: ``"Bad Request"` `,`

`  ``"status"` `: 400,`

`  ``"detail"` `: ``"No token found"`

`}`

`// 401 Unauthorized - Invalid token`

`{`

`  ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.1"` `,`

`  ``"title"` `: ``"Unauthorized"` `,`

`  ``"status"` `: 401`

`}`

`/AuthorizationHeader/{serviceName}`

**Path Parameter**

`serviceName` – Name of the downstream API in configuration

**Parameter**

**Type**

**Description**

**Example**

`optionsOverride.Scopes`

string\[\]

Override

configured

scopes

(repeatable)

`?`

`optionsOverride.Scopes=User.Read&optionsOverride.Scopes=Mail.Read`

`optionsOverride.RequestAppToken`

boolean

Force app-

only token

(skip OBO)

`?optionsOverride.RequestAppToken=true`

`optionsOverride.AcquireTokenOptions.Tenant`

string

Override

tenant ID

`?optionsOverride.AcquireTokenOptions.Tenant=tenant-guid`

`optionsOverride.AcquireTokenOptions.PopPublicKey`

string

Enable

PoP/SHR

(base64

public key)

`?optionsOverride.AcquireTokenOptions.PopPublicKey=base64key`

`optionsOverride.AcquireTokenOptions.PopClaims`

string

Additional

PoP claims

(JSON)

`?optionsOverride.AcquireTokenOptions.PopClaims={"nonce":"abc"}`

**Parameter**

**Type**

**Description**

**Example**

`AgentIdentity`

string

Agent app (client) ID

`?AgentIdentity=11111111-2222-3333-4444-555555555555`

`AgentUsername`

string

User principal name (delegated agent)

`?AgentIdentity=<id>&AgentUsername=user@contoso.com`

`AgentUserId`

string

User object ID (delegated agent)

`?AgentIdentity=<id>&AgentUserId=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`

Rules:

`AgentUsername` or `AgentUserId` require `AgentIdentity` (user agent).

`AgentUsername` and `AgentUserId` are mutually exclusive.

`AgentIdentity` alone = autonomous agent.

`AgentIdentity` \+ user inbound token = delegated agent.

Basic request:

HTTP

**Query Parameters**

**Standard Overrides**

ﾉ

**Expand table**

**Agent Identity**

ﾉ

**Expand table**

**Examples**

`GET` ` ` `/AuthorizationHeader/Graph` ` HTTP/1.1`

`Authorization` `: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

HTTP

HTTP

JSON

PoP/SHR response:

JSON

Same behavior and parameters as `/AuthorizationHeader/{serviceName}` but no inbound user token is expected. Used for app-

only or autonomous/agent identity acquisition without a user context. Avoids the overhead of validating a user token.

HTTP

JSON

Acquires an access token and performs an HTTP request to the downstream API. Returns status code, headers, and body from the

downstream response. Supports user OBO, app-only, or agent identity patterns.

`serviceName` – Configured downstream API name.

`GET` ` ` `/AuthorizationHeader/Graph?optionsOverride.RequestAppToken=true` ` HTTP/1.1`

`Authorization` `: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

`GET` ` ` `/AuthorizationHeader/Graph?AgentIdentity=agent-id` ` HTTP/1.1`

`Authorization` `: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

**Response**

`{`

`  ``"authorizationHeader"` `: ``"Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."`

`}`

`{`

`  ``"authorizationHeader"` `: ``"PoP eyJ0eXAiOiJhdCtqd3QiLCJhbGc..."`

`}`

`/AuthorizationHeaderUnauthenticated/{serviceName}`

**Request**

`GET` ` ` `/AuthorizationHeaderUnauthenticated/Graph` ` HTTP/1.1`

**Response**

`{`

`  ``"authorizationHeader"` `: ``"Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."`

`}`

`/DownstreamApi/{serviceName}`

**Path Parameter**

**Parameter**

**Type**

**Description**

**Example**

`optionsOverride.HttpMethod`

string

Override HTTP method

`?optionsOverride.HttpMethod=POST`

`optionsOverride.RelativePath`

string

Append relative path to configured BaseUrl

`?optionsOverride.RelativePath=me/messages`

`optionsOverride.CustomHeader.<Name>`

string

Add custom header(s)

`?optionsOverride.CustomHeader.X-Custom=value`

Body is passed through unchanged:

HTTP

JSON

JSON

Errors mirror `/AuthorizationHeader` plus downstream API error status codes.

Same as `/DownstreamApi/{serviceName}` but no inbound user token is validated. Use for app-only or autonomous agent

operations.

Basic health probe endpoint.

**Healthy (200):**

**Additional Query Parameters (in addition to** `/AuthorizationHeader`

**parameters)**

ﾉ

**Expand table**

**Request Body Forwarding**

`POST` ` ` `/DownstreamApi/Graph?optionsOverride.RelativePath=me/messages` ` HTTP/1.1`

`Authorization` `: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

`Content-Type` `: application/json`

`{ `

`  ``"subject"` `: ``"Hello"` `, `

`   ``"body"` `: { ``"contentType"` `: ``"Text"` `, ``"content"` `: ``"Hello world"` ` } `

`}`

**Response**

`{`

`  ``"statusCode"` `: 200,`

`  ``"headers"` `: {`

`    ``"content-type"` `: ``"application/json"`

`  },`

`  ``"content"` `: ``"{\"@odata.context\":\"...\",\"displayName\":\"...\"}"`

`}`

`/DownstreamApiUnauthenticated/{serviceName}`

**/healthz**

**Response**

HTTP

**Unhealthy (503):**

HTTP

Returns OpenAPI 3.0 specification (development environment only). Use to:

Generate client code

Validate requests

Discover endpoints

Missing service name:

JSON

JSON

`HTTP/1.1 200 OK`

`HTTP/1.1 503 Service Unavailable`

`/openapi/v1.json`

**Common Error Patterns**

**Bad Request (400)**

`// 400 Bad Request - Missing service name`

`{ ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.1"` `, ``"title"` `: ``"Bad Request"` `, ``"status"` `: 400, ``"detail"` `: `

`"Service name is required"` ` }`

`// 400 Bad Request - Invalid agent combination`

`{ ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.1"` `, ``"title"` `: ``"Bad Request"` `, ``"status"` `: 400, ``"detail"` `: `

`"AgentUsername and AgentUserId are mutually exclusive"` ` }`

`// 401 Unauthorized - Invalid token`

`{ ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.1"` `, ``"title"` `: ``"Unauthorized"` `, ``"status"` `: 401 }`

`// 403 Forbidden - Missing scope`

`{ ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.3"` `, ``"title"` `: ``"Forbidden"` `, ``"status"` `: 403, ``"detail"` `: ``"The `

`scope 'access_as_user' is required"` ` }`

`// 404 Not Found - Service not configured`

`{ ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.5.4"` `, ``"title"` `: ``"Not Found"` `, ``"status"` `: 404, ``"detail"` `: `

`"Downstream API 'UnknownService' not configured"` ` }`

`// 500 Internal Server Error - Token acquisition failure`

`{ ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.6.1"` `, ``"title"` `: ``"Internal Server Error"` `, ``"status"` `: 500, `

`"detail"` `: ``"Failed to acquire token for downstream API"` ` }`

**MSAL Error Example**

`{ ``"type"` `: ``"https://tools.ietf.org/html/rfc7231#section-6.6.1"` `, ``"title"` `: ``"Internal Server Error"` `, ``"status"` `: 500, `

`"detail"` `: ``"MSAL.NetCore.invalid_grant: AADSTS50076: Due to a configuration change ..."` `, ``"extensions"` `: { ``"errorCode"` `: `

`"invalid_grant"` `, ``"correlationId"` `: ``"..."` ` } }`

**Complete Override Reference**

text

**Override scopes**:

HTTP

The Microsoft Entra SDK for AgentID itself does not impose rate limits. Effective limits come from:

1\. Microsoft Entra ID token service throttling (shouldn't happen as the SDK caches token)

2\. Downstream API limits

3\. Token cache efficiency (reduces acquisition volume)

1\. Prefer configuration over ad-hoc overrides.

2\. Keep service names static and declarative.

3\. Implement retry policies for transient failures (HTTP 500/503).

4\. Validate agent parameters before calling.

5\. Log correlation IDs for tracing across services.

6\. Monitor token acquisition latency and error rates.

7\. Use health probes in orchestration platforms.

Configuration Reference

Agent Identities

Scenarios: Validate Authorization Header

Scenarios: Obtain Authorization Header

Scenarios: Call Downstream API

**Last updated on 11/12/2025**

`optionsOverride.Scopes=<scope>     # Repeatable`

`optionsOverride.RequestAppToken=<true|false>`

`optionsOverride.BaseUrl=<url>`

`optionsOverride.RelativePath=<path>`

`optionsOverride.HttpMethod=<method>`

`optionsOverride.AcquireTokenOptions.Tenant=<tenant-id>`

`optionsOverride.AcquireTokenOptions.AuthenticationScheme=<scheme>`

`optionsOverride.AcquireTokenOptions.CorrelationId=<guid>`

`optionsOverride.AcquireTokenOptions.PopPublicKey=<base64-key>`

`optionsOverride.AcquireTokenOptions.PopClaims=<json>`

`optionsOverride.CustomHeader.<Name>=<value>`

`AgentIdentity=<agent-client-id>`

`AgentUsername=<user-upn>            # Requires AgentIdentity`

`AgentUserId=<user-object-id>        # Requires AgentIdentity`

**Examples of override**

`GET` ` ` `/AuthorizationHeader/Graph?optionsOverride.Scopes=User.Read&optionsOverride.Scopes=Mail.Read` ` HTTP/1.1`

`Authorization` `: Bearer eyJ0eXAiOiJKV1QiLCJhbGc...`

**Rate Limiting**

**Best Practices**

**See Also**

**Troubleshooting: Common Microsoft Entra**

**SDK for AgentID Issues**

Solutions for common SDK deployment and operational issues.

Bash

Bash

Pod shows `CrashLoopBackOff` or `Error` status.

**Quick Diagnostics**

**Check SDK Health**

`# Check if SDK is running`

`kubectl get pods -l app=myapp`

`# Check SDK logs`

`kubectl logs <pod-name> -c sidecar`

`# Test health endpoint`

`kubectl ` `exec` ` <pod-name> -c sidecar -- curl http://localhost:5000/health`

**Check Configuration**

`# View SDK environment variables`

`kubectl ` `exec` ` <pod-name> -c sidecar -- env | grep AzureAd`

`# Check ConfigMap`

`kubectl get configmap sidecar-config -o yaml`

`# Check Secrets`

`kubectl get secret sidecar-secrets -o yaml`

**Common Issues**

**Container Won't Start**

**Symptom**

**Missing Required Configuration**

Bash

**Solution**:

YAML

**Invalid Credential Configuration**

Bash

**Solution**: Verify credential configuration and access to Key Vault or secrets.

**Port Conflict**

Bash

**Solution**: Change SDK port if needed:

YAML

**Possible Causes**

`# Check logs for configuration errors`

`kubectl logs <pod-name> -c sidecar`

`# Look for messages like:`

`# "AzureAd:TenantId is required"`

`# "AzureAd:ClientId is required"`

`# Ensure all required configuration is set`

`env:`

`- name:`  ` `  `AzureAd__TenantId`

`  value:` ` ` `"<your-tenant-id>"`

`- name:`  ` `  `AzureAd__ClientId`

`  value:` ` ` `"<your-client-id>"`

`# Check for credential errors in logs`

`kubectl logs <pod-name> -c sidecar | grep -i ``"credential"`

`# Check if port 5000 is already in use`

`kubectl ` `exec` ` <pod-name> -c sidecar -- netstat -tuln | grep 5000`

`env:`

`- name:`  ` `  `ASPNETCORE_URLS`

`  value:` ` ` `"http://+:5001"`

Requests to SDK return 401 Unauthorized.

**Missing Authorization Header**

Bash

**Solution**: Include Authorization header:

Bash

**Invalid or Expired Token**

Bash

**Solution**: Obtain a new token from Microsoft Entra ID.

**Audience Mismatch**

Bash

**Solution**: Verify audience configuration matches token:

YAML

**401 Unauthorized Errors**

**Symptom**

**Possible Causes**

`# Test with curl`

`curl -v http://localhost:5000/AuthorizationHeader/Graph`

`# Should show 401 because no Authorization header`

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  http://localhost:5000/AuthorizationHeader/Graph`

`# Check token claims`

`kubectl ` `exec` ` <pod-name> -c sidecar -- curl -H ``"Authorization: Bearer <token>"` ` \`

`  http://localhost:5000/Validate`

`# Check logs for audience validation errors`

`kubectl logs <pod-name> -c sidecar | grep -i ``"audience"`

`env:`

`- name:`  ` `  `AzureAd__Audience`

**Scope Validation Failure**

Bash

**Solution**: Ensure token contains required scopes:

YAML

To understand the detailed errors, you might need to increase the log level:

Bash

Requests with agent identity parameters return 400 Bad Request.

**Request**:

`  value:` ` ` `"api://<your-api-id>"`

７ **Note**

The expected audience value depends on your app registration's

**requestedAccessTokenVersion**:

**Version 2**: Use the `{ClientId}` value directly

**Version 1** or **null**: Use the App ID URI (typically `api://{ClientId}` unless you

customized it)

`# Check logs for scope errors`

`kubectl logs <pod-name> -c sidecar | grep -i ``"scope"`

`env:`

`- name:`  ` `  `AzureAd__Scopes`

`  value:` ` ` `"access_as_user"` `  ` `# Or remove to disable scope validation`

`Logging__LogLevel__Default=Debug `

`Logging__LogLevel__Microsoft.Identity.Web=Debug `

`Logging__LogLevel__Microsoft.AspNetCore=Debug `

**400 Bad Request - Agent Identity Validation**

**Symptom**

**Error: AgentUsername Without AgentIdentity**

Bash

**Error Response**:

JSON

**Solution**: Include AgentIdentity parameter:

Bash

**Request**:

Bash

**Error Response**:

JSON

**Solution**: Use only one:

Bash

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  ``"http://localhost:5000/AuthorizationHeader/Graph?AgentUsername=user@contoso.com"`

`{`

`  ``"status"` `: 400,`

`  ``"detail"` `: ``"AgentUsername requires AgentIdentity to be specified"`

`}`

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  ``"http://localhost:5000/AuthorizationHeader/Graph?AgentIdentity=<client-`

`id>&AgentUsername=user@contoso.com"`

**Error: AgentUsername and AgentUserId Both Specified**

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  ``"http://localhost:5000/AuthorizationHeader/Graph?AgentIdentity=`

`<id>&AgentUsername=user@contoso.com&AgentUserId=<oid>"`

`{`

`  ``"status"` `: 400,`

`  ``"detail"` `: ``"AgentUsername and AgentUserId are mutually exclusive"`

`}`

`# Use AgentUsername`

`curl -H ``"Authorization: Bearer <token>"` ` \`

**Request**:

Bash

**Error Response**:

JSON

**Solution**: Provide a valid GUID:

Bash

JSON

`  ``"http://localhost:5000/AuthorizationHeader/Graph?AgentIdentity=`

`<id>&AgentUsername=user@contoso.com"`

`# OR use AgentUserId`

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  ``"http://localhost:5000/AuthorizationHeader/Graph?AgentIdentity=<id>&AgentUserId=`

`<oid>"`

**Error: Invalid AgentUserId Format**

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  ``"http://localhost:5000/AuthorizationHeader/Graph?AgentIdentity=`

`<id>&AgentUserId=invalid-guid"`

`{`

`  ``"status"` `: 400,`

`  ``"detail"` `: ``"AgentUserId must be a valid GUID"`

`}`

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  ``"http://localhost:5000/AuthorizationHeader/Graph?AgentIdentity=`

`<id>&AgentUserId=12345678-1234-1234-1234-123456789012"`

**404 Not Found - Service Not Configured**

**Symptom**

`{`

`  ``"status"` `: 404,`

`  ``"detail"` `: ``"Downstream API 'UnknownService' not configured"`

`}`

**Service Name Typo**

Bash

**Solution**: Use correct service name from configuration.

**Missing DownstreamApis Configuration**

**Solution**: Add service configuration:

YAML

500 Internal Server Error when acquiring tokens.

**AADSTS50076: Multi-Factor Authentication Required**

**Solution**: User must complete MFA. This is expected behavior for conditional access policies.

**AADSTS65001: User Consent Required**

**Possible Causes**

`# Wrong service name in URL`

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  http://localhost:5000/AuthorizationHeader/Grafh`

`# Should be "Graph"`

`env:`

`- name:`  ` `  `DownstreamApis__Graph__BaseUrl`

`  value:` ` ` `"https://graph.microsoft.com/v1.0"`

`- name:`  ` `  `DownstreamApis__Graph__Scopes`

`  value:` ` ` `"User.Read"`

**Token Acquisition Failures**

**Symptom**

**AADSTS Error Codes**

`AADSTS50076: Due to a configuration change made by your administrator, `

`or because you moved to a new location, you must use multi-factor authentication.`

**Solution**:

1\. Request admin consent for the application

2\. Ensure delegated permissions are properly configured

**AADSTS700016: Application Not Found**

**Solution**: Verify ClientId is correct and application exists in tenant.

**AADSTS7000215: Invalid Client Secret**

**Solution**:

1\. Verify client secret is correct

2\. Check if secret has expired

3\. Generate new secret and update configuration

**AADSTS700027: Certificate or Private Key Not Configured**

**Solution**:

1\. Verify certificate is registered in app registration

2\. Check certificate configuration in the SDK

3\. Ensure certificate is accessible from container

**Solution**: Clear token cache and restart:

Bash

`AADSTS65001: The user or administrator has not consented to use the application.`

`AADSTS700016: Application with identifier '<client-id>' was not found.`

`AADSTS7000215: Invalid client secret is provided.`

`AADSTS700027: The certificate with identifier '<thumbprint>' was not found.`

**Token Cache Issues**

For distributed cache (Redis):

Bash

**Symptom**: Timeout errors when acquiring tokens.

**Diagnostics**:

Bash

**Solution**:

Check network policies

Verify firewall rules allow HTTPS to login.microsoftonline.com

Ensure DNS is working correctly

**Diagnostics**:

Bash

**Solution**:

`kubectl rollout restart deployment <deployment-name>`

`# Clear Redis cache`

`redis-cli FLUSHDB`

**Network Connectivity Issues**

**Cannot Reach Microsoft Entra ID**

`# Test connectivity from SDK container`

`kubectl ` `exec` ` <pod-name> -c sidecar -- curl -v https://login.microsoftonline.com`

`# Check DNS resolution`

`kubectl ` `exec` ` <pod-name> -c sidecar -- nslookup login.microsoftonline.com`

**Cannot Reach Downstream APIs**

`# Test connectivity to downstream API`

`kubectl ` `exec` ` <pod-name> -c sidecar -- curl -v https://graph.microsoft.com`

`# Check configuration`

`kubectl ` `exec` ` <pod-name> -c sidecar -- env | grep DownstreamApis__Graph__BaseUrl`

Verify downstream API URL is correct

Check network egress rules

Ensure API is accessible from cluster

Application shows connection errors when calling the SDK.

**Diagnostics**:

Bash

**Solution**:

Verify SIDECAR\_URL environment variable

Check the SDK is running: `kubectl get pods`

Ensure port 5000 is not blocked

**Diagnostics**:

Bash

**Solutions**:

1\. **Check Token Cache**: Ensure caching is enabled and working

**Application cannot reach the SDK**

**Symptom**

`# Test from application container`

`kubectl ` `exec` ` <pod-name> -c app -- curl -v http://localhost:5000/health`

`# Check if sidecar is listening`

`kubectl ` `exec` ` <pod-name> -c sidecar -- netstat -tuln | grep 5000`

**Performance Issues**

**Slow Token Acquisition**

`# Enable detailed logging`

`# Add to SDK configuration:`

`# - name: Logging__LogLevel__Microsoft.Identity.Web`

`#   value: "Debug"`

`# Check logs for timing information`

`kubectl logs <pod-name> -c sidecar | grep ``"Token acquisition"`

2\. **Increase Resources**: Allocate more CPU/memory to the SDK

3\. **Network Latency**: Check latency to Microsoft Entra ID

4\. **Connection Pooling**: Verify HTTP connection reuse

**Diagnostics**:

Bash

**Solutions**:

1\. Increase memory limits

2\. Check for token cache size issues

3\. Review application usage patterns

4\. Consider distributed cache for multiple replicas

**Symptom**:

**Solution**:

Verify certificate is mounted correctly

Check certificate store path

Ensure certificate permissions are correct

**Symptom**:

**High Memory Usage**

`# Check resource usage`

`kubectl top pod <pod-name> --containers`

`# Check for memory leaks in logs`

`kubectl logs <pod-name> -c sidecar | grep -i ``"memory"`

**Certificate Issues**

**Certificate Not Found**

`Certificate with thumbprint '<thumbprint>' not found in certificate store.`

**Certificate Expired**

**Solution**:

1\. Generate new certificate

2\. Register in Microsoft Entra ID

3\. Update SDK configuration

4\. Redeploy containers

**Symptom**:

**Solution**:

Verify managed identity has access policy to Key Vault

Check Key Vault firewall rules

Ensure certificate exists in Key Vault

**Symptom**: Downstream API rejects PoP token.

**Diagnostics**:

Bash

**Solution**:

Verify public key is correctly base64 encoded

Ensure downstream API supports PoP tokens

`The certificate has expired.`

**Key Vault Access Denied**

`Access denied to Key Vault '<vault-name>'.`

**Signed HTTP Request (SHR) Issues**

**Invalid PoP Token**

`# Check if PoP token is being requested`

`kubectl logs <pod-name> -c sidecar | grep -i ``"pop"`

`# Verify PopPublicKey is configured correctly`

`kubectl ` `exec` ` <pod-name> -c sidecar -- env | grep PopPublicKey`

Check PoP token format

**Symptom**: Cannot sign HTTP request.

**Solution**: Ensure private key is available to application for signing requests.

**Error**

**Code**

**Message**

**Cause**

**Solution**

400

AgentUsername requires

AgentIdentity

AgentUsername without

AgentIdentity

Add AgentIdentity

parameter

400

AgentUsername and AgentUserId

are mutually exclusive

Both parameters specified

Use only one parameter

400

AgentUserId must be a valid GUID

Invalid GUID format

Provide valid GUID

400

Service name is required

Missing service name in

path

Include service name in

URL

400

No token found

Missing Authorization

header

Include valid token

401

Unauthorized

Invalid or expired token

Obtain new token

403

Forbidden

Missing required scopes

Request token with

correct scopes

404

Downstream API not configured

Service not in

configuration

Add DownstreamApis

configuration

500

Failed to acquire token

Various MSAL errors

Check logs for specific

AADSTS error

503

Service Unavailable

Health check failure

Check SDK status and

configuration

**Missing Private Key**

**Error Reference Table**

ﾉ

**Expand table**

**Debugging Tools**

**Enable Detailed Logging**

YAML

**Warning**: Debug/Trace logging may log sensitive information. Use only in development or

temporarily in production.

Bash

Bash

If configured:

Bash

`env:`

`- name:`  ` `  `Logging__LogLevel__Default`

`  value:` ` ` `"Debug"`

`- name:`  ` `  `Logging__LogLevel__Microsoft.Identity.Web`

`  value:` ` ` `"Trace"`

`- name:`  ` `  `Logging__LogLevel__Microsoft.AspNetCore`

`  value:` ` ` `"Debug"`

**Test Token Validation**

`# Validate token`

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  http://localhost:5000/Validate | jq .`

`# Check claims`

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  http://localhost:5000/Validate | jq ``'.claims'`

**Test Token Acquisition**

`# Get authorization header`

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  http://localhost:5000/AuthorizationHeader/Graph | jq .`

`# Extract and decode token`

`curl -H ``"Authorization: Bearer <token>"` ` \`

`  http://localhost:5000/AuthorizationHeader/Graph | \`

`  jq -r ``'.authorizationHeader'` ` | \`

`  cut -d` `' '` ` -f2 | \`

`  jwt decode -`

**Monitor with Application Insights**

When opening an issue, include:

1\. **SDK Version**:

Bash

2\. **Configuration** (redact sensitive data):

Bash

3\. **Logs** (last 100 lines):

Bash

4\. **Error Messages**: Full error response from the SDK

5\. **Request Details**: HTTP method, endpoint, parameters used

**GitHub Issues**: microsoft-identity-web/issues

**Microsoft Q&A**: Microsoft Identity Platform

**Stack Overflow**: Tag `[microsoft-identity-web]`

1\. **Start with Health Check**: Always verify the SDK is healthy first

`# Query Application Insights`

`az monitor app-insights query \`

`  --app <app-insights-name> \`

`  --analytics-query ``"traces | where message contains 'token acquisition' | take 100"`

**Getting Help**

**Collect Diagnostic Information**

`kubectl describe pod <pod-name> | grep -A 5 ``"sidecar:"`

`kubectl get configmap sidecar-config -o yaml`

`kubectl logs <pod-name> -c sidecar --tail=100`

**Support Resources**

**Best Practices for Troubleshooting**

2\. **Check Logs**: SDK logs contain valuable diagnostic information

3\. **Verify Configuration**: Ensure all required settings are present and correct

4\. **Test Incrementally**: Start with simple requests, add complexity gradually

5\. **Use Correlation IDs**: Include correlation IDs for tracing across services

6\. **Monitor Continuously**: Set up alerts for authentication failures

7\. **Document Issues**: Keep notes on issues and resolutions for future reference

Installation Guide

Configuration Reference

Security Best Practices

FAQ

**Last updated on 11/14/2025**

**Related Resources**

**Frequently Asked Questions about the**

**Microsoft Entra SDK for AgentID**

The Microsoft Entra SDK for AgentID is a containerized web service that handles token

acquisition, validation, and secure downstream API calls. It runs as a companion container

alongside your application, allowing you to offload identity logic to a dedicated service. By

centralizing identity operations in the SDK, you eliminate the need to embed complex token

management logic in each service, reducing code duplication and potential security

vulnerabilities.

**Feature**

**Microsoft.Identity.Web**

**Microsoft Entra SDK for AgentID**

**Language Support**

C# / .NET only

Any language (HTTP)

**Deployment**

In-process library

Separate container

**Token Acquisition**

✅ Direct MSAL.NET

✅ Via HTTP API

**Token Caching**

✅ In-memory, ✅ distributed

✅ In-memory, ❌distributed

**OBO Flow**

✅ Native support

✅ Via HTTP endpoint

**Client Credentials**

✅ Native support

✅ Via HTTP endpoint

**Managed Identity**

✅ Direct support

✅ Direct support

**Agent Identities**

✅ Via extensions

✅ Query parameters

**Token Validation**

✅ Middleware

✅ /Validate endpoint

**Downstream API**

✅ IDownstreamApi

✅ /DownstreamApi endpoint

**Microsoft Graph**

✅ Graph SDK integration

⚠Via DownstreamApi

**Performance**

⚡ In-process (fastest)

🔄 HTTP overhead

**General Questions**

**What is the Microsoft Entra SDK for AgentID?**

**Why would I use the Microsoft Entra SDK for AgentID instead**

**of Microsoft.Identity.Web?**

ﾉ

**Expand table**

**Feature**

**Microsoft.Identity.Web**

**Microsoft Entra SDK for AgentID**

**Configuration**

`appsettings.json` and code

`appsettings.json` and Environment variables

**Debugging**

✅ Standard .NET debugging

⚠Container debugging

**Hot Reload**

✅ .NET Hot Reload

❌ Container restart

**Package Updates**

📦 NuGet packages

🐳 Container images

**License**

MIT

MIT

See Comparison Guide for detailed guidance.

Yes, the SDK is production ready. Refer to the GitHub releases

for the latest release status

and production readiness guidelines.

Yes - Refer to the Installation Guide for available images and version tags.

Yes - Refer to the Installation Guide for instructions on running the SDK in Docker Compose or

other container environments (Docker Compose, Azure Container Instances, AWS ECS/Fargate,

Standalone Docker).

Default port: `5000` (configurable)

The SDK should only be accessible from your application container, never exposed externally.

Learn about deployment options, resource requirements, and integration with container

platforms like Docker Compose and Kubernetes.

**Is the Microsoft Entra SDK for AgentID production-ready?**

**Are container images available?**

**Can I run the SDK outside Kubernetes?**

**What network ports does the SDK use?**

**Deployment**

**What are the resource requirements?**

Yes - see the Installation Guide for resource requirements.

Yes - see the Installation Guide for Docker Compose examples.

Yes - follow the Installation Guide in the _Azure Kubernetes Service (AKS) with Managed Identity_

section.

Configure the SDK settings including credentials, downstream APIs, and request overrides to

match your deployment requirements.

Yes - see the Configuration Reference for detailed configuration options.

**Prefer certificates** over client secrets:

More secure

Easier to rotate

Recommended by Microsoft

**Best**: Use Managed Identity in Azure (no credentials needed)

See Security Best Practices for guidance.

Yes. Configure each with its own section:

YAML

**Can I use the SDK with Docker Compose?**

**How do I deploy to AKS with Managed Identity?**

**Configuration**

**Is a configuration reference available?**

**Should I use client secrets or certificates?**

**Can I configure multiple downstream APIs?**

`DownstreamApis__Graph__BaseUrl:` ` ` `"https://graph.microsoft.com/v1.0"`

`DownstreamApis__Graph__Scopes:` ` ` `"User.Read"`

Use query parameters on endpoints:

Bash

See Configuration Reference for all options.

Agent identities enable scenarios where an agent application can operate autonomously or on

behalf of a user, with proper context isolation and scoping.

Agent identities enable scenarios where an agent application acts either:

**Autonomously** \- in its own application context

**Interactive** \- on behalf of the user that called it

See Agent Identities for comprehensive documentation.

Use autonomous agent mode for:

Batch processing without user context

Background tasks

System-to-system operations

Scheduled jobs

Example:

`DownstreamApis__MyApi__BaseUrl:` ` ` `"https://api.contoso.com"`

`DownstreamApis__MyApi__Scopes:` ` ` `"api://myapi/.default"`

**How do I override configuration per request?**

`# Override scopes`

`GET /AuthorizationHeader/Graph?optionsOverride.Scopes=User.Read`

`# Request app token instead of OBO`

`GET /AuthorizationHeader/Graph?optionsOverride.RequestAppToken=`  `true`

`# Override relative path`

`GET /DownstreamApi/Graph?optionsOverride.RelativePath=me/messages`

**Agent Identities**

**What are agent identities?**

**When should I use autonomous agent mode?**

Bash

Use delegated agent mode for:

Interactive agent applications

AI assistants acting on behalf of users

User-scoped automation

Personalized workflows

Example:

Bash

`AgentUsername` is a modifier that specifies which user the agent operates on behalf of. It

requires `AgentIdentity` to specify which agent context to use. Without `AgentIdentity` , the

parameter has no meaning.

They're two ways to identify the same user:

`AgentUsername` \- User Principal Name (UPN)

`AgentUserId` \- Object ID (OID)

Allowing both creates ambiguity. Choose the one that fits your scenario:

Use `AgentUsername` when you have the user's UPN

Use `AgentUserId` when you have the user's object ID

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-client-id>`

**When should I use interactive agent mode?**

`GET /AuthorizationHeader/Graph?AgentIdentity=<agent-client-`

`id>&AgentUsername=user@contoso.com`

**Why can't I use AgentUsername without AgentIdentity?**

**Why are AgentUsername and AgentUserId mutually**

**exclusive?**

**API Usage**

The SDK exposes several HTTP endpoints for token acquisition, validation, and downstream API

calls with support for both authenticated and unauthenticated flows.

`/Validate` \- Validate token and return claims

`/AuthorizationHeader/{serviceName}` \- Get authorization header with token

`/AuthorizationHeaderUnauthenticated/{serviceName}` \- Get token without inbound user

token

`/DownstreamApi/{serviceName}` \- Call downstream API directly

`/DownstreamApiUnauthenticated/{serviceName}` \- Call downstream API without inbound

user token

`/healthz` \- Health probe

See Endpoints Reference for details.

**Authenticated**: Require bearer token in `Authorization` header (for OBO flows)

**Unauthenticated**: Don't validate inbound token (for app-only or agent scenarios)

Bash

Response includes all claims from the token.

Bash

Response includes authorization header ready to use with downstream API.

**What endpoints does the SDK expose?**

**What's the difference between authenticated and**

**unauthenticated endpoints?**

**How do I validate a user token?**

`GET /Validate`

`Authorization: Bearer <user-token>`

**How do I get an access token for a downstream API?**

`GET /AuthorizationHeader/Graph`

`Authorization: Bearer <user-token>`

**Can I override HTTP method or path per request?**

Yes, using query parameters:

Bash

The SDK automatically caches tokens in memory to optimize performance and reduce

redundant token acquisition requests.

Yes - the SDK caches tokens in memory by default.

Tokens are cached until near expiration, then automatically refreshed. Exact duration depends

on token lifetime (typically 1 hour for Entra ID tokens).

Token caching is automatic and optimized. There's currently no option to disable it.

No - each SDK instance maintains its own in-memory cache. In high-availability deployments,

each pod has independent caching.

Secure SDK deployments follow Microsoft Entra identity and data protection best practices,

including managed identity usage, network isolation, and proper credential handling.

Yes - see the Security Best Practices for security best practices.

`# Override method`

`GET /DownstreamApi/Graph?optionsOverride.HttpMethod=POST`

`# Override path`

`GET /DownstreamApi/Graph?optionsOverride.RelativePath=me/messages`

**Token Caching**

**Does the SDK cache tokens?**

**How long are tokens cached?**

**Can I disable caching?**

**Is token cache shared across SDK instances?**

**Security**

**Is it safe to run the SDK?**

**Never** \- The SDK should only be accessible from your application container. For detailed

security best practices, see Security Best Practices.

See Security Best Practices for comprehensive guidance.

Preference order:

1\. **Managed Identity** (Azure) - Most secure, no credentials

2\. **Certificates** \- Secure, can be rotated

3\. **Client Secrets** \- Less preferred, keep in secure vault

Check the GitHub repository

for current compliance information.

SDK performance depends on token caching effectiveness and network round-trip latency, with

typical response times between 10-50ms for cached tokens.

Typical HTTP round-trip: 10-50ms

Token caching minimizes repeated acquisitions. The first request is slower (token acquisition),

subsequent requests use cached tokens.

In-process libraries are faster (no network round-trip) but the SDK provides:

Language agnostic access

Centralized configuration

Shared token cache across services

Simplified scaling

**Should I expose the SDK externally?**

**How should I secure the SDK?**

**What credentials should I use?**

**Is the SDK compliance-certified?**

**Performance**

**What's the performance impact of using the SDK?**

**How does SDK performance compare to in-process libraries?**

See Comparison Guide for details.

Yes. Deploy multiple SDK replicas using Kubernetes Deployment. Each pod maintains

independent token caching.

Moving from Microsoft.Identity.Web to the SDK offers advantages in multi-language support,

centralized configuration, and simplified scaling across services.

Yes - see the Comparison Guide for detailed migration steps

Get help with issues, find additional documentation, and access community resources through

official channels.

Report issues on the GitHub repository

, using the Entra ID template.

When you encounter issues with the SDK, refer to the comprehensive troubleshooting guide

for diagnostic steps, common problems, and solutions in Troubleshooting Guide.

Microsoft Learn Documentation

Identity Platform Docs

Agent Identity Platform

**Can I scale the SDK horizontally?**

**Migration**

**Can I migrate from Microsoft.Identity.Web to the Microsoft**

**Entra SDK for AgentID?**

**Support**

**Where do I report bugs?**

**Troubleshooting**

**Where can I get more information?**

**See Also**

**Last updated on 11/14/2025**

