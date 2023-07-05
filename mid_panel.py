#!/usr/bin/env python3


import wx
from command import Command 


class MidPanel(wx.Panel):
    def __init__(self, body_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._body_panel = body_panel
        size = self._body_panel.GetSize()
        super().__init__(self._body_panel)
        self.SetBackgroundColour("#614CC2")