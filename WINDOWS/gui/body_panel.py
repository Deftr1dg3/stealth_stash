#!/usr/bin/env python3


import wx 
from command import Command
from gui.leftpanel.left_panel import LeftPanel
from gui.midpanel.mid_panel import MidPanel
from gui.rightpanel.right_panel import RightPanel



class BodyPanel(wx.Panel):
    def __init__(self, main_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._main_panel = main_panel
        super().__init__(self._main_panel)
        
        self._colours = self._command.colours()
        
        self._background_colour = self._colours.BODY_PANEL
        self.SetBackgroundColour(self._background_colour)
                        
        self._init_ui()
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        left_box = wx.BoxSizer(wx.VERTICAL)
        mid_box = wx.BoxSizer(wx.VERTICAL)
        right_box = wx.BoxSizer(wx.VERTICAL)
        
        self._left_panel = LeftPanel(self, self._command)
        self._command.left = self._left_panel
        self._mid_panel = MidPanel(self, self._command)
        self._command.mid = self._mid_panel
        self._right_panel = RightPanel(self, self._command)
        self._command.right = self._right_panel
        
        left_box.Add(self._left_panel, 1, wx.EXPAND | wx.TOP, 1)
        mid_box.Add(self._mid_panel, 1, wx.EXPAND)
        right_box.Add(self._right_panel, 1, wx.EXPAND | wx.TOP, 1)
        
        main_box.Add(left_box, 0, wx.EXPAND)
        main_box.Add(mid_box, 1, wx.EXPAND)
        main_box.Add(right_box, 0, wx.EXPAND)
        
        self.SetSizer(main_box)
        self.Layout()