from langchain_core.prompts import ChatPromptTemplate

from app.prompts.personas import (
    GENERAL_SYSTEM_PROMPT,
    DATA_ENGINEER_SYSTEM_PROMPT,
)


class MarkdownPromptManager:

    PROMPTS = {
        "general": GENERAL_SYSTEM_PROMPT,
        "data_engineer": DATA_ENGINEER_SYSTEM_PROMPT,
    }

    @classmethod
    def get_prompt(
        cls,
        persona: str = "general",
    ):

        system_prompt = cls.PROMPTS.get(
            persona,
            GENERAL_SYSTEM_PROMPT,
        )

        system_prompt += """
        Always answer using Markdown.

        Requirements

        - Use headings
        - Use bullet points
        - Use code blocks when needed
        - Use tables when appropriate
        - Never return plain text.
        """

        return ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{question}"),
            ]
        )
