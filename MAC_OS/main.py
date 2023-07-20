#!/usr/bin/env python3

import os
from command import Command
from data_file import DataFile
from settings import Settings
from gui.main_frame import launch_gui
from gui.modals.get_password_from_user import launch_get_password
from gui.modals.first_launch import launch_first_start
from exceptions import UnsupportedSystem, UnableToDecodeTheFile


settings = Settings()


def _get_datafile_path() -> str:
    path = settings.DATAFILE_PATH
    return path


def _validate_file_path(file_path: str) -> bool:
    if not os.path.exists(file_path):
        dirname = os.path.dirname(file_path)
        os.makedirs(dirname, exist_ok=True)
        return False
    return True


def _load_data(file_path: str) -> DataFile:
    file_exists = _validate_file_path(file_path)
    data_file = DataFile(file_path)
    if not file_exists:
        launch_first_start(data_file, settings)
        return data_file
    else:
        launch_get_password(data_file, settings)
        return data_file


def main():
    path = _get_datafile_path()
    data_file = _load_data(path)
    command = Command(data_file, settings)
    launch_gui(command)
   

    
if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f"Exception in MAIN --> {ex}")
        exit(1)



# There  last changes to  be jubh iub iuh oiuh