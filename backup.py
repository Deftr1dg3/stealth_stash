#!/usr/bin/env python3

import os
from datetime import datetime
from hashlib import sha256
from settings import Settings


settings = Settings()


class BackUp:
    
    _BACKUP_DIR_PATH = settings.BACKUP_PATH
    _CONTROL_HASH_PATH = os.path.abspath("./") + os.sep + "data" + os.sep + "control_hash"
    
    def __init__(self) -> None:
        self._hash_file = self._control_hash_path()
        self._backup_dir = self._backup_dir_path()
    
    def _backup_dir_path(self) -> str:
        if not os.path.exists(self._BACKUP_DIR_PATH):
            os.makedirs(self._BACKUP_DIR_PATH)
        return self._BACKUP_DIR_PATH
        
    def _control_hash_path(self) -> str:
        if not os.path.exists(self._CONTROL_HASH_PATH):
            dirname = os.path.dirname(self._CONTROL_HASH_PATH)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            with open(self._CONTROL_HASH_PATH, "w") as f:
                ...
        return self._CONTROL_HASH_PATH
        
    def _get_backup_file_name(self) -> str:
        seconds = int(datetime.now().timestamp())
        file_name = str(seconds)
        return file_name

    def _create_control_hash(self, json_data: str) -> str:
        data_hash = sha256(json_data.encode("utf-8")).hexdigest()
        return data_hash

    def _get_control_hash(self) -> str:
        with open(self._hash_file, "r") as f:
            control_hash = f.read()
        return control_hash
    
    def _made_changes(self, json_data: str) -> bool:
        self._new_hash = self._create_control_hash(json_data)
        current_hash = self._get_control_hash()
        if not self._new_hash == current_hash:
            return True
        return False
    
    def _backup_data(self, b64_data: str) -> None:
        file_name = self._get_backup_file_name()
        file_path = self._backup_dir + os.sep + file_name 
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(b64_data)
        with open(self._hash_file, "w") as f:
            f.write(self._new_hash)
    
    def save_backup_file(self, json_data: str, b64_data: str) -> None:
        if self._made_changes(json_data):
            self._backup_data(b64_data)


