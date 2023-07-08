#!/usr/bin/env python3


import wx 
from gui.command import Command
from data_file import Entry


class NotesPanel(wx.Panel):
    def __init__(self, right_panel: wx.Panel, command: Command) -> None:
        self._right_panel = right_panel
        self._command = command
        super().__init__(self._right_panel)
        
        self._entry: Entry
        
        self._title = "Notes:"
        
        self._init_ui()
        self._bind_events()
        
    @property
    def entry(self) -> Entry:
        return self._entry
    
    @entry.setter
    def entry(self, entry: Entry) -> None:
        self._entry = entry
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.VERTICAL)
        title_box = wx.BoxSizer(wx.HORIZONTAL)
        notes_box = wx.BoxSizer(wx.HORIZONTAL)
        
        title = wx.StaticText(self, label=self._title)
        self._notes = wx.TextCtrl(self, size=(-1, 150), style=wx.TE_MULTILINE)
        if self._command.selected_entry_row is None:
            self._notes.Disable()
        else:
            self.entry = self._command.selected_entry_row.entry
            notes = self.entry.notes
            self._notes.SetValue(notes)
        
        title_box.Add(title, 1, wx.EXPAND)
        notes_box.Add(self._notes, 1, wx.EXPAND)
        
        main_box.Add(title_box, 0, wx.EXPAND | wx.ALL, 5)
        main_box.Add(notes_box, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(main_box)
        self.Layout()
        
    def _bind_events(self):
        self._notes.Bind(wx.EVT_TEXT, self._on_typing)
        
    def _on_typing(self, event):
        value = self._notes.GetValue()
        self.entry.notes = value