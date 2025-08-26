import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
import sys
sys.path.insert(0, "/app")
import requests

def test_fallback_to_chat():
    url = "http://localhost:9006/chat"
    payload = {"prompt": "whats for dinner"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200

    result = response.json()
    assert "response" in result
    assert "couldn't understand" in result["response"].lower()
