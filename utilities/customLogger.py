import logging
import os


# Configure the logger at the module level
logs_directory = os.path.join(os.path.dirname(__file__), "logs")
logs_file = "automation.log"
log_file_path = os.path.join(logs_directory, logs_file)
logging.basicConfig(
    filename=log_file_path,
    format='%(asctime)s: %(levelname)s: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG
)

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        return logger


# class LogGen:
#     @staticmethod
#     def loggen():
#         logs_directory = os.path.join(os.path.dirname(__file__), "logs")
#         logs_file = "automation.log"
#         # if not os.path.exists(logs_directory):
#         #     os.makedirs(logs_directory)
#         log_file_path = os.path.join(logs_directory, logs_file)
#         print("Log file path:", log_file_path)  # Print the log file path
#         logging.basicConfig(filename=log_file_path, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         logger.setLevel(logging.DEBUG)
#         return logger
