import psutil
import subprocess
import time

def manage_docker_container(container_name, cpu_threshold=70):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > cpu_threshold:
            subprocess.run(['docker', 'stop', container_name])
            print(f"Container {container_name} stopped due to high CPU usage")
        else:
            subprocess.run(['docker', 'start', container_name])
            print(f"Container {container_name} started")
        time.sleep(5)

manage_docker_container('your_container_name')
