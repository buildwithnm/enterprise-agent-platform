from typing import TypedDict


class AgentState(TypedDict):
    question: str
    persona: str
    answer: str
