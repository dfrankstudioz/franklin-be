import os
import importlib.util
import pytest

def test_secret_logic_encrypted():
    logic_path = "/app/ai-middleware/secret_logic.py"
    assert os.path.exists(logic_path), f"{logic_path} does not exist"

    spec = importlib.util.spec_from_file_location("secret_logic", logic_path)
    secret_logic = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(secret_logic)
    except Exception:
        with open(logic_path, "r") as f:
            content = f.read()

        if "__pyarmor__" in content:
            print("[ENCRYPTED MODE] PyArmor obfuscated logic detected")
        elif "NotImplementedError" in content:
            print("[STUB MODE] import-time failure detected")
        else:
            pytest.fail("File is not obfuscated or stubbed")
        return

    # Import succeeded, check if function raises
    with pytest.raises(NotImplementedError):
        secret_logic.secret_summary("test")
    print("[STUB MODE] function-level failure detected")
