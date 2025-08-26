import requests

def test_ui_index_served():
    """Ensure FastAPI root path is mounted and returning health check"""
    resp = requests.get("http://localhost:9006/")
    assert resp.status_code == 200
    assert resp.json().get("status") == "ok"
