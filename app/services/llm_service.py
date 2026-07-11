import time
from datetime import datetime, timezone
from app.utils.exceptions import LLMException
from app.utils.sse import format_sse
from app.models.stream_response import StreamChunk
from app.config.settings import settings
from app.models.chat_response import ChatResponse

from loguru import logger


class LLMService:

    def __init__(self, chain):
        self.chain = chain

    async def ask(self, question: str, persona: str):
        try:
            start = time.perf_counter()

            runnable = self.chain.build(persona)

            print(runnable.input_schema.model_json_schema())

            payload = {"question": question}
            print(type(payload))
            print(payload)

            answer = await runnable.ainvoke(payload)

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

    async def ask_markdown(
        self,
        question: str,
        persona: str,
    ):

        start = time.perf_counter()

        runnable = self.chain.build(persona)

        answer = await runnable.ainvoke({"question": question})

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

    async def stream(self, question: str, persona: str):
        runnable = self.chain.build(persona)

        try:
            async for chunk in runnable.astream({"question": question}):
                yield format_sse(chunk)
                # yield f"data: {chunk}\n\n"
                StreamChunk(
                    token=str(chunk),
                    finished=False,
                ).model_dump_json()

            yield "event: end\ndata: [DONE]\n\n"

        except Exception as ex:
            yield format_sse(
                str(ex),
                event="error",
            )
