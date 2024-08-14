import os
import zipfile
from datetime import datetime

def backup_directory(directory_path):
    backup_name = f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.zip"
    with zipfile.ZipFile(backup_name, 'w') as backup_zip:
        for folder_name, subfolders, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                backup_zip.write(file_path, os.path.relpath(file_path, directory_path))
    print(f"Backup completed: {backup_name}")

backup_directory('test_dir')
