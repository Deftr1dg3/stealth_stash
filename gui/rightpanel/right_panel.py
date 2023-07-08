#!/usr/bin/env python3


import wx 
from gui.command import Command
from gui.colours import Colours
from gui.rightpanel.edit_panel import EditPanel
from gui.rightpanel.notes_panel import NotesPanel

class RightPanel(wx.Panel):
    def __init__(self, body_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._body_panel = body_panel
        super().__init__(self._body_panel, size=(250, -1))
        
        self._background_colour = Colours.RIGHT_PANEL
        
        self.SetBackgroundColour(self._background_colour)
        
        self._init_ui()
        self._bind_events()
        
    def _init_ui(self):
        self._main_box = wx.BoxSizer(wx.VERTICAL)
        edit_box = wx.BoxSizer(wx.HORIZONTAL)
        notes_box = wx.BoxSizer(wx.HORIZONTAL)
        
        edit_panel = EditPanel(self, self._command)
        notes_panel = NotesPanel(self, self._command)
        
        edit_box.Add(edit_panel, 1, wx.EXPAND)
        notes_box.Add(notes_panel, 1, wx.EXPAND)
        
        self._main_box.Add(edit_box, 1, wx.EXPAND)
        self._main_box.Add(notes_box, 0, wx.EXPAND)
        
        self.SetSizer(self._main_box)
        self.Layout()
        
           
    def _bind_events(self):
        ...

    def refresh(self):
        self._main_box.Clear(True)
        self._init_ui()