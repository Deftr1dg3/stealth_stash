#!/usr/bin/env python3


import wx 
from command import Command
from data_file import Entry
from gui.rightpanel.entry_state import EntryState
from config import RightPanelConst
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.rightpanel.right_panel import RightPanel


class NotesPanel(wx.Panel):
    def __init__(self, right_panel: "RightPanel", command: Command) -> None:
        self._right_panel = right_panel
        self._command = command
        super().__init__(self._right_panel)
        
        self._entry: Entry
        
        self._title = RightPanelConst.NOTES_TITLE
        self._notes_field_size = RightPanelConst.NOTES_FIELD_SIZE
        
        self._colours = self._command.colours()
        self._background_colour = self._colours.RIGHT_PANEL
        self._input_background_colour = self._colours.INPUT_BACKGROUND
        self._text_colour = self._colours.TEXT
        
        self._undo_in_progress = False
        
        self.SetBackgroundColour(self._background_colour)
        
        # Initializing visible objects and binding events
        self._init_ui()
        self._bind_events()
        
        
    @property
    def entry(self) -> Entry:
        return self._entry
    
    @entry.setter
    def entry(self, entry: Entry) -> None:
        self._entry = entry
        
    @property
    def undo_in_progress(self) -> bool:
        return self._undo_in_progress
    
    @undo_in_progress.setter
    def undo_in_progress(self, arg: bool) -> None:
        self._undo_in_progress = arg

        
    def _init_ui(self):
        """ Function initializing visible interface. """
        
        # Create main sizer
        self._main_box = wx.BoxSizer(wx.VERTICAL)
        
        # Create secondary sizers
        title_box = wx.BoxSizer(wx.HORIZONTAL)
        notes_box = wx.BoxSizer(wx.HORIZONTAL)
        
        # Create GUI objects
        title = wx.StaticText(self, label=self._title)
        title.SetForegroundColour(self._text_colour)
        self._notes = wx.TextCtrl(self, size=self._notes_field_size, style=wx.TE_MULTILINE)
        self._notes.SetForegroundColour(self._text_colour)
        self._notes.SetBackgroundColour(self._input_background_colour)
        
        # Enable or disable GUI objects depending on selected EntryRow
        if self._command.selected_entry_row is None:
            self._notes.Disable()
        else:
            self.entry = self._command.selected_entry_row.entry
            notes = self.entry.notes
            self._notes.SetValue(notes)
        
        # Add GUI objects to secondary sizers
        title_box.Add(title, 1, wx.EXPAND)
        notes_box.Add(self._notes, 1, wx.EXPAND)
        
        # Add secondary sizers to the main sizer
        self._main_box.Add(title_box, 0, wx.EXPAND | wx.ALL, 5)
        self._main_box.Add(notes_box, 1, wx.EXPAND | wx.ALL, 5)
        
        # Set main sizer to the panel
        self.SetSizer(self._main_box)
        
        # Refresh lauout
        self.Layout()
        
    def _bind_events(self):
        self._notes.Bind(wx.EVT_TEXT, self._on_typing)
        self._notes.Bind(wx.EVT_SET_FOCUS, self._on_set_focus)
    
    def _on_set_focus(self, evet) -> None:
        self._right_panel.undo_availbale(True)
        
    def _on_typing(self, event):
        value = self._notes.GetValue()
        self.entry.notes = value
        if not self.undo_in_progress:
            self._right_panel.make_snapshot()
        
    def set_value(self, value: str) -> None:
        self._notes.SetValue(value)
        self._notes.SetInsertionPointEnd()