import psutil
import time
import platform

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def show_stats():
    print("="*40, "System Health Monitor", "="*40)
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print("="*100)

    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        print(f"\nCPU Usage: {cpu}%")
        print(f"RAM Usage: {memory.percent}% of {get_size(memory.total)}")
        print(f"Disk Usage: {disk.percent}% of {get_size(disk.total)}")

        if cpu > 80:
            print("⚠️ High CPU usage!")
        if memory.percent > 80:
            print("⚠️ High RAM usage!")
        if disk.percent > 90:
            print("⚠️ Low Disk Space!")

        time.sleep(5)

if __name__ == "__main__":
    show_stats()
