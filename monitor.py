import psutil
import time
import platform
from plyer import notification

# Convert bytes to human-readable format
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# Send desktop notification
def send_alert(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5  # seconds
    )

# System monitor function
def monitor_system():
    print("="*40, "System Health Monitor", "="*40)
    print(f"Platform     : {platform.system()} {platform.release()}")
    print(f"CPU Cores    : {psutil.cpu_count(logical=True)}")
    print("="*100)

    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        print(f"\nCPU Usage    : {cpu}%")
        print(f"RAM Usage    : {memory.percent}% of {get_size(memory.total)}")
        print(f"Disk Usage   : {disk.percent}% of {get_size(disk.total)}")
        print("-" * 100)

        # Alerts
        if cpu > 90:
            print("⚠️ High CPU usage!")
            send_alert("⚠️ High CPU Usage", f"CPU usage is at {cpu}%")
        if memory.percent > 90:
            print("⚠️ High RAM usage!")
            send_alert("⚠️ High RAM Usage", f"RAM usage is at {memory.percent}%")
        if disk.percent > 90:
            print("⚠️ Low Disk Space!")
            send_alert("⚠️ High Disk Usage", f"Disk usage is at {disk.percent}%")

        time.sleep(3)

if __name__ == "__main__":
    monitor_system()

