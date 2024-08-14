import subprocess
from datetime import datetime

def backup_database(db_user, db_password, db_name):
    backup_file = f"{db_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.sql"
    subprocess.run([
        'mysqldump',
        '-u', db_user,
        '-p' + db_password,
        db_name,
        '>', backup_file
    ])
    print(f"Database backup completed: {backup_file}")

backup_database('your_user', 'your_password', 'your_database')
