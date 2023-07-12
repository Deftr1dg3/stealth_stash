#!/usr/bin/env python3


import wx 
from gui.command import Command
from gui.topbar.top_left_panel import TopLeftPanel
from gui.topbar.top_mid_panel import TopMidPanel
from gui.topbar.top_right_panel import TopRightPanel

class TopBarPanel(wx.Panel):
    def __init__(self, main_panel: wx.Panel, command: Command):
        self._command = command
        self._main_panel = main_panel
        super().__init__(self._main_panel, size=(-1, 30))
        
        self._colours = self._command.colours()
        self._background_colour = self._colours.TOP_BAR
        
        self.SetBackgroundColour(self._background_colour)
        
        self._init_ui()
        
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        left_box = wx.BoxSizer(wx.VERTICAL)
        mid_box = wx.BoxSizer(wx.VERTICAL)
        right_box = wx.BoxSizer(wx.VERTICAL)
        
        top_left_panel = TopLeftPanel(self, self._command)
        top_mid_panel = TopMidPanel(self, self._command)
        top_right_panel = TopRightPanel(self, self._command)
        
        left_box.Add(top_left_panel, 1, wx.EXPAND)
        mid_box.Add(top_mid_panel, 1, wx.EXPAND)
        right_box.Add(top_right_panel, 1, wx.EXPAND)
        
        main_box.Add(left_box, 0 , wx.EXPAND)
        main_box.Add(mid_box, 1 , wx.EXPAND)
        main_box.Add(right_box, 0 , wx.EXPAND)
        
        self.SetSizer(main_box)
        self.Layout()