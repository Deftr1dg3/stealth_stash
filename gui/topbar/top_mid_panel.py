#!/usr/bin/env python3


import wx 
from gui.command import Command
from gui.colours import Colours


class TopMidPanel(wx.Panel):
    def __init__(self, top_bar: wx.Panel, command: Command):
        self._top_bar = top_bar
        self._command = command 
        super().__init__(self._top_bar)
        
        self._init_ui()
        self._bind_events()
        
        self.SetBackgroundColour(Colours.TOP_BAR)
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        button_box = wx.BoxSizer(wx.VERTICAL)
        search_box = wx.BoxSizer(wx.VERTICAL)
        
        self.add = wx.Button(self, label='Entry  +')
        self.search = wx.TextCtrl(self, size=(200, -1))
        self.search.SetHint('Search record ...')

        button_box.Add(self.add, 0, wx.EXPAND | wx.LEFT, 10)
        search_box.Add(self.search, 0, wx.EXPAND)


        main_box.Add(button_box, 0, wx.ALL | wx.EXPAND, 5)
        main_box.AddStretchSpacer()
        main_box.Add(search_box, 0, wx.ALL | wx.EXPAND, 3)
        
        self.SetSizer(main_box)
        self.Layout()

    def _bind_events(self):
        self.add.Bind(wx.EVT_BUTTON, self._add_entry)
        self.search.Bind(wx.EVT_TEXT, self._on_search)
        
    def _add_entry(self, event) -> None:
        self._command.add_entry()
        
    def _on_search(self, event) -> None:
        query = self.search.GetValue()
        self._command.query = query
        self._command.refresh_mid()
    
