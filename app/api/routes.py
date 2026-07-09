from fastapi import APIRouter

from app.services.llm_service import LLMService
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse

from loguru import logger

router = APIRouter(prefix="/api/v1")

service = LLMService()


@router.get("/health")
def health():

    return {"status": "UP"}


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    logger.info("Question received")

    logger.info(request.question)

    answer = service.ask(request.question, request.persona)

    logger.info("Response generated")

    # return {
    #     "persona": persona,
    #     "question": question,
    #     "answer": answer,
    # }

    return answer
