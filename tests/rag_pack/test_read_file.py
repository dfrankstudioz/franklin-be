import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
import sys
sys.path.insert(0, "/app")
from ai_middleware.tools.read_file import read_file

def test_read_file_tool():
    result = read_file("/memory/stub_file_1.txt")
    assert result == "This is a stubbed file content."
