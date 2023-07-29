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
        
        self._init_menu()
        self._bind_events()
        
    def _init_menu(self) -> None:
        self.Append(421, f"&{MenueConst.COPY_PASSOWRD_LABEL}\t{MenueConst.COPY_PASSOWRD_SHORTCUT}")
        self.Append(422, f"&{MenueConst.COPY_USERNALE_LABEL}\t{MenueConst.COPY_USERNAME_SHORTCUT}")
        self.Append(423, f"&{MenueConst.COPY_URL_LABEL}\t{MenueConst.COPY_URL_SHORTCUT}")
        self.AppendSeparator()
        self.Append(35, f"&{MenueConst.MOVE_ENTRY_UP_LABLE}")
        self.Append(36, f"&{MenueConst.MOVE_ENTRY_DOWN_LABLE}")
        self.AppendSeparator()
        self.Append(33, f"&{MenueConst.REMOVE_ENTRY_LABEL}\t{MenueConst.REMOVE_ENTRY_SHORTCUT}")
   
    def _bind_events(self) -> None:
        self.Bind(wx.EVT_MENU, self._on_copy_password, id=421)
        self.Bind(wx.EVT_MENU, self._on_copy_username, id=422)
        self.Bind(wx.EVT_MENU, self._on_copy_url, id=423)
        self.Bind(wx.EVT_MENU, self._on_remove_entry, id=33)
        self.Bind(wx.EVT_MENU, self._on_move_entry_up, id=35)
        self.Bind(wx.EVT_MENU, self._on_move_entry_down, id=36)
        
    def _on_move_entry_up(self, event) -> None:
        self._command.move_entry_up()
    
    def _on_move_entry_down(self, event) -> None:
        self._command.move_entry_down() 
        
    def _on_copy_password(self, event) -> None:
        self._command.copy_password()
        
    def _on_copy_username(self, event) -> None:
        self._command.copy_username()
    
    def _on_copy_url(self, event) -> None:
        self._command.copy_url()
               
    def _on_remove_entry(self, event) -> None:
        self._command.remove_entry(self._entry)