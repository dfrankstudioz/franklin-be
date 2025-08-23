import os, json, urllib.request, pathlib

INSIDE = os.path.exists("/app")
BASE = "http://127.0.0.1:80" if INSIDE else "http://127.0.0.1:9006"
MEM = "/host-root/home/frank/docker/memory"
HOST = pathlib.Path.home() / "docker" / "memory"
HOST.mkdir(parents=True, exist_ok=True)
(HOST / "multi.txt").write_text("Franklin multi-intent test file.\n")

def _post(prompt, timeout=40):
    req = urllib.request.Request(f"{BASE}/chat",
        data=json.dumps({"prompt": prompt}).encode(),
        headers={"Content-Type":"application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode()

def test_multi_intent_list_then_read_then_summarize():
    prompt = f"list files in {MEM}; then read file {MEM}/multi.txt; then summarize file {MEM}/multi.txt"
    body = _post(prompt)
    low = body.lower()
    assert "multi.txt" in low and ("summary" in low or "summar" in low)
