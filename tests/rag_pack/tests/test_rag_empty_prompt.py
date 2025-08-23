import requests

def test_empty_prompt():
    res = requests.post("http://localhost:9006/chat", json={"prompt": ""})
    assert res.status_code == 200
    assert "empty" in res.json()["response"].lower() or "invalid" in res.json()["response"].lower()