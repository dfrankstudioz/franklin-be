import os, json, urllib.request, pathlib

HOST_PATH = pathlib.Path.home() / "docker" / "memory"
HOST_PATH.mkdir(parents=True, exist_ok=True)
(HOST_PATH / "example.txt").write_text("Docker is a platform for running containers.\n")

INSIDE = os.path.exists("/app")
BASE = "http://127.0.0.1:80" if INSIDE else "http://127.0.0.1:9006"
MEM = "/host-root/home/frank/docker/memory"

def _post(prompt):
    req = urllib.request.Request(f"{BASE}/chat",
        data=json.dumps({"prompt": prompt}).encode(),
        headers={"Content-Type":"application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode()

def test_list_dir_returns_example_txt():
    body = _post(f"list files in {MEM}")
    assert "example.txt" in body.lower(), f"list_dir missing example.txt. Body: {body[:200]}"

def test_read_file_returns_content():
    body = _post(f"read file {MEM}/example.txt")
    assert "platform for running containers" in body.lower(), f"read_file did not read real content. Body: {body[:200]}"

def test_summarize_file_mentions_docker():
    body = _post(f"summarize file {MEM}/example.txt")
    assert "docker" in body.lower(), f"summarize_file seems generic/LLM-only. Body: {body[:200]}"
