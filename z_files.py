import os
from pathlib import Path
import logging

# configure logging information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# name of the base folder
BASE_FILE = 'cnnclassifier'

# lists of all the files we will need for the project(only add files here)
file_list = [
    f"src/{BASE_FILE}/__init__.py",
    f"src/{BASE_FILE}/components/__init__.py",
    f"src/{BASE_FILE}/utils/__init__.py",
    f"src/{BASE_FILE}/config/__init__.py",
    f"src/{BASE_FILE}/config/configuration.py",
    f"src/{BASE_FILE}/pipeline/__init__.py",
    f"src/{BASE_FILE}/entity/__init__.py",
    f"src/{BASE_FILE}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "setup.py",
    "analysis/__init__.ipynb",
    "README.md"
]


def create_directories_and_files():
    """
    create directories and files specified in the file list
    """

    for file in file_list:
        _path = Path(file).resolve() # create a root path object
        folder_path, file_path = os.path.split(_path) # split into a folder and file path

        if folder_path != '':
            os.makedirs(folder_path, exist_ok=True) # create the folder if it doesn't exist
            logging.info(f"creating directory: {folder_path}")

        if file_path != '':
            if not os.path.exists(_path): # check if file doesn't exist or is empty
                with open(_path, 'w') as f:
                    pass # create a file by opening it in write mode
                logging.info(f"Creating file: {_path}")
            else:
                logging.info(f"File already exists: {_path}")

create_directories_and_files()
