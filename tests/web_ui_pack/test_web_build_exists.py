import os

def test_web_ui_build_exists():
    build_dir = os.path.expanduser("~/docker/franklin-be/web-ui/dist")
    index_path = os.path.join(build_dir, "index.html")
    assert os.path.exists(index_path), "Web UI build missing: index.html not found"
