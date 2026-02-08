from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class ChatRequest:
    message: str
    session_id: str = "default_user"

@dataclass
class ChatResponse:
    response: str
    session_id: str
    context_state: Optional[str]
    intent: Optional[str] = None
    confidence: float = 0.0

@dataclass
class ErrorResponse:
    error: str
    details: Optional[str] = None

# For Flask (without pydantic extension), these serve as documentation 
# or can be used with `dataclasses.asdict` for serialization if manually handled.
