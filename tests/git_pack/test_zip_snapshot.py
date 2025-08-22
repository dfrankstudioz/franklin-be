import os
import zipfile

def test_zip_snapshot_valid():
    zip_path = os.path.expanduser("~/docker/franklin-be/snapshots/franklin-be.zip")
    assert os.path.exists(zip_path), "ZIP file not found"

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        assert any("main.py" in f for f in zip_ref.namelist()), "main.py missing from ZIP"
        assert any("index.html" in f for f in zip_ref.namelist()), "index.html missing from ZIP"
        assert any("docker-compose.yml" in f for f in zip_ref.namelist()), "docker-compose.yml missing from ZIP"
