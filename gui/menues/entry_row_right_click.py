#!/usr/bin/env python3


import wx 
from command import Command
from data_file import Entry
from config import MenueConst


class EntryRightClickMenu(wx.Menu):
    def __init__(self, parent: wx.Panel, command: Command, entry: Entry) -> None:
        self._command = command 
        self._parent = parent 
        self._entry = entry
        super().__init__()
        
        self._remove_button_label = MenueConst.REMOVE_ENTRY_LABEL
        self._remove_button_shortcut = MenueConst.REMOVE_ENTRY_SHORTCUT
        
        self._init_menu()
        self._bind_events()
        
    def _init_menu(self) -> None:
        self.Append(421, f"&{MenueConst.COPY_PASSOWRD_LABEL}\t{MenueConst.COPY_PASSOWRD_SHORTCUT}")
        self.Append(422, f"&{MenueConst.COPY_USERNALE_LABEL}\t{MenueConst.COPY_USERNAME_SHORTCUT}")
        self.Append(423, f"&{MenueConst.COPY_URL_LABEL}\t{MenueConst.COPY_URL_SHORTCUT}")
        self.AppendSeparator()
        self.Append(33, f"&{self._remove_button_label}\t{self._remove_button_shortcut}")
   
    def _bind_events(self) -> None:
        self.Bind(wx.EVT_MENU, self._on_copy, id=421)
        self.Bind(wx.EVT_MENU, self._on_copy, id=422)
        self.Bind(wx.EVT_MENU, self._on_copy, id=423)
        self.Bind(wx.EVT_MENU, self._on_remove_entry, id=33)
        
    def _on_copy(self, event) -> None:
        id = event.GetId()
        self._command.copy_to_clipboard(id)
               
    def _on_remove_entry(self, event) -> None:
        self._command.remove_entry(self._entry)