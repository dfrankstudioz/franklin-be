import os
import subprocess
import time
from pathlib import Path
from diagnostic_logger import export_diagnostic_snapshot

def run(label, cmd):
    print(f"▶️ {label}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print("⚠️ stderr:", result.stderr)
    return result.returncode == 0

def dump_container_logs():
    print("📄 Dumping Docker logs (ai_middleware)...")
    try:
        logs = subprocess.check_output(
            ["docker", "compose", "logs", "ai_middleware"],
            cwd=str(Path.home() / "docker" / "docker-compose"),
            stderr=subprocess.STDOUT
        ).decode()
        print(logs)
    except Exception as e:
        print(f"❌ Failed to get docker logs: {e}")

def dump_routes():
    print("🧭 FastAPI route list:")
    try:
        routes = subprocess.check_output(
            ["docker", "exec", "ai_middleware", "python3", "-c",
             "from main import app; print([(r.path, list(getattr(r, 'methods', []))) for r in app.routes])"]
        ).decode()
        print(routes)
    except Exception as e:
        print(f"❌ Failed to get route list: {e}")

def validate_env_key():
    env_path = Path.home() / "docker" / ".env"
    if not env_path.exists():
        print("❌ .env file is missing!")
        return
    with open(env_path) as f:
        for line in f:
            if line.startswith("OPENAI_API_KEY") and "xxx" not in line.lower():
                print("✅ OPENAI_API_KEY found.")
                return
    print("❌ OPENAI_API_KEY not set properly.")

def print_file_header(path, label):
    print(f"📄 {label} ({path}):")
    if not Path(path).exists():
        print("❌ File not found.")
        return
    with open(path) as f:
        for line in f:
            if "OPENAI_API_KEY" in line:
                print("OPENAI_API_KEY=***MASKED***")
            else:
                print(line.strip())

def print_folder_tree():
    print("📁 Folder tree ~/docker:")
    os.system("tree ~/docker || echo 'tree not installed'")
    print("📁 Contents of /memory:")
    os.system("ls -lh ~/docker/memory || echo '/memory not found'")
    print("📁 Contents of /logs:")
    os.system("ls -lh ~/docker/logs || echo '/logs not found'")

def run_all_diagnostics():
    print("🧠 Restarting container and running full AI Middleware diagnostic suite...")
    subprocess.run(["docker", "compose", "restart", "ai_middleware"],
                   cwd=str(Path.home() / "docker" / "docker-compose"))
    print("[RESTARTED] ai_middleware container restarted")

    start = time.time()

    dump_routes()
    validate_env_key()

    run("FastAPI container health", "python3 ~/docker/tests/test_fastapi_health.py")
    if not run("FastAPI /chat test", "python3 ~/docker/tests/test_fastapi_entry.py"):
        dump_container_logs()
        run("FastAPI Validator", "python3 ~/docker/tests/fastapi_validator.py")

    run("TinyLlama direct test", "python3 ~/docker/tests/test_tinyllama_direct.py")
    run("RAG logic test", "python3 ~/docker/tests/test_rag_logic.py")

    print("📦 Exporting full diagnostic snapshot...")
    snapshot_path = export_diagnostic_snapshot()
    print(f"📦 Snapshot saved to: {snapshot_path}")

    print_file_header(Path.home() / "docker" / "ai_middleware" / "main.py", "main.py")
    print_file_header(Path.home() / "docker" / "docker-compose" / "docker-compose.yml", "docker-compose.yml")
    print_file_header(Path.home() / "docker" / ".env", ".env")
    print_folder_tree()

    print(f"✅ All tests completed in {round(time.time() - start, 2)} seconds.")

if __name__ == "__main__":
    run_all_diagnostics()
