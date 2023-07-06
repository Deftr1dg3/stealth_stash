#!/usr/bin/env python3


import wx
from gui.command import Command 
from gui.colours import Colours

class MidPanel(wx.Panel):
    def __init__(self, body_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._body_panel = body_panel
        super().__init__(self._body_panel)
        
        self._background_colour = Colours.MID_PANEL
        
        self.SetBackgroundColour(self._background_colour)