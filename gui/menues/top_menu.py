#!/usr/bin/env python3


import wx
from gui.command import Command

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
        file_menu.AppendSeparator()
        file_menu.Append(3, "&Exit\tCtrl+Q")

        self.Append(file_menu, "&File")

        # Create "Edit" menu
        edit_menu = wx.Menu()
        edit_menu.Append(31, "&Copy\tCtrl+C")
        edit_menu.Append(32, "&Paste\tCtrl+V")

        self.Append(edit_menu, "&Edit")
        
    def _bind_events(self):
        # Bind "File" menu
        self._main_frame.Bind(wx.EVT_MENU, self._add_category, id=1)
        self._main_frame.Bind(wx.EVT_MENU, self._add_entry, id=2)
        self._main_frame.Bind(wx.EVT_MENU, self.on_exit, id=3)
        # Bind "Edit" menu
        self._main_frame.Bind(wx.EVT_MENU, self.on_copy, id=31)
        self._main_frame.Bind(wx.EVT_MENU, self.on_paste, id=32)

    def _add_category(self, event):
        self._command.add_category(self._main_frame)

    def _add_entry(self, event):
        self._command.add_entry()

    def on_exit(self, event):
        # self._main_frame = wx.GetApp().GetTopWindow()
        self._main_frame.Destroy()

    def on_copy(self, event):
        print("Copy clicked!")

    def on_paste(self, event):
        print("Paste clicked!")