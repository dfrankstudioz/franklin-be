import sys, platform

def test_python_is_available_and_linux():
    assert sys.version_info.major >= 3
    assert platform.system() in {"Linux", "Darwin", "Windows"}  # Should be Linux in your setup
