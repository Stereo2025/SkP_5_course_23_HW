import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data/apache_logs.txt")


class BaseError(Exception):
    pass


class FileNotFound(BaseError):
    message = 'File Not Found'
