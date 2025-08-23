import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "ai_middleware"))

from ai_middleware.tools import read_file

def test_read_file_tool():
    result = read_file("/memory/stub_file_1.txt")
    assert isinstance(result, str)
