from fastapi import APIRouter

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
def chat(request: ChatRequest):

    logger.bind(request_id=request_id_ctx.get()).info("Question received",)
    logger.info(request.question)

    answer = container.service.ask(request.question, request.persona.value)

    logger.info("Response generated")

    # return {
    #     "persona": persona,
    #     "question": question,
    #     "answer": answer,
    # }

    return answer


@router.post(
    "/chat/markdown",
    response_model=ChatResponse,
)
def markdown_chat(
    request: ChatRequest,
):

    return container.service.ask_markdown(
        question=request.question,
        persona=request.persona.value,
    )
