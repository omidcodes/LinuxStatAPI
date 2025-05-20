from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_syslog():
    response = client.get("/api/logs/syslog")
    assert response.status_code == 200
    assert len(response.json()["output"]) > 0
