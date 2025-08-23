import subprocess

def test_mount_integrity():
    cmd = r"""docker compose exec -T ai_middleware bash -lc 'find /host-root/home/frank/docker/memory -type f | wc -l'"""
    out = subprocess.check_output(cmd, shell=True, timeout=60).decode().strip()
    assert out.isdigit()
    assert int(out) >= 1
