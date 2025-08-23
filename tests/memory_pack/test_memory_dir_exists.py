from pathlib import Path
import pytest

def test_memory_dir_exists_on_host():
    mem = Path.home() / "docker" / "memory"
    if not mem.exists():
        pytest.skip(f"host memory directory not found at {mem}")
    assert mem.is_dir(), f"{mem} exists but is not a directory"
