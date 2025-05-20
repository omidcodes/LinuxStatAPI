from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_df():
    response = client.get("/api/disk/df")
    assert response.status_code == 200
    assert "Filesystem" in response.json()["output"]
