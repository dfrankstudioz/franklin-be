import os, json, urllib.request, socket

def _post(url, payload, timeout=10, no_proxy=True):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({})) if no_proxy else urllib.request.build_opener()
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type":"application/json"}, method="POST")
    with opener.open(req, timeout=timeout) as r:
        return r.status, r.read().decode()

def _port_open(host, port, timeout=2):
    try:
        socket.create_connection((host, port), timeout=timeout).close()
        return True
    except Exception:
        return False

def test_api_inside_container_or_skip():
    if not os.path.exists("/app"):
        import pytest; pytest.skip("not inside container")
    assert _port_open("127.0.0.1", 80), "container port 80 closed"
    code, body = _post("http://127.0.0.1:80/chat", {"prompt":"hello"})
    assert code == 200 and '"response"' in body

def test_api_from_host_mapping_or_skip():
    if os.path.exists("/app"):
        import pytest; pytest.skip("running inside container")
    assert _port_open("127.0.0.1", 9006), "host port 9006 closed"
    code, body = _post("http://127.0.0.1:9006/chat", {"prompt":"hello"})
    assert code == 200 and '"response"' in body
