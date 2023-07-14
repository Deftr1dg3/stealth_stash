#!/usr/bin/env python3


import wx
from command import Command

class TopBarMenu(wx.MenuBar):
    def __init__(self, main_frame: wx.Frame, command: Command):
        super().__init__()
        self._main_frame = main_frame
        self._command = command
        self._init_menu()
        self._bind_events()
        
    def _init_menu(self):
        # Create "File" menu
        file_menu = wx.Menu()
        file_menu.Append(1, "&New Category\tShift+Ctrl+N")
        file_menu.Append(2, "&New Entry\tCtrl+N")
        file_menu.Append(3, "&Remove Category\tShift+Ctrl+D")
        file_menu.Append(4, "&Remove Entry\tCtrl+D")
        file_menu.AppendSeparator()
        file_menu.Append(5, "&Clear Catogory")
        file_menu.AppendSeparator()
        file_menu.AppendSeparator()
        file_menu.Append(30, "&Exit\tCtrl+Q")

        self.Append(file_menu, "&File")

        # Create "Edit" menu
        edit_menu = wx.Menu()
        edit_menu.Append(31, "&Undo\tCtrl+Z")
        edit_menu.Append(32, "&Reverse Undo\tShift+Ctrl+Z")

        self.Append(edit_menu, "&Edit")
        
    def _bind_events(self):
        # Bind "File" menu
        self._main_frame.Bind(wx.EVT_MENU, self._on_add_category, id=1)
        self._main_frame.Bind(wx.EVT_MENU, self._on_add_entry, id=2)
        self._main_frame.Bind(wx.EVT_MENU, self._on_remove_category, id=3)
        self._main_frame.Bind(wx.EVT_MENU, self._on_remove_entry, id=4)
        self._main_frame.Bind(wx.EVT_MENU, self._on_clear_category, id=5)
        
        self._main_frame.Bind(wx.EVT_MENU, self._on_exit, id=30)
        # Bind "Edit" menu
        self._main_frame.Bind(wx.EVT_MENU, self._on_undo, id=31)
        self._main_frame.Bind(wx.EVT_MENU, self._on_reverse_undo, id=32)

    def _on_add_category(self, event) -> None:
        self._command.add_category(self._main_frame)
        
    def _on_remove_category(self, event) -> None:
        self._command.remove_category()
    
    def _on_clear_category(self, event) -> None:
        self._command.clear_category()

    def _on_add_entry(self, event) -> None:
        self._command.add_entry()
    
    def _on_remove_entry(self, event) -> None:
        self._command.remove_entry()

    def _on_exit(self, event) -> None:
        # self._main_frame = wx.GetApp().GetTopWindow()
        self._main_frame.Destroy()
    
    def _on_undo(self, event) -> None:
        try:
            self._command.manage_entry_states()
        except AttributeError:
            pass
    
    def _on_reverse_undo(self, event) -> None:
        try:
            self._command.manage_entry_states(0)
        except AttributeError:
            pass