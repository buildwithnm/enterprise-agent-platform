import re
from loguru import logger

from langchain_core.runnables import RunnableLambda

from app.processors.base_processor import BaseProcessor


class QuestionProcessor(BaseProcessor):
    """
    Responsible for preprocessing user questions before
    they reach the prompt template.

    Every transformation should preserve the payload
    structure to keep the LCEL pipeline composable.
    """

    def build(self) -> RunnableLambda:
        return RunnableLambda( self.normalize() | self.validate())
    
    def normalize(self): 
        return RunnableLambda( self._normalize_payload)
    
    def _normalize_payload( self, payload,):
        payload["question"] = re.sub( r"\s+", " ", payload["question"] ).strip()
        logger.debug("Normalized question: {}",payload["question"])
        return payload
    

    def validate(self): 
        return RunnableLambda( self._validate)
    

    def _validate( self, payload, ):
        question = payload["question"]
        if not question:
            raise ValueError(
                "Question cannot be empty."
                )

        return payload
