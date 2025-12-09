"""Data models for blueprints and agent identities."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BlueprintInfo:
    """Information about a stored blueprint."""
    
    app_id: str
    object_id: str
    principal_id: str
    client_secret: str
    display_name: str = ""


@dataclass
class AgentIdentityInfo:
    """Information about an agent identity."""
    
    id: str
    app_id: str
    display_name: str
    blueprint_app_id: Optional[str] = None


@dataclass
class TokenResult:
    """Result of a token acquisition."""
    
    access_token: str
    token_type: str = "Bearer"
    expires_in: int = 0
    
    def decoded_claims(self) -> dict:
        """Decode and return JWT claims (without verification)."""
        import base64
        import json
        
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

