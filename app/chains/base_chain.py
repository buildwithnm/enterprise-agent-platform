from langchain_core.runnables import RunnableLambda

from app.parsers.text_parser import get_output_parser


class BaseChain:

    def __init__(self, llm):
        self.llm = llm

    def get_output_parser(self):
        return get_output_parser()

    def compose(self, runnable):

        parser = get_output_parser()

        return runnable | self.llm | parser
