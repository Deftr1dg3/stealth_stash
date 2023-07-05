#!/usr/bin/env python3


import wx 
from command import Command

class RightPanel(wx.Panel):
    def __init__(self, body_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._body_panel = body_panel
        super().__init__(self._body_panel, size=(250, -1))
        self.SetBackgroundColour("#E961DC")
