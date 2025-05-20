from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_ps():
    response = client.get("/api/processes/ps")
    assert response.status_code == 200
    assert "PID" in response.json()["output"]
