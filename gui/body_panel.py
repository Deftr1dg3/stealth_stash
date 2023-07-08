#!/usr/bin/env python3


import wx 
from gui.colours import Colours
from gui.leftpanel.left_panel import LeftPanel
from gui.midpanel.mid_panel import MidPanel
from gui.rightpanel.right_panel import RightPanel
from gui.command import Command

class BodyPanel(wx.Panel):
    def __init__(self, main_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._main_panel = main_panel
        super().__init__(self._main_panel)
        
        self._text_colour = wx.Colour(wx.WHITE)
        self._selection_colour = wx.Colour(wx.BLUE)
        
        self._init_ui()
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        left_box = wx.BoxSizer(wx.VERTICAL)
        mid_box = wx.BoxSizer(wx.VERTICAL)
        right_box = wx.BoxSizer(wx.VERTICAL)
        
        left_panel = LeftPanel(self, self._command)
        self._command.left = left_panel
        mid_panel = MidPanel(self, self._command)
        self._command.mid = mid_panel
        right_panel = RightPanel(self, self._command)
        self._command.right = right_panel
        
        left_box.Add(left_panel, 1, wx.EXPAND | wx.TOP, 1)
        mid_box.Add(mid_panel, 1, wx.EXPAND)
        right_box.Add(right_panel, 1, wx.EXPAND | wx.TOP, 1)
        
        main_box.Add(left_box, 0, wx.EXPAND)
        main_box.Add(mid_box, 1, wx.EXPAND)
        main_box.Add(right_box, 0, wx.EXPAND)
        
        self.SetSizer(main_box)
        self.Layout()
        