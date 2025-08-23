import requests

def test_ui_route_mount():
    res = requests.get("http://localhost:9006/ui/")
    assert res.status_code == 200, f"Expected 200 OK, got {res.status_code}"
    assert "<!DOCTYPE html>" in res.text or "<html" in res.text.lower(), "UI route did not return HTML content"