"""Microsoft Graph API client for Agent Identity operations."""

import time
from typing import Optional

import httpx
from rich.console import Console

from .models import BlueprintInfo, AgentIdentityInfo, MCPServerAppInfo


console = Console()

GRAPH_BASE_URL = "https://graph.microsoft.com"
GRAPH_BETA_URL = f"{GRAPH_BASE_URL}/beta"
GRAPH_V1_URL = f"{GRAPH_BASE_URL}/v1.0"


class GraphClient:
    """Client for Microsoft Graph API operations."""
    
    def __init__(self, access_token: str):
        """Initialize Graph client.
        
        Args:
            access_token: Bearer token for Graph API
        """
        self.access_token = access_token
        self._headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "OData-Version": "4.0",
        }
    
    def _request(
        self,
        method: str,
        url: str,
        json_data: Optional[dict] = None,
        extra_headers: Optional[dict] = None,
    ) -> tuple[bool, dict]:
        """Make an HTTP request to Graph API.
        
        Args:
            method: HTTP method
            url: Full URL
            json_data: JSON body (optional)
            extra_headers: Additional headers (optional)
            
        Returns:
            Tuple of (success, response_data)
        """
        headers = self._headers.copy()
        if extra_headers:
            headers.update(extra_headers)
        
        with httpx.Client() as client:
            response = client.request(
                method=method,
                url=url,
                json=json_data,
                headers=headers,
            )
            
            if response.status_code in (200, 201):
                return True, response.json()
            elif response.status_code == 204:
                # No content - success for PATCH/DELETE operations
                return True, {}
            else:
                try:
                    error_data = response.json()
                except Exception:
                    error_data = {"error": {"message": response.text}}
                return False, error_data
    
    def get_current_user(self) -> Optional[dict]:
        """Get the current user's profile.
        
        Returns:
            User profile dict or None
        """
        success, data = self._request("GET", f"{GRAPH_V1_URL}/me")
        if success:
            return data
        console.print(f"[red]Failed to get current user: {data}[/red]")
        return None
    
    def list_blueprints(self) -> list[dict]:
        """List all Agent Identity Blueprint applications.
        
        Returns:
            List of blueprint application dicts
        """
        success, data = self._request(
            "GET",
            f"{GRAPH_BETA_URL}/applications/graph.agentIdentityBlueprint",
        )
        
        if success:
            return data.get("value", [])
        
        # Handle case where no blueprints exist
        error = data.get("error", {})
        if error.get("code") == "Request_ResourceNotFound":
            return []
        
        console.print(f"[red]Failed to list blueprints: {data}[/red]")
        return []
    
    def list_blueprint_principals(self) -> list[dict]:
        """List all Agent Identity Blueprint service principals.
        
        Returns:
            List of blueprint principal dicts
        """
        success, data = self._request(
            "GET",
            f"{GRAPH_BETA_URL}/servicePrincipals/graph.agentIdentityBlueprintPrincipal",
        )
        
        if success:
            return data.get("value", [])
        
        error = data.get("error", {})
        if error.get("code") == "Request_ResourceNotFound":
            return []
        
        console.print(f"[red]Failed to list blueprint principals: {data}[/red]")
        return []
    
    def create_blueprint(
        self,
        display_name: str,
        user_id: str,
    ) -> Optional[dict]:
        """Create a new Agent Identity Blueprint.
        
        Args:
            display_name: Name for the blueprint
            user_id: User ID for sponsor and owner
            
        Returns:
            Created blueprint dict or None
        """
        body = {
            "@odata.type": "Microsoft.Graph.AgentIdentityBlueprint",
            "displayName": display_name,
            "sponsors@odata.bind": [
                f"{GRAPH_V1_URL}/users/{user_id}"
            ],
            "owners@odata.bind": [
                f"{GRAPH_V1_URL}/users/{user_id}"
            ],
        }
        
        success, data = self._request(
            "POST",
            f"{GRAPH_BETA_URL}/applications/",
            json_data=body,
        )
        
        if success:
            return data
        
        console.print(f"[red]Failed to create blueprint: {data}[/red]")
        return None
    
    def create_blueprint_principal(self, app_id: str) -> Optional[dict]:
        """Create a service principal for a blueprint.
        
        Args:
            app_id: Blueprint application ID
            
        Returns:
            Created principal dict or None
        """
        body = {
            "appId": app_id,
        }
        
        success, data = self._request(
            "POST",
            f"{GRAPH_BETA_URL}/serviceprincipals/graph.agentIdentityBlueprintPrincipal",
            json_data=body,
        )
        
        if success:
            return data
        
        console.print(f"[red]Failed to create blueprint principal: {data}[/red]")
        return None
    
    def add_client_secret(
        self,
        object_id: str,
        display_name: str = "Agent Identity CLI Secret",
    ) -> Optional[str]:
        """Add a client secret to an application.
        
        Args:
            object_id: Application object ID
            display_name: Display name for the secret
            
        Returns:
            Secret value or None
        """
        body = {
            "passwordCredential": {
                "displayName": display_name,
            }
        }
        
        success, data = self._request(
            "POST",
            f"{GRAPH_BETA_URL}/applications/{object_id}/addPassword",
            json_data=body,
        )
        
        if success:
            return data.get("secretText")
        
        console.print(f"[red]Failed to add client secret: {data}[/red]")
        return None
    
    def get_application_by_app_id(self, app_id: str) -> Optional[dict]:
        """Get an application by its app ID.
        
        Args:
            app_id: Application (client) ID
            
        Returns:
            Application dict or None
        """
        success, data = self._request(
            "GET",
            f"{GRAPH_BETA_URL}/applications?$filter=appId eq '{app_id}'",
        )
        
        if success:
            values = data.get("value", [])
            if values:
                return values[0]
        return None
    
    def list_agent_identities(self) -> list[dict]:
        """List all Agent Identities.
        
        Returns:
            List of agent identity dicts
        """
        success, data = self._request(
            "GET",
            f"{GRAPH_BETA_URL}/servicePrincipals/graph.agentIdentity",
        )
        
        if success:
            return data.get("value", [])
        
        error = data.get("error", {})
        if error.get("code") == "Request_ResourceNotFound":
            return []
        
        console.print(f"[red]Failed to list agent identities: {data}[/red]")
        return []
    
    def create_agent_identity(
        self,
        display_name: str,
        blueprint_app_id: str,
        sponsor_user_id: str,
    ) -> Optional[dict]:
        """Create a new Agent Identity.
        
        Note: This requires a blueprint access token, not a user token.
        
        Args:
            display_name: Name for the agent identity
            blueprint_app_id: Blueprint application ID
            sponsor_user_id: User ID for sponsor
            
        Returns:
            Created agent identity dict or None
        """
        body = {
            "displayName": display_name,
            "agentIdentityBlueprintId": blueprint_app_id,
            "sponsors@odata.bind": [
                f"{GRAPH_V1_URL}/users/{sponsor_user_id}"
            ],
        }
        
        success, data = self._request(
            "POST",
            f"{GRAPH_BETA_URL}/serviceprincipals/Microsoft.Graph.AgentIdentity",
            json_data=body,
        )
        
        if success:
            return data
        
        console.print(f"[red]Failed to create agent identity: {data}[/red]")
        return None
    
    def expose_api(
        self,
        object_id: str,
        app_id: str,
        scope_name: str = "access_as_user",
        max_retries: int = 3,
        retry_delay: int = 5,
    ) -> bool:
        """Expose an API on an application with a delegated permission scope.
        
        This sets the App ID URI and adds a delegated permission scope,
        which is required for OBO flows.
        
        Args:
            object_id: Application object ID
            app_id: Application (client) ID
            scope_name: Name of the scope to add (default: access_as_user)
            max_retries: Number of retries if the request fails (default: 3)
            retry_delay: Seconds to wait between retries (default: 5)
            
        Returns:
            True if successful, False otherwise
        """
        import uuid
        
        app_id_uri = f"api://{app_id}"
        scope_id = str(uuid.uuid4())
        
        # Update the application with App ID URI and scope
        body = {
            "identifierUris": [app_id_uri],
            "api": {
                "oauth2PermissionScopes": [
                    {
                        "id": scope_id,
                        "adminConsentDescription": f"Allow the application to access the agent on behalf of the signed-in user",
                        "adminConsentDisplayName": "Access agent as user",
                        "isEnabled": True,
                        "type": "User",
                        "userConsentDescription": f"Allow the application to access the agent on your behalf",
                        "userConsentDisplayName": "Access agent as user",
                        "value": scope_name,
                    }
                ]
            }
        }
        
        # Retry logic for Azure AD propagation delays
        for attempt in range(max_retries):
            success, data = self._request(
                "PATCH",
                f"{GRAPH_BETA_URL}/applications/{object_id}",
                json_data=body,
            )
            
            if success:
                return True
            
            # Check if it's a propagation/timing issue (typically shows as empty error or 404)
            error_msg = str(data.get("error", {}).get("message", ""))
            error_code = data.get("error", {}).get("code", "")
            
            if attempt < max_retries - 1:
                console.print(f"[yellow]Attempt {attempt + 1} failed, retrying in {retry_delay}s...[/yellow]")
                if error_msg:
                    console.print(f"[dim]  Error: {error_msg}[/dim]")
                time.sleep(retry_delay)
            else:
                console.print(f"[red]Failed to expose API after {max_retries} attempts: {data}[/red]")
        
        return False
    
    def get_service_principal_by_app_id(self, app_id: str) -> Optional[dict]:
        """Get a service principal by its application ID.
        
        Args:
            app_id: Application (client) ID
            
        Returns:
            Service principal dict or None
        """
        success, data = self._request(
            "GET",
            f"{GRAPH_V1_URL}/servicePrincipals?$filter=appId eq '{app_id}'",
        )
        
        if success:
            values = data.get("value", [])
            if values:
                return values[0]
        return None
    
    def grant_admin_consent(
        self,
        client_sp_id: str,
        resource_sp_id: str,
        scopes: str,
    ) -> bool:
        """Grant admin consent for delegated permissions.
        
        This creates an OAuth2PermissionGrant that grants consent
        for all principals in the tenant.
        
        Args:
            client_sp_id: Service principal ID of the client (e.g., Agent Identity)
            resource_sp_id: Service principal ID of the resource (e.g., Microsoft Graph)
            scopes: Space-separated list of scopes to grant
            
        Returns:
            True if successful, False otherwise
        """
        body = {
            "clientId": client_sp_id,
            "consentType": "AllPrincipals",
            "resourceId": resource_sp_id,
            "scope": scopes,
        }
        
        success, data = self._request(
            "POST",
            f"{GRAPH_V1_URL}/oauth2PermissionGrants",
            json_data=body,
        )
        
        if success:
            return True
        
        # Check if consent already exists
        error = data.get("error", {})
        if "already exists" in str(error.get("message", "")).lower():
            console.print("[yellow]Admin consent already exists[/yellow]")
            return True
        
        console.print(f"[red]Failed to grant admin consent: {data}[/red]")
        return False
    
    def create_application(
        self,
        display_name: str,
        sign_in_audience: str = "AzureADMyOrg",
    ) -> Optional[dict]:
        """Create a new application registration.
        
        Args:
            display_name: Name for the application
            sign_in_audience: Supported account types (default: single tenant)
            
        Returns:
            Created application dict or None
        """
        body = {
            "displayName": display_name,
            "signInAudience": sign_in_audience,
        }
        
        success, data = self._request(
            "POST",
            f"{GRAPH_V1_URL}/applications",
            json_data=body,
        )
        
        if success:
            return data
        
        console.print(f"[red]Failed to create application: {data}[/red]")
        return None
    
    def create_service_principal(self, app_id: str) -> Optional[dict]:
        """Create a service principal for an application.
        
        Args:
            app_id: Application (client) ID
            
        Returns:
            Created service principal dict or None
        """
        body = {
            "appId": app_id,
        }
        
        success, data = self._request(
            "POST",
            f"{GRAPH_V1_URL}/servicePrincipals",
            json_data=body,
        )
        
        if success:
            return data
        
        # Check if already exists
        error = data.get("error", {})
        if "already exists" in str(error.get("message", "")).lower():
            console.print("[yellow]Service principal already exists, looking it up...[/yellow]")
            return self.get_service_principal_by_app_id(app_id)
        
        console.print(f"[red]Failed to create service principal: {data}[/red]")
        return None
    
    def add_required_resource_access(
        self,
        app_object_id: str,
        resource_app_id: str,
        delegated_permission_ids: list[str],
    ) -> bool:
        """Add required resource access (API permissions) to an application.
        
        Args:
            app_object_id: Application object ID
            resource_app_id: Resource application ID (e.g., Microsoft Graph)
            delegated_permission_ids: List of permission (scope) IDs to add
            
        Returns:
            True if successful, False otherwise
        """
        # Build the resource access array
        resource_access = [
            {"id": perm_id, "type": "Scope"}
            for perm_id in delegated_permission_ids
        ]
        
        body = {
            "requiredResourceAccess": [
                {
                    "resourceAppId": resource_app_id,
                    "resourceAccess": resource_access,
                }
            ]
        }
        
        success, data = self._request(
            "PATCH",
            f"{GRAPH_V1_URL}/applications/{app_object_id}",
            json_data=body,
        )
        
        if success:
            return True
        
        console.print(f"[red]Failed to add required resource access: {data}[/red]")
        return False
    
    def configure_agent_identity_optional_claims(self, app_object_id: str) -> bool:
        """Configure optional claims for Agent Identity tokens.
        
        Adds the xms_* claims that identify the token as coming from an Agent Identity:
        - xms_act_fct: Actor facet claim (value 11 = AgentIdentity)
        - xms_sub_fct: Subject facet claim
        - xms_par_app_azp: Parent application of the authorized party
        - xms_idrel: Identity relationship claim
        
        Args:
            app_object_id: Application object ID
            
        Returns:
            True if successful, False otherwise
        """
        body = {
            "optionalClaims": {
                "accessToken": [
                    {"name": "xms_act_fct", "essential": False},
                    {"name": "xms_sub_fct", "essential": False},
                    {"name": "xms_par_app_azp", "essential": False},
                    {"name": "xms_idrel", "essential": False},
                    {"name": "xms_tnt_fct", "essential": False},
                ]
            }
        }
        
        success, data = self._request(
            "PATCH",
            f"{GRAPH_V1_URL}/applications/{app_object_id}",
            json_data=body,
        )
        
        if success:
            return True
        
        console.print(f"[red]Failed to configure optional claims: {data}[/red]")
        return False

    def get_graph_delegated_permission_id(self, permission_name: str) -> Optional[str]:
        """Get the ID of a Microsoft Graph delegated permission by name.
        
        Args:
            permission_name: Permission name (e.g., "User.Read")
            
        Returns:
            Permission ID or None
        """
        # Get Microsoft Graph service principal
        graph_sp = self.get_service_principal_by_app_id(MICROSOFT_GRAPH_APP_ID)
        if not graph_sp:
            return None
        
        # Search for the permission in oauth2PermissionScopes
        scopes = graph_sp.get("oauth2PermissionScopes", [])
        for scope in scopes:
            if scope.get("value") == permission_name:
                return scope.get("id")
        
        console.print(f"[yellow]Permission '{permission_name}' not found in Microsoft Graph[/yellow]")
        return None

    def get_blueprint_by_app_id(self, app_id: str) -> Optional[dict]:
        """Get a Blueprint application by its app ID using Beta API.
        
        Note: Agent Blueprints require the Beta Graph API.
        
        Args:
            app_id: Blueprint application (client) ID
            
        Returns:
            Blueprint application dict or None
        """
        success, data = self._request(
            "GET",
            f"{GRAPH_BETA_URL}/applications?$filter=appId eq '{app_id}'",
        )
        
        if success:
            values = data.get("value", [])
            if values:
                return values[0]
        return None

    def add_federated_identity_credential(
        self,
        app_object_id: str,
        name: str,
        issuer: str,
        subject: str,
        audiences: list[str],
        description: str = "",
    ) -> tuple[bool, Optional[dict]]:
        """Add a Federated Identity Credential to an application.
        
        Note: Agent Blueprints require the Beta Graph API.
        
        Args:
            app_object_id: Application object ID (not app/client ID)
            name: Unique name for the credential
            issuer: OIDC issuer URL (e.g., Kubernetes OIDC provider)
            subject: Subject claim (e.g., system:serviceaccount:namespace:name)
            audiences: List of allowed audiences (typically ["api://AzureADTokenExchange"])
            description: Optional description
            
        Returns:
            Tuple of (success, credential_dict or error_dict)
        """
        body = {
            "name": name,
            "issuer": issuer,
            "subject": subject,
            "audiences": audiences,
        }
        
        if description:
            body["description"] = description
        
        success, data = self._request(
            "POST",
            f"{GRAPH_BETA_URL}/applications/{app_object_id}/federatedIdentityCredentials",
            json_data=body,
        )
        
        return success, data

    def list_applications(
        self,
        name_filter: Optional[str] = None,
        use_search: bool = True,
    ) -> list[dict]:
        """List applications, optionally filtering by display name.
        
        Args:
            name_filter: Filter string to match in display name
            use_search: If True, use $search (substring match). If False, use startswith filter.
            
        Returns:
            List of application dicts
        """
        if name_filter:
            if use_search:
                # Use $search for substring matching (requires ConsistencyLevel header)
                url = f'{GRAPH_V1_URL}/applications?$search="displayName:{name_filter}"&$orderby=displayName&$select=id,appId,displayName,createdDateTime'
                extra_headers = {"ConsistencyLevel": "eventual"}
            else:
                # Use $filter with startswith (more limited but doesn't require special header)
                url = f"{GRAPH_V1_URL}/applications?$filter=startswith(displayName, '{name_filter}')&$orderby=displayName&$select=id,appId,displayName,createdDateTime"
                extra_headers = None
        else:
            # List all applications (limited to top 100)
            url = f"{GRAPH_V1_URL}/applications?$top=100&$orderby=displayName&$select=id,appId,displayName,createdDateTime"
            extra_headers = None
        
        success, data = self._request("GET", url, extra_headers=extra_headers)
        
        if success:
            return data.get("value", [])
        
        console.print(f"[red]Failed to list applications: {data}[/red]")
        return []

    def list_federated_identity_credentials(self, app_object_id: str) -> list[dict]:
        """List all Federated Identity Credentials on an application.
        
        Note: Agent Blueprints require the Beta Graph API.
        
        Args:
            app_object_id: Application object ID (not app/client ID)
            
        Returns:
            List of federated identity credential dicts
        """
        success, data = self._request(
            "GET",
            f"{GRAPH_BETA_URL}/applications/{app_object_id}/federatedIdentityCredentials",
        )
        
        if success:
            return data.get("value", [])
        
        console.print(f"[red]Failed to list federated identity credentials: {data}[/red]")
        return []

    def delete_federated_identity_credential(
        self,
        app_object_id: str,
        credential_id: str,
    ) -> bool:
        """Delete a Federated Identity Credential from an application.
        
        Args:
            app_object_id: Application object ID
            credential_id: Federated credential ID
            
        Returns:
            True if successful, False otherwise
        """
        success, data = self._request(
            "DELETE",
            f"{GRAPH_BETA_URL}/applications/{app_object_id}/federatedIdentityCredentials/{credential_id}",
        )
        
        if success:
            return True
        
        console.print(f"[red]Failed to delete federated identity credential: {data}[/red]")
        return False


