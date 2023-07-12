#!/usr/bin/env python3


import wx 
from gui.command import Command
from data_file import Entry
from gui.rightpanel.entry_state import EntryState
from config import RightPanelConst


class NotesPanel(wx.Panel):
    def __init__(self, right_panel: wx.Panel, command: Command) -> None:
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
        
    def _init_ui(self):
        """ Function initializing visible interface. """
        
        # Create main sizer
        main_box = wx.BoxSizer(wx.VERTICAL)
        
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
        main_box.Add(title_box, 0, wx.EXPAND | wx.ALL, 5)
        main_box.Add(notes_box, 1, wx.EXPAND | wx.ALL, 5)
        
        # Set main sizer to the panel
        self.SetSizer(main_box)
        
        # Refresh lauout
        self.Layout()
        
    def _bind_events(self):
        self._notes.Bind(wx.EVT_TEXT, self._on_typing)
        
    def _on_typing(self, event):
        value = self._notes.GetValue()
        self.entry.notes = value