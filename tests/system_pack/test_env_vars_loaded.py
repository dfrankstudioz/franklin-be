import pytest

@pytest.mark.skip(reason="No OPENAI_API_KEY in container for public build")
def test_openai_api_key_in_container():
    pass
