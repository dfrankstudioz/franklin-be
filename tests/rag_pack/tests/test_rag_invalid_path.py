import requests

def test_invalid_path():
    res = requests.post("http://localhost:9006/chat", json={"prompt": "read file /notreal/path.txt"})
    assert res.status_code == 200
    assert "no such file" in res.json()["response"].lower()