def create_full_blueprint(
    access_token: str,
    display_name: str,
    enable_obo: bool = True,
) -> Optional[BlueprintInfo]:
    """Create a complete blueprint with principal, client secret, and OBO support.
    
    This performs the full creation flow:
    1. Get current user
    2. Create blueprint application
    3. Wait for propagation
    4. Create blueprint service principal
    5. Add client secret
    6. Expose API for OBO (if enable_obo=True)
    
    Args:
        access_token: User access token with required permissions
        display_name: Name for the blueprint
        enable_obo: If True, expose API with access_as_user scope for OBO flows
        
    Returns:
        BlueprintInfo with all details or None
    """
    client = GraphClient(access_token)
    
    # Step 1: Get current user
    console.print("[bold blue]Getting current user...[/bold blue]")
    user = client.get_current_user()
    if not user:
        return None
    
    user_id = user["id"]
    console.print(f"[green]✓ User ID: {user_id}[/green]")
    
    # Step 2: Create blueprint
    console.print(f"[bold blue]Creating blueprint '{display_name}'...[/bold blue]")
    blueprint = client.create_blueprint(display_name, user_id)
    if not blueprint:
        return None
    
    app_id = blueprint["appId"]
    object_id = blueprint["id"]
    console.print(f"[green]✓ Blueprint created![/green]")
    console.print(f"  App ID: {app_id}")
    console.print(f"  Object ID: {object_id}")
    
    # Step 3: Wait for propagation
    console.print("[bold blue]Waiting for Azure AD propagation (5 seconds)...[/bold blue]")
    time.sleep(5)
    
    # Step 4: Create service principal
    console.print("[bold blue]Creating blueprint service principal...[/bold blue]")
    principal = client.create_blueprint_principal(app_id)
    if not principal:
        console.print("[yellow]Warning: Failed to create principal, but blueprint exists[/yellow]")
        principal_id = ""
    else:
        principal_id = principal["id"]
        console.print(f"[green]✓ Principal created![/green]")
        console.print(f"  Principal ID: {principal_id}")
    
    # Step 5: Add client secret
    console.print("[bold blue]Adding client secret...[/bold blue]")
    secret = client.add_client_secret(object_id)
    if not secret:
        console.print("[red]Failed to add client secret![/red]")
        return None
    
    console.print("[green]✓ Client secret created![/green]")
    console.print(f"[yellow]  Secret: {secret}[/yellow]")
    console.print("[yellow]  (Save this! You won't see it again)[/yellow]")
    
    # Step 6: Expose API for OBO (if enabled)
    if enable_obo:
        console.print("[bold blue]Exposing API for OBO flows...[/bold blue]")
        if client.expose_api(object_id, app_id):
            console.print(f"[green]✓ API exposed![/green]")
            console.print(f"  App ID URI: api://{app_id}")
            console.print(f"  Scope: api://{app_id}/access_as_user")
        else:
            console.print("[yellow]Warning: Failed to expose API. OBO flows may not work.[/yellow]")
            console.print("[yellow]You can manually set this up - see OBO-GUIDE.md[/yellow]")
    
    return BlueprintInfo(
        app_id=app_id,
        object_id=object_id,
        principal_id=principal_id,
        client_secret=secret,
        display_name=display_name,
    )


