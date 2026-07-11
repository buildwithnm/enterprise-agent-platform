from app.chains.base_chain import BaseChain
from app.prompts.markdown import MarkdownPromptManager


class MarkdownChain(BaseChain):

    def build(self, persona):

        prompt = MarkdownPromptManager.get_prompt(persona)

        return self.compose(prompt)
