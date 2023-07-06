#!/usr/bin/env python3


import wx 
from gui.command import Command
from gui.colours import Colours


class TopRightPanel(wx.Panel):
    def __init__(self, top_bar: wx.Panel, command: Command):
        self._top_bar = top_bar
        self._command = command 
        super().__init__(self._top_bar, size=(250, 30))
        
        self._init_ui()
        
        self.SetBackgroundColour(Colours.TOP_BAR)
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        
        main_box.AddStretchSpacer()
        entry_edit_title = wx.StaticText(self, label="Edit Entry:")
        main_box.Add(entry_edit_title, 0, wx.ALIGN_CENTRE)
        main_box.AddStretchSpacer()
        
        self.SetSizer(main_box)
        self.Layout()
        
   
        