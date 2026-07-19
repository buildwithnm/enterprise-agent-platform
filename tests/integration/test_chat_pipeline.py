import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_chat_pipeline():

    async with AsyncClient(
        app=app,
        base_url="http://test",
    ) as client:

        response = await client.post(
            "/api/v1/chat",
            json={
                "question":
                "   Explain      Kafka   ",
                "persona":
                "general",
            },
        )

        assert response.status_code == 200

        body = response.json()

        assert body["question"] == \
            "Explain Kafka"