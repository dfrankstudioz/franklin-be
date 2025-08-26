import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
import sys
sys.path.insert(0, "/app")
from ai_middleware.tools.list_dir import list_dir

def test_list_dir_tool():
    result = list_dir("/memory")
    assert isinstance(result, list) and "stub_file_1.txt" in result
