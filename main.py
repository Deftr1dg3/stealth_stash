#!/usr/bin/env python3

import os
import sys
from command import Command
from typing import NamedTuple
from data_file import DataFile
from settings import Settings
from main_frame import launch_gui
from exceptions import UnsupportedSystem, UnreadableToDecodeTheFile
from config import DataFilePath

# print(sys.executable)

settings = Settings()

current_dir = DataFilePath.DATA_FILE_PATH

class DefaultPath(NamedTuple):
    DARWIN = current_dir + os.sep + "gui" + os.sep + "KeyKeeperDataFile.kkdf"
    LINUX = ""
    WINDOWS = ""


def _path_exists(path: str) -> bool:
    return os.path.exists(path)
        
    
def _get_default_datafile_path() -> str:
    path = settings.DATAFILE_PATH
    return path


def _get_datafile_path() -> str:
    path = _get_default_datafile_path()
    return path
  

def _unable_to_decode():
    ...
      
    
def _get_password() -> str:
    password = "pass"
    return password


def _load_data(file_path: str, password: str) -> DataFile:
    data_file = DataFile(file_path, password)
    if not _path_exists(file_path):
        data_file.create()
    data_file.load_data()
    return data_file


def main():
    try:
        path = _get_datafile_path()
    except UnsupportedSystem:
        print(f"Unsupported system. Exit(1)")
        exit(1)
    try:
        password = _get_password()
    except Exception as ex:
        print(f"Occured exception whyle getting password from user -->\n{ex}")
        exit(1)
    try:
        data_file = _load_data(path, password)
    except UnreadableToDecodeTheFile:
        print("UNRABLE TO DECODE THE FILE")
        exit(1)
    command = Command(data_file, settings)
    try:
        launch_gui(command)
    except Exception as ex:
        print(f"Exception in MAIN --> {ex}")

    
if __name__ == "__main__":
    main()


# There  last changes to  be jubh iub iuh oiuh