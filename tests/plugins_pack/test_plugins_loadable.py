import pytest

@pytest.mark.skip(reason="No plugins directory in public build")
def test_plugins_loadable():
    pass
