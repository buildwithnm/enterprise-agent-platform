import time

from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.request_context import request_id_ctx

class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start = time.perf_counter()

        response = await call_next(request)

        elapsed = int((time.perf_counter() - start) * 1000)

        logger.info(
            {
                "request_id": request_id_ctx.get(),
                "method": request.method,
                "path": request.url.path,
                "status": response.status_code,
                "latency_ms": elapsed,
                "client_ip": request.client.host,
                "user_agent": response.headers["User-Agent"],
                "response_size": len(response.body)

            }
        )

        return response