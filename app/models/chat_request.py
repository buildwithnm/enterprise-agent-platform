from pydantic import BaseModel

from app.models.persona import Persona


class ChatRequest(BaseModel):
    question: str
    persona: Persona = Persona.GENERAL
