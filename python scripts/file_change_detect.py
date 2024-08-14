import os
import time
import logging

logging.basicConfig(filename='file_changes.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')

def monitor_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    last_modified = os.path.getmtime(file_path)
    while True:
        current_modified = os.path.getmtime(file_path)
        if current_modified != last_modified:
            logging.info(f"File changed: {file_path}")
            last_modified = current_modified
        time.sleep(1)

monitor_file('your_file.txt')
