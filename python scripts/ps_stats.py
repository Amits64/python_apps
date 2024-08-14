import psutil
import smtplib
from email.mime.text import MIMEText


def send_alert(disk_usage):
    msg = MIMEText(f"Disk usage alert! Current usage: {disk_usage}%")
    msg['Subject'] = 'Disk Usage Alert'
    msg['From'] = 'alert@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('localhost') as server:
        server.send_message(msg)


def monitor_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    print(f"Current disk usage: {disk_usage}%")
    if disk_usage > 80:
        send_alert(disk_usage)


monitor_disk_usage()
