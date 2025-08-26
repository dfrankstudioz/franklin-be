import requests, os

def test_openai_down(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "invalid_key")
    res = requests.post("http://localhost:9006/chat", json={"prompt": "summarize /memory/example.txt"})
    assert res.status_code == 200
    "summary" in res.json()["response"].lower()