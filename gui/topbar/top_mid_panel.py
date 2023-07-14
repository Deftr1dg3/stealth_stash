#!/usr/bin/env python3


import wx 
from command import Command
from config import TopBarConst


class TopMidPanel(wx.Panel):
    def __init__(self, top_bar: wx.Panel, command: Command):
        self._top_bar = top_bar
        self._command = command 
        super().__init__(self._top_bar)
        
        self._colours = self._command.colours()
        self._text_colour = self._colours.TEXT
        self._input_background_colour = self._colours.INPUT_BACKGROUND
        
        # Initializing visible objects and bindig events
        self._init_ui()
        self._bind_events() 
        
    def _init_ui(self):
        # Create main sizer
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        
        # Create secondary sizers, that will be added to the main sizer.
        button_box = wx.BoxSizer(wx.VERTICAL)
        search_box = wx.BoxSizer(wx.VERTICAL)
        
        # Create gui objects
        self._new_entry = wx.Button(self, label=TopBarConst.NEW_ENTRY_LABEL)

        self._search = wx.TextCtrl(self, size=TopBarConst.SEARCH_FILED_SIZE)
        self._search.SetHint(TopBarConst.SEARCH_PLACE_HOLDER)
        self._search.SetForegroundColour(self._text_colour)
        self._search.SetBackgroundColour(self._input_background_colour)
        
        # Add created objects to the sizers
        button_box.Add(self._new_entry, 0, wx.EXPAND | wx.LEFT, 10)
        search_box.Add(self._search, 0, wx.EXPAND)
        
        # Add sizers to the main sizer.
        main_box.Add(button_box, 0, wx.ALL | wx.EXPAND, 5)
        main_box.AddStretchSpacer()
        
        main_box.Add(search_box, 0, wx.ALL | wx.EXPAND, 3)
        
        # Set main sizer to the panel
        self.SetSizer(main_box)
        
        # Refresh layout
        self.Layout()

    def _bind_events(self):
        self._new_entry.Bind(wx.EVT_BUTTON, self._add_entry)
        self._search.Bind(wx.EVT_TEXT, self._on_search)
        
    def _add_entry(self, event) -> None:
        self._command.add_entry()
        
    def _on_search(self, event) -> None:
        query = self._search.GetValue()
        self._command.query = query
        self._command.refresh_mid()
        self._command.refresh_right()