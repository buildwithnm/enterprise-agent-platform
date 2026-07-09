from app.llm.provider import get_llm
from app.prompts.manager import PromptManager


class LLMClient:

    def __init__(self):

        self.llm = get_llm()

    def invoke(self, question: str, persona: str):

        prompt = PromptManager.get_prompt(persona)
        chain = prompt | self.llm
        response = chain.invoke({"question": question})

        return response.content
