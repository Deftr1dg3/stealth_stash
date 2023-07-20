#!/usr/bin/env python3



from typing import NamedTuple
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
    
    def __init__(self, entry_id: int) -> None:
        self._id = entry_id
        self._cursor = self._cursor_states[self._id]
        self.is_ready = False
        
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
        
    def snapshot(self, snapshot: EntrySnapshot) -> None:
        self._entry_states[self._id].insert(self._cursor + 1, snapshot)
        self._update_cursor()

    def undo(self) -> EntrySnapshot:
        self._move_back()
        snapshot = self._entry_states[self._id][self._cursor]
        return snapshot
    
    def reverse_undo(self) -> EntrySnapshot:
        self._move_forvard()
        snapshot = self._entry_states[self._id][self._cursor]
        return snapshot