# 🖥️ System Health Monitor

A lightweight and real-time system resource monitoring tool built with **Python**. This project helps track **CPU**, **RAM**, and **Disk** usage directly from the terminal — along with desktop alerts when any resource crosses safe usage thresholds.

> 🔔 Designed to run silently in the background and alert you only when something needs attention!

---

## 🚀 Features

- ✅ Live monitoring of:
  - CPU usage
  - Memory (RAM) usage
  - Disk space usage
- ✅ Clean and readable terminal output
- ✅ Desktop notifications when resource usage gets too high
- ✅ Cross-platform support (Linux, Windows, macOS)
- ✅ Simple and minimal setup — perfect for learning or productivity

---

## 📂 Project Structure

system-health-monitor/
├── monitor.py # Main monitoring script
├── requirements.txt # Required Python packages
├── README.md # Project documentation
└── .gitignore # Ignored files


---

## 🛠️ Installation & Setup

### 1. Clone this repository

```bash
git clone https://github.com/Aishwaryap015/system-health-monitor.git
cd system-health-monitor

🛠️ Installation & Setup on Ubuntu/Linux
1. Clone this repository

git clone https://github.com/Aishwaryap015/system-health-monitor.git
cd system-health-monitor

2. (Optional) Create a Virtual Environment

Using Python's built-in venv module:

sudo apt update
sudo apt install python3-venv  # if not already installed
python3 -m venv venv
source venv/bin/activate

    Use deactivate to exit the virtual environment later.

3. Install Required Dependencies

pip install -r requirements.txt

    If you face issues with plyer notifications not showing, make sure libnotify-bin is installed:

sudo apt install libnotify-bin

▶️ Run the Monitor

python monitor.py

You’ll start seeing live updates in the terminal like:

CPU Usage   : 27.4%
RAM Usage   : 65.1% of 7.8GB
Disk Usage  : 79.2% of 256GB

If any of the usage stats cross 90%, a desktop notification will appear.

    Use Ctrl + C to stop the program safely.

✅ Why It Keeps Running:

It keeps running due to:

while True:
    # Monitor CPU, RAM, Disk
    time.sleep(2)

BY: 👩‍💻 
Aishwarya Priydarshni
CSE (Data Science), Government Engineering College, Arwal
GitHub: Aishwaryap015
