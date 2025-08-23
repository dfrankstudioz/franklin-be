from pathlib import Path
import pytest
import os

def test_logs_dir_exists_and_writable():
    logs = Path.home() / "docker" / "logs"
    if not logs.exists():
        pytest.skip(f"logs directory not found at {logs}")
    # Check writability (directory perms)
    can_write = os.access(str(logs), os.W_OK)
    assert can_write, f"logs directory exists but not writable: {logs}"
