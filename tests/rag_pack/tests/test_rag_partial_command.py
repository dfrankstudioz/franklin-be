import requests

def test_partial_command():
    res = requests.post("http://localhost:9006/chat", json={"prompt": "summarize /memory"})
    assert res.status_code == 200
    assert "directory" in res.json()["response"].lower() or "invalid" in res.json()["response"].lower()