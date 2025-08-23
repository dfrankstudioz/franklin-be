import requests

def test_list_dir_tool():
    response = requests.post("http://localhost:9006/chat", json={"prompt": "List the memory folder"})
    assert response.status_code == 200
    assert "You said" not in response.text  # This fails if fallback is echoing
