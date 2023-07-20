#!/usr/bin/env python3


import wx 
from command import Command
from gui.rightpanel.edit_panel import EditPanel
from gui.rightpanel.notes_panel import NotesPanel
from config import RightPanelConst


class RightPanel(wx.Panel):
    def __init__(self, body_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._body_panel = body_panel
        self._panel_size = RightPanelConst.PANEL_SIZE
        super().__init__(self._body_panel, size=self._panel_size)
        
        self._colours = self._command.colours()
        self._background_colour = self._colours.RIGHT_PANEL
        
        # Initializing visible objects
        self._init_ui()
        
        self.SetBackgroundColour(self._background_colour)
        
        
    @property
    def notes_panel(self) -> NotesPanel:
        return self._notes_panel
    
    @property
    def edit_panel(self) -> EditPanel:
        return self._edit_panel
    
        
    def _init_ui(self):
        """ Function initializing visible interface. """
        
        # Create main sizer
        self._main_box = wx.BoxSizer(wx.VERTICAL)
        
        # Create secondary sizers
        edit_box = wx.BoxSizer(wx.HORIZONTAL)
        notes_box = wx.BoxSizer(wx.HORIZONTAL)
        
        # Create GUI objects
        self._notes_panel = NotesPanel(self, self._command)
        self._edit_panel = EditPanel(self, self._command)
        
        # Add GUI objects to secondary sizers
        edit_box.Add(self._edit_panel, 1, wx.EXPAND)
        notes_box.Add(self._notes_panel, 1, wx.EXPAND)
        
        # Add secondary sizers to the main sizer
        self._main_box.Add(edit_box, 1, wx.EXPAND)
        self._main_box.Add(notes_box, 0, wx.EXPAND)
        
        # Add main sizer tot eh panel
        self.SetSizer(self._main_box)
        
        # Refresh layout
        self.Layout()
        
    def refresh(self):
        self._main_box.Clear(True)
        self._init_ui()
        
    def undo_availbale(self, arg: bool) -> None:
        self._edit_panel.undo_available = arg
        
    def make_snapshot(self) -> None:
        self._edit_panel.make_snapshot()
        
    def undo_in_progress_notes(self, arg: bool) -> None:
        self._notes_panel.undo_in_progress = arg
        
    def set_notes_value(self, value: str) -> None:
        self._notes_panel.set_value(value)