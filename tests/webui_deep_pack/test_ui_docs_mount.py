
import requests

def test_docs_route_mount():
    res = requests.get("http://localhost:9006/docs")
    assert res.status_code == 200, "/docs not reachable"
    assert "Swagger UI" in res.text or "<title>Swagger UI</title>" in res.text, "Docs UI not served properly"
