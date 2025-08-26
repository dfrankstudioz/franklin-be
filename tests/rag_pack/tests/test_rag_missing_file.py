import requests
import os

def test_missing_file():
    path = "/memory/surely_does_not_exist_abc123.txt"
    assert not os.path.exists(path), f"Test file unexpectedly exists: {path}"

    res = requests.post("http://localhost:9006/chat", json={"prompt": f"summarize {path}"})
    assert res.status_code == 200
    assert "no such file" in res.json()["response"].lower()
