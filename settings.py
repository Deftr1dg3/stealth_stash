#!/usr/bin/env python3


import os
import json

class Settings:
    
    DEFAULT_DATAFILE_PATH = os.path.abspath("./") + os.sep + "KeyKeeperDataFile.kkdf"
    DEFAULT_BACKUP_PATH = ""
    DEFAULT_COLOUR_SCHEME = "LIGHT_GREEN"
    
    def __init__(self) -> None:
        self._datafile_path = os.path.abspath("./") + os.sep +  "settings"
        self._settings = self._get_settings()
    
    @property
    def DATAFILE_PATH(self) -> str:
        return self._settings["DATAFILE_PATH"]
    
    @DATAFILE_PATH.setter
    def DATAFILE_PATH(self, path: str) -> None:
        self._settings["DATAFILE_PATH"] = path
        self._save_settings()
    
    @property
    def BACKUP_PATH(self) -> str:
        return self._settings["BACKUP_PATH"]
    
    @BACKUP_PATH.setter
    def BACKUP_PATH(self, path: str) -> None:
        self._settings["BACKUP_PATH"] = path
        self._save_settings()
    
    @property
    def COLOUR_SCHEME(self) -> str:
        return self._settings["COLOUR_SCHEME"]
    
    @COLOUR_SCHEME.setter
    def COLOUR_SCHEME(self, colour_scheme: str) -> None:
        self._settings["COLOUR_SCHEME"] = colour_scheme
        self._save_settings()
        
    def _get_settings(self) -> dict:
        if os.path.exists(self._datafile_path):
            with open(self._datafile_path, "r") as f:
                settings = json.load(f)
                return settings
        settings = self._create_file()
        return settings
            
    def _create_file(self) -> dict:
        settings = {
                    "DATAFILE_PATH": self.DEFAULT_DATAFILE_PATH,
                    "BACKUP_PATH": self.DEFAULT_BACKUP_PATH,
                    "COLOUR_SCHEME": self.DEFAULT_COLOUR_SCHEME,
                    }
        with open(self._datafile_path, "w") as f:
            json.dump(settings, f)
        return settings
    
    def _save_settings(self):
        with open(self._datafile_path, "w") as f:
            json.dump(self._settings, f)