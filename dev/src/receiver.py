import socket
import subprocess

def event_handler():
    print("Tiến hành gửi email")
    subprocess.call(['python', 'service_sent_email.py'])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 1234))
sock.listen(1)

while True:
    try:
        connection, address = sock.accept()
        data = connection.recv(1024)
        result = int(data.decode())
        event_handler()
        connection.close()
    except KeyboardInterrupt:
        print("Ctrl+C detected. Exiting...")
        break