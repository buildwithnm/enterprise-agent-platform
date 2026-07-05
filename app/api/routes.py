from fastapi import APIRouter

from app.services.llm_service import LLMService

from loguru import logger

router = APIRouter(prefix="/api/v1")

service = LLMService()


@router.get("/health")
def health():

    return {"status": "UP"}


@router.get("/chat")
def chat(question: str):

    logger.info("Question received")

    logger.info(question)

    answer = service.ask(question)

    logger.info("Response generated")

    return {"answer": answer}
