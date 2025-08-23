import os
import zipfile

def test_zip_snapshot_valid():
    snapshot_dir = os.path.expanduser("~/docker/franklin-be/snapshots")
    zip_files = [f for f in os.listdir(snapshot_dir) if f.startswith("franklin-be-v") and f.endswith(".zip")]
    assert zip_files, "No versioned ZIP file found"

    zip_files.sort(reverse=True)  # Use latest version
    zip_path = os.path.join(snapshot_dir, zip_files[0])
    print(f"🧪 Validating ZIP: {zip_path}")

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        assert any("main.py" in f for f in zip_ref.namelist()), "main.py missing from ZIP"
        assert any("index.html" in f for f in zip_ref.namelist()), "index.html missing from ZIP"
        assert any("docker-compose.yml" in f for f in zip_ref.namelist()), "docker-compose.yml missing from ZIP"
