import requests

def test_favicon_exists():
    resp = requests.get("http://localhost:9006/favicon.ico")
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] in ["image/x-icon", "image/vnd.microsoft.icon"]
