#!/usr/bin/env python3

from __future__ import annotations
import json 
import atexit
from base64 import b64encode, b64decode
from aes import AES_Encripton
from exceptions import UnableToDecodeTheFile
from manage_password import PasswordStrength, GeneratePassword
from backup import BackUp


class Entry:
    def __init__(self, entry_data: (list | None) = None):
        if entry_data is None:
            self._entry_data = ["New Record", "Username", self._generate_password(), "URL", "N/A"]
        else:
            self._entry_data = entry_data
            
        self._id = id(self._entry_data)
    
    @property
    def id(self) -> int:
        return self._id
        
    @property
    def entry_data(self) -> list:
        return self._entry_data
        
    @property
    def record_name(self) -> str:
        return self._entry_data[0]
    
    @record_name.setter
    def record_name(self, new_value: str) -> None:
        self._entry_data[0] = new_value
        
    @property
    def username(self) -> str:
        return self._entry_data[1]
    
    @username.setter
    def username(self, new_value: str) -> None:
        self._entry_data[1] = new_value
        
    @property
    def password(self) -> str:
        return self._entry_data[2]
    
    @password.setter
    def password(self, new_value: str) -> None:
        self._entry_data[2] = new_value
        
    @property
    def url(self) -> str:
        return self._entry_data[3]
    
    @url.setter
    def url(self, new_value: str) -> None:
        self._entry_data[3] = new_value
        
    @property
    def notes(self) -> str:
        return self._entry_data[4]
    
    @notes.setter
    def notes(self, new_value: str) -> None:
        self._entry_data[4] = new_value
        
    def _generate_password(self) -> str:
        g = GeneratePassword()
        password = g.generate_password(PasswordStrength.STRONG)
        return password
    
    

class Category:
    def __init__(self, name: str, data_file: DataFile, id: int) -> None:
        self._data_file = data_file
        self._name = name 
        self._id = id
        
    @property
    def id(self) -> int:
        return self._id
        
    @property
    def name(self) -> str:
        return self._name
        
    def get_content(self) -> list[Entry]:
        content = self._data_file.get_category_content(self._name)
        return content
    
    def rename(self, new_name: str) -> None:
        self._data_file.rename_category(self.name, new_name)
        self._name = new_name
    
    def remove(self) -> None:
        self._data_file.delete_category(self.name)
    
    def remove_entry(self, entry: Entry) -> None:
        entry_data = entry.entry_data
        self._data_file.delete_row_from_category(self._name, entry_data)
    
    def new_entry(self) -> Entry:
        new_row = Entry()
        self._data_file.add_row_to_categoty(self.name, new_row.entry_data)
        return new_row
    
    def clear_category(self) -> None:
        self._data_file.clear_category(self.name)
    
    def commit(self):
        self._data_file.commit()
        
    
class Data(dict):
    def __init__(self):
        super().__init__()
        self["Internet"] = []
        self["Emails"] = []
        self["Crypto"] = []
        self["Development"] = []
        self["Databases"] = []
        self["Funds"] = []
        self["Payments"] = []
        self["Apps"] = []
    


class IODataFile:
    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        
    def get_data(self) -> str:
        with open(self._file_path, "r", encoding="utf-8") as f:
            data = f.read()
        return data
        
    def save_data(self, data: str) -> None:
        with open(self._file_path, "w", encoding="utf-8") as f:
            f.write(data)



class DataFile:
    def __init__(self, file_path: str) -> None:
        # self._aes_encription = AES_Encripton(password)
        self._io_data = IODataFile(file_path)
        self._backup = BackUp()
        self._datafile_path = file_path
        self._password = ""
        atexit.register(self._atexit)
    
    @property
    def datafile(self) -> str:
        return self._datafile_path
    
    @datafile.setter
    def datafile(self, path: str) -> None:
        self._io_data = IODataFile(path)
        self._datafile_path = path
        
    @property
    def password(self) -> str:
        return self._password 
    
    @password.setter
    def password(self, password: str) -> None:
        if password:
            self._password = password
            self._aes_encription = AES_Encripton(password)
    
    
    def create(self) -> None:
        self._data = Data()
        self.commit()
    
    def load_data(self) -> None:
        b64_str_data = self._io_data.get_data()
        encrypted_bytes_data = b64decode(b64_str_data)
        try:
            decrypted_bytes_data = self._aes_encription.decrypt(encrypted_bytes_data)
            json_data = decrypted_bytes_data.decode("utf-8")
        except ValueError:
            raise UnableToDecodeTheFile()
        self._data = json.loads(json_data)
        
    def _atexit(self) -> None:
        self.commit()
        self._backup.save_backup_file(self._json_data, self._b64_str_data)
        
    def commit(self):
        try:
            self._json_data = json.dumps(self._data)
        except AttributeError:
            return 
        bytes_data = self._json_data.encode("utf-8")
        encrypted_bytes_packet = self._aes_encription.encrypt(bytes_data)
        self._b64_str_data = b64encode(encrypted_bytes_packet).decode('utf-8')
        self._io_data.save_data(self._b64_str_data)
        
    def get_category_data(self, category: str) -> list[list]:
        return self._data[category]
    
    def get_category_content(self, category: str) -> list[Entry]:
        categoty_data = [Entry(row) for row in self._data[category]]
        return categoty_data
            
    def add_category(self, categoty: str) -> None:
        self._data[categoty] = []
        self.commit()
        
    def rename_category(self, category: str, new_name: str) -> None:
        keys = list(self._data.keys())
        values = list(self._data.values())
        categoty_index = keys.index(category)
        keys[categoty_index] = new_name
        self._data = dict(zip(keys, values))
        self.commit()
        
    def delete_category(self, category: str) -> None:
        del self._data[category]
        self.commit()
        
    def add_row_to_categoty(self, category: str, row: list[str]) -> None:
        self._data[category].append(row)
        self.commit()
        
    def delete_row_from_category(self, category: str, entry_data: list) -> None:
        index = 0
        for row in self._data[category]:
            if row is entry_data:
                del self._data[category][index]
                return
            index += 1
        self.commit()
        
    def clear_category(self, category_name: str) -> None:
        self._data[category_name] = []
        self.commit()
    
    def get_categories(self) -> list[Category]:
        categories = []
        for category_name in self._data.keys():
            categories.append(Category(category_name, self, id(self._data[category_name])))
        return categories
    
    def get_categories_namespace(self) -> set:
        return set(self._data.keys())
    
    def search(self, query: str) -> list[Entry]:
        all_entries = []
        for categoty_value in self._data.values():
            all_entries.extend([Entry(entry) for entry in categoty_value])
        if query == "ALL":
            return all_entries
        found = [entry for entry in all_entries if query.lower() in entry.record_name.lower() or query in entry.username.lower()]
        return found
        
        

        
        


# def main():
#     D = "./KeyKeeperDataFile.kkdf"
#     df = DataFile(D, "pass")
#     # df.create()
#     df.load_data()
#     # print(df)
    
#     cats = df.get_categories()
#     c = cats[0]
#     # c2 = cats[2]
#     # c2.remove()
#     for cat in cats:
#         print(cat.name)
#     # c.new_row()
#     # r = c.get_row(1)
#     # r.record_name = "new_name"
#     # c.remove_row(r)
#     r = c.get_row(1)
#     # r.record_name = "again"
#     # r.password = "******"
#     # c.get_row(0).record_name = "111"
#     for r in c.content:
#         print(r)
   


# if __name__ == "__main__":
#     main()