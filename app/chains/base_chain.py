from app.parsers.text_parser import get_output_parser


class BaseChain:

    def __init__(self, llm):

        self.llm = llm

    def compose(self, prompt):

        parser = get_output_parser()

        return prompt | self.llm | parser