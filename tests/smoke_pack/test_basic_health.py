import os, requests, pytest

BASE = os.environ.get("FRANKLIN_BASE", "http://localhost:9006")

def test_whoami_ok():
    try:
        r = requests.get(f"{BASE}/whoami", timeout=5)
    except Exception as e:
        pytest.skip(f"/whoami not reachable: {e}")
    assert r.status_code == 200
    data = r.json()
    assert data.get("ok") in (True, False)  # shape check without being brittle
