import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%MM_%DD_%YYYY_%HH_%MM_%SS').logs}" # Define the log file name with a timestamp
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # Define the logs directory path
os.makedirs(os.path.dirname(logs_path), exist_ok=True) # Create the logs directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # Full path to the log file

logging.basicConfig(
    filename=LOG_FILE_PATH, # Set the log file path
    level=logging.INFO, # Set the logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s', # Define the format for log entries
)