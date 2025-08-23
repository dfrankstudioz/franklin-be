import subprocess

def test_static_files_present_in_container():
    files = ["/app/ui/index.html", "/app/ui/assets"]
    for f in files:
        result = subprocess.run(
            ["docker", "compose", "-f", "/home/frank/docker/docker-compose/docker-compose.yml", "exec", "-T", "ai_middleware", "test", "-e", f],
            capture_output=True
        )
        assert result.returncode == 0, f"Missing in container: {f}"
