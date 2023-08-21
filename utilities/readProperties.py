import configparser
import os

config = configparser.RawConfigParser()
config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "configurations", "config.ini")
config.read(config_file_path)
# script_dir = os.path.dirname(os.path.abspath(__file__))
# config_file_path = os.path.join(script_dir, 'configurations', 'config.ini')
# config.read(config_file_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        email = config.get('commonInfo', 'customer_email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('commonInfo', 'customer_password')
        return password


