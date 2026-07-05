from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat():

    response = client.get("/api/v1/chat", params={"question": "Hello"})

    assert response.status_code == 200
