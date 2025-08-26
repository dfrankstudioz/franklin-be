import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
import sys
sys.path.insert(0, "/app")
from ai_middleware.tools.summarize_file import summarize_file

def test_summarize_file_tool():
    result = summarize_file("/memory/stub_file_1.txt")
    assert result == "This is a stubbed summary."
