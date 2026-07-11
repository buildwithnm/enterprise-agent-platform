from fastapi import FastAPI
from app.api.routes import router
from app.config.settings import settings
from app.utils.exceptions import LLMException

from app.middleware.request_context import RequestContextMiddleware
from app.middleware.logging import LoggingMiddleware
from app.handlers.exception_handler import llm_exception_handler

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)

app.add_middleware(RequestContextMiddleware)
app.add_middleware(LoggingMiddleware)
app.add_exception_handler(LLMException, llm_exception_handler)
