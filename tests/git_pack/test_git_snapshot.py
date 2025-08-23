import os

def test_git_snapshot_pack():
    result = os.system("bash ~/docker/tests/git/run_git_snapshot.sh")
    assert result == 0
