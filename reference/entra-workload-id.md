**Tell us about your PDF experience.**

**Microsoft Entra Workload ID**

**documentation**

Microsoft Entra Workload ID helps you manage and secure identities for digital

workloads, such as apps and services.

![](./assets/output_0_1.jpeg)![](./assets/output_0_2.jpeg)

**About workload identities**

ｅ**OVERVIEW**

What are workload identities?

Frequently asked questions about license plans

![](./assets/output_0_3.jpeg)![](./assets/output_0_4.jpeg)

**Check app health status and mitigate risk**

ｃ**HOW-TO GUIDE**

Remove unused applications

Remove unused credentials from apps

Renew expiring application credentials

![](./assets/output_0_5.jpeg)![](./assets/output_0_6.jpeg)

**Connect workloads without managing secrets**

ｅ**OVERVIEW**

What is workload identity federation?

ｑ**VIDEO**

Learn why you would use workload identity federation

ｃ**HOW-TO GUIDE**

Configure an app to trust an external identity provider

![](./assets/output_1_1.jpeg)![](./assets/output_1_2.jpeg)

Configure a managed identity to trust an external identity provider

![](./assets/output_1_3.jpeg)![](./assets/output_1_4.jpeg)

**Enforce best practice for how apps use auth methods**

ｅ**OVERVIEW**

Application authentication methods API

![](./assets/output_1_5.jpeg)![](./assets/output_1_6.jpeg)

**Secure risky workload identities**

ｅ**OVERVIEW**

Secure workload identities

![](./assets/output_1_7.jpeg)![](./assets/output_1_8.jpeg)

**Configuring applications to trust managed identities**

ｃ**HOW-TO GUIDE**

Configure an application to trust a managed identity (preview)

![](./assets/output_1_9.jpeg)![](./assets/output_1_10.jpeg)

**Apply Conditional Access policies to service principals**

ｃ**HOW-TO GUIDE**

Conditional Access for workload identities

![](./assets/output_1_11.jpeg)![](./assets/output_1_12.jpeg)

**Enable real-time enforcement of Conditional Access location and risk**

**policies**

ｃ**HOW-TO GUIDE**

Continuous access evaluation for workload identities

![](./assets/output_2_1.jpeg)![](./assets/output_2_2.jpeg)

**Contain threats and reduce risk to workload identities**

ｃ**HOW-TO GUIDE**

Microsoft Entra ID Protection

![](./assets/output_2_3.jpeg)![](./assets/output_2_4.jpeg)

**Review service principals and applications privileged directory roles**

ｃ**HOW-TO GUIDE**

Access reviews for service principals

**What are workload identities?**

Article • 03/13/2025

A workload identity is an identity you assign to a software workload (such as an

application, service, script, or container) to authenticate and access other services and

resources. The terminology is inconsistent across the industry, but generally a workload

identity is something you need for your software entity to authenticate with some

system. For example, in order for GitHub Actions to access Azure subscriptions the

action needs a workload identity which has access to those subscriptions. A workload

identity could also be an AWS service role attached to an EC2 instance with read-only

access to an Amazon S3 bucket.

In Microsoft Entra, workload identities are applications, service principals, and managed

identities.

An application is an abstract entity, or template, defined by its application object. The

application object is the _global_ representation of your application for use across all

tenants. The application object describes how tokens are issued, the resources the

application needs to access, and the actions that the application can take.

A service principal is the _local_ representation, or application instance, of a global

application object in a specific tenant. An application object is used as a template to

create a service principal object in every tenant where the application is used. The

service principal object defines what the app can actually do in a specific tenant, who

can access the app, and what resources the app can access.

A managed identity is a special type of service principal that eliminates the need for

developers to manage credentials.

Here are some ways that workload identities in Microsoft Entra ID are used:

An app that enables a web app to access Microsoft Graph based on admin or user

consent. This access could be either on behalf of the user or on behalf of the

application.

A managed identity used by a developer to provision their service with access to

an Azure resource such as Azure Key Vault or Azure Storage.

A service principal used by a developer to enable a CI/CD pipeline to deploy a web

app from GitHub to Azure App Service.

**Workload identities, other machine identities,**

**and human identities**

At a high level, there are two types of identities: human and machine/non-human

identities. Workload identities and device identities together make up a group called

machine (or non-human) identities. Workload identities represent software workloads

while device identities represent devices such as desktop computers, mobile, IoT

sensors, and IoT managed devices. Machine identities are distinct from human identities,

which represent people such as employees (internal workers and front line workers) and

external users (customers, consultants, vendors, and partners).

![](./assets/output_4_1.png)![](./assets/output_4_2.png)![](./assets/output_4_3.png)![](./assets/output_4_4.png)![](./assets/output_4_5.png)![](./assets/output_4_6.png)![](./assets/output_4_7.png)![](./assets/output_4_8.png)![](./assets/output_4_9.png)![](./assets/output_4_10.png)![](./assets/output_4_11.png)

More and more, solutions are reliant on non-human entities to complete vital tasks and

the number of non-human identities is increasing dramatically. Recent cyber attacks

show that adversaries are increasingly targeting non-human identities over human

identities.

Human users typically have a single identity used to access a broad range of resources.

Unlike a human user, a software workload may deal with multiple credentials to access

different resources and those credentials need to be stored securely. It’s also hard to

track when a workload identity is created or when it should be revoked. Enterprises risk

their applications or services being exploited or breached because of difficulties in

securing workload identities.

![](./assets/output_4_12.png)

**Need for securing workload identities**

**Feedback**

**Was this page helpful?**

Provide product feedback

Most identity and access management solutions on the market today are focused only

on securing human identities and not workload identities. Microsoft Entra Workload ID

helps resolve these issues when securing workload identities.

Here are some ways you can use workload identities.

Secure access with adaptive policies:

Apply Conditional Access policies to service principals owned by your organization

using Conditional Access for workload identities.

Enable real-time enforcement of Conditional Access location and risk policies using

Continuous access evaluation for workload identities.

Manage custom security attributes for an app

Intelligently detect compromised identities:

Detect risks (like leaked credentials), contain threats, and reduce risk to workload

identities using Microsoft Entra ID Protection.

Simplify lifecycle management:

Access Microsoft Entra protected resources without needing to manage secrets for

workloads that run on Azure using managed identities.

Access Microsoft Entra protected resources without needing to manage secrets

using workload identity federation for supported scenarios such as GitHub Actions,

workloads running on Kubernetes, or workloads running in compute platforms

outside of Azure.

Review service principals and applications that are assigned to privileged directory

roles in Microsoft Entra ID using access reviews for service principals.

Get answers to frequently asked questions about workload identities.

**Key scenarios**

**Next steps**

 **Yes**

 **No**

**Frequently asked questions about**

**Microsoft Entra Workload ID**

Article • 03/18/2025

Microsoft Entra Workload ID is available in two editions: **Free** and **Microsoft Entra**

**Workload ID Premium**. The free edition of workload identities is included with a

subscription of a commercial online service such as Azure

and Power Platform

. The

Workload ID Premium offering is available through a Microsoft representative, the Open

Volume License Program

, and the Cloud Solution Providers program. Azure and

Microsoft 365 subscribers can purchase Workload ID Premium online.

For more information, see what are workload identities?

Learn more about Workload ID pricing

.

This document addresses Microsoft Entra Workload ID most frequent customer

questions.

Microsoft Entra Workload ID (Workload ID Premium) is generally available through a

Microsoft representative, the Open Volume License Program, and the Cloud Solution

Providers program. Azure and Office 365 subscribers can buy it online. Workload ID

Premium is a standalone stock-keeping unit (SKU), $3 per workload identity per month,

and not part of another SKU.

The free features come with a subscription for a commercial online service such as

Azure, Power Platform, and others. Examples are managed identities and workload

identity federation.

７ **Note**

Workload ID Premium is a standalone product and isn't included in other premium

product plans. All subscribers require a license to use Workload ID Premium

features.

**What are Workload ID Premium features, and**

**which are free?**

ﾉ

**Expand table**

**Capabilities**

**Description**

**Free**

**Premium**

**Authentication and**

**authorization**

Create, read, update, and delete

workload identities

Create and update identities to secure

service to service access

Yes

Yes

Access resources by

authenticating workload

identities and tokens

Use Microsoft Entra ID to protect resource

access

Yes

Yes

Workload identities sign-in

activity and audit trail

Monitor and track workload identity

behavior

Yes

Yes

**Managed identities**

Use Microsoft Entra identities in Azure

without handling credentials

Yes

Yes

Workload identity federation

To access Microsoft Entra protected

resources, use workloads tested by

external identity providers (IdPs)

Yes

Yes

**Lifecycle management**

Application management

policies

IT admins can enforce best practices for

how apps are configured

Yes

Yes

Access reviews for service

provider-assigned privileged

roles

Closely monitor workload identities with

impactful permissions

Yes

App Health Recommendations

Identify unused or inactive workload

identities and their risk levels. Get

remediation guidelines.

Yes

**Microsoft Entra Conditional**

**Access**

Conditional Access policies for

workload identities

Define the condition for a workload to

access a resource, such as an IP range.

Doesn't cover managed identities.

Yes

**Microsoft Entra ID Protection**

ID Protection for workload

identities

Detect and remediate compromised

workload identities

Yes

The Microsoft Entra Workload ID Premium

is $3/workload identity/month.

**How much is the Workload ID Premium plan?**

Only workload identities eligible for premium features require licensing. License

enterprise apps and service principals listed appear in the first category, on the

Workload ID landing page, in the Microsoft Entra admin center. To use premium

features for a subset of enterprise apps and service principals, procure needed licenses

tailored to your requirements. An exception appears if you use access reviews for

managed identities. Obtain licenses based on the number of managed identities in the

graph.

You can use Conditional Access for workload identities for single-tenant applications. ID

Protection protects single and multitenant applications under Enterprise apps/Service

Principals. Microsoft apps and managed identities aren't eligible for Conditional Access

and ID Protection. Access reviews are applicable for Service Principals assigned to

privileged roles, including managed identities. This feature requires Microsoft Entra ID

P2 licenses for reviewers, and Workload ID Premium licenses for access review Service

Principles.

You need a current or new Azure or Microsoft 365 subscription. Sign in to the Microsoft

Microsoft Entra admin center

with your credentials, then buy Workload ID licenses.

No, license assignment isn't required. One license in the tenant unlocks all features for

all workload identities.

７ **Note**

Learn about **Conditional Access for workload identities**.

**How many licenses do I need? Do I need to**

**license all workload identities, including**

**Microsoft applications and managed identities?**

**How do I purchase a Workload ID Premium**

**plan?**

**Do the licenses require individual workload**

**identities assignment?**

Unfortunately, we don’t provide a dashboard to track that information. You can track

enabled Conditional Access policies targeting workload identities in the **Insights and**

**reporting** area.

![](./assets/output_9_1.png)

Yes. You can get a 90-day free trial

. In the Modern channel, a 30-day trial is available.

Free trial is unavailable in Microsoft Azure Government

clouds.

Yes. For Azure Government cloud customers, contact your account manager to proceed

with the trial.

Yes, customers can have a mix of licenses in one tenant.

**How can I track licenses assigned to workload**

**identities?**

**Can I get a free trial of Workload ID Premium?**

**Is the Workload ID Premium plan available on**

**Azure Government clouds?**

**Can I have Microsoft Entra ID P1, P2, and**

**Workload ID Premium licenses in one tenant?**

**Feedback**

**Was this page helpful?**

Provide product feedback

Learn more about workload identities.

**Next steps**

 **Yes**

 **No**

**Application and service principal objects**

**in Microsoft Entra ID**

Article • 10/01/2024

This article describes application registration, application objects, and service principals

in Microsoft Entra ID, what they are, how they're used, and how they're related to each

other. A multitenant example scenario is also presented to illustrate the relationship

between an application's application object and corresponding service principal objects.

To delegate identity and access management functions to Microsoft Entra ID, an

application must be registered with a Microsoft Entra tenant. When you register your

application with Microsoft Entra ID, you're creating an identity configuration for your

application that allows it to integrate with Microsoft Entra ID. When you register an app,

you choose whether it's a single tenant, or multitenant, and can optionally set a redirect

URI. For step-by-step instructions on registering an app, see the app registration

quickstart.

When you've completed the app registration, you have a globally unique instance of the

app (the application object) that lives within your home tenant or directory. You also

have a globally unique ID for your app (the app/client ID). You can add secrets or

certificates and scopes to make your app work, customize the branding of your app in

the sign-in dialog, and more.

If you register an application, an application object and a service principal object are

automatically created in your home tenant. If you register/create an application using

the Microsoft Graph APIs, creating the service principal object is a separate step.

A Microsoft Entra application is defined by its one and only application object, which

resides in the Microsoft Entra tenant where the application was registered (known as the

application's "home" tenant). An application object is used as a template or blueprint to

create one or more service principal objects. A service principal is created in every

tenant where the application is used. Similar to a class in object-oriented programming,

the application object has some static properties that are applied to all the created

service principals (or application instances).

**Application registration**

**Application object**

The application object describes three aspects of an application:

How the service can issue tokens in order to access the application

The resources that the application might need to access

The actions that the application can take

You can use the **App registrations** page in the Microsoft Entra admin center

to list

and manage the application objects in your home tenant.

![](./assets/output_12_1.png)

The Microsoft Graph Application entity defines the schema for an application object's

properties.

To access resources that are secured by a Microsoft Entra tenant, the entity that requires

access must be represented by a security principal. This requirement is true for both

users (user principal) and applications (service principal). The security principal defines

the access policy and permissions for the user/application in the Microsoft Entra tenant.

This enables core features such as authentication of the user/application during sign-in,

and authorization during resource access.

There are three types of service principal:

**Application** \- This type of service principal is the local representation, or

application instance, of a global application object in a single tenant or directory.

https://learn-video.azurefd.net/vod/player?id=af3ad1eb-63b4-4ab7-b976-

16946fbbb099&locale=en-us&embedUrl=%2Fentra%2Fidentity-platform%2Fapp-

objects-and-service-principals

**Service principal object**

In this case, a service principal is a concrete instance created from the application

object and inherits certain properties from that application object. A service

principal is created in each tenant where the application is used and references the

globally unique app object. The service principal object defines what the app can

actually do in the specific tenant, who can access the app, and what resources the

app can access.

When an application is given permission to access resources in a tenant (upon

registration or consent), a service principal object is created. When you register an

application, a service principal is created automatically. You can also create service

principal objects in a tenant using Azure PowerShell, Azure CLI, Microsoft Graph,

and other tools.

**Managed identity** \- This type of service principal is used to represent a managed

identity. Managed identities eliminate the need for developers to manage

credentials. Managed identities provide an identity for applications to use when

connecting to resources that support Microsoft Entra authentication. When a

managed identity is enabled, a service principal representing that managed

identity is created in your tenant. Service principals representing managed

identities can be granted access and permissions, but can't be updated or

modified directly.

**Legacy** \- This type of service principal represents a legacy app, which is an app

created before app registrations were introduced or an app created through

legacy experiences. A legacy service principal can have credentials, service principal

names, reply URLs, and other properties that an authorized user can edit, but

doesn't have an associated app registration. The service principal can only be used

in the tenant where it was created.

The Microsoft Graph ServicePrincipal entity defines the schema for a service principal

object's properties.

You can use the **Enterprise applications** page in the Microsoft Entra admin center to list

and manage the service principals in a tenant. You can see the service principal's

permissions, user consented permissions, which users have done that consent, sign in

information, and more.

![](./assets/output_14_1.png)

The application object is the _global_ representation of your application for use across all

tenants, and the service principal is the _local_ representation for use in a specific tenant.

The application object serves as the template from which common and default

properties are _derived_ for use in creating corresponding service principal objects.

An application object has:

A one-to-one relationship with the software application, and

A one-to-many relationship with its corresponding service principal objects

A service principal must be created in each tenant where the application is used,

enabling it to establish an identity for sign-in and/or access to resources being secured

by the tenant. A single-tenant application has only one service principal (in its home

tenant), created and consented for use during application registration. A multitenant

application also has a service principal created in each tenant where a user from that

tenant has consented to its use.

You can find the service principals associated with an application object.

In the Microsoft Entra admin center, navigate to the application registration

overview. Select **Managed application in local directory**.

**Relationship between application objects and**

**service principals**

**List service principals associated with an app**

Browser

![](./assets/output_15_1.png)

Any changes that you make to your application object are also reflected in its service

principal object in the application's home tenant only (the tenant where it was

registered). This means that deleting an application object will also delete its home

tenant service principal object. However, restoring that application object through the

app registrations UI won't restore its corresponding service principal. For more

information on deletion and recovery of applications and their service principal objects,

see delete and recover applications and service principal objects.

The following diagram illustrates the relationship between an application's application

object and corresponding service principal objects in the context of a sample

multitenant application called **HR app**. There are three Microsoft Entra tenants in this

example scenario:

**Adatum** \- The tenant used by the company that developed the **HR app**

**Contoso** \- The tenant used by the Contoso organization, which is a consumer of

the **HR app**

**Fabrikam** \- The tenant used by the Fabrikam organization, which also consumes

the **HR app**

**Consequences of modifying and deleting applications**

**Example**

In this example scenario:

**Step**

**Description**

1

The process of creating the application and service principal objects in the application's

home tenant.

2

When Contoso and Fabrikam administrators complete consent, a service principal object is

created in their company's Microsoft Entra tenant and assigned the permissions that the

administrator granted. Also note that the HR app could be configured/designed to allow

consent by users for individual use.

3

The consumer tenants of the HR application (Contoso and Fabrikam) each have their own

service principal object. Each represents their use of an instance of the application at

runtime, governed by the permissions consented by the respective administrator.

Learn how to create a service principal:

Using the Microsoft Entra admin center

Using Azure PowerShell

Using Azure CLI

Using Microsoft Graph and then use Microsoft Graph Explorer to query both the

application and service principal objects.

ﾉ

**Expand table**

**Next steps**

**Feedback**

**Was this page helpful?**

Provide product feedback

 **Yes**

 **No**

