from fastapi.testclient import TestClient

from src import app

client = TestClient(app)


def test_create_user():

    request_data = {
        "username": "test@gmail.com",
        "password": "test",
    }

    response = client.post(
        "/auth/signup",
        json=request_data)

    assert response.status_code == 200
    response_data = response.json()

    assert response_data["username"] == request_data["username"]
    assert "id" in response_data
