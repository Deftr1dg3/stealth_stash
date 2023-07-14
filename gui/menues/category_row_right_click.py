#!/usr/bin/env python3


import wx 
from command import Command
from data_file import Category
from config import MenueConst

class CategoryRightClickMenu(wx.Menu):
    def __init__(self, parent: wx.Panel, command: Command, category: Category) -> None:
        self._command = command 
        self._parent = parent 
        self._category = category
        super().__init__()
        self._init_menu()
        self._bind_events()
        
    def _init_menu(self) -> None:
        self.Append(1, f'&{MenueConst.RENAME_CATEGORY_LABEL}')
        self.Append(2, f'&{MenueConst.REMOVE_CATEGORY_LABEL}\t{MenueConst.REMOVE_CATEGORY_SHORTCUT}')
        self.AppendSeparator()
        self.Append(3, f'&{MenueConst.CLEAR_CATEGORY_LABEL}')

    def _bind_events(self) -> None:
        self.Bind(wx.EVT_MENU, self._on_rename_category, id=1)
        self.Bind(wx.EVT_MENU, self._on_remove_category, id=2)
        self.Bind(wx.EVT_MENU, self._on_clear_category, id=3)
        
    def _on_rename_category(self, event) -> None:
        self._command.rename_category()
        
    def _on_remove_category(self, event) -> None:
        self._command.remove_category()
    
    def _on_clear_category(self, event) -> None:
        self._command.clear_category()