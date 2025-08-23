import requests

def test_read_file_tool():
    response = requests.post("http://localhost:9006/chat", json={"prompt": "Read file example.txt"})
    assert response.status_code == 200
    assert "You said" not in response.text  # Detects if fallback echo is returned
