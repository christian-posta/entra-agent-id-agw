"""Azure OpenAI agent with tool calling support."""

import json
from typing import Optional, Generator

from openai import AzureOpenAI
from azure.identity import get_bearer_token_provider, DefaultAzureCredential
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from .models import ChatMessage, TokenResult
from .mcp_client import MCPManager


console = Console()


class Agent:
    """Interactive AI agent using Azure OpenAI with MCP tool support."""
    
    SYSTEM_PROMPT = """You are a helpful AI assistant. You can use tools when they are available to help answer questions and perform tasks.

When using tools:
- Call tools when they would help answer the user's question
- Explain what you're doing when calling tools
- Present tool results clearly to the user

Be concise but thorough in your responses."""
    
    def __init__(
        self,
        endpoint: str,
        deployment: str,
        api_version: str = "2024-02-15-preview",
        api_key: Optional[str] = None,
        token: Optional[TokenResult] = None,
        mcp_manager: Optional[MCPManager] = None,
    ):
        """Initialize the agent.
        
        Args:
            endpoint: Azure OpenAI endpoint URL
            deployment: Deployment name
            api_version: API version
            api_key: API key (for API key auth mode)
            token: Token result (for Entra auth mode)
            mcp_manager: MCP manager for tool access
        """
        self.endpoint = endpoint
        self.deployment = deployment
        self.api_version = api_version
        self.mcp_manager = mcp_manager or MCPManager()
        self._conversation: list[ChatMessage] = []
        
        # Initialize OpenAI client
        if api_key:
            self._client = AzureOpenAI(
                azure_endpoint=endpoint,
                api_key=api_key,
                api_version=api_version,
            )
        elif token:
            # Use token-based auth with a custom token provider
            self._client = AzureOpenAI(
                azure_endpoint=endpoint,
                azure_ad_token=token.access_token,
                api_version=api_version,
            )
        else:
            # Use DefaultAzureCredential (will use cached Entra token)
            credential = DefaultAzureCredential()
            token_provider = get_bearer_token_provider(
                credential,
                "https://cognitiveservices.azure.com/.default"
            )
            self._client = AzureOpenAI(
                azure_endpoint=endpoint,
                azure_ad_token_provider=token_provider,
                api_version=api_version,
            )
        
        # Add system message
        self._conversation.append(ChatMessage(
            role="system",
            content=self.SYSTEM_PROMPT
        ))
    
    def set_mcp_manager(self, manager: MCPManager) -> None:
        """Set the MCP manager for tool access.
        
        Args:
            manager: MCP manager instance
        """
        self.mcp_manager = manager
    
    def clear_history(self) -> None:
        """Clear conversation history (keeps system prompt)."""
        self._conversation = [self._conversation[0]]
    
    def chat(self, user_message: str) -> str:
        """Send a message and get a response.
        
        This handles the full tool-calling loop if needed.
        
        Args:
            user_message: User's message
            
        Returns:
            Assistant's response
        """
        # Add user message to conversation
        self._conversation.append(ChatMessage(role="user", content=user_message))
        
        # Get available tools
        tools = self.mcp_manager.get_openai_tools() if self.mcp_manager else []
        
        while True:
            # Prepare messages for API
            messages = [msg.to_dict() for msg in self._conversation]
            
            # Call Azure OpenAI
            try:
                if tools:
                    response = self._client.chat.completions.create(
                        model=self.deployment,
                        messages=messages,
                        tools=tools,
                        tool_choice="auto",
                    )
                else:
                    response = self._client.chat.completions.create(
                        model=self.deployment,
                        messages=messages,
                    )
            except Exception as e:
                error_msg = f"Error calling Azure OpenAI: {e}"
                console.print(f"[red]{error_msg}[/red]")
                return error_msg
            
            # Get the assistant's response
            assistant_message = response.choices[0].message
            
            # Check if the assistant wants to call tools
            if assistant_message.tool_calls:
                # Add assistant message with tool calls
                self._conversation.append(ChatMessage(
                    role="assistant",
                    content=assistant_message.content,
                    tool_calls=[
                        {
                            "id": tc.id,
                            "type": "function",
                            "function": {
                                "name": tc.function.name,
                                "arguments": tc.function.arguments
                            }
                        }
                        for tc in assistant_message.tool_calls
                    ]
                ))
                
                # Execute each tool call
                for tool_call in assistant_message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)
                    
                    console.print(f"[dim]Calling tool: {tool_name}[/dim]")
                    
                    # Call the tool
                    result = self.mcp_manager.call_tool(tool_name, tool_args)
                    
                    if result is None:
                        result = "Tool execution failed"
                    elif not isinstance(result, str):
                        result = json.dumps(result, indent=2)
                    
                    # Add tool result to conversation
                    self._conversation.append(ChatMessage(
                        role="tool",
                        content=result,
                        tool_call_id=tool_call.id,
                        name=tool_name
                    ))
                
                # Continue the loop to get the final response
                continue
            
            # No tool calls - we have the final response
            content = assistant_message.content or ""
            
            # Add to conversation
            self._conversation.append(ChatMessage(role="assistant", content=content))
            
            return content
    
    def chat_stream(self, user_message: str) -> Generator[str, None, None]:
        """Send a message and stream the response.
        
        Note: Streaming doesn't support tool calls in this simplified version.
        For tool calls, use chat() instead.
        
        Args:
            user_message: User's message
            
        Yields:
            Chunks of the response as they arrive
        """
        # Add user message
        self._conversation.append(ChatMessage(role="user", content=user_message))
        
        messages = [msg.to_dict() for msg in self._conversation]
        
        try:
            response = self._client.chat.completions.create(
                model=self.deployment,
                messages=messages,
                stream=True,
            )
            
            full_response = ""
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    yield content
            
            # Add to conversation
            self._conversation.append(ChatMessage(role="assistant", content=full_response))
            
        except Exception as e:
            error_msg = f"Error: {e}"
            yield error_msg


def create_agent_with_entra_token(
    endpoint: str,
    deployment: str,
    token: TokenResult,
    api_version: str = "2024-02-15-preview",
    mcp_manager: Optional[MCPManager] = None,
) -> Agent:
    """Create an agent using Entra ID token authentication.
    
    Args:
        endpoint: Azure OpenAI endpoint
        deployment: Deployment name
        token: Entra token result
        api_version: API version
        mcp_manager: Optional MCP manager
        
    Returns:
        Configured Agent instance
    """
    return Agent(
        endpoint=endpoint,
        deployment=deployment,
        api_version=api_version,
        token=token,
        mcp_manager=mcp_manager,
    )


def create_agent_with_api_key(
    endpoint: str,
    deployment: str,
    api_key: str,
    api_version: str = "2024-02-15-preview",
    mcp_manager: Optional[MCPManager] = None,
) -> Agent:
    """Create an agent using API key authentication.
    
    Args:
        endpoint: Azure OpenAI endpoint
        deployment: Deployment name
        api_key: Azure OpenAI API key
        api_version: API version
        mcp_manager: Optional MCP manager
        
    Returns:
        Configured Agent instance
    """
    return Agent(
        endpoint=endpoint,
        deployment=deployment,
        api_version=api_version,
        api_key=api_key,
        mcp_manager=mcp_manager,
    )

