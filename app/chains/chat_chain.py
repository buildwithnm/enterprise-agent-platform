from app.chains.base_chain import BaseChain
from app.prompts.manager import PromptManager


class ChatChain(BaseChain):

    def __init__( self, llm, question_processor,):
        super().__init__(llm)
        self.question_processor = question_processor

    def build( self, persona: str,):

        prompt = PromptManager.get_prompt(persona)

        processing_pipeline = (
            self.question_processor.build()
        )

        chat_pipeline = (
            processing_pipeline
            | prompt
        )

        return self.compose(
            chat_pipeline
        )

        return self.compose(pipeline)