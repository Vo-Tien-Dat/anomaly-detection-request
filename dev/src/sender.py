import socket
def send_event():
    result = 200

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 1234))

    sock.sendall(str(result).encode())
    # Đóng kết nối
    sock.close()