**What is managed identities for Azure**

**resources?**

08/19/2025

A common challenge for developers is the management of secrets, credentials, certificates, and

keys used to secure communication between services. Manual handling of secrets and

certificates are a known source of security issues and outages. Managed identities eliminate

the need for developers to manage these credentials. Applications can use managed identities

to obtain Microsoft Entra tokens without having to manage any credentials.

At a high level, there are two types of identities: human and machine/non-human identities.

Machine / non-human identities consist of device and workload identities. In Microsoft Entra,

workload identities are applications, service principals, and managed identities.

A managed identity is an identity that can be assigned to an Azure compute resource (Azure

Virtual Machine, Azure Virtual Machine Scale Set, Service Fabric Cluster, Azure Kubernetes

cluster) or any App hosting platform supported by Azure. Once a managed identity is assigned

on the compute resource, it can be authorized, directly or indirectly, to access downstream

dependency resources, such as a storage account, SQL database, Cosmos DB, and so on.

Managed identity replaces secrets such as access keys or passwords. In addition, managed

identities can replace certificates or other forms of authentication for service-to-service

dependencies.

The following video shows how you can use managed identities:

Here are some of the benefits of using managed identities:

You don't need to manage credentials. Credentials aren’t even accessible to you.

You can use managed identities to authenticate to any resource that supports Microsoft

Entra authentication, including your own applications.

Managed identities can be used at no extra cost.

There are two types of managed identities:

**What are managed identities?**

https://learn-video.azurefd.net/vod/player?show=on-net&ep=using-azure-managed-

identities&locale=en-us&embedUrl=%2Fentra%2Fidentity%2Fmanaged-identities-azure-

resources%2Foverview

**Managed identity types**

**System-assigned**. Some Azure resources, such as virtual machines allow you to enable a

managed identity directly on the resource. When you enable a system-assigned managed

identity:

A service principal of a special type is created in Microsoft Entra ID for the identity. The

service principal is tied to the lifecycle of that Azure resource. When the Azure resource

is deleted, Azure automatically deletes the service principal for you.

By design, only that Azure resource can use this identity to request tokens from

Microsoft Entra ID.

You authorize the managed identity to have access to one or more services.

The name of the system-assigned service principal is always the same as the name of

the Azure resource it's created for. For a deployment slot, the name of its system-

assigned managed identity is `<app-name>/slots/<slot-name>` .

**User-assigned**. You may also create a managed identity as a standalone Azure resource.

You can create a user-assigned managed identity and assign it to one or more Azure

Resources. When you enable a user-assigned managed identity:

A service principal of a special type is created in Microsoft Entra ID for the identity. The

service principal is managed separately from the resources that use it.

User-assigned managed identities can be used by multiple resources.

You authorize the managed identity to have access to one or more services.

User-assigned managed identities, which are provisioned independently from compute

and can be assigned to multiple compute resources, are the recommended managed

identity type for Microsoft services.

Resources that support system assigned managed identities allow you to:

Enable or disable managed identities at the resource level.

Use role-based access control (RBAC) to grant permissions.

View the create, read, update, and delete (CRUD) operations in Azure Activity logs.

View sign in activity in Microsoft Entra ID sign in logs.

If you choose a user assigned managed identity instead:

You can create, read, update, and delete the identities.

You can use RBAC role assignments to grant permissions.

User assigned managed identities can be used on more than one resource.

CRUD operations are available for review in Azure Activity logs.

View sign in activity in Microsoft Entra ID sign in logs.

Operations on managed identities can be performed by using an Azure Resource Manager

template, the Azure portal, Azure CLI, PowerShell, and REST APIs.

The following table summarizes the differences between system-assigned and user-assigned

managed identities:

**Property**

**System-assigned managed identity**

**User-assigned managed identity**

Creation

Created as part of an Azure resource (for

example, Azure Virtual Machines or

Azure App Service).

Created as a stand-alone Azure resource.

Life cycle

Shared life cycle with the Azure resource

that the managed identity is created

with.

When the parent resource is deleted,

the managed identity is deleted as well.

Independent life cycle.

Must be explicitly deleted.

Sharing across

Azure resources

Can’t be shared.

It can only be associated with a single

Azure resource.

Can be shared.

The same user-assigned managed identity

can be associated with more than one

Azure resource.

Common use

cases

Workloads contained within a single

Azure resource.

Workloads needing independent

identities.

For example, an application that runs on

a single virtual machine.

Workloads that run on multiple resources

and can share a single identity.

Workloads needing preauthorization to a

secure resource, as part of a provisioning

flow.

Workloads where resources are recycled

frequently, but permissions should stay

consistent.

For example, a workload where multiple

virtual machines need to access the same

resource.

Service code running on your Azure compute resource uses either the Microsoft Authentication

Library (MSAL) or Azure.Identity SDK to retrieve a managed identity token from Entra ID

backed by the managed identity. This token acquisition doesn't require any secrets and is

automatically authenticated based on the environment where the code runs. As long as the

**Differences between system-assigned and user-**

**assigned managed identities**

ﾉ

**Expand table**

**Use managed identities for Azure resources**

**Use managed identity directly**

managed identity is authorized, the service code can access downstream dependencies that

support Entra ID authentication.

For example, you can use an Azure Virtual Machine (VM) as Azure Compute. You can then

create a user-assigned managed identity and assign it to the VM. The workload running on the

VM interfaces with both Azure.Identity (or MSAL) and Azure Storage client SDKs to access a

storage account. The user-assigned managed identity is authorized to access the storage

account.

Typically, you use managed identities in the following steps:

1\. Create a managed identity in Azure. You can choose between system-assigned managed

identity or user-assigned managed identity.

a. When using a user-assigned managed identity, you assign the managed identity to the

"source" Azure Resource, such as a Virtual Machine, Azure Logic App or an Azure Web

App.

2\. Authorize the managed identity to have access to the "target" service.

3\. Use the managed identity to access a resource. In this step, you can use the Azure SDK

with the Azure.Identity library or the Microsoft Authentication Library (MSAL). Some

"source" resources offer connectors that know how to use Managed identities for the

connections. In that case, you use the identity as a feature of that "source" resource.

Workload Identity Federation enables using a managed identity as a credential, just like

certificate or password, on Entra ID Applications. Whenever an Entra ID app is required, this is

the recommended way to be credential-free. There's a limit of 20 FICs when using managed

identities as FIC on an Entra ID App.

A workload acting in the capacity of Entra ID application can be hosted on any Azure compute

which has a managed identity. The workload uses the managed identity to acquire a token to

be exchanged for an Entra ID Application token, via workload identity federation. This feature is

also referred to as managed identity as FIC (Federated Identity Credentials). For more

information, see configure an application to trust a managed identity.

Managed identities for Azure resources can be used to authenticate to services that support

Microsoft Entra authentication. For a list of supported Azure services, see services that support

managed identities for Azure resources.

**Use managed identity as a Federated Identity Credential (FIC)**

**on an Entra ID app**

**Azure services that support managed identities**

Developer introduction and guidelines

Create a user-assigned managed identity

Workload identities.

**Related content**

**Workload identity federation concepts**

Article • 04/09/2025

Learn how workload identity federation enables secure access to Microsoft Entra protected

resources without managing secrets. This article provides an overview of its benefits and

supported scenarios.

You can use workload identity federation in scenarios such as GitHub Actions, workloads

running on Kubernetes, or workloads running in compute platforms outside of Azure.

Watch this video to learn why you would use workload identity federation.

Typically, a software workload (such as an application, service, script, or container-based

application) needs an identity in order to authenticate and access resources or communicate

with other services. When these workloads run on Azure, you can use managed identities and

the Azure platform manages the credentials for you. For a software workload running outside

of Azure, or those running in Azure but use app registrations for their identities, you need to

use application credentials (a secret or certificate) to access Microsoft Entra protected

resources (such as Azure, Microsoft Graph, Microsoft 365, or third-party resources). These

credentials pose a security risk and have to be stored securely and rotated regularly. You also

run the risk of service downtime if the credentials expire.

You use workload identity federation to configure a user-assigned managed identity or app

registration in Microsoft Entra ID to trust tokens from an external identity provider (IdP), such

as GitHub or Google. The user-assigned managed identity or app registration in Microsoft

Entra ID becomes an identity for software workloads running, for example, in on-premises

Kubernetes or GitHub Actions workflows. Once that trust relationship is created, your external

software workload exchanges trusted tokens from the external IdP for access tokens from

Microsoft identity platform. Your software workload uses that access token to access the

Microsoft Entra protected resources to which the workload has been granted access. You

eliminate the maintenance burden of manually managing credentials and eliminates the risk of

leaking secrets or having certificates expire.

**Why use workload identity federation?**

https://learn-video.azurefd.net/vod/player?id=4b15d772-e6de-4347-b8f6-

d943c200667a&locale=en-us&embedUrl=%2Fentra%2Fworkload-id%2Fworkload-

identity-federation

**Supported scenarios**

The following scenarios are supported for accessing Microsoft Entra protected resources using

workload identity federation:

Workloads running on any Kubernetes cluster (Azure Kubernetes Service (AKS), Amazon

Web Services EKS, Google Kubernetes Engine (GKE), or on-premises). Establish a trust

relationship between your user-assigned managed identity or app in Microsoft Entra ID

and a Kubernetes workload (described in the workload identity overview).

GitHub Actions. First, configure a trust relationship between your user-assigned managed

identity or application in Microsoft Entra ID and a GitHub repo in the Microsoft Entra

admin center

or using Microsoft Graph. Then configure a GitHub Actions workflow to

get an access token from Microsoft identity provider and access Azure resources.

Workloads running on Azure compute platforms using app identities. First assign a user-

assigned managed identity to your Azure VM or App Service. Then, configure a trust

relationship between your app and the user-assigned identity.

Google Cloud. First, configure a trust relationship between your user-assigned managed

identity or app in Microsoft Entra ID and an identity in Google Cloud. Then configure your

software workload running in Google Cloud to get an access token from Microsoft

identity provider and access Microsoft Entra protected resources. See Access Microsoft

Entra protected resources from an app in Google Cloud

.

Workloads running in Amazon Web Services (AWS). First, configure a trust relationship

between your user-assigned managed identity or app in Microsoft Entra ID and an

identity in Amazon Cognito. Then configure your software workload running in AWS to

get an access token from Microsoft identity provider and access Microsoft Entra

protected resources. See Workload identity federation with AWS

.

Other workloads running in compute platforms outside of Azure. Configure a trust

relationship between your user-assigned managed identity or application in Microsoft

Entra ID and the external IdP for your compute platform. You can use tokens issued by

that platform to authenticate with Microsoft identity platform and call APIs in the

Microsoft ecosystem. Use the client credentials flow to get an access token from

Microsoft identity platform, passing in the identity provider's JWT instead of creating one

yourself using a stored certificate.

SPIFFE and SPIRE are a set of platform agnostic, open-source standards for providing

identities to your software workloads deployed across platforms and cloud vendors. First,

configure a trust relationship between your user-assigned managed identity or app in

Microsoft Entra ID and a SPIFFE ID for an external workload. Then configure your external

software workload to get an access token from Microsoft identity provider and access

Microsoft Entra protected resources. See Workload identity federation with SPIFFE and

SPIRE

.

Create a service connection in Azure Pipelines. Create an Azure Resource Manager service

connection using workload identity federation.

Create a trust relationship between the external IdP and a user-assigned managed identity or

application in Microsoft Entra ID. The federated identity credential is used to indicate which

token from the external IdP should be trusted by your application or managed identity. You

configure a federated identity either:

On a user-assigned managed identity through the Microsoft Entra admin center

, Azure

CLI, Azure PowerShell, Azure SDK, and Azure Resource Manager (ARM) templates. The

external workload uses the access token to access Microsoft Entra protected resources

without needing to manage secrets (in supported scenarios). The steps for configuring

the trust relationship differs, depending on the scenario and external IdP.

On an app registration in the Microsoft Entra admin center

or through Microsoft Graph.

This configuration allows you to get an access token for your application without needing

to manage secrets outside Azure. For more information, learn how to configure an app to

trust an external identity provider and how to configure trust between an app and a user-

assigned managed identity.

The workflow for exchanging an external token for an access token is the same, however, for all

scenarios. The following diagram shows the general workflow of a workload exchanging an

external token for an access token and then accessing Microsoft Entra protected resources.

７ **Note**

Microsoft Entra ID issued tokens may not be used for federated identity flows. The

federated identity credentials flow does not support tokens issued by Microsoft Entra ID.

**How it works**

７ **Note**

The Federated Identity Credential `issuer` , `subject` , and `audience` values must case-

sensitively match the corresponding `issuer` , `subject` and `audience` values contained in

the token being sent to Microsoft Entra ID by the external IdP in order for the scenario to

be authorized. For more information surrounding this change, please visit **What's new for**

**Authentication**.

![](./assets/output_26_1.png)![](./assets/output_26_2.png)![](./assets/output_26_3.png)![](./assets/output_26_4.png)![](./assets/output_26_5.png)![](./assets/output_26_6.png)![](./assets/output_26_7.png)![](./assets/output_26_8.png)![](./assets/output_26_9.png)![](./assets/output_26_10.png)![](./assets/output_26_11.png)

1\. The external workload (such as a GitHub Actions workflow) requests a token from the

external IdP (such as GitHub).

2\. The external IdP issues a token to the external workload.

3\. The external workload (the sign in action in a GitHub workflow, for example) sends the

token to Microsoft identity platform and requests an access token.

4\. Microsoft identity platform checks the trust relationship on the user-assigned managed

identity or app registration and validates the external token against the OpenID Connect

(OIDC) issuer URL on the external IdP.

5\. When the checks are satisfied, Microsoft identity platform issues an access token to the

external workload.

6\. The external workload accesses Microsoft Entra protected resources using the access

token from Microsoft identity platform. A GitHub Actions workflow, for example, uses the

access token to publish a web app to Azure App Service.

The Microsoft identity platform stores only the first 100 signing keys when they're downloaded

from the external IdP's OIDC endpoint. If the external IdP exposes more than 100 signing keys,

you may experience errors when using workload identity federation.

How to create, delete, get, or update federated identity credentials on a user-assigned

managed identity or federated identity credentials on an app registration.

Set up a user-assigned managed identity as a federated identity credential on an app

registration.

Read the workload identity overview to learn how to configure a Kubernetes workload to

get an access token from Microsoft identity provider and access Microsoft Entra

protected resources.

Read the GitHub Actions documentation

to learn more about configuring your GitHub

Actions workflow to get an access token from Microsoft identity provider and access

Microsoft Entra protected resources.

**See also**

How Microsoft Entra ID uses the OAuth 2.0 client credentials grant and a client assertion

issued by another IdP to get a token.

For information about the required format of JWTs created by external identity providers,

read about the assertion format.

**Securing workload identities**

08/06/2025

Microsoft Entra ID Protection can detect, investigate, and remediate workload identities to protect

applications and service principals in addition to user identities.

A workload identity is an identity that allows an application access to resources, sometimes in the context

of a user. These workload identities differ from traditional user accounts as they:

Can’t perform multifactor authentication.

Often have no formal lifecycle process.

Need to store their credentials or secrets somewhere.

These differences make workload identities harder to manage and put them at higher risk for compromise.

To make use of workload identity risk reports, including **Risky workload identities** and the **Workload**

**identity detections** tab in the **Risk detections** in the admin center, you must have the following.

One of the following administrator roles assigned

Security Administrator

Security Operator

Security Reader

Users assigned the Conditional Access Administrator role can create policies that use risk as a

condition.

To take action on risky workload identities we recommend setting up risk-based Conditional Access

policies, which requires Workload Identities Premium

licensing: You can view, start a trial, and

acquire licenses on the Workload Identities

.

） **Important**

Full risk details and risk-based access controls are available to Workload Identities Premium

customers; however, customers without the **Workload Identities Premium**

licenses still receive all

detections with limited reporting details.

７ **Note**

ID Protection detects risk on single tenant, non-Microsoft SaaS, and multitenant apps. Managed

Identities aren't currently in scope.

**Prerequisites**

７ **Note**

We detect risk on workload identities across sign-in behavior and offline indicators of compromise.

**Detection**

**name**

**Detection**

**type**

**Description**

**riskEventType**

Microsoft

Entra threat

intelligence

Offline

This risk detection indicates some activity

that is consistent with known attack

patterns based on Microsoft's internal and

external threat intelligence sources.

investigationsThreatIntelligence

Suspicious

Sign-ins

Offline

This risk detection indicates sign-in

properties or patterns that are unusual for

this service principal. The detection learns

the baselines sign-in behavior for workload

identities in your tenant. This detection

takes between 2 and 60 days, and fires if

one or more of the following unfamiliar

properties appear during a later sign-in: IP

address / ASN, target resource, user agent,

hosting/non-hosting IP change, IP country,

credential type. Because of the

programmatic nature of workload identity

sign-ins, we provide a timestamp for the

suspicious activity instead of flagging a

specific sign-in event. Sign-ins that are

initiated after an authorized configuration

change might trigger this detection.

suspiciousSignins

Admin

confirmed

service

principal

compromised

Offline

This detection indicates an admin selected

'Confirm compromised' in the Risky

Workload Identities UI or using

riskyServicePrincipals API. To see which

admin confirmed this account

compromised, check the account’s risk

history (via UI or API).

adminConfirmedServicePrincipalCompromised

Leaked

Credentials

Offline

This risk detection indicates that the

account's valid credentials leaked. This leak

can occur when someone checks in the

credentials in public code artifact on

GitHub, or when the credentials are leaked

through a data breach. When the Microsoft

leaked credentials service acquires

credentials from GitHub, the dark web,

leakedCredentials

With **Microsoft Security Copilot**, you can use natural language prompts to get insights on risky

workload identities. Learn more about how to **Assess application risks using Microsoft Security**

**Copilot in Microsoft Entra**.

**Workload identity risk detections**

ﾉ

**Expand table**

**Detection**

**name**

**Detection**

**type**

**Description**

**riskEventType**

paste sites, or other sources, they're

checked against current valid credentials in

