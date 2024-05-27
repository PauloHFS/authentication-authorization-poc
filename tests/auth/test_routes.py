from fastapi.testclient import TestClient

from src import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/auth/signup",
        data={
            "username": "test-user@gmail.com",
            "password": "test-password",
        })
    assert response.status_code == 200
