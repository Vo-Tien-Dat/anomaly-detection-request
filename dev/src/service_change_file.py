import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from sender import send_event

listener_file = ['normalize_date.txt']
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        file_path = event.src_path
        file_name = file_path.split("\\")[-1]
        if file_name in listener_file: 
            send_event()
            # print("oke")

folder_path = os.getcwd()
observer = Observer()
observer.schedule(FileChangeHandler(), folder_path, recursive=True)

observer.start()
try:
    print("Chạy dịch vụ nghe sự kiện thay đổi dữ liệu")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()