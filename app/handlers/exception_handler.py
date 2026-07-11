from fastapi import Request
from fastapi.responses import JSONResponse

from app.utils.exceptions import LLMException
from app.utils.request_context import request_id_ctx


async def llm_exception_handler(
    request: Request,
    exc: LLMException,
):

    return JSONResponse(
        status_code=500,
        content={
            "request_id": request_id_ctx.get(),
            "error": str(exc),
        },
    )