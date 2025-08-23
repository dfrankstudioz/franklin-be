import os
import platform

def test_required_directories_exist():
    is_container = os.path.exists("/app") and not os.path.exists("/home/frank")
    
    if is_container:
        required_dirs = [
            "/memory",
            "/logs",
            "/docker-compose",
            "/app/web-ui/build",
            "/tests"
        ]
    else:
        root = os.path.expanduser("~/docker")
        required_dirs = [
            f"{root}/memory",
            f"{root}/logs",
            f"{root}/docker-compose",
            f"{root}/web-ui/build",
            f"{root}/tests"
        ]

    for path in required_dirs:
        assert os.path.exists(path), f"Missing required path: {path}"