import os, sys, importlib
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[2]   # repo root (…/tests -> repo root)

CANDIDATES = [
    ROOT / "plugins",
    Path.home() / "docker" / "plugins",
]

def _find_plugins_dir():
    for c in CANDIDATES:
        if c.is_dir():
            return c
    return None

def test_plugins_are_loadable():
    plugdir = _find_plugins_dir()
    if not plugdir:
        pytest.skip(f"No plugins directory found in any of: {', '.join(map(str, CANDIDATES))}")
    # ensure import works as a package named "plugins"
    if str(plugdir.parent) not in sys.path:
        sys.path.insert(0, str(plugdir.parent))
    pkg = importlib.import_module("plugins")
    assert hasattr(pkg, "__path__")
