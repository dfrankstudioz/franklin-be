import requests

def test_chat_api_responds():
    url = "http://localhost:9006/chat"
    payload = {"prompt": "ping"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    
    assert response.status_code == 200
    assert "response" in response.json()
