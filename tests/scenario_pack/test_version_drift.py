import json, subprocess

def test_version_drift():
    cmd = r"""docker compose exec -T ai_middleware bash -lc "python - <<'PY'
import os,hashlib,glob,json
base='/app'
res={}
for p in glob.glob(base+'/**/*.py', recursive=True):
    try:
        with open(p,'rb') as f:
            res[p.replace(base+'/','')] = hashlib.sha256(f.read()).hexdigest()
    except Exception:
        pass
print(json.dumps(res))
PY"
"""
    out = subprocess.check_output(cmd, shell=True, timeout=180).decode()
    data = json.loads(out)
    # should have multiple python files with 64-char hashes
    assert isinstance(data, dict) and len(data) >= 3
    assert all(isinstance(v, str) and len(v) == 64 for v in data.values())
