import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "ai_middleware"))

from ai_middleware.tools import list_dir

def test_list_dir_tool():
    result = list_dir("/memory")
    assert isinstance(result, list)
    assert all(isinstance(x, str) for x in result)
