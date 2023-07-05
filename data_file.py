#!/usr/bin/env python3

from __future__ import annotations
import json 
import atexit
from aes import AES_Encripton
from exceptions import UnreadableToDecodeTheFile


class Row:
    def __init__(self, row: list = ["New Record", "", "", "", ""]):
        self._row = row 
      
    @property    
    def row(self) -> list:
        return self._row
        
    @property
    def record_name(self) -> str:
        return self._row[0]
    
    @record_name.setter
    def record_name(self, new_value: str) -> None:
        self._row[0] = new_value
        
    @property
    def username(self) -> str:
        return self._row[1]
    
    @username.setter
    def username(self, new_value: str) -> None:
        self._row[1] = new_value
        
    @property
    def password(self) -> str:
        return self._row[2]
    
    @password.setter
    def password(self, new_value: str) -> None:
        self._row[2] = new_value
        
    @property
    def url(self) -> str:
        return self._row[3]
    
    @url.setter
    def url(self, new_value: str) -> None:
        self._row[3] = new_value
        
    @property
    def notes(self) -> str:
        return self._row[4]
    
    @notes.setter
    def notes(self, new_value: str) -> None:
        self._row[4] = new_value
    

class Category:
    def __init__(self, name: str, data_file: DataFile) -> None:
        self._data_file = data_file
        self._name = name 
        
    @property
    def name(self) -> str:
        return self._name
        
    def get_content(self) -> list[Row]:
        content = self._data_file.get_category_content(self._name)
        return content
    
    def rename(self, new_name: str) -> None:
        self._data_file.rename_category(self.name, new_name)
        self._name = new_name
    
    def remove(self) -> None:
        self._data_file.delete_category(self.name)
    
    def remove_row(self, row: Row) -> None:
        content = self.get_content()
        index = content.index(row)
        self._data_file.delete_row_from_category(self.name, index)
    
    def get_row(self, index) -> Row:
        content = self.get_content()
        return content[index]
    
    def new_row(self) -> Row:
        new_row = Row()
        self._data_file.add_row_to_categoty(self.name, new_row.row)
        return new_row
        
    
class Data(dict):
    def __init__(self):
        super().__init__()
        self["General"] = []
        self["Internet"] = []
        self["Email"] = []


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
    def __init__(self, file_path: str, password: str) -> None:
        self._aes_encription = AES_Encripton(password)
        self._io_data = IODataFile(file_path)
        atexit.register(self.commit)
    
    def create(self) -> None:
        self._data = Data()
        self.commit()
    
    def load_data(self) -> None:
        encrypted_str_data = self._io_data.get_data()
        try:
            json_data = self._aes_encription.decrypt(encrypted_str_data)
        except ValueError:
            raise UnreadableToDecodeTheFile()
        self._data = json.loads(json_data)
        
    def commit(self):
        try:
            json_data = json.dumps(self._data)
        except AttributeError:
            return 
        bytes_data = json_data.encode("utf-8")
        encrypted_str_data = self._aes_encription.encrypt(bytes_data)
        self._io_data.save_data(encrypted_str_data)
    
    def get_category_content(self, category: str) -> list[Row]:
        categoty_data = [Row(row) for row in self._data[category]]
        return categoty_data
            
    def add_category(self, categoty: str) -> None:
        self._data[categoty] = []
        
    def rename_category(self, category: str, new_name: str) -> None:
        keys = list(self._data.keys())
        values = list(self._data.values())
        categoty_index = keys.index(category)
        keys[categoty_index] = new_name
        self._data = dict(zip(keys, values))
        
    def delete_category(self, category: str) -> None:
        del self._data[category]
        
    def add_row_to_categoty(self, category: str, row: list[str]) -> None:
        self._data[category].append(row)
        
    def delete_row_from_category(self, category: str, row_index: int) -> None:
        del self._data[category][row_index]
    
    def get_categories(self) -> list[Category]:
        categories = [Category(category, self) for category in self._data.keys()]
        return categories
        
        
            
        
        


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