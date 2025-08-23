import os
import importlib.util
import pytest

def test_secret_logic_encrypted():
    logic_path = "/app/ai_middleware/secret_logic.py"

    # Check if file exists
    assert os.path.exists(logic_path), f"{logic_path} does not exist"

    # Try loading the module
    spec = importlib.util.spec_from_file_location("secret_logic", logic_path)
    secret_logic = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(secret_logic)
    except Exception as e:
        # Expected failure if encrypted or stubbed
        with open(logic_path, "r") as f:
            content = f.read()
        assert "__pyarmor__" in content or "NotImplementedError" in content, "File is not obfuscated or stubbed"
        return

    # If no error occurred, the logic was not protected
    assert False, "Encrypted module executed without error – encryption may have failed"
