import psutil
import time
import logging

logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')


def log_system_usage(interval=5):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        logging.info(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_info.percent}%")
        time.sleep(interval)


log_system_usage()
