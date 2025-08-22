import requests

BASE_URL = "http://ai-middleware:80"

def test_chat_endpoint_alive():
    """Basic health check on /chat endpoint"""
    resp = requests.post(f"{BASE_URL}/chat", json={"prompt": "ping"})
    assert resp.status_code == 200, f"/chat unhealthy: {resp.status_code} {resp.text}"

def test_ui_index_served():
    """Ensure Web UI is mounted and serving index.html"""
    resp = requests.get(f"{BASE_URL}/ui/index.html")
    assert resp.status_code == 200, f"/ui/index.html missing: {resp.status_code}"
    assert "<!DOCTYPE html>" in resp.text
