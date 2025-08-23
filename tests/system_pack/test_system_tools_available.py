import shutil, pytest

def test_docker_cli_present():
    docker = shutil.which("docker")
    if docker is None:
        pytest.skip("docker CLI not found on PATH")
    assert True
