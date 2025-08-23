
import subprocess
import re
from pathlib import Path

EXPECTED_PORT = "9006"
CONTAINER_NAME = "ai_middleware"

def get_uvicorn_port():
    try:
        logs = subprocess.check_output(
            ["docker", "compose", "logs", CONTAINER_NAME],
            cwd=str(Path.home() / "docker" / "docker-compose"),
            stderr=subprocess.STDOUT
        ).decode()
        match = re.search(r"Uvicorn running on http://0\.0\.0\.0:(\d+)", logs)
        if match:
            return match.group(1)
    except Exception as e:
        print(f"⚠️ Failed to check logs: {e}")
    return None

def show_last_logs(lines=50):
    try:
        logs = subprocess.check_output(
            ["docker", "compose", "logs", "--tail", str(lines), CONTAINER_NAME],
            cwd=str(Path.home() / "docker" / "docker-compose"),
            stderr=subprocess.STDOUT
        ).decode()
        print("\n📄 Last {} log lines:".format(lines))
        print(logs)
    except Exception as e:
        print(f"⚠️ Failed to retrieve logs: {e}")

def validate_fastapi():
    print("🧠 FastAPI Diagnostic Validator Starting...")
    port = get_uvicorn_port()
    if not port:
        print("❌ Could not determine Uvicorn port.")
        show_last_logs()
        return
    if port != EXPECTED_PORT:
        print(f"❌ Uvicorn is running on port {port}, but expected {EXPECTED_PORT}.")
        print("🔧 Fix Dockerfile CMD or docker-compose.yml port mapping.")
        show_last_logs()
    else:
        print(f"✅ Uvicorn is correctly running on port {EXPECTED_PORT}.")

if __name__ == "__main__":
    validate_fastapi()