def create_agent_identity_from_blueprint(
    blueprint_token: str,
    display_name: str,
    blueprint_app_id: str,
    sponsor_user_id: str,
) -> Optional[AgentIdentityInfo]:
    """Create an agent identity using a blueprint access token.
    
    Args:
        blueprint_token: Access token for the blueprint (client credentials)
        display_name: Name for the agent identity
        blueprint_app_id: Blueprint application ID
        sponsor_user_id: User ID for sponsor
        
    Returns:
        AgentIdentityInfo or None
    """
    client = GraphClient(blueprint_token)
    
    console.print(f"[bold blue]Creating agent identity '{display_name}'...[/bold blue]")
    result = client.create_agent_identity(display_name, blueprint_app_id, sponsor_user_id)
    
    if result:
        console.print("[green]✓ Agent identity created![/green]")
        console.print(f"  ID: {result['id']}")
        console.print(f"  App ID: {result['appId']}")
        
        return AgentIdentityInfo(
            id=result["id"],
            app_id=result["appId"],
            display_name=display_name,
            blueprint_app_id=blueprint_app_id,
        )
    
    return None


# Microsoft Graph application ID (well-known)
MICROSOFT_GRAPH_APP_ID = "00000003-0000-0000-c000-000000000000"

# Default scopes for OBO flows
DEFAULT_OBO_SCOPES = "User.Read openid profile offline_access"


