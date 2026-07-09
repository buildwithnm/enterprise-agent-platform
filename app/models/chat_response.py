from pydantic import BaseModel


class ChatResponse(BaseModel):
    question: str
    persona: str
    answer: str
    model: str
    execution_time_ms: int