Microsoft Entra ID to find valid matches.

Malicious

application

Offline

This detection combines alerts from ID

Protection and Microsoft Defender for

Cloud Apps to indicate when Microsoft

disables an application for violating our

terms of service. We recommend

conducting an investigation

of the

application. Note: These applications show

`DisabledDueToViolationOfServicesAgreement`

on the `disabledByMicrosoftStatus` property

on the related application and service

principal resource types in Microsoft Graph.

To prevent them from being instantiated in

your organization again in the future, you

can't delete these objects.

maliciousApplication

Suspicious

application

Offline

This detection indicates that ID Protection

or Microsoft Defender for Cloud Apps

identified an application that might be

violating our terms of service but hasn't

disabled it. We recommend conducting an

investigation

of the application.

suspiciousApplication

Anomalous

service

principal

activity

Offline

This risk detection baselines normal

administrative service principal behavior in

Microsoft Entra ID, and spots anomalous

patterns of behavior like suspicious changes

to the directory. The detection is triggered

against the administrative service principal

making the change or the object that was

changed.

anomalousServicePrincipalActivity

Suspicious

API Traffic

Offline

This risk detection is reported when

abnormal GraphAPI traffic or directory

enumeration of a service principal is

observed. The Suspicious API Traffic

detection might indicate abnormal

reconnaissance or data exfiltration by a

service principal.

suspiciousAPITraffic

Organizations can find workload identities flagged for risk in one of two locations:

1\. Sign in to the Microsoft Entra admin center

as at least a Security Reader.

2\. Browse to **ID Protection** \> **Risky workload identities**.

**Identify risky workload identities**

You can also query risky workload identities using the Microsoft Graph API. There are two new collections

in the ID Protection APIs.

`riskyServicePrincipals`

`servicePrincipalRiskDetections`

Organizations can export data by configuring diagnostic settings in Microsoft Entra ID to send risk data to

a Log Analytics workspace, archive it to a storage account, stream it to an event hub, or send it to a SIEM

solution.

Using Conditional Access for workload identities, you can block access for specific accounts you choose

when ID Protection marks them "at risk." Policy can be applied to single-tenant service principals

registered in your tenant. Non-Microsoft SaaS, multi-tenanted apps, and managed identities are out of

scope.

For improved security and resilience of your workload identities, Continuous Access Evaluation (CAE) for

workload identities is a powerful tool that offers instant enforcement of your Conditional Access policies

and any detected risk signals. CAE-enabled non-Microsoft workload identities accessing CAE-capable first

party resources are equipped with 24 hour Long Lived Tokens (LLTs) that are subject to continuous security

![](./assets/output_31_1.png)



**Microsoft Graph APIs**

**Export risk data**

**Enforce access controls with risk-based Conditional**

**Access**

checks. For more information on configuring workload identity clients for CAE and current feature scope,

see CAE for workload identities documentation.

ID Protection provides organizations with two reports they can use to investigate workload identity risk.

These reports are the risky workload identities, and risk detections for workload identities. All reports allow

for downloading of events in .CSV format for further analysis.

Some of the key questions to answer during your investigation include:

Do accounts show suspicious sign-in activity?

Were there unauthorized changes to the credentials?

Were there suspicious configuration changes to accounts?

Did the account acquire unauthorized application roles?

The Microsoft Entra security operations guide for Applications provides detailed guidance on investigation

areas.

Once you determine if the workload identity was compromised, you should dismiss the account’s risk or

confirm the account as compromised in the Risky workload identities report. You can also select "Disable

service principal" if you want to block the account from further sign-ins.

1\. Inventory any credentials assigned to the risky workload identity, whether for the service principal or

application objects.

**Investigate risky workload identities**

![](./assets/output_32_1.png)



**Remediate risky workload identities**

2\. Add a new credential. Microsoft recommends using x509 certificates.

3\. Remove the compromised credentials. If you believe the account is at risk, we recommend removing

all existing credentials.

4\. Remediate any Azure KeyVault secrets that the Service Principal has access to by rotating them.

The Microsoft Entra Toolkit

is a PowerShell module that can help you perform some of these actions.

Conditional Access for workload identities

Microsoft Graph API

Microsoft Entra audit logs

Microsoft Entra sign-in logs

Simulate risk detections

**Related content**

**Conditional Access for workload identities**

Article • 04/25/2025

Conditional Access policies historically applied only to users when they access apps and

services like SharePoint Online. We're now extending support for Conditional Access policies to

be applied to service principals owned by the organization. We call this capability Conditional

Access for workload identities.

A workload identity is an identity that allows an application or service principal access to

resources, sometimes in the context of a user. These workload identities differ from traditional

user accounts as they:

Can’t perform multifactor authentication.

Often have no formal lifecycle process.

Need to store their credentials or secrets somewhere.

These differences make workload identities harder to manage and put them at higher risk for

compromise.

Conditional Access for workload identities enables blocking service principals:

From outside of known public IP ranges.

Based on risk detected by Microsoft Entra ID Protection.

In combination with authentication contexts.

） **Important**

Workload Identities Premium licenses are required to create or modify Conditional Access

policies scoped to service principals. In directories without appropriate licenses, existing

Conditional Access policies for workload identities continue to function, but can't be

modified. For more information, see **Microsoft Entra Workload ID**

.

７ **Note**

Policy can be applied to single tenant service principals that are registered in your tenant.

Third party SaaS and multi-tenanted apps are out of scope. Managed identities aren't

covered by policy. Managed identities could be included in an **access review** instead.

**Implementation**

Create a location based Conditional Access policy that applies to service principals.

1\. Sign in to the Microsoft Entra admin center

as at least a Conditional Access

Administrator.

2\. Browse to **Entra ID** \> **Conditional Access** \> **Policies**.

3\. Select **New policy**.

4\. Give your policy a name. We recommend that organizations create a meaningful standard

for the names of their policies.

5\. Under **Assignments**, select **Users or workload identities**.

a. Under **What does this policy apply to?**, select **Workload identities**.

b. Under **Include**, choose **Select service principals**, and select the appropriate service

principals from the list.

6\. Under **Target resources** \> **Resources (formerly cloud apps)** \> **Include**, select **All**

**resources (formerly 'All cloud apps')**. The policy applies only when a service principal

requests a token.

7\. Under **Conditions** \> **Locations**, include **Any location** and exclude **Selected locations**

where you want to allow access.

8\. Under **Grant**, **Block access** is the only available option. Access is blocked when a token

request is made from outside the allowed range.

9\. Your policy can be saved in **Report-only** mode, allowing administrators to estimate the

effects, or policy is enforced by turning policy **On**.

10\. Select **Create** to complete your policy.

Create a risk-based Conditional Access policy that applies to service principals.

**Create a location-based Conditional Access policy**

**Create a risk-based Conditional Access policy**

1\. Sign in to the Microsoft Entra admin center

as at least a Conditional Access

Administrator.

2\. Browse to **Entra ID** \> **Conditional Access** \> **Policies**.

3\. Select **New policy**.

4\. Give your policy a name. We recommend that organizations create a meaningful standard

for the names of their policies.

5\. Under **Assignments**, select **Users or workload identities**.

a. Under **What does this policy apply to?**, select **Workload identities**.

b. Under **Include**, choose **Select service principals**, and select the appropriate service

principals from the list.

6\. Under **Target resources** \> **Resources (formerly cloud apps)** \> **Include**, select **All**

**resources (formerly 'All cloud apps')**. The policy applies only when a service principal

requests a token.

7\. Under **Conditions** \> **Service principal risk**

a. Set the **Configure** toggle to **Yes**.

![](./assets/output_36_1.png)



b. Select the levels of risk where you want this policy to trigger.

c. Select **Done**.

8\. Under **Grant**, **Block access** is the only available option. Access is blocked when the

specified risk levels are seen.

9\. Your policy can be saved in **Report-only** mode, allowing administrators to estimate the

effects, or policy is enforced by turning policy **On**.

10\. Select **Create** to complete your policy.

If you wish to roll back this feature, you can delete or disable any created policies.

The sign-in logs are used to review how policy is enforced for service principals or the expected

affects of policy when using report-only mode.

1\. Browse to **Entra ID** \> **Monitoring & health** \> **Sign-in logs** \> **Service principal sign-ins**.

2\. Select a log entry and choose the **Conditional Access** tab to view evaluation information.

Failure reason when Conditional Access blocks a Service Principal: "Access has been blocked

due to Conditional Access policies."

To view results of a location-based policy, go to the **Report-only** tab of events in the **Sign-in**

**report**, or use the **Conditional Access Insights and Reporting** workbook.

To view results of a risk-based policy, refer to the **Report-only** tab of events in the **Sign-in**

**report**.

You can get the objectID of the service principal from Microsoft Entra Enterprise Applications.

The Object ID in Microsoft Entra App registrations can’t be used. This identifier is the Object ID

of the app registration, not of the service principal.

1\. Browse to **Entra ID** \> **Enterprise apps**, find the application you registered.

**Roll back**

**Sign-in logs**

**Report-only mode**

**Reference**

**Finding the objectID**

2\. From the **Overview** tab, copy the **Object ID** of the application. This identifier is the unique

to the service principal, used by Conditional Access policy to find the calling app.

Sample JSON for location-based configuration using the Microsoft Graph beta endpoint.

JSON

Using network location in a Conditional Access policy

What is Conditional Access report-only mode?

**Microsoft Graph**

`{`

`  ``"displayName"` `: ``"Name"` `,`

`  ``"state"` `: ``"enabled OR disabled OR enabledForReportingButNotEnforced"` `,`

`  ``"conditions"` `: {`

`    ``"applications"` `: {`

`      ``"includeApplications"` `: [`

`        ``"All"`

`      ]`

`    },`

`    ``"clientApplications"` `: {`

`      ``"includeServicePrincipals"` `: [`

`        ``"[Service principal Object ID] OR ServicePrincipalsInMyTenant"`

`      ],`

`      ``"excludeServicePrincipals"` `: [`

`        ``"[Service principal Object ID]"`

`      ]`

`    },`

`    ``"locations"` `: {`

`      ``"includeLocations"` `: [`

`        ``"All"`

`      ],`

`      ``"excludeLocations"` `: [`

`        ``"[Named location ID] OR AllTrusted"`

`      ]`

`    }`

`  },`

`  ``"grantControls"` `: {`

`    ``"operator"` `: ``"and"` `,`

`    ``"builtInControls"` `: [`

`      ``"block"`

`    ]`

`  }`

`}`

**Next steps**

**Continuous access evaluation for workload**

**identities**

08/29/2025

Continuous access evaluation (CAE) for workload identities improves your organization's

security. It enforces Conditional Access location and risk policies in real time and instantly

enforces token revocation events for workload identities.

Continuous access evaluation doesn't currently support managed identities.

Continuous access evaluation for workload identities is supported only on access requests sent

to Microsoft Graph as a resource provider. More resource providers will be added over time.

Service principals for line-of-business (LOB) applications are supported.

The following revocation events are supported:

Service principal disable

Service principal delete

High service principal risk as detected by Microsoft Entra ID Protection

Continuous access evaluation for workload identities supports Conditional Access policies that

target location and risk.

Developers can opt in to continuous access evaluation for workload identities when their API

requests `xms_cc` as an optional claim. The `xms_cc` claim with a value of `cp1` in the access token

is the authoritative way to identify that a client application is capable of handling a claims

challenge. For more information about how to make this work in your application, see Claims

challenges, claims requests, and client capabilities.

To opt out, don't send the `xms_cc` claim with a value of `cp1` .

Organizations that have Microsoft Entra ID P1 or P2 can create a Conditional Access policy to

disable continuous access evaluation applied to specific workload identities as an immediate

**Scope of support**

**Enable your application**

**Disable**

stopgap measure.

When a client's access to a resource is blocked because CAE is triggered, the client's session is

revoked, and the client needs to reauthenticate. You can verify this behavior in the sign-in logs.

Follow these steps to verify sign-in activity in the sign-in logs:

1\. Sign in to the Microsoft Entra admin center

as at least a Security Reader.

2\. Browse to **Entra ID** \> **Monitoring & health** \> **Sign-in logs** \> **Service Principal Sign-ins**.

Use filters to simplify the debugging process.

3\. Select an entry to view activity details. The **Continuous access evaluation** field shows

whether a CAE token is issued for a specific sign-in attempt.

Learn how to register an application with Microsoft Entra ID and create a service principal.

Learn how to use Continuous Access Evaluation enabled APIs in your applications.

Explore a sample application using continuous access evaluation

.

Learn about securing workload identities with Microsoft Entra ID Protection.

Understand what continuous access evaluation is.

**Troubleshooting**

**Related content**

**How to use Microsoft Entra**

**Recommendations**

08/22/2025

The Microsoft Entra recommendations feature provides you with personalized insights with

actionable guidance to:

Help you identify opportunities to implement best practices for Microsoft Entra related

features.

Improve the state of your Microsoft Entra tenant.

Optimize the configurations for your scenarios.

This article covers how to work with Microsoft Entra recommendations. Each Microsoft Entra

recommendation contains similar details such as a description, the value of addressing the

recommendation, and the steps to address the recommendation. Microsoft Graph API

guidance is also provided in this article.

There are different role requirements for viewing or updating a recommendation. Use the

least-privileged role for the type of access needed. For a full list of roles, see Least privileged

roles by task.

**Microsoft Entra role**

**Access type**

Reports Reader

Read-only

Security Reader

Read-only

Global Reader

Read-only

Authentication Policy Administrator

Update and read

Exchange Administrator

Update and read

Security Administrator

Update and read

`DirectoryRecommendations.Read.All`

Read-only in Microsoft Graph

`DirectoryRecommendations.ReadWrite.All`

Update and read in Microsoft Graph

**Prerequisites**

ﾉ

**Expand table**

Some recommendations might require a P2 or other license. For more information, see the

Recommendations overview table.

Most recommendations follow the same pattern. You're provided information about how the

recommendation works, its value, and some action steps to address the recommendation. This

section provides an overview of the details provided in a recommendation, but aren't specific

to one recommendation.

1\. Sign in to the Microsoft Entra admin center

as at least a Reports Reader.

2\. Browse to **Entra ID** \> **Overview** \> **Recommendations**.

3\. Select a recommendation from the list.

![](./assets/output_42_1.png)

Each recommendation provides the same set of details that explain what the recommendation

is, why it's important, and how to fix it. Recommendation data refreshes every 24 hours with a

one-day lag. In rare instances, updates may take up to 72 hours to appear.

![](./assets/output_42_2.png)

**How to read a recommendation**

The **Status** of a recommendation can be active, completed, dismissed, or postponed. The

recommendation service automatically marks a recommendation as completed when all

impacted resources are addressed.

**Active**: The recommendation has resources that need to be addressed. A dismissed,

postponed, or completed recommendation can be manually changed back to active.

**Completed**: All resources in the recommendation have been addressed. The status is

updated automatically by the system when all resources are addressed according to the

action plan. Recommendations can't be manually marked as completed.

**Dismissed**: If the recommendation is irrelevant or the data is wrong, you can dismiss the

recommendation. You must provide a reason for dismissing the recommendation.

**Postponed**: If you want to address the recommendation at a later time, you can postpone

it. The recommendation becomes active when the selected date occurs. You can postpone

a recommendation for up to a year.

The **Priority** of a recommendation could be low, medium, or high. These values are determined

by several factors, such as security implications, health concerns, or potential breaking changes.

**High**: Must do. Not acting will result in severe security implications or potential

downtime.

**Medium**: Should do. No severe risk if action isn't taken.

**Low**: Might do. No security risks or health concerns if action isn't taken.

The **Status description** tells you the date the recommendation status changed.

The recommendation's **Value** is an explanation of why completing the recommendation

benefits your organization and the value of the associated feature.

The **Action plan** provides step-by-step instructions to implement a recommendation. The

Action plan might include links to relevant documentation or direct you to other pages in

the Azure portal.

Some recommendations might include a **User impact** that describes the user experience

when the recommendation is addressed.

**Status**

**Priority**

**Recommendation details**

![](./assets/output_44_1.png)

The **Impacted resources** for a recommendation could be applications, users, or your full tenant.

If the impacted resource is at the tenant level, you might need to make a global change. Not all

recommendations populate the impacted resources table. For example, the "Remove unused

applications" recommendation lists all applications that were identified by the

recommendation service. Tenant-level recommendations, however, won't have any resources

listed in the table.

For those recommendations where there are separate resources to address, the **Impacted**

**resources** table contains a list of resources identified by the recommendation. The resource's

name, ID, date it was first detected, and status are provided. The resource could be an

application, user, or resource service principal, for example.

You can mark individual impacted resources as _dismissed_ or _postponed_. The rules and

functionality at the resource level are the same as at the recommendation level. In some

recommendations, you can select the resource or the **More details** link to access the resource

directly.

**Impacted resources**

![](./assets/output_45_1.png)

In the Microsoft Entra admin enter, the impacted resources are limited to a maximum of 50

resources. To view all impacted resources for a recommendation, use the following Microsoft

Graph API request: `GET /directory/recommendations/{recommendationId}/impactedResources`

You can update the status of a recommendation and any related resource in the Microsoft

Entra admin center or using Microsoft Graph.

1\. Sign in to the Microsoft Entra admin center

as at least a Reports Reader.

2\. Browse to **Entra ID** \> **Overview** \> **Recommendations**.

3\. Select a recommendation from the list.

4\. Follow the guidance in the **Action plan**.

5\. If you need to manually change the status of a recommendation, select **Mark as** from

the top of the page and select a status.

**How to update a recommendation and impacted**

**resources**

Microsoft Entra admin center

![](./assets/output_46_1.png)

Mark a recommendation as **Dismissed** if you think the recommendation is

irrelevant or the data is wrong.

In the panel that opens, select a dismissed reason so we can improve the

service.

Mark a recommendation as **Postponed** if you want to address the

recommendation at a later time.

In the panel that opens, select a date within the next year to postpone the

recommendation.

The recommendation becomes active when the selected date occurs.

Mark a dismissed, postponed, or completed recommendation as **Active** to

reassess the resources and resolve the issue.

