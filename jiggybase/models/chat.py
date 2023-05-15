"""
Config for chat-related functionality
"""

from pydantic import BaseModel, Field
from .chatmodel import ChatModelName
from typing import Optional


class CollectionChatConfig(BaseModel):
    """Config for Collection chat-related functionality"""    
    model_name          : str           = Field(description="The model associated with this configuration")
    rate_limit_messages : int           = Field(description="The total number of messages allowed in the rate limit time period across all collection users")
    rate_limit_hours    : int           = Field(description="The number of hours in the rate limit time period")
    prompt_task_id      : Optional[int] = Field(description="The prompt task id of the prompt to use for chat with this collection")


class PatchCollectionChatConfig(BaseModel):
    """Config for Collection chat-related functionality"""    
    prompt_task_id      : Optional[int] = Field(description="The prompt task id of the prompt to use for chat with this collection")




## Chat Completion Request objects sent to the chat completion endpoint

class Message(BaseModel):
    role: str
    content: str
    
class CompletionRequest(BaseModel):
    model: str
    messages: list[Message]
    max_tokens: Optional[int] = None
    temperature: float
    stream: bool


# Response returned from JiggyBase Chat Completion api endpoint
# While the inputs to our chat completion api are similar to OpenAI, the output response model is quite different:

class ChatCompletion(BaseModel):
    collection_id:   int           = Field(description="The collection ID used to inform the completion")
    model:           str           = Field(description="The name of the model used to generate the completion")
    user_message:    str           = Field(description="The user's input message")
    input_tokens:    int           = Field(description="The number of input tokens sent to the model")
    output_tokens:   int           = Field(description="The number of output tokens generated by the model")
    messages_json:   Optional[str] = Field(description="JSON representation of the input messages sent to model endpoint")    
    completion:      Optional[str] = Field(description="The completion text returned by the model")
    created_at:      float         = Field(description="The epoch timestamp associated with the completion.")
    
    def __str__(self):
        return self.completion