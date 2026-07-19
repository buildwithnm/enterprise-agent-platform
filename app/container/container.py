from app.llm.provider import get_llm
from app.services.llm_service import LLMService
from app.chains.chat_chain import ChatChain
from app.chains.advanced_chain import AdvancedChain
from app.prompts.manager import PromptManager
from app.processors.question_processor import (QuestionProcessor,)


class AppContainer:

    def __init__(self):

        self.llm = get_llm()

        self.prompt_manager = PromptManager()

        self.question_processor = QuestionProcessor()

        self.chat_chain = ChatChain(
            llm=self.llm,
            question_processor=self.question_processor,
            )

        self.advanced_chain = AdvancedChain(self.llm)

        self.service = LLMService(self.chat_chain)


container = AppContainer()
