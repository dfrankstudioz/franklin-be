import os, urllib.request

INSIDE = os.path.exists("/app")
BASE = "http://127.0.0.1:80" if INSIDE else "http://127.0.0.1:9006"

def _head(url, timeout=12):
    req = urllib.request.Request(url, method="HEAD")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status

def test_ui_root_served():
    assert _head(f"{BASE}/ui/") in (200, 301, 302, 304)

def test_ui_chat_fetch():
    data = b'{"prompt":"ping"}'
    req = urllib.request.Request(f"{BASE}/chat", data=data, headers={"Content-Type":"application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=25) as r:
        body = r.read().decode()
        assert '"response"' in body
