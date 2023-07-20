#!/usr/bin/env python3

import wx
from command import Command
from gui.topbar.top_bar_panel import TopBarPanel
from gui.body_panel import BodyPanel


class MainPanel(wx.Panel):
    def __init__(self, main_frame: wx.Frame, command: Command) -> None:
        self._command = command
        self._main_frame = main_frame
        super().__init__(self._main_frame)
       
        self._init_ui()
   
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.VERTICAL)
        top_bar_box = wx.BoxSizer(wx.HORIZONTAL)
        body_box = wx.BoxSizer(wx.HORIZONTAL)
        
        self._top_bar_panel = TopBarPanel(self, self._command)
        self._command.top = self._top_bar_panel
        self._body_panel = BodyPanel(self, self._command)
        self._command.body_panel = self._body_panel
        
        top_bar_box.Add(self._top_bar_panel, 1, wx.EXPAND)
        body_box.Add(self._body_panel, 1, wx.EXPAND)
        
        main_box.Add(top_bar_box, 0, wx.EXPAND)
        main_box.Add(body_box, 1, wx.EXPAND | wx.TOP, 0)
        
        self.SetSizer(main_box)