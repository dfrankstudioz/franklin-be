import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

import requests

def test_natural_prompt_to_read_file():
    url = "http://localhost:9006/chat"
    payload = {"prompt": "read /memory/test.txt"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    assert "read_file" in response.text, "Expected routing to read_file(...)"
    assert "/memory/test.txt" in response.text, "Expected correct file path in response"
