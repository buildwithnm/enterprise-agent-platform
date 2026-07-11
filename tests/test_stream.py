import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_stream():

    async with AsyncClient(
        app=app,
        base_url="http://test",
    ) as client:

        async with client.stream(
            "POST",
            "/api/v1/chat/stream",
            json={
                "question": "Hello",
                "persona": "general",
            },
        ) as response:

            assert response.status_code == 200

            async for line in response.aiter_lines():
                assert line is not None
                break
