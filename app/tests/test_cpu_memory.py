from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_lscpu():
    response = client.get("/api/cpu/lscpu")
    assert response.status_code == 200
    assert (
        "CPU" in response.json()["output"]
        or "Architecture" in response.json()["output"]
    )
