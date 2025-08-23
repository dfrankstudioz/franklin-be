import requests
import json

UI_BASE_URL = "http://localhost:9006/ui"
API_BASE_URL = "http://localhost:9006"

def test_ui_root():
    url = f"{UI_BASE_URL}/"
    resp = requests.get(url)
    print(f"UI root {url} status:", resp.status_code)
    assert resp.status_code == 200
    assert "<html" in resp.text.lower()

def test_chat_endpoint():
    url = f"{API_BASE_URL}/chat"
    payload = {"prompt": "test list /memory"}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"/chat POST {url} status:", resp.status_code)
    print("Response:", resp.json())
    assert resp.status_code == 200
    assert "tool" in resp.json()

if __name__ == "__main__":
    test_ui_root()
    test_chat_endpoint()
    print("All tests passed.")
