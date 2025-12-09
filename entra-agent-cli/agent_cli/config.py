"""Configuration management for the Agent Identity CLI."""

import json
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from .models import BlueprintInfo, AgentIdentityInfo


# Default config file location
DEFAULT_CONFIG_PATH = Path.home() / ".agent-identity-cli.json"


class Config:
    """Manages CLI configuration including stored blueprints and agent identities."""
    
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize config manager.
        
        Args:
            config_path: Path to config file. Defaults to ~/.agent-identity-cli.json
        """
        self.config_path = config_path or DEFAULT_CONFIG_PATH
        self._data: dict = {}
        self._load_env()
        self._load_config()
    
    def _load_env(self) -> None:
        """Load environment variables from .env file."""
        # Try to load from current directory's .env
        load_dotenv()
        
        # Get tenant ID from environment
        self._tenant_id_env = os.getenv("TENANT_ID")
        self._default_blueprint = os.getenv("DEFAULT_BLUEPRINT_NAME")
    
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
        if "blueprints" not in self._data:
            self._data["blueprints"] = {}
        if "agent_identities" not in self._data:
            self._data["agent_identities"] = {}
    
    def _save_config(self) -> None:
        """Save configuration to file."""
        # Ensure parent directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.config_path, "w") as f:
            json.dump(self._data, f, indent=2)
    
    @property
    def tenant_id(self) -> Optional[str]:
        """Get tenant ID from config or environment."""
        return self._data.get("tenant_id") or self._tenant_id_env
    
    @tenant_id.setter
    def tenant_id(self, value: str) -> None:
        """Set tenant ID in config."""
        self._data["tenant_id"] = value
        self._save_config()
    
    @property
    def default_blueprint_name(self) -> Optional[str]:
        """Get default blueprint name."""
        return self._data.get("default_blueprint") or self._default_blueprint
    
    @default_blueprint_name.setter
    def default_blueprint_name(self, value: str) -> None:
        """Set default blueprint name."""
        self._data["default_blueprint"] = value
        self._save_config()
    
    def get_blueprint(self, name: str) -> Optional[BlueprintInfo]:
        """Get a stored blueprint by name.
        
        Args:
            name: Blueprint display name
            
        Returns:
            BlueprintInfo if found, None otherwise
        """
        blueprints = self._data.get("blueprints", {})
        if name in blueprints:
            bp_data = blueprints[name]
            return BlueprintInfo(
                app_id=bp_data["app_id"],
                object_id=bp_data["object_id"],
                principal_id=bp_data["principal_id"],
                client_secret=bp_data["client_secret"],
                display_name=name,
            )
        return None
    
    def save_blueprint(self, name: str, blueprint: BlueprintInfo) -> None:
        """Save a blueprint to config.
        
        Args:
            name: Blueprint display name (used as key)
            blueprint: Blueprint information to save
        """
        self._data["blueprints"][name] = {
            "app_id": blueprint.app_id,
            "object_id": blueprint.object_id,
            "principal_id": blueprint.principal_id,
            "client_secret": blueprint.client_secret,
        }
        self._save_config()
    
    def list_blueprints(self) -> dict[str, BlueprintInfo]:
        """List all stored blueprints.
        
        Returns:
            Dictionary of blueprint name to BlueprintInfo
        """
        result = {}
        for name, bp_data in self._data.get("blueprints", {}).items():
            result[name] = BlueprintInfo(
                app_id=bp_data["app_id"],
                object_id=bp_data["object_id"],
                principal_id=bp_data["principal_id"],
                client_secret=bp_data["client_secret"],
                display_name=name,
            )
        return result
    
    def delete_blueprint(self, name: str) -> bool:
        """Delete a blueprint from config.
        
        Args:
            name: Blueprint display name
            
        Returns:
            True if deleted, False if not found
        """
        if name in self._data.get("blueprints", {}):
            del self._data["blueprints"][name]
            self._save_config()
            return True
        return False
    
    def save_agent_identity(self, agent: AgentIdentityInfo) -> None:
        """Save an agent identity to config.
        
        Args:
            agent: Agent identity information to save
        """
        self._data["agent_identities"][agent.display_name] = {
            "id": agent.id,
            "app_id": agent.app_id,
            "blueprint_app_id": agent.blueprint_app_id,
        }
        self._save_config()
    
    def get_agent_identity(self, name: str) -> Optional[AgentIdentityInfo]:
        """Get a stored agent identity by name.
        
        Args:
            name: Agent identity display name
            
        Returns:
            AgentIdentityInfo if found, None otherwise
        """
        agents = self._data.get("agent_identities", {})
        if name in agents:
            agent_data = agents[name]
            return AgentIdentityInfo(
                id=agent_data["id"],
                app_id=agent_data["app_id"],
                display_name=name,
                blueprint_app_id=agent_data.get("blueprint_app_id"),
            )
        return None
    
    def list_agent_identities(self) -> dict[str, AgentIdentityInfo]:
        """List all stored agent identities.
        
        Returns:
            Dictionary of agent identity name to AgentIdentityInfo
        """
        result = {}
        for name, agent_data in self._data.get("agent_identities", {}).items():
            result[name] = AgentIdentityInfo(
                id=agent_data["id"],
                app_id=agent_data["app_id"],
                display_name=name,
                blueprint_app_id=agent_data.get("blueprint_app_id"),
            )
        return result


# Global config instance
_config: Optional[Config] = None


def get_config() -> Config:
    """Get the global config instance."""
    global _config
    if _config is None:
        _config = Config()
    return _config

