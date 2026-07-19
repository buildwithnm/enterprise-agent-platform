from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.container.container import container
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.config.settings import settings

from app.utils.request_context import request_id_ctx

from loguru import logger

router = APIRouter(prefix="/api/v1")


@router.get("/health")
def health():

    return {
        "status": "UP",
        "application": settings.APP_NAME,
        "provider": settings.PROVIDER,
        "model": settings.MODEL_NAME,
    }


@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest):

    logger.bind(request_id=request_id_ctx.get()).info(
        "Question received",
    )
    logger.info(request.question)

    answer = await container.service.ask(request.question, request.persona.value)

    logger.info("Response generated")

    return answer


@router.post(
    "/chat/markdown",
    response_model=ChatResponse,
)
async def markdown_chat(
    request: ChatRequest,
):

    return await container.service.ask_markdown(
        question=request.question,
        persona=request.persona.value,
    )


@router.post("/chat/stream")
async def stream_chat(request: ChatRequest):

    generator = container.service.stream(
        question=request.question,
        persona=request.persona.value,
    )

    return StreamingResponse(
        generator,
        media_type="text/event-stream",
    )