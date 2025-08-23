import subprocess

def test_openai_api_key_in_container():
    cwd = "/home/frank/docker/docker-compose"
    result = subprocess.run(
        ["docker", "compose", "exec", "ai_middleware", "printenv", "OPENAI_API_KEY"],
        capture_output=True, text=True, cwd=cwd
    )
    assert result.returncode == 0 and result.stdout.strip(), "OPENAI_API_KEY missing"
