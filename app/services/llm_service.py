from app.llm.client import LLMClient
from app.utils.exceptions import LLMException


class LLMService:

    def __init__(self):

        self.client = LLMClient()

    def ask(self, question: str, persona: str):
        try:

            return self.client.invoke(question, persona)

        except Exception as ex:

            raise LLMException(str(ex))
