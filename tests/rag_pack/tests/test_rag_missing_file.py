import requests

def test_missing_file():
    res = requests.post("http://localhost:9006/chat", json={"prompt": "summarize /memory/missing.txt"})
    assert res.status_code == 200
    assert "not found" in res.json()["response"].lower()