import requests

def test_summarize_file_tool():
    response = requests.post("http://localhost:9006/chat", json={"prompt": "Summarize example.txt"})
    assert response.status_code == 200
    assert "summary" in response.text.lower()
