import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

log_file = os.path.join("logs", "alerts.log")

def log_alert(message):
    with open(log_file, "a") as f:
        f.write("[ALERT] " + message + "\n")
