"""Microsoft Graph API client for Agent Identity operations."""

import time
from typing import Optional

import httpx
from rich.console import Console

from .models import BlueprintInfo, AgentIdentityInfo


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
    ) -> bool:
        """Expose an API on an application with a delegated permission scope.
        
        This sets the App ID URI and adds a delegated permission scope,
        which is required for OBO flows.
        
        Args:
            object_id: Application object ID
            app_id: Application (client) ID
            scope_name: Name of the scope to add (default: access_as_user)
            
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
        
        success, data = self._request(
            "PATCH",
            f"{GRAPH_BETA_URL}/applications/{object_id}",
            json_data=body,
        )
        
        if success:
            return True
        
        console.print(f"[red]Failed to expose API: {data}[/red]")
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

