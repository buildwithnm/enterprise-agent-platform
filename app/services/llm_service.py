import time
from datetime import datetime, timezone
from app.llm.client import LLMClient
from app.utils.exceptions import LLMException
from app.config.settings import settings
from app.models.chat_response import ChatResponse
from loguru import logger


class LLMService:

    def __init__(self):

        self.client = LLMClient()

    def ask(self, question: str, persona: str):
        try:
            start = time.perf_counter()

            answer = self.client.invoke(question, persona)

            elapsed = int((time.perf_counter() - start) * 1000)

            logger.info(
                "LLM response generated",
                extra={
                    "latency_ms": elapsed,
                    "model": settings.MODEL_NAME,
                    "persona": persona,
                },
            )

            return ChatResponse(
                question=question,
                persona=persona,
                answer=str(answer),
                model=settings.MODEL_NAME,
                execution_time_ms=elapsed,
                provider=settings.PROVIDER,
                timestamp=datetime.now(timezone.utc),
            )

        except Exception as ex:

            raise LLMException(str(ex))

    def ask_markdown(
        self,
        question: str,
        persona: str,
    ):

        start = time.perf_counter()
        answer = self.client.invoke_markdown(
            question,
            persona,
        )
        elapsed = int((time.perf_counter() - start) * 1000)
        return ChatResponse(
            question=question,
            persona=persona,
            answer=str(answer),
            model=settings.MODEL_NAME,
            execution_time_ms=elapsed,
            provider=settings.PROVIDER,
            timestamp=datetime.now(timezone.utc),
        )
