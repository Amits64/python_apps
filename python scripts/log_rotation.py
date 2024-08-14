import os
import shutil


def rotate_log(log_file, max_size_kb=100):
    if os.path.exists(log_file) and os.path.getsize(log_file) > max_size_kb * 1024:
        backup_file = f"{log_file}.1"
        if os.path.exists(backup_file):
            os.remove(backup_file)
        shutil.move(log_file, backup_file)
        print(f"Rotated log file: {log_file} to {backup_file}")


log_file_path = 'application.log'
rotate_log(log_file_path)
