from app.llm.provider import get_llm
from app.chains.chat_chain import ChatChain
from app.chains.markdown_chain import MarkdownChain


class LLMClient:

    def invoke(self, question: str, persona: str):
        chain = ChatChain.build(persona=persona)

        return chain.invoke({"question": question})

    def invoke_markdown(
        self,
        question: str,
        persona: str,
    ):
        chain = MarkdownChain.build(persona)

        return chain.invoke({"question": question})
