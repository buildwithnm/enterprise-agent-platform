from app.chains.base_chain import BaseChain
from app.prompts.manager import PromptManager


class ChatChain(BaseChain):

    def build(self, persona: str):

        prompt = PromptManager.get_prompt(persona)

        return self.compose(prompt)
