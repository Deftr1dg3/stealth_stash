#!/usr/bin/env python3


import wx 
from gui.command import Command
from data_file import Entry


class EntryRightClickMenu(wx.Menu):
    def __init__(self, parent: wx.Panel, command: Command, entry: Entry) -> None:
        self._command = command 
        self._parent = parent 
        self._entry = entry
        super().__init__()
        self._init_menu()
        self._bind_events()
        
    def _init_menu(self) -> None:
        self.Append(1, 'Remove')
   
    def _bind_events(self) -> None:
        self.Bind(wx.EVT_MENU, self._remove_entry, id=1)
        
    def _remove_entry(self, event) -> None:
        self._command.remove_entry(self._entry)