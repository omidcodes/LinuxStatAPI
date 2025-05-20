from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_ip():
    response = client.get("/api/network/ip")
    assert response.status_code == 200
    assert "inet" in response.json()["output"]
