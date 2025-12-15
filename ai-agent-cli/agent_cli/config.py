"""Configuration management for the AI Agent CLI."""

import json
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from .models import MCPServer


# Default config file location
DEFAULT_CONFIG_PATH = Path.home() / ".ai-agent-cli.json"


class Config:
    """Manages CLI configuration including Azure OpenAI settings and MCP servers."""
    
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize config manager.
        
        Args:
            config_path: Path to config file. Defaults to ~/.ai-agent-cli.json
        """
        self.config_path = config_path or DEFAULT_CONFIG_PATH
        self._data: dict = {}
        self._load_env()
        self._load_config()
    
    def _load_env(self) -> None:
        """Load environment variables from .env file."""
        # Try to load from current directory's .env
        load_dotenv()
        
        # Get configuration from environment
        self._tenant_id_env = os.getenv("TENANT_ID")
        self._auth_mode_env = os.getenv("AUTH_MODE", "entra")
        self._azure_openai_endpoint_env = os.getenv("AZURE_OPENAI_ENDPOINT")
        self._azure_openai_deployment_env = os.getenv("AZURE_OPENAI_DEPLOYMENT")
        self._azure_openai_api_version_env = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
        self._azure_openai_api_key_env = os.getenv("AZURE_OPENAI_API_KEY")
        
        # Blueprint and Agent Identity for OBO flows
        self._blueprint_app_id_env = os.getenv("BLUEPRINT_APP_ID")
        self._blueprint_client_secret_env = os.getenv("BLUEPRINT_CLIENT_SECRET")
        self._agent_identity_app_id_env = os.getenv("AGENT_IDENTITY_APP_ID")
    
    def _load_config(self) -> None:
        """Load configuration from file."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r") as f:
                    self._data = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._data = {}
        else:
            self._data = {}
        
        # Ensure required keys exist
        if "mcp_servers" not in self._data:
            self._data["mcp_servers"] = {}
    
    def _save_config(self) -> None:
        """Save configuration to file."""
        # Ensure parent directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.config_path, "w") as f:
            json.dump(self._data, f, indent=2)
    
    # Tenant ID
    @property
    def tenant_id(self) -> Optional[str]:
        """Get tenant ID from config or environment."""
        return self._data.get("tenant_id") or self._tenant_id_env
    
    @tenant_id.setter
    def tenant_id(self, value: str) -> None:
        """Set tenant ID in config."""
        self._data["tenant_id"] = value
        self._save_config()
    
    # Auth Mode
    @property
    def auth_mode(self) -> str:
        """Get auth mode from config or environment. Returns 'entra' or 'api_key'."""
        return self._data.get("auth_mode") or self._auth_mode_env or "entra"
    
    @auth_mode.setter
    def auth_mode(self, value: str) -> None:
        """Set auth mode in config."""
        if value not in ("entra", "api_key"):
            raise ValueError("auth_mode must be 'entra' or 'api_key'")
        self._data["auth_mode"] = value
        self._save_config()
    
    # Azure OpenAI Endpoint
    @property
    def azure_openai_endpoint(self) -> Optional[str]:
        """Get Azure OpenAI endpoint from config or environment."""
        return self._data.get("azure_openai_endpoint") or self._azure_openai_endpoint_env
    
    @azure_openai_endpoint.setter
    def azure_openai_endpoint(self, value: str) -> None:
        """Set Azure OpenAI endpoint in config."""
        self._data["azure_openai_endpoint"] = value
        self._save_config()
    
    # Azure OpenAI Deployment
    @property
    def azure_openai_deployment(self) -> Optional[str]:
        """Get Azure OpenAI deployment name from config or environment."""
        return self._data.get("azure_openai_deployment") or self._azure_openai_deployment_env
    
    @azure_openai_deployment.setter
    def azure_openai_deployment(self, value: str) -> None:
        """Set Azure OpenAI deployment name in config."""
        self._data["azure_openai_deployment"] = value
        self._save_config()
    
    # Azure OpenAI API Version
    @property
    def azure_openai_api_version(self) -> str:
        """Get Azure OpenAI API version from config or environment."""
        return self._data.get("azure_openai_api_version") or self._azure_openai_api_version_env or "2024-02-15-preview"
    
    @azure_openai_api_version.setter
    def azure_openai_api_version(self, value: str) -> None:
        """Set Azure OpenAI API version in config."""
        self._data["azure_openai_api_version"] = value
        self._save_config()
    
    # Azure OpenAI API Key (for api_key mode)
    @property
    def azure_openai_api_key(self) -> Optional[str]:
        """Get Azure OpenAI API key from config or environment."""
        return self._data.get("azure_openai_api_key") or self._azure_openai_api_key_env
    
    @azure_openai_api_key.setter
    def azure_openai_api_key(self, value: str) -> None:
        """Set Azure OpenAI API key in config."""
        self._data["azure_openai_api_key"] = value
        self._save_config()
    
    # Blueprint App ID (for OBO flows)
    @property
    def blueprint_app_id(self) -> Optional[str]:
        """Get Blueprint application ID from config or environment."""
        return self._data.get("blueprint_app_id") or self._blueprint_app_id_env
    
    @blueprint_app_id.setter
    def blueprint_app_id(self, value: str) -> None:
        """Set Blueprint application ID in config."""
        self._data["blueprint_app_id"] = value
        self._save_config()
    
    # Blueprint Client Secret (for OBO flows)
    @property
    def blueprint_client_secret(self) -> Optional[str]:
        """Get Blueprint client secret from config or environment."""
        return self._data.get("blueprint_client_secret") or self._blueprint_client_secret_env
    
    @blueprint_client_secret.setter
    def blueprint_client_secret(self, value: str) -> None:
        """Set Blueprint client secret in config."""
        self._data["blueprint_client_secret"] = value
        self._save_config()
    
    # Agent Identity App ID (for OBO flows)
    @property
    def agent_identity_app_id(self) -> Optional[str]:
        """Get Agent Identity application ID from config or environment."""
        return self._data.get("agent_identity_app_id") or self._agent_identity_app_id_env
    
    @agent_identity_app_id.setter
    def agent_identity_app_id(self, value: str) -> None:
        """Set Agent Identity application ID in config."""
        self._data["agent_identity_app_id"] = value
        self._save_config()
    
    # MCP Servers
    def add_mcp_server(self, server: MCPServer) -> None:
        """Add an MCP server to config.
        
        Args:
            server: MCP server configuration
        """
        self._data["mcp_servers"][server.name] = server.to_dict()
        self._save_config()
    
    def remove_mcp_server(self, name: str) -> bool:
        """Remove an MCP server from config.
        
        Args:
            name: Server name
            
        Returns:
            True if removed, False if not found
        """
        if name in self._data.get("mcp_servers", {}):
            del self._data["mcp_servers"][name]
            self._save_config()
            return True
        return False
    
    def get_mcp_server(self, name: str) -> Optional[MCPServer]:
        """Get an MCP server by name.
        
        Args:
            name: Server name
            
        Returns:
            MCPServer if found, None otherwise
        """
        servers = self._data.get("mcp_servers", {})
        if name in servers:
            return MCPServer.from_dict(servers[name])
        return None
    
    def list_mcp_servers(self) -> list[MCPServer]:
        """List all configured MCP servers.
        
        Returns:
            List of MCPServer objects
        """
        servers = []
        for name, data in self._data.get("mcp_servers", {}).items():
            # Ensure name is in the data
            data["name"] = name
            servers.append(MCPServer.from_dict(data))
        return servers
    
    def is_configured(self) -> bool:
        """Check if the minimum required configuration is present.
        
        Returns:
            True if configuration is valid for the selected auth mode
        """
        if self.auth_mode == "api_key":
            # API key mode: need endpoint, deployment, and API key
            return bool(
                self.azure_openai_endpoint and 
                self.azure_openai_deployment and 
                self.azure_openai_api_key
            )
        else:  # entra mode
            # Entra mode: need tenant, endpoint, deployment, and OBO config
            return bool(
                self.tenant_id and 
                self.azure_openai_endpoint and 
                self.azure_openai_deployment and
                self.blueprint_app_id and
                self.blueprint_client_secret and
                self.agent_identity_app_id
            )


# Global config instance
_config: Optional[Config] = None


def get_config() -> Config:
    """Get the global config instance."""
    global _config
    if _config is None:
        _config = Config()
    return _config
