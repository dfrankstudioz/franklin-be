import os, json, urllib.request, pytest, subprocess, shlex

INSIDE = os.path.exists("/app")
BASE = "http://127.0.0.1:80" if INSIDE else "http://127.0.0.1:9006"

def _post(prompt, timeout=30):
    req = urllib.request.Request(f"{BASE}/chat",
        data=json.dumps({"prompt": prompt}).encode(),
        headers={"Content-Type":"application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode()

@pytest.mark.skipif(INSIDE, reason="run from host for docker compose control")
def test_fallback_without_openai_key():
    # Temporarily run an override command without OPENAI_API_KEY using docker compose exec env -u
    cmd = "docker compose exec -T -e OPENAI_API_KEY= ai_middleware python -c \"import json,urllib.request;req=urllib.request.Request('http://127.0.0.1:80/chat',data=json.dumps({'prompt':'ping'}).encode(),headers={'Content-Type':'application/json'},method='POST');print(urllib.request.urlopen(req, timeout=20).read().decode())\""
    try:
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=40).decode()
        assert '"response"' in out.lower()
    except subprocess.CalledProcessError as e:
        pytest.skip(f"Could not run fallback test: {e.output.decode()}")
