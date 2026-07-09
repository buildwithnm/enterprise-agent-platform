from pydantic import BaseModel
from datetime import datetime
class ChatResponse(BaseModel):
    question: str
    persona: str
    answer: str
    model: str
    execution_time_ms: int
    provider: str
    timestamp: datetime