Recommendations change to **Completed** when all impacted resources were

addressed.

If the service identifies an active resource for a completed recommendation

the next time the service runs, the recommendation automatically changes

back to **Active**.

Completing a recommendation is the only action collected in the audit log.

To view these logs, go to **Microsoft Entra ID** \> **Audit logs** and filter the

service to "Microsoft Entra recommendations."

6\. If you need to manually change the status of an impacted resource, select the

checkbox for that resource in the **Impacted resources** table and select the status

from the menu.

7\. Continue to monitor the recommendations in your tenant for changes.

７ **Note**

You can't manually mark a recommendation as completed. The system automatically

marks a recommendation as completed when all impacted resources are addressed.

When the service runs, if no active resources are found, the recommendation is

marked as completed.

Review the Microsoft Entra recommendations overview

Learn about Service Health notifications

**Related content**

**Overview of federated identity credentials**

**in Microsoft Entra ID**

Namespace: microsoft.graph

Traditionally, developers use certificates or client secrets for their application's credentials to

authenticate with and access services in Microsoft Entra ID. To access the services in their

Microsoft Entra tenant, developers had to store and manage application credentials outside

Azure, introducing the following bottlenecks:

A maintenance burden for certificates and secrets.

The risk of leaking secrets.

Certificates expiring and service disruptions because of failed authentication.

**Federated identity credentials** are a new type of credential that enables workload identity

federation for software workloads. Workload identity federation allows you to access Microsoft

Entra protected resources without needing to manage secrets (for supported scenarios).

You create a trust relationship between an external identity provider (IdP) and an app in

Microsoft Entra ID by configuring a federated identity credential. The federated identity

credential is used to indicate which token from the external IdP your application can trust. After

that trust relationship is created, your software workload can exchange trusted tokens from the

external identity provider for access tokens from the Microsoft identity platform. Your software

workload then uses that access token to access the Microsoft Entra protected resources to

which the workload has access. This process eliminates the maintenance burden of manually

managing credentials and eliminates the risk of leaking secrets or having certificates expire. For

more information and supported scenarios, see workload identity federation.

**How do federated identity credentials work?**

７ **Note**

The match performed between the Federated Identity Credential `issuer` , `subject` , and

`audience` values and the corresponding values in the token being sent to Microsoft Entra

ID by the external IdP is case-sensitive. These values must match exactly in order for the

scenario to be authorized. For more information,see **Federated Identity Credentials now**

**use case-sensitive matching**.

The federatedIdentityCredential resource represents the configuration of a federated identity

credential via Microsoft Graph. Use the Create federatedIdentityCredential API to configure the

object. The following properties are the building blocks of federated identity credentials:

**audiences** \- The audience that can appear in the external token. This field is mandatory

and should be set to `api://AzureADTokenExchange` for Microsoft Entra ID. It says what

Microsoft identity platform should accept in the `aud` claim in the incoming token. This

value represents Microsoft Entra ID in your external identity provider and has no fixed

value across identity providers - you might need to create a new application registration

in your IdP to serve as the audience of this token.

**issuer** \- The URL of the external identity provider. Must match the **issuer** claim of the

external token being exchanged.

**subject** \- The identifier of the external software workload within the external identity

provider. Like the audience value, it has no fixed format, as each IdP uses their own -

sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings.

The value here must match the `sub` claim within the token presented to Microsoft Entra

ID.

**name** \- A unique string to identify the credential. This property is an alternate key and the

value can be used to reference the federated identity credential via the GET and UPSERT

operations.

The combination of **issuer** and **subject** must be unique on the app. When the external software

workload requests Microsoft identity platform to exchange the external token for an access

token, the **issuer** and **subject** values of the federated identity credential are checked against

the `issuer` and `subject` claims provided in the external token. If that validation check passes,

Microsoft identity platform issues an access token to the external software workload.

A maximum of 20 federated identity credentials can be added per application object or user-

assigned managed identity.

federatedIdentityCredential resource type

Workload identity federation

What are managed identities for Azure resources?

**Set up federated identity credentials through**

**Microsoft Graph**

**Design considerations**

**Related content**

**Last updated on 10/12/2024**

**Flexible federated identity credentials**

**(preview)**

Article • 02/27/2025

Flexible federated identity credentials are an advanced feature of Microsoft Entra

Workload ID that enhances the existing federated identity credential model. This article

explains how these credentials work, their benefits, and current limitations.

Flexible federated identity credentials allow the use of a restricted expression language

for matching incoming `subject` claims and enabling the inclusion of custom claims,

helping reduce management overhead and address scale limits in workload identity

federation. If you're looking to streamline authentication for external workloads with

Microsoft Entra, this guide provides you with the necessary insights and steps to use this

powerful feature.

The current behavior of federated identity credentials within workload identity

federation requires explicit matching when comparing the defined `subject` , `issuer` , and

`audience` in the federated identity credential against the `subject` , `issuer` , and `audience`

contained in the token sent to Microsoft Entra. When combined with the current limit of

20 federated identity credentials for a given application or user-assigned managed

identity, scale limits can be hit quickly.

Flexible federated identity credentials extend the existing federated identity credential

model by allowing the use of a restricted expression language when matching against

incoming `subject` claims. It can also be used to extend the federated identity credential

authorization model beyond the `subject` , `issuer` , and `audience` claims by enabling the

inclusion of certain allowed custom claims within your federated identity credentials.

Flexible federated identity credentials can help reduce management overhead when

attempting to authenticate external workloads with Microsoft Entra, and address the

scale limits in workload identity federation implementations.

**Why use flexible federated identity credentials?**

**How do flexible federated identity credentials**

**work?**

Flexible federated identity credentials don't change the baseline functionality provided

by federated identity credentials. These trust relationships are still used to indicate

which token from the external IdP should be trusted by your application. Instead, they

extend the ability of federated identity credentials by enabling scenarios which

previously required multiple federated identity credentials to instead be managed under

a single flexible federated identity credential. A few examples include:

GitHub repositories with various workflows, each running on a different branch (or

being used across branches). Previously, a unique federated identity credential was

required for each of the branches in which workflows could run across. With

flexible federated identity credentials, this scenario can be managed under a single

federated identity credential.

Terraform cloud `run_phases` plans, which each requires a unique federated identity

credential. With flexible federated identity credentials, this can be managed under

a single flexible federated identity credential.

Reusable GitHub Actions workflows, where wildcards can be used against GitHub's

custom `job_workflow_ref` claim.

A flexible federated identity credentials expression is made up of three parts, the claim

lookup, the operator, and the comparand. Refer to the following table for a breakdown

of each part:

**Name**

**Description**

**Example**

Claim

lookup

The claim lookup must follow the pattern of

`claims['<claimName>']`

`claims['sub']`

７ **Note**

Flexible federated identity credentials support is currently provided for matching

against GitHub, GitLab, and Terraform Cloud issued tokens. This support exists only

for federated identity credentials configured on application objects currently. You

can only create and manage flexible federated identity credentials via Microsoft

Graph or the Azure portal.

**Flexible federated identity credential language**

**structure**

ﾉ

**Expand table**

**Name**

**Description**

**Example**

Operator

The operator portion must be just the operator

name, separated from the claim lookup and

comparand by a single space

`matches`

Comparand

The comparand contains what you intend to

compare the claim specified in the lookup against

– it must be contained within single quotes

`'repo:contoso/contoso-`

`repo:ref:refs/heads/*'`

Put together, an example flexible federated identity credentials expression would look

like the following JSON object:

JSON

To accommodate the flexible federated identity credential functionality, the

`federatedIdentityCredentials` resource is being extended with a new

`claimsMatchingExpression` property. In addition to this, the `subject` property is now

nullable. The `claimsMatchingExpression` and `subject` properties are mutually exclusive,

so you can't define both within a federated identity credential.

`audiences` : The audience that can appear in the external token. This field is

mandatory and should be set to `api://AzureADTokenExchange` for Microsoft Entra ID.

It says what Microsoft identity platform should accept in the `aud` claim in the

incoming token. This value represents Microsoft Entra ID in your external identity

provider and has no fixed value across identity providers - you might need to

create a new application registration in your IdP to serve as the audience of this

token.

`issuer` : The URL of the external identity provider. Must match the issuer claim of

the external token being exchanged.

`subject` : The identifier of the external software workload within the external

identity provider. Like the audience value, it has no fixed format, as each IdP uses

their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes

arbitrary strings. The value here must match the `sub` claim within the token

presented to Microsoft Entra ID. If `subject` is defined, `claimsMatchingExpression`

must be set to null.

`"claims['sub'] matches 'repo:contoso/contoso-repo:ref:refs/heads/*'."`

**Set up federated identity credentials through**

**Microsoft Graph**

`name` : A unique string to identify the credential. This property is an alternate key

and the value can be used to reference the federated identity credential via

the GET and UPSERT operations.

`claimsMatchingExpression` : a new complex type containing two properties, `value`

and `languageVersion` . Value is used to define the expression, and `languageVersion`

is used to define the version of the flexible federated identity credential expression

language (FFL) being used. `languageVersion` should always be set to 1. If

`claimsMatchingExpression` is defined, `subject` must be set to null.

Flexible federated identity credentials currently support the use of a few operators

across the enabled issuers. Single quotes are interpreted as escape characters within the

flexible federated identity credential expression language.

**Operator**

**Description**

**Example**

`matches`

Enables the use of single-

character (denoted by `?` )

and multi-character

(denoted by `*` ) wildcard

matching for the specified

claim

• `"claims['sub'] matches 'repo:contoso/contoso-`

`repo:ref:refs/heads/*'"`

• `"claims['sub'] matches 'repo:contoso/contoso-repo-`

`*:ref:refs/heads/????'"`

`eq`

Used for explicitly

matching against a

specified claim

• `"claims['sub'] eq 'repo:contoso/contoso-`

`repo:ref:refs/heads/main'"`

`and`

Boolean operator for

combining expressions

against multiple claims

• `"claims['sub'] eq 'repo:contoso/contoso-`

`repo:ref:refs/heads/main' and`

`claims['job_workflow_ref'] matches 'foo-org/bar-repo`

`/.github/workflows/*@refs/heads/main'"`

Depending on the platform you're using, you need to implement different issuer URLs,

claims, and operators. Use the following tabs to select your chosen platform.

**Flexible federated identity credential**

**expression language functionality**

ﾉ

**Expand table**

**Issuer URLs, supported claims, and operators**

**by platform**

Supported issuer URLs: `https://token.actions.githubusercontent.com`

Supported claims and operators per claim:

Claim `sub` supports operators `eq` and `matches`

Claim `job_workflow_ref` supports operators `eq` and `matches`

Explicit flexible federated identity credential support doesn't yet exist within Azure CLI,

Azure PowerShell, or Terraform providers. If you attempt to configure a flexible

federated identity credential with any of these tools, you see an error. Additionally, if

you configure a flexible federated identity credential via either Microsoft Graph or the

Azure portal and attempt to read that flexible federated identity credential with any of

these tools, you see an error.

You can use Azure CLI's `az rest` method to make REST API requests for flexible

federated identity credential creation and management.

Bash

Implement a flexible federated identity credential

Configure a user-assigned managed identity to trust an external identity provider

How to create, delete, get, or update federated identity credentials on an app

registration.

GitHub

**Azure CLI, Azure PowerShell, and Terraform**

**providers**

`az rest --method post \`

`    --url `

`https://graph.microsoft.com/beta/applications/{objectId}/federatedIdentityCr`

`edentials`

`    --body ``"{'name': 'FlexFic1', 'issuer': `

`'https://token.actions.githubusercontent.com', 'audiences': `

`['api://AzureADTokenExchange'], 'claimsMatchingExpression': {'value': `

`'claims[\'sub\'] matches \'repo:contoso/contoso-org:ref:refs/heads/*\'', `

`'languageVersion': 1}}"`

**Related content**

**Feedback**

**Was this page helpful?**

Provide product feedback

Read the GitHub Actions documentation

to learn more about configuring your

GitHub Actions workflow to get an access token from Microsoft identity provider

and access Microsoft Entra protected resources.

Learn about the assertion format.

 **Yes**

 **No**

**Configure an app to trust an external**

**identity provider**

Article • 12/13/2024

This article describes how to manage a federated identity credential on an application in

Microsoft Entra ID. The federated identity credential creates a trust relationship between

an application and an external identity provider (IdP).

You can then configure an external software workload to exchange a token from the

external IdP for an access token from Microsoft identity platform. The external workload

can access Microsoft Entra protected resources without needing to manage secrets (in

supported scenarios). To learn more about the token exchange workflow, read about

workload identity federation.

In this article, you learn how to create, list, and delete federated identity credentials on

an application in Microsoft Entra ID.

To create, update, or delete a federated identity credential, the account performing the

action must have the Application Administrator, Application Developer, Cloud

Application Administrator, or Application Owner role. The

microsoft.directory/applications/credentials/update permission is required to update a

federated identity credential.

A maximum of 20 federated identity credentials can be added to an application or user-

assigned managed identity.

When you configure a federated identity credential, there are several important pieces

of information to provide:

_issuer_ and _subject_ are the key pieces of information needed to set up the trust

relationship. The combination of `issuer` and `subject` must be unique on the app.

When the external software workload requests Microsoft identity platform to

exchange the external token for an access token, the _issuer_ and _subject_ values of

the federated identity credential are checked against the `issuer` and `subject`

claims provided in the external token. If that validation check passes, Microsoft

identity platform issues an access token to the external software workload.

**Important considerations and restrictions**

_issuer_ is the URL of the external identity provider and must match the `issuer` claim

of the external token being exchanged. Required. If the `issuer` claim has leading

or trailing whitespace in the value, the token exchange is blocked. This field has a

character limit of 600 characters.

_subject_ is the identifier of the external software workload and must match the `sub`

( ` subject` ) claim of the external token being exchanged. _subject_ has no fixed format,

as each IdP uses their own - sometimes a GUID, sometimes a colon delimited

identifier, sometimes arbitrary strings. This field has a character limit of 600

characters.

_audiences_ lists the audiences that can appear in the external token. Required. You

must add a single audience value, which has a limit of 600 characters. The

recommended value is "api://AzureADTokenExchange". It says what Microsoft

identity platform must accept in the `aud` claim in the incoming token.

_name_ is the unique identifier for the federated identity credential. Required. This

field has a character limit of 3-120 characters and must be URL friendly.

Alphanumeric, dash, or underscore characters are supported, the first character

must be alphanumeric only. It's immutable once created.

_description_ is the user-provided description of the federated identity credential.

Optional. The description isn't validated or checked by Microsoft Entra ID. This field

has a limit of 600 characters.

Wildcard characters aren't supported in any federated identity credential property value.

） **Important**

The _subject_ setting values must exactly match the configuration on the GitHub

workflow configuration. Otherwise, Microsoft identity platform will look at the

incoming external token and reject the exchange for an access token. You

won't get an error, the exchange fails without error.

） **Important**

If you accidentally add the incorrect external workload information in the

_subject_ setting the federated identity credential is created successfully without

error. The error does not become apparent until the token exchange fails.

To learn more about supported regions, time to propagate federated credential updates,

supported issuers and more, read Important considerations and restrictions for

federated identity credentials.

Create an app registration or managed identity in Microsoft Entra ID. Grant your

app access to the Azure resources targeted by your external software workload.

Find the object ID of the app (not the application (client) ID), which you need in the

following steps. You can find the object ID of the app in the Microsoft Entra admin

center

. Go to the list of app registrations and select your app registration. In

**Overview**, you can find the **Object ID**.

Get the _subject_ and _issuer_ information for your external IdP and software workload,

which you need in the following steps.

To add a federated identity for GitHub actions, follow these steps:

1\. Find your app registration in the app registrations experience of the Microsoft

Entra admin center

. Select **Certificates & secrets** in the left nav pane, select the

**Federated credentials** tab, and select **Add credential**.

2\. In the **Federated credential scenario** drop-down box, select **GitHub actions**

**deploying Azure resources**.

3\. Specify the **Organization** and **Repository** for your GitHub Actions workflow.

4\. For **Entity type**, select **Environment**, **Branch**, **Pull request**, or **Tag** and specify the

value. The values must exactly match the configuration in the GitHub workflow

.

Pattern matching isn't supported for branches and tags. Specify an environment if

your on-push workflow runs against many branches or tags. For more info, read

the examples.

5\. Add a **Name** for the federated credential.

6\. The **Issuer**, **Audiences**, and **Subject identifier** fields autopopulate based on the

values you entered.

**Prerequisites**

**Configure a federated identity credential on an**

**app**

**GitHub Actions**

7\. Select **Add** to configure the federated credential.

![](./assets/output_60_1.png)

Use the following values from your Microsoft Entra application registration for your

GitHub workflow:

`AZURE_CLIENT_ID` the **Application (client) ID**

`AZURE_TENANT_ID` the **Directory (tenant) ID**

The following screenshot demonstrates how to copy the application ID and tenant

ID.

![](./assets/output_61_1.png)

`AZURE_SUBSCRIPTION_ID` your subscription ID. To get the subscription ID, open

**Subscriptions** in Azure portal

and find your subscription. Then, copy the

**Subscription ID**.

For a workflow triggered by a push or pull request event on the main branch:

yml

Specify an **Entity type** of **Branch** and a **GitHub branch name** of "main".

For Jobs tied to an environment named "production":

yml

**Entity type examples**

**Branch example**

`on:`

`  push:`

`    branches:` ` ` `[`  ` `  `main` ` ` `]`

`  pull_request:`

`    branches:` ` ` `[`  ` `  `main` ` ` `]`

**Environment example**

`on:`

`  push:`

`    branches:`

`      -`  ` `  `main`

Specify an **Entity type** of **Environment** and a **GitHub environment name** of

"production".

For example, for a workflow triggered by a push to the tag named "v2":

yml

Specify an **Entity type** of **Tag** and a **GitHub tag name** of "v2".

For a workflow triggered by a pull request event, specify an **Entity type** of **Pull request**

Find your app registration in the app registrations experience of the Microsoft Entra

admin center

