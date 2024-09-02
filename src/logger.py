import logging
import os
from datetime import datetime

# Define the log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory where the log file will be stored
logs_dir = os.path.join(os.getcwd(), 'logs')

# Ensure the logs directory exists
os.makedirs(logs_dir, exist_ok=True)

# Define the full path for the log file
logs_path = os.path.join(logs_dir, LOG_FILE)

print(f"Log file will be created at: {logs_path}")

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)