from app.llm.provider import get_llm
from app.services.llm_service import LLMService
from app.chains.chat_chain import ChatChain
from app.prompts.manager import PromptManager


class AppContainer:

    def __init__(self):

        self.llm = get_llm()

        self.prompt_manager = PromptManager()

        self.chat_chain = ChatChain(self.llm)

        self.service = LLMService(self.chat_chain)


container = AppContainer()