def grant_agent_admin_consent(
    access_token: str,
    agent_identity_app_id: str,
    resource_app_id: str = MICROSOFT_GRAPH_APP_ID,
    scopes: str = DEFAULT_OBO_SCOPES,
) -> bool:
    """Grant admin consent for an agent identity to access a resource.
    
    This is required for OBO flows since agent identities cannot
    prompt users for consent.
    
    Args:
        access_token: User access token with DelegatedPermissionGrant.ReadWrite.All
        agent_identity_app_id: Agent identity's application ID
        resource_app_id: Resource application ID (default: Microsoft Graph)
        scopes: Space-separated scopes to grant
        
    Returns:
        True if successful, False otherwise
    """
    client = GraphClient(access_token)
    
    # Get the agent identity's service principal ID
    console.print("[bold blue]Looking up agent identity service principal...[/bold blue]")
    agent_sp = client.get_service_principal_by_app_id(agent_identity_app_id)
    if not agent_sp:
        console.print(f"[red]Agent identity service principal not found for app ID: {agent_identity_app_id}[/red]")
        return False
    
    agent_sp_id = agent_sp["id"]
    console.print(f"[green]✓ Agent Identity SP ID: {agent_sp_id}[/green]")
    
    # Get the resource's service principal ID
    console.print("[bold blue]Looking up resource service principal...[/bold blue]")
    resource_sp = client.get_service_principal_by_app_id(resource_app_id)
    if not resource_sp:
        console.print(f"[red]Resource service principal not found for app ID: {resource_app_id}[/red]")
        return False
    
    resource_sp_id = resource_sp["id"]
    resource_name = resource_sp.get("displayName", resource_app_id)
    console.print(f"[green]✓ Resource SP ID: {resource_sp_id} ({resource_name})[/green]")
    
    # Grant admin consent
    console.print(f"[bold blue]Granting admin consent for scopes: {scopes}...[/bold blue]")
    if client.grant_admin_consent(agent_sp_id, resource_sp_id, scopes):
        console.print(f"[green]✓ Admin consent granted![/green]")
        return True
    
    return False


