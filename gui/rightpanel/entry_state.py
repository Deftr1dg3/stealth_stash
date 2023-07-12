#!/usr/bin/env python3


import time
from typing import NamedTuple
from data_file import Entry
from collections import defaultdict
from typing import DefaultDict


# STARTS HERE
class EntrySnapshot(NamedTuple):
    record_name: str
    username: str 
    password: str
    url: str 
    notes: str
    

class EntryState:
    _entry_states: DefaultDict[int, list[EntrySnapshot]] = defaultdict(list)
    _cursor_states: DefaultDict[int, int] = defaultdict(lambda: -1)
    
    def __init__(self, entry: Entry) -> None:
        self._entry = entry 
        self._id = entry.id
        self._cursor = self._cursor_states[self._id]
        self.is_ready = False
        # print(f"{self._cursor=}")
    
    # def display_states(self):
    #     i = 0
    #     for s in self._entry_states[self._id]:
    #         print(f"{i} --> {s.record_name}, {s.username}, {s.password}, {s.url}, {s.notes}")
    #         i += 1
    #     print(f"{self._cursor=}")
        
    def _update_cursor(self) -> None:
        self._cursor += 1
        self._cursor_states[self._id] = self._cursor
        if self._cursor > 0:
            self.is_ready = True

    def _move_back(self) -> None:
        if self._entry_states[self._id]:
            self._cursor -= 1 
            if self._cursor < 0:
                self._cursor = 0
        self._cursor_states[self._id] = self._cursor
        
    def _move_forvard(self) -> None:
        if self._entry_states[self._id]:
            self._cursor += 1
            if self._cursor > len(self._entry_states[self._id]) - 1:
                self._cursor = len(self._entry_states[self._id]) - 1
        self._cursor_states[self._id] = self._cursor
        
    def snapshot(self) -> None:
        record_name = self._entry.record_name
        username = self._entry.username
        password = self._entry.password 
        url = self._entry.url 
        notes = self._entry.notes 
        snapshot = EntrySnapshot(record_name=record_name, username=username, password=password, url=url, notes=notes)
        self._entry_states[self._id].insert(self._cursor + 1, snapshot)
        self._update_cursor()
       

    def undo(self) -> (EntrySnapshot | None):
        if not self._entry_states:
            return 
        self._move_back()
        snapshot = self._entry_states[self._id][self._cursor]
        self._entry.record_name = snapshot.record_name 
        self._entry.username = snapshot.username
        self._entry.password = snapshot.password
        self._entry.url = snapshot.url 
        self._entry.notes = snapshot.notes
        # self.display_states()
        return snapshot
    
    def reverse_undo(self) -> (EntrySnapshot | None):
        if not self._entry_states:
            return 
        self._move_forvard()
        snapshot = self._entry_states[self._id][self._cursor]
        self._entry.record_name = snapshot.record_name 
        self._entry.username = snapshot.username
        self._entry.password = snapshot.password
        self._entry.url = snapshot.url 
        self._entry.notes = snapshot.notes
        # self.display_states()
        return snapshot