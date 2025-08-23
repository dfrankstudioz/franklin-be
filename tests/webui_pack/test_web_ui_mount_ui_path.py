import requests

def test_web_ui_mounted_on_ui_path():
    response = requests.get("http://localhost:9006/ui/")
    assert response.status_code == 200
    assert "html" in response.headers.get("content-type", "").lower()