. Select **Certificates & secrets** in the left nav pane, select the **Federated**

**credentials** tab, and select **Add credential**.

Select the **Kubernetes accessing Azure resources** scenario from the dropdown menu.

Fill in the **Cluster issuer URL**, **Namespace**, **Service account name**, and **Name** fields:

`jobs:`

`  deployment:`

`    runs-on:`  ` `  `ubuntu-latest`

`    environment:`  ` `  `production`

`    steps:`

`      - name:`  ` `  `deploy`

`        ``# ...deployment-specific steps`

**Tag example**

`on:`

`  push:`

`    ``# Sequence of patterns matched against refs/heads`

`    branches:`

`      -`  ` `  `main`

`      -` ` ` `'mona/octocat'`

`      -` ` ` `'releases/**'`

`    ``# Sequence of patterns matched against refs/tags`

`    tags:`

`      -`  ` `  `v2`

`      -`  ` `  `v1.*`

**Pull request example**

**Kubernetes**

**Cluster issuer URL** is the OIDC issuer URL for the managed cluster or the OIDC

Issuer URL

for a self-managed cluster.

**Service account name** is the name of the Kubernetes service account, which

provides an identity for processes that run in a Pod.

**Namespace** is the service account namespace.

**Name** is the name of the federated credential, which can't be changed later.

Find your app registration in the app registrations experience of the Microsoft Entra

admin center

. Select **Certificates & secrets** in the left nav pane, select the **Federated**

**credentials** tab, and select **Add credential**.

Select the **Other issuer** scenario from the dropdown menu.

Specify the following fields (using a software workload running in Google Cloud as an

example):

**Name** is the name of the federated credential, which can't be changed later.

**Subject identifier**: must match the `sub` claim in the token issued by the external

identity provider. In this example using Google Cloud, _subject_ is the Unique ID of

the service account you plan to use.

**Issuer**: must match the `iss` claim in the token issued by the external identity

provider. A URL that complies with the OIDC Discovery spec. Microsoft Entra ID

uses this issuer URL to fetch the keys that are necessary to validate the token. For

Google Cloud, the _issuer_ is `https://accounts.google.com` .

Find your app registration in the app registrations experience of the Microsoft Entra

admin center

. Select **Certificates & secrets** in the left nav pane and select the

**Federated credentials** tab. The federated credentials that are configured on your app

are listed.

Find your app registration in the app registrations experience of the Microsoft Entra

admin center

. Select **Certificates & secrets** in the left nav pane and select the

**Other identity providers**

**List federated identity credentials on an app**

**Delete a federated identity credential from an**

**app**

**Feedback**

**Was this page helpful?**

Provide product feedback

**Federated credentials** tab. The federated credentials that are configured on your app

are listed.

To delete a federated identity credential, select the **Delete** icon for the credential.

1\. Navigate to Microsoft Entra ID and select the application where you want to

configure the federated identity credential.

2\. In the left-hand navigation pane, select **Certificates & secrets**.

3\. Under the **Federated credentials** tab, select **\+ Add credential**.

4\. In the **Add a credential** window that appears, from the dropdown menu next to

**Federated credential scenario**, select **Other issuer**.

5\. In **Value** enter the claim matching expression you want to use.

To learn how to use workload identity federation for Kubernetes, see Microsoft

Entra Workload ID for Kubernetes

open source project.

To learn how to use workload identity federation for GitHub Actions, see Configure

a GitHub Actions workflow to get an access token.

Read the GitHub Actions documentation

to learn more about configuring your

GitHub Actions workflow to get an access token from Microsoft identity provider

and access Azure resources.

For more information, read about how Microsoft Entra ID uses the OAuth 2.0 client

credentials grant and a client assertion issued by another IdP to get a token.

For information about the required format of JWTs created by external identity

providers, read about the assertion format.

**Set up a Flexible Federated identity credential**

**(preview)**

**See also**

 **Yes**

 **No**

**Configure an application to trust a**

**managed identity**

06/06/2025

This article describes how to configure a Microsoft Entra application to trust a managed

identity. You can then exchange the managed identity token for an access token that can

access Microsoft Entra protected resources without needing to use or manage App secrets.

An Azure account with an active subscription. Create an account for free

.

This Azure account must have permissions to update application credentials. Any of the

following Microsoft Entra roles include the required permissions:

Application Administrator

Application Developer

Cloud Application Administrator

An understanding of the concepts in managed identities for Azure resources.

A user-assigned managed identity assigned to the Azure compute resource (for example,

a virtual machine or Azure App Service) that hosts your workload.

An app registration in Microsoft Entra ID. This app registration must belong to the same

tenant as the managed identity

If you need to access resources in another tenant, your app registration must be a

multitenant application and provisioned into the other tenant. Learn about how to add

a multitenant app in other tenants.

The app registration must have access granted to Microsoft Entra protected resources (for

example, Azure, Microsoft Graph, Microsoft 365, etc.). This access can be granted through

API permissions or delegated permissions.

To create, update, or delete a federated identity credential, the account performing the action

must have the Application Administrator, Application Developer, Cloud Application

Administrator, or Application Owner role. The

microsoft.directory/applications/credentials/update permission is required to update a

federated identity credential.

A maximum of 20 federated identity credentials can be added to an application or user-

assigned managed identity.

**Prerequisites**

**Important considerations and restrictions**

When you configure a federated identity credential, there are several important pieces of

information to provide:

_issuer_, _subject_ are the key pieces of information needed to set up the trust relationship.

When the Azure workload requests Microsoft identity platform to exchange the managed

identity token for an Entra app access token, the _issuer_ and _subject_ values of the federated

identity credential are checked against the `issuer` and `subject` claims provided in the

Managed Identity token. If that validation check passes, Microsoft identity platform issues

an access token to the external software workload.

_issuer_ is the URL of the Microsoft Entra tenant's Authority URL in the form

`https://login.microsoftonline.com/{tenant}/v2.0` . Both the Microsoft Entra app and

managed identity must belong to the same tenant. If the `issuer` claim has leading or

trailing whitespace in the value, the token exchange is blocked.

`subject` : This is the case-sensitive GUID of the managed identity’s **Object (Principal) ID**

assigned to the Azure workload. The managed identity must be in the same tenant as the

app registration, even if the target resource is in a different cloud. The Microsoft identity

platform will reject the token exchange if the `subject` in the federated identity credential

configuration does not exactly match the managed identity's Principal ID.

_audiences_ specifies the value that appears in the `aud` claim in the managed identity token

(Required). The value must be one of the following depending on the target cloud.

**Microsoft Entra ID global service**: `api://AzureADTokenExchange`

**Microsoft Entra ID for US Government**: `api://AzureADTokenExchangeUSGov`

**Microsoft Entra China operated by 21Vianet**: `api://AzureADTokenExchangeChina`

） **Important**

Only user-assigned managed identities can be used as a federated credential for

apps. system-assigned identities aren't supported.

） **Important**

Accessing resources in _another tenant_ is supported. Accessing resources in _another_

_cloud_ is not supported. Token requests to other clouds will fail.

） **Important**

_name_ is the unique identifier for the federated identity credential. (Required) This field has

a character limit of 3-120 characters and must be URL friendly. Alphanumeric, dash, or

underscore characters are supported, and the first character must be alphanumeric only.

It's immutable once created.

_description_ is the user-provided description of the federated identity credential (Optional).

The description isn't validated or checked by Microsoft Entra ID. This field has a limit of

600 characters.

Wildcard characters aren't supported in any federated identity credential property value.

In this section, you'll configure a federated identity credential on an existing application to trust

a managed identity. Use the following tabs to choose how to configure a federated identity

credential on an existing application.

1\. Sign in to the Microsoft Entra admin center

. Check that you are in the tenant where

your application is registered.

2\. Browse to **Entra ID** \> **App registrations**, and select your application in the main

window.

3\. Under **Manage**, select **Certificates & secrets**.

4\. Select the Federated credentials tab and select **Add credential**.

If you accidentally add incorrect information in the _issuer_, _subject_ or _audience_ setting

the federated identity credential is created successfully without error. The error does

not become apparent until the token exchange fails.

**Configure a federated identity credential on an**

**application**

Microsoft Entra admin center

![](./assets/output_68_1.png)

5\. From the **Federated credential scenario** dropdown, select **Managed Identity** and fill

in the values according to the following table:

**Field**

**Description**

**Example**

Issuer

The OAuth 2.0 / OIDC

issuer URL of the

Microsoft Entra ID

authority that issues

the managed identity

token. This value is

automatically

populated with the

current Entra tenant

issuer.

`https://login.microsoftonline.com/{tenantID}/v2.0`

Select

managed

identity

Click on this link to

select the managed

identity that will act as

the federated identity

credential. You can

only use User-

Assigned Managed

Identities as a

credential.

_msi-webapp1_

ﾉ

**Expand table**

**Field**

**Description**

**Example**

Description

(Optional)

A user-provided

description of the

federated identity

credential.

_Trust the workloads UAMI as a credential to my App_

Audience

The audience value

that must appear in

the external token.

Must be set to one of the following values:

• **Entra ID Global Service**:

_api://AzureADTokenExchange_

• **Entra ID for US Government**:

_api://AzureADTokenExchangeUSGov_

• **Entra ID China operated by 21Vianet**:

_api://AzureADTokenExchangeChina_

![](./assets/output_69_1.png)

**Update your application code to request an access**

**token**

The following code snippets demonstrate how to acquire a managed identity token and use it

as a credential for your Entra application. The samples are valid in both cases where the target

resource in the same tenant as the Entra application, or in a different tenant.

The following code samples demonstrate accessing an Azure Key Vault secret, but can be

adapted to access any resource protected by Microsoft Entra.

C#

**Azure Identity client libraries**

.NET

`using` ` Azure.Core;`

`using` ` Azure.Identity;`

`using` ` Azure.Security.KeyVault.Secrets;`

`// Audience value must be one of the below values depending on the target `

`cloud:`

`// - Entra ID Global cloud: api://AzureADTokenExchange`

`// - Entra ID US Government: api://AzureADTokenExchangeUSGov`

`// - Entra ID China operated by 21Vianet: api://AzureADTokenExchangeChina`

`string` ` miAudience = ``"api://AzureADTokenExchange"` `;`

`// Create an assertion with the managed identity access token, so that it can `

`be`

`// exchanged for an app token. Client ID is passed here. Alternatively, either`

`// object ID or resource ID can be passed.`

`ManagedIdentityCredential miCredential = ` `new` `(`

`    ManagedIdentityId.FromUserAssignedClientId(` `"<YOUR_MI_CLIENT_ID>"` `));`

`TokenRequestContext tokenRequestContext = ` `new` `([`  `$"` `{miAudience}` `/.default"` `]);`

`ClientAssertionCredential clientAssertionCredential = ` `new` `(`

`    ``"<YOUR_RESOURCE_TENANT_ID>"` `,`

`    ``"<YOUR_APP_CLIENT_ID>"` `,`

`    ` `async` ` _ =>`

`        (`  `await` ` miCredential`

`            .GetTokenAsync(tokenRequestContext)`

`            .ConfigureAwait(`  `false` `)).Token`

`);`

`// Create a new SecretClient using the assertion`

`SecretClient client = ` `new` `(`

`    ` `new` ` Uri(` `"https://testfickv.vault.azure.net/"` `), `

`    clientAssertionCredential);`

`// Retrieve the secret`

`KeyVaultSecret secret = client.GetSecret(` `"<SECRET_NAME>"` `);`

In **Microsoft.Identity.Web**, you can set the `ClientCredentials` section in your _appsettings.json_

to use `SignedAssertionFromManagedIdentity` to enable your code use the configured managed

identity as a credential:

JSON

In **MSAL**, you can use the ManagedClientApplication class to acquire a Managed Identity

token. This token can then be used as a client assertion when constructing a confidential client

application.

C#

**Microsoft.Identity.Web**

`{`

`  ``"AzureAd"` `: {`

`    ``"Instance"` `: ``"https://login.microsoftonline.com/"` `,`

`    ``"ClientId"` `: ``"YOUR_APPLICATION_ID"` `,`

`    ``"TenantId"` `: ``"YOUR_TENANT_ID"` `,`

`    `

`    ``"ClientCredentials"` `: [`

`      {`

`        ``"SourceType"` `: ``"SignedAssertionFromManagedIdentity"` `,`

`        ``"ManagedIdentityClientId"` `: `

`"YOUR_USER_ASSIGNED_MANAGED_IDENTITY_CLIENT_ID"` `,`

`        ``"TokenExchangeUrl"` `: ``"api://AzureADTokenExchange/.default"`

`      }`

`    ]`

`  }`

`}`

**MSAL (.NET)**

`using` ` Microsoft.Identity.Client;`

`using` ` Microsoft.Identity.Client.AppConfig;`

`using` ` Azure.Storage.Blobs;`

`using` ` Azure.Core;`

`using` ` Azure.Storage.Blobs.Models;`

`internal`  ` `  `class`  ` `  `Program`

`{`

`  ` `static`  ` `  `async` ` Task ` `Main` `(`  `string` `[] args)`

`  {`

`      ` `string` ` storageAccountName = ``"YOUR_STORAGE_ACCOUNT_NAME"` `;`

`      ` `string` ` containerName = ``"CONTAINER_NAME"` `;`

`      ` `string` ` appClientId = ``"YOUR_APP_CLIENT_ID"` `;`

`      ` `string` ` resourceTenantId = ``"YOUR_RESOURCE_TENANT_ID"` `;`

`      Uri authorityUri = `

Important considerations and restrictions for federated identity credentials.

`new` `(`  `$"https://login.microsoftonline.com/` `{resourceTenantId}` `"` `);`

`      ` `string` ` miClientId = ``"YOUR_MI_CLIENT_ID"` `;`

`      ` `string` ` audience = ``"api://AzureADTokenExchange/.default"` `;`

`      ``// Get mi token to use as assertion`

`      ` `var` ` miAssertionProvider = ` `async` ` (AssertionRequestOptions _) =>`

`      {`

`            ` `var` ` miApplication = ManagedIdentityApplicationBuilder`

`                .Create(ManagedIdentityId.WithUserAssignedClientId(miClientId))`

`                .Build();`

`            ` `var` ` miResult = ` `await` ` `

`miApplication.AcquireTokenForManagedIdentity(audience)`

`                .ExecuteAsync()`

`                .ConfigureAwait(`  `false` `);`

`            ` `return` ` miResult.AccessToken;`

`      };`

`      ``// Create a confidential client application with the assertion.`

`      IConfidentialClientApplication app = `

`ConfidentialClientApplicationBuilder.Create(appClientId)`

`        .WithAuthority(authorityUri, ` `false` `)`

`        .WithClientAssertion(miAssertionProvider)`

`        .WithCacheOptions(CacheOptions.EnableSharedCacheOptions)`

`        .Build();`

`        ``// Get the federated app token for the storage account`

`        ` `string` `[] scopes = `

`[`  `$"https://` `{storageAccountName}` `.blob.core.windows.net/.default"` `];`

`        AuthenticationResult result = ` `await` ` `

`app.AcquireTokenForClient(scopes).ExecuteAsync().ConfigureAwait(`  `false` `);`

`        TokenCredential tokenCredential = ` `new` ` `

`AccessTokenCredential(result.AccessToken);`

`        ` `var` ` containerClient = ` `new` ` BlobContainerClient(`

`            ` `new` ` `

`Uri(`  `$"https://` `{storageAccountName}` `.blob.core.windows.net/` `{containerName}` `"` `),`

`            tokenCredential);`

`        ` `await`  ` `  `foreach` ` (BlobItem blob ` `in` ` containerClient.GetBlobsAsync())`

`        {`

`            ``// ` `TODO:` ` perform operations with the blobs`

`            BlobClient blobClient = containerClient.GetBlobClient(blob.Name);`

`            Console.WriteLine(`  `$"Blob name: ``{blobClient.Name}` `, URI: `

`{blobClient.Uri}` `"` `);`

`        }`

`    }`

`}`

**See also**



**Configure a user-assigned managed**

**identity to trust an external identity**

**provider**

Article • 05/12/2025

This article describes how to manage a federated identity credential on a user-assigned

managed identity in Microsoft Entra ID. The federated identity credential creates a trust

relationship between a user-assigned managed identity and an external identity provider (IdP).

Configuring a federated identity credential on a system-assigned managed identity isn't

supported.

After you configure your user-assigned managed identity to trust an external IdP, configure

your external software workload to exchange a token from the external IdP for an access token

from Microsoft identity platform. The external workload uses the access token to access

Microsoft Entra protected resources without needing to manage secrets (in supported

scenarios). To learn more about the token exchange workflow, read about workload identity

federation.

In this article, you learn how to create, list, and delete federated identity credentials on a user-

assigned managed identity.

A maximum of 20 federated identity credentials can be added to an application or user-

assigned managed identity.

When you configure a federated identity credential, there are several important pieces of

information to provide:

_issuer_ and _subject_ are the key pieces of information needed to set up the trust

relationship. The combination of `issuer` and `subject` must be unique on the app. When

the external software workload requests Microsoft identity platform to exchange the

external token for an access token, the _issuer_ and _subject_ values of the federated identity

credential are checked against the `issuer` and `subject` claims provided in the external

token. If that validation check passes, Microsoft identity platform issues an access token

to the external software workload.

_issuer_ is the URL of the external identity provider and must match the `issuer` claim of the

external token being exchanged. Required. If the `issuer` claim has leading or trailing

**Important considerations and restrictions**

whitespace in the value, the token exchange is blocked. This field has a character limit of

600 characters.

_subject_ is the identifier of the external software workload and must match the `sub`

( ` subject` ) claim of the external token being exchanged. _subject_ has no fixed format, as

each IdP uses their own - sometimes a GUID, sometimes a colon delimited identifier,

sometimes arbitrary strings. This field has a character limit of 600 characters.

_audiences_ lists the audiences that can appear in the external token. Required. You must

add a single audience value, which has a limit of 600 characters. The recommended value

is "api://AzureADTokenExchange". It says what Microsoft identity platform must accept in

the `aud` claim in the incoming token.

