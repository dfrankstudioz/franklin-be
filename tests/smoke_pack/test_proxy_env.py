import os, json, urllib.request, pytest

@pytest.mark.skipif(not os.path.exists("/app"), reason="only meaningful inside container")
def test_proxies_not_set_or_ignored():
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    req = urllib.request.Request("http://127.0.0.1:80/chat",
        data=json.dumps({"prompt":"hello"}).encode(),
        headers={"Content-Type":"application/json"}, method="POST")
    with opener.open(req, timeout=10) as r:
        assert r.status == 200
