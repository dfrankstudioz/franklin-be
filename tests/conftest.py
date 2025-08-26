import pytest

BASE_URL = "http://localhost:9006"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL
