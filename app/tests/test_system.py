from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_uname():
    response = client.get("/api/system/uname")
    assert response.status_code == 200
    assert "Linux" in response.json()["output"]
