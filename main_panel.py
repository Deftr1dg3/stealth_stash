#!/usr/bin/env python3

import wx
import os 
import sys
from top_bar import TopBarPanel
from body_panel import BodyPanel

main_scope_path = os.path.abspath("../")
sys.path.append(main_scope_path)

from command import Command


class MainPanel(wx.Panel):
    def __init__(self, main_frame: wx.Frame, command: Command) -> None:
        self._command = command
        self._main_frame = main_frame
        super().__init__(self._main_frame)
        self._init_ui()
        self.SetBackgroundColour("#D0D366")
        # screen_size = wx.DisplaySize()
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.VERTICAL)
        top_bar_box = wx.BoxSizer(wx.HORIZONTAL)
        body_box = wx.BoxSizer(wx.HORIZONTAL)
        
        top_bar_panel = TopBarPanel(self, self._command)
        self._command.top = top_bar_panel
        body_panel = BodyPanel(self, self._command)
        
        top_bar_box.Add(top_bar_panel, 1, wx.EXPAND)
        body_box.Add(body_panel, 1, wx.EXPAND)
        
        main_box.Add(top_bar_box, 0, wx.EXPAND)
        main_box.Add(body_box, 1, wx.EXPAND | wx.TOP, 0)
        
        self.SetSizer(main_box)
        
        