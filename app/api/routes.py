from fastapi import APIRouter
from app.services.ollama_service import OllamaService
from app.config.settings import settings
import httpx

router = APIRouter()
service = OllamaService()


@router.get("/health")
def health():
    response = httpx.get(settings.OLLAMA_HOST)
    if response.status_code == 200 and "Ollama is running" in response.text:
        print("✅ Ollama is up, healthy, and accepting requests.")
        return {"status": "ok"}

    print("❌ Ollama is offline or unreachable.")
    return {"status": "server down"}


@router.get("/ask")
def ask(question: str):
    answer = service.ask(question)
    return {"question": question, "answer": answer}


@router.get("/models")
def models():
    model_name = settings.MODEL_NAME
    return {"Model": model_name}