_name_ is the unique identifier for the federated identity credential. Required. This field has

a character limit of 3-120 characters and must be URL friendly. Alphanumeric, dash, or

underscore characters are supported, the first character must be alphanumeric only. It's

immutable once created.

_description_ is the user-provided description of the federated identity credential. Optional.

The description isn't validated or checked by Microsoft Entra ID. This field has a limit of

600 characters.

Wildcard characters aren't supported in any federated identity credential property value.

To learn more about supported regions, time to propagate federated credential updates,

supported issuers and more, read Important considerations and restrictions for federated

identity credentials.

） **Important**

The _subject_ setting values must exactly match the configuration on the GitHub

workflow configuration. Otherwise, Microsoft identity platform will look at the

incoming external token and reject the exchange for an access token. You won't get

an error, the exchange fails without error.

） **Important**

If you accidentally add the incorrect external workload information in the _subject_

setting the federated identity credential is created successfully without error. The

error does not become apparent until the token exchange fails.

If you're unfamiliar with managed identities for Azure resources, check out the overview

section. Be sure to review the difference between a system-assigned and user-assigned

managed identity.

If you don't already have an Azure account, sign up for a free account

before you

continue.

Get the information for your external IdP and software workload, which you need in the

following steps.

To create a user-assigned managed identity and configure a federated identity credential,

your account needs the Contributor or Owner role assignment.

Create a user-assigned managed identity

Find the name of the user-assigned managed identity, which you need in the following

steps.

In the Microsoft Azure portal

, navigate to the user-assigned managed identity you created.

Under **Settings** in the left nav bar, select **Federated credentials** and then **Add Credential**.

In the **Federated credential scenario** dropdown box, select your scenario.

To add a federated identity for GitHub actions, follow these steps:

1\. For **Entity type**, select **Environment**, **Branch**, **Pull request**, or **Tag** and specify the value.

The values must exactly match the configuration in the GitHub workflow

. For more info,

read the examples.

2\. Add a **Name** for the federated credential.

3\. The **Issuer**, **Audiences**, and **Subject identifier** fields autopopulate based on the values

you entered.

4\. Select **Add** to configure the federated credential.

Use the following values from your Microsoft Entra managed identity for your GitHub

workflow:

`AZURE_CLIENT_ID` the managed identity **Client ID**

**Prerequisites**

**Configure a federated identity credential on a user-**

**assigned managed identity**

**GitHub Actions deploying Azure resources**

`AZURE_SUBSCRIPTION_ID` the **Subscription ID**.

The following screenshot demonstrates how to copy the managed identity ID and

subscription ID.

`AZURE_TENANT_ID` the **Directory (tenant) ID**. Learn how to find your Microsoft Entra tenant

ID.

For a workflow triggered by a push or pull request event on the main branch:

yml

Specify an **Entity type** of **Branch** and a **GitHub branch name** of "main".

For Jobs tied to an environment named "production":

yml

![](./assets/output_77_1.png)



**Entity type examples**

**Branch example**

`on:`

`  push:`

`    branches:` ` ` `[`  ` `  `main` ` ` `]`

`  pull_request:`

`    branches:` ` ` `[`  ` `  `main` ` ` `]`

**Environment example**

`on:`

`  push:`

Specify an **Entity type** of **Environment** and a **GitHub environment name** of "production".

For example, for a workflow triggered by a push to the tag named "v2":

yml

Specify an **Entity type** of **Tag** and a **GitHub tag name** of "v2".

For a workflow triggered by a pull request event, specify an **Entity type** of **Pull request**

Fill in the **Cluster issuer URL**, **Namespace**, **Service account name**, and **Name** fields:

**Cluster issuer URL** is the OIDC issuer URL for the managed cluster or the OIDC Issuer

URL

for a self-managed cluster.

**Service account name** is the name of the Kubernetes service account, which provides an

identity for processes that run in a Pod.

**Namespace** is the service account namespace.

`    branches:`

`      -`  ` `  `main`

`jobs:`

`  deployment:`

`    runs-on:`  ` `  `ubuntu-latest`

`    environment:`  ` `  `production`

`    steps:`

`      - name:`  ` `  `deploy`

`        ``# ...deployment-specific steps`

**Tag example**

`on:`

`  push:`

`    ``# Sequence of patterns matched against refs/heads`

`    branches:`

`      -`  ` `  `main`

`      -` ` ` `'mona/octocat'`

`      -` ` ` `'releases/**'`

`    ``# Sequence of patterns matched against refs/tags`

`    tags:`

`      -`  ` `  `v2`

`      -`  ` `  `v1.*`

**Pull request example**

**Kubernetes accessing Azure resources**

**Name** is the name of the federated credential, which can't be changed later.

Select **Add** to configure the federated credential.

Select the **Other issuer** scenario from the dropdown menu.

Specify the following fields (using a software workload running in Google Cloud as an

example):

**Name** is the name of the federated credential, which can't be changed later.

**Subject identifier**: must match the `sub` claim in the token issued by the external identity

provider. In this example using Google Cloud, _subject_ is the Unique ID of the service

account you plan to use.

**Issuer**: must match the `iss` claim in the token issued by the external identity provider. A

URL that complies with the OIDC Discovery spec. Microsoft Entra ID uses this issuer URL

to fetch the keys that are necessary to validate the token. For Google Cloud, the _issuer_ is

"https://accounts.google.com".

Select **Add** to configure the federated credential.

In the Microsoft Azure portal

, navigate to the user-assigned managed identity you created.

Under **Settings** in the left nav bar and select **Federated credentials**.

The federated identity credentials configured on that user-assigned managed identity are

listed.

In the Microsoft Azure portal

, navigate to the user-assigned managed identity you created.

Under **Settings** in the left nav bar and select **Federated credentials**.

The federated identity credentials configured on that user-assigned managed identity are

listed.

To delete a specific federated identity credential, select the **Delete** icon for that credential.

**Other**

**List federated identity credentials on a user-**

**assigned managed identity**

**Delete a federated identity credential from a user-**

**assigned managed identity**

For information about the required format of JWTs created by external identity providers,

read about the assertion format.

**Next steps**

**Block workload identity federation on**

**managed identities using a policy**

Article • 01/29/2025

This article describes how to block the creation of federated identity credentials on user-

assigned managed identities by using Azure Policy. By blocking the creation of

federated identity credentials, you can block everyone from using workload identity

federation to access Microsoft Entra protected resources. Azure Policy helps enforce

certain business rules on your Azure resources and assess compliance of those

resources.

The Not allowed resource types built-in policy can be used to block the creation of

federated identity credentials on user-assigned managed identities.

To create a policy assignment for the Not allowed resource types that blocks the

creation of federated identity credentials in a subscription or resource group:

1\. Sign in to the Azure portal

.

2\. Navigate to **Policy** in the Azure portal.

3\. Go to the **Definitions** pane.

4\. In the **Search** box, search for "Not allowed resource types" and select the _Not_

_allowed resource types_ policy in the list of returned items.

![](./assets/output_81_1.png)

5\. After selecting the policy, you can now see the **Definition** tab.

**Create a policy assignment**

**Feedback**

**Was this page helpful?**

Provide product feedback

6\. Click the **Assign** button to create an Assignment.

![](./assets/output_82_1.png)

7\. In the **Basics** tab, fill out **Scope** by setting the **Subscription** and optionally set the

**Resource Group**.

8\. In the **Parameters** tab, select **userAssignedIdentities/federatedIdentityCredentials**

from the **Not allowed resource types** list. Select **Review and create**.

![](./assets/output_82_2.png)

9\. Apply the Assignment by selecting **Create**.

10\. View your assignment in the **Assignments** tab next to **Definition**.

Learn how to manage a federated identity credential on a user-assigned managed

identity in Microsoft Entra ID.

**Next steps**

 **Yes**

 **No**

**Set up a Flexible Federated identity**

**credential (preview)**

Article • 12/13/2024

This article provides a guide on how to set up a Flexible Federated identity credential in

the Azure portal or Microsoft Graph Explorer. Flexible federated identity credentials are

an advanced feature of Microsoft Entra Workload ID that enhances the existing

federated identity credential model.

An Azure account with an active subscription. If you don't already have one, Create

an account for free

.

Create an app registration or managed identity in Microsoft Entra ID. Grant your

app access to the Azure resources targeted by your external software workload.

To accommodate the flexible federated identity credential functionality, the

`federatedIdentityCredentials` resource is being extended with a new

`claimsMatchingExpression` property. In addition to this, the `subject` property is now

nullable. The `claimsMatchingExpression` and `subject` properties have been made

mutually exclusive, so you can't define both within a federated identity credential.

`audiences` : The audience that can appear in the external token. This field is

mandatory and should be set to `api://AzureADTokenExchange` for Microsoft Entra ID.

It says what Microsoft identity platform should accept in the `aud` claim in the

incoming token. This value represents Microsoft Entra ID in your external identity

provider and has no fixed value across identity providers - you might need to

create a new application registration in your IdP to serve as the audience of this

token.

`issuer` : The URL of the external identity provider. Must match the issuer claim of

the external token being exchanged.

`subject` : The identifier of the external software workload within the external

identity provider. Like the audience value, it has no fixed format, as each IdP uses

their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes

**Prerequisites**

**Setting up federated identity credentials**

**through Microsoft Graph**

arbitrary strings. The value here must match the `sub` claim within the token

presented to Microsoft Entra ID. If `subject` is defined, `claimsMatchingExpression`

must be set to null.

`name` : A unique string to identify the credential. This property is an alternate key

and the value can be used to reference the federated identity credential via

the GET and UPSERT operations.

`claimsMatchingExpression` : a new complex type containing two properties, `value`

and `languageVersion` . Value is used to define the expression, and `languageVersion`

is used to define the version of the flexible federated identity credential expression

language (FFL) being used. `languageVersion` should always be set to 1. If

`claimsMatchingExpression` is defined, `subject` must be set to null.

1\. Navigate to Microsoft Entra ID and select the application where you want to

configure the federated identity credential.

2\. In the left-hand navigation pane, select **Certificates & secrets**.

3\. Under the **Federated credentials** tab, select **\+ Add credential**.

4\. In the **Add a credential** window that appears, from the dropdown menu next

to **Federated credential scenario**, select **Other issuer**.

5\. Under **Connect your account** enter the \* **Issuer** URL of the external identity

provider. For example;

GitHub: `https://token.actions.githubusercontent.com`

GitLab: `https://gitlab.example.com`

Terraform Cloud: `https://app.terraform.io`

6\. In **Value** enter the claim matching expression you want to use, for example

`claims['sub'] matches 'repo:contoso/contoso-repo:ref:refs/heads/*'`

7\. Select **Add** to save the credential.

Flexible federated identity credentials can use different issuers, such as GitHub, GitLab,

and Terraform Cloud. Use the following tabs to set up a flexible federated identity

**Set up a Flexible Federated identity credential**

Azure portal

**More examples of Flexible Federated identity**

**credentials**

**Feedback**

**Was this page helpful?**

Provide product feedback

credential for each of these issuers.

This example shows how to set up a Flexible Federated identity credential for

GitHub with an expression for the `job_workflow_ref` claim. Use

JSON

Flexible federated identity credentials

Configure a user-assigned managed identity to trust an external identity provider

GitHub

`{`

`  ``"audiences"` `: [`

`    ``"api://AzureADTokenExchange"`

`  ],`

`  ``"name"` `: ``"MyGitHubFlexibleFIC"` `,`

`  ``"issuer"` `: ``"https://token.actions.githubusercontent.com"` `,`

`  ``"claimsMatchingExpression"` `: {`

`    ``"value"` `: ``"claims['sub'] matches 'repo:contoso/contoso-`

`repo:ref:refs/heads/*' and claims['job_workflow_ref'] matches `

`'contoso/contoso-prod/.github/workflows/*.yml@refs/heads/main'"` `,`

`    ``"languageVersion"` `: 1`

`  }`

`}`

**Related content**

 **Yes**

 **No**

**Create an access review of Azure resource**

**and Microsoft Entra roles in PIM**

Article • 04/30/2025

The need for access to privileged Azure resource and Microsoft Entra roles by your users

changes over time. To reduce the risk associated with stale role assignments, you should

regularly review access. You can use Microsoft Entra Privileged Identity Management (PIM) to

create access reviews for privileged access to Azure resource and Microsoft Entra roles. You can

also configure recurring access reviews that occur automatically. This article describes how to

create one or more access reviews.

Using Privileged Identity Management requires licenses. For more information on licensing, see

Microsoft Entra ID Governance licensing fundamentals .

For more information about licenses for PIM, see License requirements to use Privileged

Identity Management.

To create access reviews for Azure resources, you must be assigned to the Owner or the User

Access Administrator role for the Azure resources. To create access reviews for Microsoft Entra

roles, you must be assigned at least the Privileged Role Administrator role.

Using Access Reviews for **Service Principals** requires a Microsoft Entra Workload ID Premium

plan in addition to a Microsoft Entra ID P2 or Microsoft Entra ID Governance license.

Workload Identities Premium licensing: You can view and acquire licenses on the

Workload Identities blade

in the Microsoft Entra admin center.

1\. Sign in to the Microsoft Entra admin center

as a user that is assigned to one of the

prerequisite roles.

**Prerequisites**

７ **Note**

Access reviews capture a snapshot of access at the beginning of each review instance. Any

changes made during the review process will be reflected in the subsequent review cycle.

Essentially, with the commencement of each new recurrence, pertinent data regarding the

users, resources under review, and their respective reviewers is retrieved.

**Create access reviews**

2\. Browse to **ID Governance** \> **Privileged Identity Management**.

3\. For **Microsoft Entra roles**, select **Microsoft Entra roles**. For **Azure resources**, select **Azure**

**resources**

4\. For **Microsoft Entra roles**, select **Microsoft Entra roles** again under **Manage**. For **Azure**

**resources**, select the subscription you want to manage.

5\. Under Manage, select **Access reviews**, and then select **New** to create a new access review.

![](./assets/output_87_1.png)



![](./assets/output_88_1.png)

6\. Name the access review. Optionally, give the review a description. The name and

description are shown to the reviewers.

![](./assets/output_88_2.png)

7\. Set the **Start date**. By default, an access review occurs once. It starts at creation time, and

it ends in one month. You can change the start and end dates to have an access review

start in the future and last however many days you want.

![](./assets/output_89_1.png)

8\. To make the access review recurring, change the **Frequency** setting from **One time** to

**Weekly**, **Monthly**, **Quarterly**, **Annually**, or **Semi-annually**. Use the **Duration** slider or text

box to specify review duration. For example, the maximum duration that you can set for a

monthly review is 27 days, to avoid overlapping reviews.

9\. Use the **End** setting to specify how to end the recurring access review series. The series

can end in three ways: it runs continuously to start reviews indefinitely, until a specific

date, or after a defined number of occurrences completes. You, or another administrator

who can manage reviews, can stop the series after creation by changing the date in

**Settings**, so that it ends on that date.

10\. In the **Users Scope** section, select the scope of the review. For **Microsoft Entra roles**, the

first scope option is Users and Groups. Directly assigned users and role-assignable groups

are included in this selection. For **Azure resource roles**, the first scope is Users. Groups

assigned to Azure resource roles are expanded to display transitive user assignments in

the review with this selection. You may also select **Service Principals** to review the

machine accounts with direct access to either the Azure resource or Microsoft Entra role.

![](./assets/output_89_2.png)

11\. Or, you can create access reviews only for inactive users. In the _Users scope_ section, set

the **Inactive users (on tenant level) only** to **true**. If the toggle is set to _true_, the scope of

the review focuses on inactive users only. Then, specify **Days inactive**. You can specify up

to 730 days (two years). Users inactive for the specified number of days are the only users

in the review.

12\. Under **Review role membership**, select the privileged Azure resource or Microsoft Entra

roles to review.

![](./assets/output_90_1.png)

13\. In **assignment type**, scope the review by how the principal was assigned to the role.

Choose **eligible assignments only** to review eligible assignments (regardless of activation

status when the review is created) or **active assignments only** to review active

assignments. Choose **all active and eligible assignments** to review all assignments

regardless of type.

![](./assets/output_90_2.png)

14\. In the **Reviewers** section, select one or more people to review all the users. Or you can

select to have the members review their own access.

![](./assets/output_90_3.png)

**Selected users** \- Use this option to designate a specific user to complete the review.

This option is available regardless of the scope of the review, and the selected

reviewers can review users, groups, and service principals.

**Members (self)** \- Use this option to have the users review their own role

assignments. This option is only available if the review is scoped to **Users and**

**Groups** or **Users**. For **Microsoft Entra roles**, role-assignable groups aren't part of the

review when this option is selected.

７ **Note**

Selecting more than one role will create multiple access reviews. For example,

selecting five roles will create five separate access reviews.

**Manager** – Use this option to have the user’s manager review their role assignment.

This option is only available if the review is scoped to **Users and Groups** or **Users**.

Upon selecting Manager, you also can specify a fallback reviewer. Fallback reviewers

are asked to review a user when the user has no manager specified in the directory.

For **Microsoft Entra roles**, role-assignable groups are reviewed by the fallback

reviewer if one is selected.

1\. To specify what happens after a review completes, expand the **Upon completion settings**

section.

![](./assets/output_91_1.png)

2\. If you want to automatically remove access for users that were denied, set **Auto apply**

**results to resource** to **Enable**. If you want to manually apply the results when the review

completes, set the switch to **Disable**.

3\. Use the **If reviewer don't respond** list to specify what happens for users that aren't

reviewed by the reviewer within the review period. This setting doesn't impact users who

were already reviewed.

**No change** \- Leave user's access unchanged

**Remove access** \- Remove user's access

**Approve access** \- Approve user's access

**Take recommendations** \- Take the system's recommendation on denying or

approving the user's continued access

4\. Use the **Action to apply on denied guest users** list to specify what happens for guest

users that are denied. This setting isn't editable for Microsoft Entra ID and Azure resource

role reviews at this time; guest users, like all users, always lose access to the resource if

denied.

**Upon completion settings**

![](./assets/output_92_1.png)