def create_mcp_server_app(
    access_token: str,
    display_name: str,
    graph_permissions: list[str],
) -> Optional[MCPServerAppInfo]:
    """Create an MCP Server app registration with exposed API and Graph permissions.
    
    This performs the full creation flow:
    1. Create application registration
    2. Expose API with access_as_user scope
    3. Wait for Azure AD propagation
    4. Create service principal
    5. Configure Agent Identity optional claims (xms_act_fct, xms_sub_fct, etc.)
    6. Add client secret
    7. Add Microsoft Graph delegated permissions
    8. Grant admin consent for Graph permissions
    
    Args:
        access_token: User access token with required permissions
        display_name: Name for the MCP server app
        graph_permissions: List of Microsoft Graph permissions (e.g., ["User.Read"])
        
    Returns:
        MCPServerAppInfo with all details or None
    """
    client = GraphClient(access_token)
    
    # Step 1: Create application
    console.print(f"[bold blue]Creating application '{display_name}'...[/bold blue]")
    app = client.create_application(display_name)
    if not app:
        return None
    
    app_id = app["appId"]
    object_id = app["id"]
    console.print(f"[green]✓ Application created![/green]")
    console.print(f"  App ID: {app_id}")
    console.print(f"  Object ID: {object_id}")
    
    # Wait for Azure AD propagation before modifying the app
    # Azure AD can take 5-15 seconds to propagate new applications
    console.print("[bold blue]Waiting for Azure AD propagation (8 seconds)...[/bold blue]")
    time.sleep(8)
    
    # Step 2: Expose API with access_as_user scope
    console.print("[bold blue]Exposing API for OBO flows (with retry)...[/bold blue]")
    if client.expose_api(object_id, app_id, "access_as_user"):
        api_scope = f"api://{app_id}/access_as_user"
        console.print(f"[green]✓ API exposed![/green]")
        console.print(f"  App ID URI: api://{app_id}")
        console.print(f"  Scope: {api_scope}")
    else:
        console.print("[red]Failed to expose API[/red]")
        return None
    
    # Step 3: Wait for propagation
    console.print("[bold blue]Waiting for Azure AD propagation (3 seconds)...[/bold blue]")
    time.sleep(3)
    
    # Step 4: Create service principal
    console.print("[bold blue]Creating service principal...[/bold blue]")
    sp = client.create_service_principal(app_id)
    if not sp:
        return None
    
    sp_id = sp["id"]
    console.print(f"[green]✓ Service principal created![/green]")
    console.print(f"  Service Principal ID: {sp_id}")
    
    # Step 5: Configure Agent Identity optional claims
    console.print("[bold blue]Configuring Agent Identity optional claims...[/bold blue]")
    if client.configure_agent_identity_optional_claims(object_id):
        console.print("[green]✓ Optional claims configured![/green]")
        console.print("  [dim]xms_act_fct, xms_sub_fct, xms_par_app_azp, xms_idrel, xms_tnt_fct[/dim]")
    else:
        console.print("[yellow]Warning: Failed to configure optional claims[/yellow]")
        console.print("[yellow]You can manually add them in Azure Portal → Token configuration[/yellow]")
    
    # Step 6: Add client secret
    console.print("[bold blue]Adding client secret...[/bold blue]")
    secret = client.add_client_secret(object_id, f"{display_name} OBO Secret")
    if not secret:
        console.print("[red]Failed to add client secret![/red]")
        return None
    
    console.print("[green]✓ Client secret created![/green]")
    console.print(f"[yellow]  Secret: {secret}[/yellow]")
    console.print("[yellow]  (Save this! You won't see it again)[/yellow]")
    
    # Step 7: Add Microsoft Graph delegated permissions
    if graph_permissions:
        console.print(f"[bold blue]Adding Microsoft Graph permissions: {', '.join(graph_permissions)}...[/bold blue]")
        
        # Get permission IDs
        permission_ids = []
        for perm_name in graph_permissions:
            perm_id = client.get_graph_delegated_permission_id(perm_name)
            if perm_id:
                permission_ids.append(perm_id)
                console.print(f"  [dim]Found permission ID for {perm_name}: {perm_id}[/dim]")
            else:
                console.print(f"[yellow]Warning: Could not find permission '{perm_name}'[/yellow]")
        
        if permission_ids:
            if client.add_required_resource_access(object_id, MICROSOFT_GRAPH_APP_ID, permission_ids):
                console.print("[green]✓ Graph permissions added to app registration![/green]")
            else:
                console.print("[yellow]Warning: Failed to add Graph permissions[/yellow]")
        
        # Step 8: Grant admin consent for Graph permissions
        console.print("[bold blue]Granting admin consent for Microsoft Graph...[/bold blue]")
        
        # Get Microsoft Graph SP
        graph_sp = client.get_service_principal_by_app_id(MICROSOFT_GRAPH_APP_ID)
        if graph_sp:
            scopes = " ".join(graph_permissions)
            if client.grant_admin_consent(sp_id, graph_sp["id"], scopes):
                console.print(f"[green]✓ Admin consent granted for: {scopes}[/green]")
            else:
                console.print("[yellow]Warning: Failed to grant admin consent for Graph[/yellow]")
                console.print("[yellow]You may need to grant consent manually in Azure Portal[/yellow]")
    
    return MCPServerAppInfo(
        app_id=app_id,
        object_id=object_id,
        service_principal_id=sp_id,
        client_secret=secret,
        display_name=display_name,
        api_scope=api_scope,
    )


