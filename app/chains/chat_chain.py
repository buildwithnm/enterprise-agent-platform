from app.llm.provider import get_llm
from app.parsers.text_parser import get_output_parser
from app.prompts.manager import PromptManager


class ChatChain:

    @staticmethod
    def build(persona: str):

        prompt = PromptManager.get_prompt(persona)

        llm = get_llm()

        parser = get_output_parser()

        return prompt | llm | parser
