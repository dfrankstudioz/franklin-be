import json, subprocess

def test_ui_asset_integrity():
    cmd = r"""docker compose exec -T ai_middleware bash -lc "python - <<'PY'
import os,hashlib,glob,json
base='/app/static/js'
res={}
for p in glob.glob(base+'/**/*.js', recursive=True):
    try:
        with open(p,'rb') as f:
            res[os.path.basename(p)] = hashlib.sha256(f.read()).hexdigest()
    except Exception:
        pass
print(json.dumps(res))
PY"
"""
    out = subprocess.check_output(cmd, shell=True, timeout=120).decode()
    data = json.loads(out)
    # at least one JS asset and each value is a 64-char sha256
    assert isinstance(data, dict) and len(data) >= 1
    assert all(isinstance(v, str) and len(v) == 64 for v in data.values())
