import requests

def test_ui_index_served():
    resp = requests.get("http://localhost:9006/")
    assert resp.status_code == 200
    assert resp.json().get("message") == "Franklin Core is live."
