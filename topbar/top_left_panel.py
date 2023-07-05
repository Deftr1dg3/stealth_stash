#!/usr/bin/env python3


import wx 
from command import Command


class TopLeftPanel(wx.Panel):
    def __init__(self, top_bar: wx.Panel, command: Command, colour: wx.Colour):
        self._top_bar = top_bar
        self._command = command 
        super().__init__(self._top_bar, size=(200, 30))
        self._init_ui()
        self._bind_events()
        
        self.SetBackgroundColour(colour)
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        
        main_box.AddStretchSpacer()
        self.add = wx.Button(self, label='Add  +', size=(180, -1))
        main_box.Add(self.add, 0, wx.ALIGN_CENTRE)
        main_box.AddStretchSpacer()
        
        self.SetSizer(main_box)
        self.Layout()
        
    def _bind_events(self):
        self.add.Bind(wx.EVT_BUTTON, self._add_category)
        
    def _add_category(self, event):
        self._command.add_category(self)
        