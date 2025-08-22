import os

def test_snapshot_files_exist():
    base_path = os.path.expanduser("~/docker/franklin-be")
    assert os.path.exists(os.path.join(base_path, "ai-middleware", "main.py")), "main.py missing from ai-middleware"
    assert os.path.exists(os.path.join(base_path, "web-ui", "dist", "index.html")), "Web UI build missing"
    assert os.path.exists(os.path.join(base_path, "docker-compose", "docker-compose.yml")), "docker-compose.yml missing"
