"""Data models for the AI Agent CLI."""

import base64
import json
from dataclasses import dataclass, field
from typing import Optional, Any


@dataclass
class TokenResult:
    """Result of a token acquisition."""
    
    access_token: str
    token_type: str = "Bearer"
    expires_in: int = 0
    
    def decoded_claims(self) -> dict:
        """Decode and return JWT claims (without verification)."""
        # Split the JWT
        parts = self.access_token.split(".")
        if len(parts) != 3:
            return {}
        
        # Decode the payload (middle part)
        payload = parts[1]
        # Add padding if needed
        padding = 4 - len(payload) % 4
        if padding != 4:
            payload += "=" * padding
        
        try:
            decoded = base64.urlsafe_b64decode(payload)
            return json.loads(decoded)
        except Exception:
            return {}


@dataclass
class MCPServer:
    """Configuration for an MCP server."""
    
    name: str
    url: str
    enabled: bool = True
    
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "url": self.url,
            "enabled": self.enabled,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "MCPServer":
        """Create from dictionary."""
        return cls(
            name=data["name"],
            url=data["url"],
            enabled=data.get("enabled", True),
        )


@dataclass
class MCPTool:
    """Represents a tool from an MCP server."""
    
    name: str
    description: str
    input_schema: dict
    server_name: str
    
    def to_openai_tool(self) -> dict:
        """Convert to OpenAI tool format."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.input_schema,
            }
        }


@dataclass
class ChatMessage:
    """A message in the conversation history."""
    
    role: str  # "system", "user", "assistant", "tool"
    content: Optional[str] = None
    tool_calls: Optional[list[dict]] = None
    tool_call_id: Optional[str] = None
    name: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary for OpenAI API."""
        msg = {"role": self.role}
        
        if self.content is not None:
            msg["content"] = self.content
        
        if self.tool_calls is not None:
            msg["tool_calls"] = self.tool_calls
        
        if self.tool_call_id is not None:
            msg["tool_call_id"] = self.tool_call_id
        
        if self.name is not None:
            msg["name"] = self.name
        
        return msg

