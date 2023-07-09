#!/usr/bin/env python3


import wx 
from typing import NamedTuple
from data_file import Entry
from gui.command import Command


class EntrySnapshot(NamedTuple):
    record_name: str
    username: str 
    password: str
    url: str 
    notes: str
    

class EntryState:
    _entry_states: list[EntrySnapshot] = []
    
    def __init__(self, entry: Entry) -> None:
        self._entry = entry 
        self._cursor = -1
    
    @property
    def entry_states(self) -> list[EntrySnapshot]:
        return self._entry_states
    
    @entry_states.setter
    def entry_states(self, lst: list) -> None:
        self._entry_states = []
        
    def _update_cursor(self) -> None:
        self._cursor = len(self._entry_states) - 1
        
    def _move_back(self) -> None:
        if self._entry_states:
            self._cursor -= 1 
            if self._cursor < 0:
                self._cursor = 0
        
    def _move_forvard(self) -> None:
        if self._entry_states:
            self._cursor += 1
            if self._cursor > len(self._entry_states) - 1:
                self._cursor = len(self._entry_states) - 1
        
    def snapshot(self) -> None:
        record_name = self._entry.record_name
        username = self._entry.username
        password = self._entry.password 
        url = self._entry.url 
        notes = self._entry.notes 
        snapshot = EntrySnapshot(record_name=record_name, username=username, password=password, url=url, notes=notes)
        self._entry_states.append(snapshot)
        self._update_cursor()

    def undo(self) -> (EntrySnapshot | None):
        if not self._entry_states:
            return 
        self._move_back()
        snapshot = self._entry_states[self._cursor]
        self._entry.record_name = snapshot.record_name 
        self._entry.username = snapshot.username
        self._entry.password = snapshot.password
        self._entry.url = snapshot.url 
        self._entry.notes = snapshot.notes
        return snapshot
    
    def reverse_undo(self) -> (EntrySnapshot | None):
        if not self._entry_states:
            return 
        self._move_forvard()
        snapshot = self._entry_states[self._cursor]
        self._entry.record_name = snapshot.record_name 
        self._entry.username = snapshot.username
        self._entry.password = snapshot.password
        self._entry.url = snapshot.url 
        self._entry.notes = snapshot.notes
        return snapshot