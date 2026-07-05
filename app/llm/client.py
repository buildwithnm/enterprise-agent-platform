from app.llm.provider import get_llm


class LLMClient:

    def __init__(self):

        self.llm = get_llm()

    def invoke(self, question: str):

        response = self.llm.invoke(question)

        return response.content
