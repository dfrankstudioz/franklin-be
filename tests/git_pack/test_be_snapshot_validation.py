import os

BASE_PATH = "/home/frank/docker/franklin-be"
EXPECTED_FILES = [
    f"{BASE_PATH}/ai_middleware/main.py",
    f"{BASE_PATH}/ai_middleware/rag_prompt_patch.py",
    f"{BASE_PATH}/ai_middleware/secret_logic.py",
    f"{BASE_PATH}/ai_middleware/Dockerfile",
    f"{BASE_PATH}/docker-compose/docker-compose.yml",
    f"{BASE_PATH}/web-ui/dist/index.html",
    f"{BASE_PATH}/tests/system_pack/test_encrypted_logic.py",
    f"{BASE_PATH}/tests/system_pack/test_service_health.py",
]

def test_secret_logic_is_stub():
    path = f"{BASE_PATH}/ai_middleware/secret_logic.py"
    with open(path, "r") as f:
        contents = f.read()
    assert "NotImplementedError" in contents, "secret_logic.py must be stubbed for public release"

def test_pyarmor_runtime_missing():
    assert not os.path.exists(f"{BASE_PATH}/ai_middleware/.pyarmor_runtime"), ".pyarmor_runtime should not be in Builder's Edition"

def test_env_file_not_included():
    assert not os.path.exists(f"{BASE_PATH}/docker-compose/.env"), ".env file should not be present in Builder's Edition"

def test_expected_files_exist():
    for path in EXPECTED_FILES:
        assert os.path.exists(path), f"Missing expected file: {path}"

def test_no_extra_tests():
    test_root = f"{BASE_PATH}/tests"
    for root, dirs, files in os.walk(test_root):
        for file in files:
            if not file.startswith("test_encrypted") and not file.startswith("test_service"):
                assert False, f"Unexpected test file in snapshot: {file}"

def test_no_pycache_or_logs():
    for root, dirs, files in os.walk(BASE_PATH):
        for d in dirs:
            assert "__pycache__" not in d and ".pytest_cache" not in d, f"Remove cache dir: {os.path.join(root, d)}"
        for f in files:
            assert not f.endswith(".pyc"), f"Remove compiled file: {os.path.join(root, f)}"
