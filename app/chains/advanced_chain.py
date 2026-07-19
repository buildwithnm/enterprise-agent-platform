from langchain_core.runnables import RunnableLambda

from app.chains.base_chain import BaseChain
from app.prompts.manager import PromptManager

class AdvancedChain(BaseChain):

    def clean_question(self):

        return RunnableLambda(
            lambda x: {
                "question": x["question"].strip()
            }
        )

    def build(self, persona: str):

        prompt = PromptManager.get_prompt(persona)

        return (
            self.clean_question()
            | prompt
            | self.llm
            | self.get_output_parser()
        )