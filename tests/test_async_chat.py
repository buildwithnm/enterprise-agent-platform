import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_chat():

    async with AsyncClient(
        app=app,
        base_url="http://test",
    ) as client:

        response = await client.post(
            "/api/v1/chat",
            json={
                "question": "Hello",
                "persona": "general",
            },
        )

    assert response.status_code == 200