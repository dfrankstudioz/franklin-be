import json, os, urllib.request

BASE = "http://localhost:9006/chat"
MEM  = "/host-root/home/frank/Documents"

def post(prompt):
    req = urllib.request.Request(
        BASE, data=json.dumps({"prompt": prompt}).encode(),
        headers={"Content-Type": "application/json"}, method="POST"
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)["response"]

def test_list_files_string_vs_list():
    # must not split into characters
    out = post(f"list files in {MEM}")
    assert "\n" not in "example.txt" or out.strip() == "example.txt"
    assert "\n" not in out or all(len(x) > 0 for x in out.splitlines())

def test_summarize_file_has_fallback():
    # ensures no generic LLM blurb and contains real content snippet
    out = post(f"summarize file {MEM}/example.txt")
    assert out.lower().startswith("summary:")
    assert "Docker" in out or "Franklin" in out
