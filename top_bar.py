#!/usr/bin/env python3


import wx 
from command import Command
from topbar.top_left_panel import TopLeftPanel

class TopBarPanel(wx.Panel):
    def __init__(self, main_panel: wx.Panel, command: Command):
        self._command = command
        self._main_panel = main_panel
        self._colour = wx.Colour("#313131")
        super().__init__(self._main_panel, size=(-1, 30))
        self.SetBackgroundColour("#51BC5F")
        self._init_ui()
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        left_box = wx.BoxSizer(wx.VERTICAL)
        mid_box = wx.BoxSizer(wx.VERTICAL)
        right_box = wx.BoxSizer(wx.VERTICAL)
        
        top_left_panel = TopLeftPanel(self, self._command, self._colour)
        
        
        left_box.Add(top_left_panel, 1, wx.EXPAND)
        
        
        main_box.Add(left_box, 0 , wx.EXPAND)
        main_box.Add(mid_box, 0 , wx.EXPAND)
        main_box.Add(right_box, 0 , wx.EXPAND)
        
        self.SetSizer(main_box)
        self.Layout()