def grant_agent_permission_to_mcp(
    access_token: str,
    agent_identity_app_id: str,
    mcp_server_app_id: str,
    scope: str = "access_as_user",
) -> bool:
    """Grant an Agent Identity permission to call the MCP Server API.
    
    This creates an OAuth2PermissionGrant that allows the Agent Identity
    to request tokens for the MCP Server's exposed API.
    
    Args:
        access_token: User access token with DelegatedPermissionGrant.ReadWrite.All
        agent_identity_app_id: Agent identity's application ID
        mcp_server_app_id: MCP Server's application ID
        scope: Scope to grant (default: access_as_user)
        
    Returns:
        True if successful, False otherwise
    """
    client = GraphClient(access_token)
    
    # Get the agent identity's service principal ID
    console.print("[bold blue]Looking up Agent Identity service principal...[/bold blue]")
    agent_sp = client.get_service_principal_by_app_id(agent_identity_app_id)
    if not agent_sp:
        console.print(f"[red]Agent Identity not found for app ID: {agent_identity_app_id}[/red]")
        return False
    
    agent_sp_id = agent_sp["id"]
    agent_name = agent_sp.get("displayName", agent_identity_app_id)
    console.print(f"[green]✓ Agent Identity: {agent_name} (SP ID: {agent_sp_id})[/green]")
    
    # Get the MCP Server's service principal ID
    console.print("[bold blue]Looking up MCP Server service principal...[/bold blue]")
    mcp_sp = client.get_service_principal_by_app_id(mcp_server_app_id)
    if not mcp_sp:
        console.print(f"[red]MCP Server not found for app ID: {mcp_server_app_id}[/red]")
        return False
    
    mcp_sp_id = mcp_sp["id"]
    mcp_name = mcp_sp.get("displayName", mcp_server_app_id)
    console.print(f"[green]✓ MCP Server: {mcp_name} (SP ID: {mcp_sp_id})[/green]")
    
    # Grant the permission
    console.print(f"[bold blue]Granting permission for scope: {scope}...[/bold blue]")
    if client.grant_admin_consent(agent_sp_id, mcp_sp_id, scope):
        console.print(f"[green]✓ Agent Identity can now call MCP Server API![/green]")
        console.print(f"[dim]  {agent_name} → api://{mcp_server_app_id}/{scope}[/dim]")
        return True
    
    return False

