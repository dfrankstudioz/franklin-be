import socket

def test_port_open():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex(("localhost", 9006))
    sock.close()
    assert result == 0, "Port 9006 is not open or FastAPI is not running"