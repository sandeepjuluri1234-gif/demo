import psutil
import time
import logging
from plyer import notification

# ---------------------------------------------
# Configuration
# ---------------------------------------------
CPU_THRESHOLD = 80  # Alert threshold in percent
CHECK_INTERVAL = 5  # Check CPU usage every 5 seconds

# ---------------------------------------------
# Logger Setup
# ---------------------------------------------
logging.basicConfig(
    filename="cpu_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# ---------------------------------------------
# Notification Function
# ---------------------------------------------
def send_notification(cpu_usage: float):
    """Send desktop notification when CPU threshold exceeds."""
    message = f"High CPU Usage Detected: {cpu_usage:.2f}%"
    logging.warning(message)

    # Desktop Notification (Cross-Platform with plyer)
    notification.notify(
        title="CPU Alert",
        message=message,
        timeout=5  # Notification visible for 5 seconds
    )

# ---------------------------------------------
# CPU Monitoring Function
# ---------------------------------------------
def monitor_cpu():
    """Monitor CPU usage continuously."""
    logging.info("Starting CPU monitoring...")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)

            if cpu_usage > CPU_THRESHOLD:
                send_notification(cpu_usage)

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        logging.info("CPU monitoring stopped by user.")
        print("\nMonitoring stopped.")

# ---------------------------------------------
# Main Execution
# ---------------------------------------------
if __name__ == "__main__":
    monitor_cpu()
