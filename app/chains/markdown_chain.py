from app.llm.provider import get_llm
from app.parsers.text_parser import get_output_parser
from app.prompts.markdown import MarkdownPromptManager


class MarkdownChain:

    @staticmethod
    def build(
        persona: str,
    ):

        prompt = MarkdownPromptManager.get_prompt(persona)

        llm = get_llm()

        parser = get_output_parser()

        return prompt | llm | parser
