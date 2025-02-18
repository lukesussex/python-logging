"""Demonstrates basic logging functionality in Python."""

import datetime
import logging
import os

# Time and path data for naming the log file
time_now = datetime.datetime.now()
timestamp = time_now.strftime("%Y%m%d-%H%M%S")
path_file_log = os.path.join(os.path.dirname(__file__), f"{timestamp}_example_log_file.log")

# Configure base logger settings
formatter_log = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
logger_root = logging.getLogger()
logger_root.setLevel(logging.DEBUG)

# Configure logger for console
loghandler_console = logging.StreamHandler()
loghandler_console.setFormatter(formatter_log)
loghandler_console.setLevel(logging.INFO)
logger_root.addHandler(loghandler_console)

# Configure logger for file
loghandler_file = logging.FileHandler(path_file_log)
loghandler_file.setFormatter(formatter_log)
loghandler_file.setLevel(logging.DEBUG)
logger_root.addHandler(loghandler_file)

logging.debug("This is a debug message that only goes to the log file")
logging.info("This is a test message that goes to the console and the log file")
logging.warning("This is a test warning message that goes to the console and the log file")
logging.error("This is a test error message that goes to the console and the log file")
