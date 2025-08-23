
import requests

def test_ui_route_mount():
    res = requests.get("http://localhost:9006/ui/")
    assert res.status_code == 200, "/ui/ path not mounted or unreachable"
    assert "<!DOCTYPE html>" in res.text or "<html" in res.text.lower(), "No HTML returned from /ui/"
