import pytest
import requests

@pytest.mark.skip(reason="Natural prompt routing is stubbed in public build")
def test_natural_prompt_to_read_file():
    url = "http://localhost:9006/chat"
    payload = {"prompt": "read /memory/test.txt"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    assert "stubbed file content" in response.text.lower(), "Expected routing to read_file(...)"
