import psutil
import time
from plyer import notification

# Function to send desktop notification
def send_alert(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5  # seconds
    )

# Main monitoring function
def monitor_system():
    print("🔍 Starting System Health Monitor...\n")
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        print(f"CPU Usage: {cpu}%")
        print(f"RAM Usage: {ram}%")
        print(f"Disk Usage: {disk}%")
        print("-" * 30)

        # Send alert if usage crosses threshold
        if cpu > 90:
            send_alert("⚠️ High CPU Usage", f"CPU usage is at {cpu}%")
        if ram > 90:
            send_alert("⚠️ High RAM Usage", f"RAM usage is at {ram}%")
        if disk > 90:
            send_alert("⚠️ High Disk Usage", f"Disk usage is at {disk}%")

        time.sleep(3)  # Delay between checks

if __name__ == "__main__":
    monitor_system()
