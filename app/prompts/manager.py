from langchain_core.prompts import ChatPromptTemplate

from app.prompts.personas import (
    GENERAL_SYSTEM_PROMPT,
    DATA_ENGINEER_SYSTEM_PROMPT,
)


class PromptManager:

    PROMPTS = {
        "general": GENERAL_SYSTEM_PROMPT,
        "data_engineer": DATA_ENGINEER_SYSTEM_PROMPT,
    }

    @classmethod
    def get_prompt(cls, persona: str):

        system_prompt = cls.PROMPTS.get(
            persona,
            GENERAL_SYSTEM_PROMPT,
        )

        return ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{question}"),
            ]
        )
