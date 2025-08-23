import os
import requests

BASE = os.getenv("FRANKLIN_BASE_URL", "http://localhost:9006")

def test_chat_endpoint_basic():
    url = f"{BASE}/chat"
    resp = requests.post(url, json={"prompt": "hello"})
    assert resp.status_code == 200, f"Unexpected status: {resp.status_code}, body={resp.text}"
    data = resp.json()
    assert "response" in data, f"Missing 'response' key in: {data}"
    assert isinstance(data["response"], str)