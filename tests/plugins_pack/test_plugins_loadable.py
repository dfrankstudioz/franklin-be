import importlib
def test_plugins_loadable():
    print("✓ Plugin loader stub running")
    assert importlib.util.find_spec("plugins") is not None
