import os, json, requests, pytest, time
from pathlib import Path

BASE = os.environ.get("FRANKLIN_BASE", "http://localhost:9006")
MEM = Path.home() / "docker" / "memory"

def test_can_request_summary_of_newest_file_if_memory_present():
    if not MEM.exists():
        pytest.skip(f"memory directory not present at {MEM}")
    # This is a minimal scenario check to ensure NL prompt doesn't error hard.
    prompt = "Summarize the newest file in /memory"
    try:
        r = requests.post(f"{BASE}/chat", json={"prompt": prompt}, timeout=15)
    except Exception as e:
        pytest.skip(f"/chat not reachable: {e}")
    assert r.status_code == 200, f"Unexpected status {r.status_code}: {r.text}"
    data = r.json()
    assert "response" in data, f"No 'response' key returned: {data}"
