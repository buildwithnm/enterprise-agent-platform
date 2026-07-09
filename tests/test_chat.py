from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat():

    payload = {
        "question": "Hello",
        "persona": "general",
    }

    response = client.post(
        "/api/v1/chat",
        json=payload,
    )

    assert response.status_code == 200

    body = response.json()

    assert "answer" in body
    assert "execution_time_ms" in body
