import requests

def test_web_ui_mount():
    r = requests.get("http://localhost:9006/ui")
    assert r.status_code == 200
    assert "<html" in r.text.lower() or "Franklin UI" in r.text