5\. You can send notifications to other users or groups to receive review completion updates.

This feature allows for stakeholders other than the review creator to be updated on the

progress of the review. To use this feature, select **Select User(s) or Group(s)** and add any

users, or groups you want receive completion status notifications.

![](./assets/output_92_2.png)

1\. To configure more settings, expand the **Advanced settings** section.

![](./assets/output_92_3.png)

2\. Set **Show recommendations** to **Enable** to show the reviewers the system

recommendations based the user's access information. Recommendations are based on a

30-day interval period. Users who have logged in the past 30 days are shown with

**Advanced settings**

recommended approval of access, while users who haven't logged in are shown with

recommended denial of access. These sign-ins are irrespective of whether they were

interactive. The last sign-in of the user is also displayed along with the recommendation.

3\. Set **Require reason on approval** to **Enable** to require the reviewer to supply a reason for

approval.

4\. Set **Mail notifications** to **Enable** to have Microsoft Entra ID send email notifications to

reviewers when an access review starts, and to administrators when a review completes.

5\. Set **Reminders** to **Enable** to have Microsoft Entra ID send reminders of access reviews in

progress to reviewers who haven't completed their review.

6\. The content of the email sent to reviewers is autogenerated based on the review details,

such as review name, resource name, due date, and so on. If you need a way to

communicate additional information such as more instructions or contact information,

you can specify these details in the **Additional content for reviewer email** are included in

the invitation and reminder emails sent to assigned reviewers. The highlighted section is

where this information is displayed.

![](./assets/output_93_1.png)

You can track the progress as the reviewers complete their reviews on the **Overview** page of

the access review. No access rights are changed in the directory until the review is completed.

**Manage the access review**

After the access review, follow the steps in Complete an access review of Azure resource and

Microsoft Entra roles to see and apply the results.

If you are managing a series of access reviews, navigate to the access review, and you find

upcoming occurrences in Scheduled reviews, and edit the end date or add/remove reviewers

accordingly.

Based on your selections in **Upon completion settings**, auto-apply will be executed after the

review's end date or when you manually stop the review. The status of the review changes from

**Completed** through intermediate states such as **Applying** and finally to state **Applied**. You

should expect to see denied users, if any, being removed from roles in a few minutes.

• For **Microsoft Entra roles**, role-assignable groups can be assigned to the role using role-

assignable groups. When a review is created on a Microsoft Entra role with role-assignable

groups assigned, the group name shows up in the review without expanding the group

membership. The reviewer can approve or deny access of the entire group to the role. Denied

groups lose their assignment to the role when review results are applied.

• For **Azure resource roles**, any security group can be assigned to the role. When a review is

created on an Azure resource role with a security group assigned, role reviewers can see a fully

expanded view of the group's membership. When a reviewer denies a user that was assigned

to the role via the security group, the user won't be removed from the group. This is because a

group may be shared with other Azure or non-Azure resources. Administrators must

implement the changes resulting from an access denial.

![](./assets/output_94_1.png)



**Impact of groups assigned to Microsoft Entra roles**

**and Azure resource roles in access reviews**

After one or more access reviews have been started, you may want to modify or update the

settings of your existing access reviews. Here are some common scenarios that you might want

to consider:

**Adding and removing reviewers** \- When updating access reviews, you may choose to

add a fallback reviewer in addition to the primary reviewer. Primary reviewers may be

removed when updating an access review. However, fallback reviewers aren't removable

by design.

**Reminding the reviewers** \- When updating access reviews, you may choose to enable the

reminder option under Advanced Settings. Once enabled, users receive an email

notification at the midpoint of the review period. Reviewers receive notifications

regardless of whether they have completed the review or not.

７ **Note**

It is possible for a security group to have other groups assigned to it. In this case, only the

users assigned directly to the security group assigned to the role will appear in the review

of the role.

**Update the access review**

７ **Note**

Fallback reviewers can only be added when reviewer type is manager. Primary

reviewers can be added when reviewer type is selected user.

![](./assets/output_96_1.png)

**Updating the settings** \- If an access review is recurring, there are separate settings under

"Current" versus under "Series". Updating the settings under "Current" will only apply

changes to the current access review while updating the settings under "Series" will

update the setting for all future recurrences.

![](./assets/output_96_2.png)



**Next steps**

Perform an access review of Azure resource and Microsoft Entra roles in PIM

Complete an access review of Azure resource and Microsoft Entra roles in PIM

**Manage custom security attributes for**

**an application**

Article • 03/06/2025

Custom security attributes in Microsoft Entra ID are business-specific attributes (key-

value pairs) that you can define and assign to Microsoft Entra objects. For example, you

can assign custom security attribute to filter your applications or to help determine who

gets access. This article describes how to assign, update, list, or remove custom security

attributes for Microsoft Entra enterprise applications.

To assign or remove custom security attributes for an application in your Microsoft Entra

tenant, you need:

A Microsoft Entra account with an active subscription. Create an account for free

.

Attribute Assignment Administrator role.

Make sure you have existing custom security attributes. To learn how to create a

security attribute, see Add or deactivate custom security attributes in Microsoft

Entra ID.

Learn how to work with custom attributes for applications in Microsoft Entra ID.

Undertake the following steps to assign custom security attributes through the

Microsoft Entra admin center.

1\. Sign in to the Microsoft Entra admin center

as an Attribute Assignment

Administrator.

**Prerequisites**

） **Important**

By default, **Global Administrator** and other administrator roles do not have

permissions to read, define, or assign custom security attributes.

**Assign, update, list, or remove custom**

**attributes for an application**

**Assign custom security attributes to an application**

2\. Browse to **Identity** \> **Applications** \> **Enterprise applications**.

3\. Find and select the application you want to add a custom security attribute to.

4\. In the Manage section, select **Custom security attributes**.

5\. Select **Add assignment**.

6\. In **Attribute set**, select an attribute set from the list.

7\. In **Attribute name**, select a custom security attribute from the list.

8\. Depending on the properties of the selected custom security attribute, you can

enter a single value, select a value from a predefined list, or add multiple values.

For freeform, single-valued custom security attributes, enter a value in the

**Assigned values** box.

For predefined custom security attribute values, select a value from the

**Assigned values** list.

For multi-valued custom security attributes, select **Add values** to open the

**Attribute values** pane and add your values. When finished adding values,

select **Done**.

9\. When finished, select **Save** to assign the custom security attributes to the

application.

1\. Sign in to the Microsoft Entra admin center

as an Attribute Assignment

Administrator.

2\. Browse to **Identity** \> **Applications** \> **Enterprise applications**.

![](./assets/output_99_1.png)



**Update custom security attribute assignment values for**

**an application**

3\. Find and select the application that has a custom security attribute assignment

value you want to update.

4\. In the Manage section, select **Custom security attributes**.

5\. Find the custom security attribute assignment value you want to update.

Once you assigned a custom security attribute to an application, you can only

change the value of the custom security attribute. You can't change other

properties of the custom security attribute, such as attribute set or custom security

attribute name.

6\. Depending on the properties of the selected custom security attribute, you can

update a single value, select a value from a predefined list, or update multiple

values.

7\. When finished, select **Save**.

You can filter the list of custom security attributes assigned to applications on the **All**

**applications** page.

1\. Sign in to the Microsoft Entra admin center

as at least an Attribute Assignment

Reader.

2\. Browse to **Identity** \> **Applications** \> **Enterprise applications**.

3\. Select **Add filters** to open the Pick a field pane.

If you don't see **Add filters**, select the banner to enable the Enterprise applications

search preview.

4\. For **Filters**, select **Custom security attribute**.

5\. Select your attribute set and attribute name.

6\. For **Operator**, you can select equals ( **==**), not equals ( **!=**), or **starts with**.

7\. For **Value**, enter or select a value.

8\. To apply the filter, select **Apply**.

**Filter applications based on custom security attributes**

**Remove custom security attribute assignments from**

**applications**

**Feedback**

**Was this page helpful?**

Provide product feedback

1\. Sign in to the Microsoft Entra admin center

as a Attribute Assignment

Administrator.

2\. Browse to **Identity** \> **Applications** \> **Enterprise applications**.

3\. Find and select the application that has the custom security attribute assignments

you want to remove.

4\. In the **Manage** section, select **Custom security attributes (preview)**.

5\. Add check marks next to all the custom security attribute assignments you want to

remove.

6\. Select **Remove assignment**.

Add or deactivate custom security attributes in Microsoft Entra ID

Assign, update, list, or remove custom security attributes for a user

Troubleshoot custom security attributes in Microsoft Entra ID

**Next steps**

 **Yes**

 **No**

**Microsoft Entra recommendation: Remove**

**unused applications (preview)**

Article • 04/10/2025

Microsoft Entra recommendations is a feature that provides you with personalized insights and

actionable guidance to align your tenant with recommended best practices.

This article covers the recommendation to investigate unused applications. This

recommendation is called `staleApps` in the recommendations API in Microsoft Graph.

There are different role requirements for viewing or updating a recommendation. Use the

least-privileged role for the type of access needed. For a full list of roles, see Least privileged

roles by task.

**Microsoft Entra role**

**Access type**

Reports Reader

Read-only

Security Reader

Read-only

Global Reader

Read-only

Authentication Policy Administrator

Update and read

Exchange Administrator

Update and read

Security Administrator

Update and read

`DirectoryRecommendations.Read.All`

Read-only in Microsoft Graph

`DirectoryRecommendations.ReadWrite.All`

Update and read in Microsoft Graph

Some recommendations might require a P2 or other license. For more information, see the

Recommendations overview table.

７ **Note**

With **Microsoft Security Copilot**, you can use natural language prompts to get insights on

unused applications. Learn more about how to **Assess application risks using Microsoft**

**Security Copilot**.

**Prerequisites**

ﾉ

**Expand table**

This recommendation shows up if your tenant has applications that haven't been used for over

90 days. The following scenarios are included in this recommendation:

The app was created but never used.

The app isn't soft deleted from the application portfolio.

The app isn't used by the tenant where it resides nor any of its instances (Service

Principal) in other tenants.

It's a client app that calls other resource apps, but hasn't been issued any tokens in the

past 90 days.

It's a resource app that doesn't have a record of any client apps requesting a token in the

past 90 days.

The following apps are exempted from this recommendation:

Apps that are managed by Microsoft, including anything created or modified by

Microsoft-owned applications.

Apps that work with other apps to obtain tokens or are used to enable scenarios that

don't require tokens.

For example, Peer-to-peer server, Application proxy, Microsoft Entra Cloud Sync, linked

single-sign-on, password SSO, Office add-ins, and managed identities are excluded

from this recommendation.

Apps that were created within the past 90 days.

Removing unused applications helps reduce the attack surface area and helps clean up the app

portfolio of a tenant.

This recommendation is available in the Microsoft Entra admin center and using the Microsoft

Graph API. Once you identify the applications that aren't being used, you can decide whether

to remove them or keep them based on your organization's needs. The action plan is therefore

broken down into two parts:

1\. Review the applications that are flagged as unused.

2\. Determine if the application is needed and how to address it.

**Description**

**Value**

**Action plan**

Microsoft Entra admin center

Applications identified by the recommendation appear in the list of **Impacted resources** at

the bottom of the recommendation.

1\. Sign in to the Microsoft Entra admin center

as at least a Security Administrator.

2\. Browse to **Identity** \> **Overview**.

3\. Select the **Recommendations** tab and select the **Remove unused applications**

recommendation.

4\. From the **Impacted resources** table, select **More details** to view more details.

5\. Select the **Resource** link to go directly to the app registration for the app.

Alternatively, you can browse to **Identity** \> **Applications** \> **App registrations**

and locate the application that was surfaced as part of this recommendation.

There are many reasons why an app might be unused. Consider the app's usage scenario

and business function. For example:

Was the app deprecated?

Is the app used for a business function that only happens at certain times of the

year?

**Review the applications**

![](./assets/output_104_1.png)



**Determine if the application is needed**

To remove the application:

1\. Soft delete the app from your tenant.

2\. Wait 15 days and then permanently delete the app.

To indicate the application is still needed and skip the recommendation:

Update the recommendation status to **dismissed** or **postponed**.

Use **dismissed** if determined that the app will remain inactive for the rest of its

lifecycle.

Use **dismissed** if you think the app as included in the recommendation in error.

Use **postponed** if you need more time to review the app.

Review the Microsoft Entra recommendations overview

Learn how to use Microsoft Entra recommendations

Explore the Microsoft Graph API properties for recommendations

**Related content**

**Microsoft Entra recommendation: Remove**

**unused credentials from apps (preview)**

Article • 04/09/2025

Microsoft Entra recommendations is a feature that provides you with personalized insights and

actionable guidance to align your tenant with recommended best practices.

This article covers the recommendation to remove unused credentials from apps. This

recommendation is called `staleAppCreds` in the recommendations API in Microsoft Graph.

There are different role requirements for viewing or updating a recommendation. Use the

least-privileged role for the type of access needed. For a full list of roles, see Least privileged

roles by task.

**Microsoft Entra role**

**Access type**

Reports Reader

Read-only

Security Reader

Read-only

Global Reader

Read-only

Authentication Policy Administrator

Update and read

Exchange Administrator

Update and read

Security Administrator

Update and read

`DirectoryRecommendations.Read.All`

Read-only in Microsoft Graph

`DirectoryRecommendations.ReadWrite.All`

Update and read in Microsoft Graph

Some recommendations might require a P2 or other license. For more information, see the

Recommendations overview table.

Application credentials can include certificates and other types of secrets that need to be

registered with that application. These credentials are used to prove the identity of the

**Prerequisites**

ﾉ

**Expand table**

**Description**

application. Only credentials actively in use by an application should remain registered with the

application.

A credential is considered unused if:

It has not been used in the past 30 days.

It's a credential that was added to an application to be used for OAuth/OIDC flows or to

the service principal for SAML flow.

The following credentials are exempted from the recommendation:

Expired credentials do not show in the **Impacted resources** list.

Credentials that were identified as unused but have expired since being flagged show as

**Completed** in the **Impacted resources** list.

Removing unused application credentials helps reduce the attack surface area and helps

declutter the app portfolio of a tenant.

This recommendation is available in the Microsoft Entra admin center and using the Microsoft

Graph API.

Applications that the recommendation identified appear in the list of **Impacted resources**

at the bottom of the recommendation.

1\. Sign in to the Microsoft Entra admin center

as at least a Security Administrator.

2\. Browse to **Identity** \> **Overview**.

3\. Select the **Recommendations** tab and select the **Remove unused credentials from**

**applications** recommendation.

4\. Take note of the following details from the **Impacted resources** table.

The **Resource** column displays the application name

The **ID** column displays the application ID

5\. Select **More Details** from the **Actions** column to view more details.

**Value**

**Action plan**

Microsoft Entra admin center

6\. From the panel that opens, select **Update Credential** to navigate directly to the

**Certificates & secrets** area of the app registration to remove the unused credential.

a. Alternatively, browse to **Identity** \> **Applications** \> **App registrations** and select

the application that was surfaced as part of this recommendation.

![](./assets/output_108_1.png)



７ **Note**

If the origin of the credential is Service Principal, follow the guidance in the

**Service principals** section.

b. Then navigate to the **Certificates & Secrets** section of the app registration.

7\. **Locate the unused credential and remove it.**

If the origin of the credential is **service principal**, there are a few considerations and extra steps

to follow.

Because there's often multiple service principals for a single application, it might be easier to

navigate to Enterprise apps to view everything in one place.

![](./assets/output_109_1.png)



![](./assets/output_109_2.png)



**Service principals**

1\. In the Microsoft Entra admin center

, browse to **Identity** \> **Applications** \> **Enterprise**

**applications**.

2\. Search for and open the application that was surfaced as part of this recommendation.

3\. Select **Single sign-on** from the side menu.

If the credential is a service principal but there are SAML certificates in use, you can

identify the details of the credential using the Microsoft Graph API. To use the Microsoft

Graph API, you need the `DirectoryRecommendations.Read.All` and

`DirectoryRecommendations.ReadWrite.All` permissions. For more information, see How to

use Identity Recommendations.

4\. Sign in to Graph Explorer

.

5\. Select **GET** as the HTTP method from the dropdown.

6\. Set the API version to **beta**.

7\. Query the `keyCredential` and `passwordCredential` endpoints.

8\. Use the `removePassword` or `removeKey` endpoints to remove the credential from the

service principal.

Review the Microsoft Entra recommendations overview

Learn how to use Microsoft Entra recommendations

Explore the Microsoft Graph API properties for recommendations

Learn about app and service principal objects in Microsoft Entra ID

**Related content**

**Microsoft Entra recommendation: Renew**

**expiring application credentials (preview)**

Article • 04/09/2025

Microsoft Entra recommendations is a feature that provides you with personalized insights and

actionable guidance to align your tenant with recommended best practices.

This article covers the recommendation to renew expiring application credentials. This

recommendation is called `applicationCredentialExpiry` in the recommendations API in

Microsoft Graph.

There are different role requirements for viewing or updating a recommendation. Use the

least-privileged role for the type of access needed. For a full list of roles, see Least privileged

roles by task.

**Microsoft Entra role**

**Access type**

Reports Reader

Read-only

Security Reader

Read-only

Global Reader

Read-only

Authentication Policy Administrator

Update and read

Exchange Administrator

Update and read

Security Administrator

Update and read

`DirectoryRecommendations.Read.All`

Read-only in Microsoft Graph

`DirectoryRecommendations.ReadWrite.All`

Update and read in Microsoft Graph

Some recommendations might require a P2 or other license. For more information, see the

Recommendations overview table.

Application credentials can include certificates and other types of secrets that need to be

registered with that application. These credentials are used to prove the identity of the

**Prerequisites**

ﾉ

**Expand table**

**Description**

application.

This recommendation shows up if your tenant has application credentials that will expire soon.

An application credential is expiring if:

It's on an application registration AND is expiring within the next 30 days.

The following credentials are exempted from this recommendation:

Credentials that were identified as expiring but have since been removed from the app

registration

Credentials whose expiration date has lapsed show as **completed** in the list of **Impacted**

**resources**.

