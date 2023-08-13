import subprocess
import signal
import sys

service_change_file = subprocess.Popen(['python', 'service_change_file.py'])
# service_receiver =  subprocess.call(['python', 'receiver.py'])

print(service_change_file.wait())

# Hàm xử lý sự kiện Ctrl + C
def handle_ctrl_c(signal, frame):
    print("Ctrl+C detected. Thực hiện các hành động cần thiết.")
    print(signal)
    service_change_file.terminate()
    sys.exit(0)

# Đăng ký xử lý sự kiện Ctrl + C
signal.signal(signal.SIGINT, handle_ctrl_c)





