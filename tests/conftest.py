import os
import pytest

def pytest_configure(config):
    # Detect build context based on current working directory
    cwd = os.getcwd()
    if "franklin-be" in cwd:
        config.build_mode = "be"
    else:
        config.build_mode = "dev"

@pytest.fixture(scope="session")
def build_mode(pytestconfig):
    return getattr(pytestconfig, "build_mode", "dev")
