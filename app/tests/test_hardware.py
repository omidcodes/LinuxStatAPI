from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_lshw():
    response = client.get("/api/hardware/lshw")
    assert response.status_code == 200
    assert "hardware" in response.json()["output"].lower() or "description" in response.json()["output"].lower()