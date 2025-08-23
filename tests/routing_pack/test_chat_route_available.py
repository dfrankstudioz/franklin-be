import os, json, requests, pytest

BASE = os.environ.get("FRANKLIN_BASE", "http://localhost:9006")

def test_chat_route_accepts_prompt_and_returns_response():
    try:
        r = requests.post(f"{BASE}/chat", json={"prompt": "ping"} , timeout=5)
    except Exception as e:
        pytest.skip(f"/chat not reachable: {e}")
    assert r.status_code == 200, f"Unexpected status {r.status_code}: {r.text}"
    data = r.json()
    assert isinstance(data, dict) and "response" in data, f"Bad payload: {data}"