Renewing an application’s credentials prior to their expiry date is crucial for maintaining

uninterrupted operations and minimizing the risk of any downtime resulting from outdated

credentials.

This recommendation is available in the Microsoft Entra admin center and using the Microsoft

Graph API.

1\. Sign in to the Microsoft Entra admin center

as at least a Security Administrator.

2\. Browse to **Identity** \> **Overview**.

3\. Select the **Recommendations** tab and select the **Renew expiring application**

**credentials** recommendation.

4\. Take note of the following details from the **Impacted resources** table.

The **Resource** column displays the application name

The **ID** column displays the application ID

**Value**

**Action plan**

Microsoft Entra admin center

5\. Select **More Details** from the **Actions** column.

6\. From the panel that opens, select **Update Credential** to navigate directly to the

**Certificates & secrets** area of the app registration to renew the expiring credential.

a. Alternatively, browse to **Identity** \> **Applications** \> **App registrations** and locate

the application for which the credential needs to be rotated.

a. Navigate to the **Certificates & Secrets** section of the app registration.

7\. Pick the credential type that you want to rotate and navigate to either **Certificates** or

**Client Secret** tab and follow the prompts.

![](./assets/output_113_1.png)



![](./assets/output_113_2.png)



8\. Once the certificate or secret is successfully added, update the service code to ensure

it works with the new credential and doesn't negatively affect customers.

9\. Use the Microsoft Entra sign-in logs to validate that the Key ID of the credential

matches the one that was recently added.

10\. After validating the new credential, navigate back to **App registrations** \> **Certificates**

**and Secrets** for the app and remove the old credential.

Review the Microsoft Entra recommendations overview

Learn how to use Microsoft Entra recommendations

Explore the Microsoft Graph API properties for recommendations

Learn about app and service principal objects in Microsoft Entra ID

![](./assets/output_114_1.png)



**Related content**

**tenantAppManagementPolicy resource**

**type**

09/13/2024

Namespace: microsoft.graph

Tenant-wide application authentication method policy to enforce app management restrictions

for all applications and service principals. This policy applies to all apps and service principals

unless overridden when an appManagementPolicy is applied to the object.

Inherits from policyBase.

**Method**

**Return type**

**Description**

Get

tenantAppManagementPolicy

Read the properties of the default app management policy set

for applications and service principals.

Update

None

Updates the default app management policy for applications

and service principals.

**Property**

**Type**

**Description**

applicationRestrictions

appManagementConfiguration

Restrictions that apply as default to all

application objects in the tenant.

description

String

The description of the default policy.

Inherited from policyBase.

displayName

String

The display name of the default policy.

Inherited from policyBase.

id

String

The default policy identifier.

isEnabled

Boolean

Denotes whether the policy is enabled.

Default value is `false` .

**Methods**

ﾉ

**Expand table**

**Properties**

ﾉ

**Expand table**

**Property**

**Type**

**Description**

servicePrincipalRestrictions

appManagementConfiguration

Restrictions that apply as default to all

service principal objects in the tenant.

None.

The following JSON representation shows the resource type.

JSON

**Relationships**

**JSON representation**

`{`

`  ``"@odata.context"` `: `

`"https://graph.microsoft.com/v1.0/$metadata#policies/defaultAppManagementPolicy"` `,`

`  ``"id"` `: ``"string (identifier)"` `,`

`  ``"description"` `: ``"string"` `,`

`  ``"displayName"` `: ``"string"` `,`

`  ``"isEnabled"` `: ` `false` `,`

`  ``"applicationRestrictions"` `: {`

`    ``"@odata.type"` `:` `"microsoft.graph.appManagementConfiguration"`

`  },`

`  ``"servicePrincipalRestrictions"` `: {`

`    ``"@odata.type"` `:` `"microsoft.graph.appManagementConfiguration"`

`  }`

`}`

**appManagementPolicy resource type**

11/07/2024

Namespace: microsoft.graph

Restrictions on app management operations for specific applications and service principals. If

this resource is not configured for an application or service principal, the restrictions default to

the settings in the tenantAppManagementPolicy object.

To learn more about how to use app management policy, see Microsoft Entra application

authentication methods API overview.

**Method**

**Return type**

**Description**

List

appManagementPolicy

Return a list of app management policies created for applications

and service principals along with their properties.

Create

appManagementPolicy

Create an app management policy that can be assigned to an

application or service principal object.

Get

appManagementPolicy

Get a single app management policy object.

Update

None

Update an app management policy.

Delete

None

Delete an app management policy from the collection of policies

in appManagementPolicies.

List applies

to

appManagementPolicy

Return a list of applications and service principals to which the

policy is applied.

Create

applies to

None

Assign an appManagementPolicy policy object to an application

or service principal object.

Delete

applies to

None

Remove an appManagementPolicy policy object from an

application or service principal object.

**Methods**

ﾉ

**Expand table**

**Properties**

ﾉ

**Expand table**

**Property**

**Type**

**Description**

displayName

String

The display name of the policy. Inherited from

policyBase.

description

String

The description of the policy. Inherited from policyBase.

id

String

The unique identifier for the policy.

isEnabled

Boolean

Denotes whether the policy is enabled.

restrictions

appManagementConfiguration

Restrictions that apply to an application or service

principal object.

**Relationship**

**Type**

**Description**

appliesTo

directoryObject

Collection of applications and service principals to which the policy is

applied.

The following JSON representation shows the resource type.

JSON

**Relationships**

ﾉ

**Expand table**

**JSON representation**

`{`

`  ``"@odata.context"` `: `

`"https://graph.microsoft.com/v1.0/$metadata#policies/appManagementPolicies"` `,`

`  ``"description"` `: ``"String"` `,`

`  ``"displayName"` `: ``"String"` `,`

`  ``"id"` `: ``"String (identifier)"` `,`

`  ``"isEnabled"` `: ``"Boolean"` `,`

`  ``"restrictions"` `: {` `"@odata.type"` `: ``"microsoft.graph.appManagementConfiguration"` `}`

`}`

**Important considerations and**

**restrictions for federated identity**

**credentials**

Article • 02/28/2024

This article describes important considerations, restrictions, and limitations for federated

identity credentials on Microsoft Entra apps and user-assigned managed identities.

For more information on the scenarios enabled by federated identity credentials, see

workload identity federation overview.

_Applies to: applications and user-assigned managed identities_

Anyone with permissions to create an app registration and add a secret or certificate can

add a federated identity credential to an app. If the **Users can register applications**

switch is set to **No** in the **Users->User Settings** blade in the Microsoft Entra admin

center

, however, you won't be able to create an app registration or configure the

federated identity credential. Find an admin to configure the federated identity

credential on your behalf, someone in the Application Administrator or Application

Owner roles.

Federated identity credentials don't consume the Microsoft Entra tenant service

principal object quota.

A maximum of 20 federated identity credentials can be added to an application or user-

assigned managed identity.

When you configure a federated identity credential, there are several important pieces

of information to provide:

_issuer_ and _subject_ are the key pieces of information needed to set up the trust

relationship. The combination of `issuer` and `subject` must be unique on the app.

When the external software workload requests Microsoft identity platform to

exchange the external token for an access token, the _issuer_ and _subject_ values of

the federated identity credential are checked against the `issuer` and `subject`

**General federated identity credential**

**considerations**

claims provided in the external token. If that validation check passes, Microsoft

identity platform issues an access token to the external software workload.

_issuer_ is the URL of the external identity provider and must match the `issuer` claim

of the external token being exchanged. Required. If the `issuer` claim has leading

or trailing whitespace in the value, the token exchange is blocked. This field has a

character limit of 600 characters.

_subject_ is the identifier of the external software workload and must match the `sub`

( ` subject` ) claim of the external token being exchanged. _subject_ has no fixed format,

as each IdP uses their own - sometimes a GUID, sometimes a colon delimited

identifier, sometimes arbitrary strings. This field has a character limit of 600

characters.

_audiences_ lists the audiences that can appear in the external token. Required. You

must add a single audience value, which has a limit of 600 characters. The

recommended value is "api://AzureADTokenExchange". It says what Microsoft

identity platform must accept in the `aud` claim in the incoming token.

_name_ is the unique identifier for the federated identity credential. Required. This

field has a character limit of 3-120 characters and must be URL friendly.

Alphanumeric, dash, or underscore characters are supported, the first character

must be alphanumeric only. It's immutable once created.

_description_ is the user-provided description of the federated identity credential.

Optional. The description isn't validated or checked by Microsoft Entra ID. This field

has a limit of 600 characters.

） **Important**

The _subject_ setting values must exactly match the configuration on the GitHub

workflow configuration. Otherwise, Microsoft identity platform will look at the

incoming external token and reject the exchange for an access token. You

won't get an error, the exchange fails without error.

） **Important**

If you accidentally add the incorrect external workload information in the

_subject_ setting the federated identity credential is created successfully without

error. The error does not become apparent until the token exchange fails.

Wildcard characters aren't supported in any federated identity credential property value.

_Applies to: user-assigned managed identities_

Creation of federated identity credentials is currently **not supported** on user-assigned

managed identities created in the following regions:

East Asia

Qatar Central

Malaysia South

Italy North

Israel Central

Support for creating federated identity credentials on user assigned identities in these

regions will be gradually rolled out. Resources in this region which need to use

federated identity credentials, can do so by leveraging a user assigned managed identity

created in a supported region.

_Applies to: applications and user-assigned managed identities_

Only issuers that provide tokens signed using the RS256 algorithm are supported for

token exchange using workload identity federation. Exchanging tokens signed with

other algorithms may work, but haven't been tested.

_Applies to: applications and user-assigned managed identities_

Creating a federation between two Microsoft Entra identities from the same or different

tenants isn't supported. When creating a federated identity credential, configuring the

_issuer_ (the URL of the external identity provider) with the following values isn't

supported:

\*.login.microsoftonline.com

\*.login.windows.net

\*.login.microsoft.com

**Unsupported regions (user-assigned managed**

**identities)**

**Supported signing algorithms and issuers**

**Microsoft Entra issuers aren't supported**

\*.sts.windows.net

While it's possible to create a federated identity credential with a Microsoft Entra issuer,

attempts to use it for authorization fail with error `AADSTS700222: AAD-issued tokens may`

`not be used for federated identity flows` .

_Applies to: applications and user-assigned managed identities_

It takes time for the federated identity credential to be propagated throughout a region

after being initially configured. A token request made several minutes after configuring

the federated identity credential may fail because the cache is populated in the directory

with old data. During this time window, an authorization request might fail with error

message: `AADSTS70021: No matching federated identity record found for presented`

`assertion.`

To avoid this issue, wait a short time after adding the federated identity credential

before requesting a token to ensure replication completes across all nodes of the

authorization service. We also recommend adding retry logic for token requests. Retries

should be done for every request even after a token was successfully obtained.

Eventually after the data is fully replicated the percentage of failures will drop.

_Applies to: user-assigned managed identities_

Creating multiple federated identity credentials under the same user-assigned managed

identity concurrently triggers concurrency detection logic, which causes requests to fail

with 409-conflict HTTP status code.

Terraform Provider for Azure (Resource Manager)

version 3.40.0 introduces an

update

which creates multiple federated identity credentials sequentially instead of

concurrently. Versions earlier than 3.40.0 can cause failures in pipelines when multiped

federated identities are created. We recommend you use Terraform Provider for Azure

(Resource Manager) v3.40.0

or later so that multiple federated identity credentials are

created sequentially.

**Time for federated credential changes to**

**propagate**

**Concurrent updates aren't supported (user-**

**assigned managed identities)**

When you use automation or Azure Resource Manager templates (ARM templates) to

create federated identity credentials under the same parent identity, create the

federated credentials sequentially. Federated identity credentials under different

managed identities can be created in parallel without any restrictions.

If federated identity credentials are provisioned in a loop, you can provision them

serially by setting _"mode": "serial"_.

You can also provision multiple new federated identity credentials sequentially using the

_dependsOn_ property. The following Azure Resource Manager template (ARM template)

example creates three new federated identity credentials sequentially on a user-

assigned managed identity by using the _dependsOn_ property:

JSON

`{ `

`    ``"$schema"` `: ``"https://schema.management.azure.com/schemas/2019-04-`

`01/deploymentTemplate.json#"` `, `

`    ``"contentVersion"` `: ``"1.0.0.0"` `, `

`    ``"parameters"` `: { `

`        ``"userAssignedIdentities_parent_uami_name"` `: { `

`            ``"defaultValue"` `: ``"parent_uami"` `, `

`            ``"type"` `: ``"String"` ` `

`        } `

`    }, `

`    ``"variables"` `: {}, `

`    ``"resources"` `: [ `

`        { `

`            ``"type"` `: ``"Microsoft.ManagedIdentity/userAssignedIdentities"` `, `

`            ``"apiVersion"` `: ``"2022-01-31-preview"` `, `

`            ``"name"` `: ``"`

`[parameters('userAssignedIdentities_parent_uami_name')]"` `, `

`            ``"location"` `: ``"eastus"` ` `

`        }, `

`        { `

`            ``"type"` `: `

`"Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentia`

`ls"` `, `

`            ``"apiVersion"` `: ``"2022-01-31-preview"` `, `

`            ``"name"` `: ``"`

`[concat(parameters('userAssignedIdentities_parent_uami_name'), '/fic01')]"` `, `

`            ``"dependsOn"` `: [ `

`                ``"`

`[resourceId('Microsoft.ManagedIdentity/userAssignedIdentities', `

`parameters('userAssignedIdentities_parent_uami_name'))]"` ` `

`            ], `

`            ``"properties"` `: { `

`                ``"issuer"` `: ``"https://kubernetes-oauth.azure.com"` `, `

`                ``"subject"` `: ``"fic01"` `, `

`                ``"audiences"` `: [ `

`                    ``"api://AzureADTokenExchange"` ` `

`                ] `

`            } `

`        }, `

`        { `

`            ``"type"` `: `

`"Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentia`

`ls"` `, `

`            ``"apiVersion"` `: ``"2022-01-31-preview"` `, `

`            ``"name"` `: ``"`

`[concat(parameters('userAssignedIdentities_parent_uami_name'), '/fic02')]"` `, `

`            ``"dependsOn"` `: [ `

`                ``"`

`[resourceId('Microsoft.ManagedIdentity/userAssignedIdentities', `

`parameters('userAssignedIdentities_parent_uami_name'))]"` `, `

`                ``"`

`[resourceId('Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdent`

`ityCredentials', parameters('userAssignedIdentities_parent_uami_name'), `

`'fic01')]"` ` `

`            ], `

`            ``"properties"` `: { `

`                ``"issuer"` `: ``"https://kubernetes-oauth.azure.com"` `, `

`                ``"subject"` `: ``"fic02"` `, `

`                ``"audiences"` `: [ `

`                    ``"api://AzureADTokenExchange"` ` `

`                ] `

`            } `

`        }, `

`        { `

`            ``"type"` `: `

`"Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentia`

`ls"` `, `

`            ``"apiVersion"` `: ``"2022-01-31-preview"` `, `

`            ``"name"` `: ``"`

`[concat(parameters('userAssignedIdentities_parent_uami_name'), '/fic03')]"` `, `

`            ``"dependsOn"` `: [ `

`                ``"`

`[resourceId('Microsoft.ManagedIdentity/userAssignedIdentities', `

`parameters('userAssignedIdentities_parent_uami_name'))]"` `, `

`                ``"`

`[resourceId('Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdent`

`ityCredentials', parameters('userAssignedIdentities_parent_uami_name'), `

`'fic02')]"` ` `

`            ], `

`            ``"properties"` `: { `

`                ``"issuer"` `: ``"https://kubernetes-oauth.azure.com"` `, `

`                ``"subject"` `: ``"fic03"` `, `

`                ``"audiences"` `: [ `

`                    ``"api://AzureADTokenExchange"` ` `

`                ] `

`            } `

`        } `

`    ] `

`} `

_Applies to: applications and user-assigned managed identities_

It's possible to use a deny Azure Policy as in the following ARM template example:

JSON

_Applies to: user-assigned managed identities_

The following table describes limits on requests to the user-assigned managed identities

REST APIS. If you exceed a throttling limit, you receive an HTTP 429 error.

**Operation**

**Requests-per-second**

**per Microsoft Entra**

**tenant**

**Requests-per-**

**second per**

**subscription**

**Requests-per-**

**second per**

**resource**

Create or update

requests

10

2

0.25

Get requests

30

10

0.5

List by resource group or

List by subscription

requests

15

5

0.25

Delete requests

10

2

0.25

**Azure policy**

`{ `

`"policyRule"` `: { `

`            ``"if"` `: { `

`                ``"field"` `: ``"type"` `, `

`                ``"equals"` `: `

`"Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentia`

`ls"` ` `

`            }, `

`            ``"then"` `: { `

`                ``"effect"` `: ``"deny"` ` `

`            } `

`        } `

`}`

**Throttling limits**

ﾉ

**Expand table**

_Applies to: applications and user-assigned managed identities_

The following error codes may be returned when creating, updating, getting, listing, or

deleting federated identity credentials.

**HTTP**

**code**

**Error message**

**Comments**

405

The request format was

unexpected: Support for

federated identity credentials

not enabled.

Federated identity credentials aren't enabled in this

region. Refer to “Currently Supported regions”.

400

Federated identity credentials

must have exactly one

audience.

Currently, federated identity credentials support a

single audience “api://AzureADTokenExchange”.

400

Federated Identity Credential

from HTTP body has empty

properties

All federated identity credential properties are

mandatory.

400

Federated Identity Credential

name '{ficName}' is invalid.

Alphanumeric, dash, underscore, no more than 3-120

symbols. First symbol is alphanumeric.

404

The parent user-assigned

identity doesn't exist.

Check user assigned identity name in federated identity

credentials resource path.

400

Issuer and subject

combination already exists

for this Managed Identity.

This is a constraint. List all federated identity credentials

associated with the user-assigned identity to find

existing federated identity credential.

409

Conflict

Concurrent write request to federated identity

credential resources under the same user-assigned

identity has been denied.

**Errors**

ﾉ

**Expand table**

