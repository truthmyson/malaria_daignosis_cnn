# this is a custom logger for the cnnclassifier packagge
import logging
import sys
import os

logging_str = "[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"

# folder to keep all the logs files
log_dir = "logs"

# file to keep all the logs
log_file = os.path.join(log_dir, "running_logs.log")

# create log folder if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# create logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file), #this handler will save every log in the log file
        logging.StreamHandler(sys.stdout) #this handler will display every log in the console
    ]
)

logger = logging.getLogger("cnnclassifierLogger")