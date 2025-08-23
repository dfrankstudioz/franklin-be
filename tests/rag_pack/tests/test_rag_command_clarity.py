import requests

def test_command_clarity():
    res = requests.post("http://localhost:9006/chat", json={"prompt": "can you summarize the file called example.txt"})
    assert res.status_code == 200
    assert "summary" in res.json()["response"].lower() or "summarize" in res.json()["response"].lower()