#!/usr/bin/env python3


import wx
from data_file import Entry
from gui.command import Command 
from gui.colours import Colours, ColoursDefinition
from gui.midpanel.entry_row import EntryRow


class MidPanel(wx.Panel):
    def __init__(self, body_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._body_panel = body_panel
        self._entry_rows: dict[int, EntryRow] = {}
        super().__init__(self._body_panel)
        
        self._init_ui()
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(20, 20, 50, 50)

        # Sizer for scrolled window
        scroll_sizer = wx.BoxSizer(wx.VERTICAL)
        
        if self._command.selected_category_row is not None:
            entries = self._command.selected_category_row.category.get_content()
            for entry in entries:
                self._display_entry(self.scroll, scroll_sizer, entry)
            
            self._command.entry_rows = self._entry_rows
            
            self._entry_rows = {}
        
        self.scroll.SetSizer(scroll_sizer)
        main_box.Add(self.scroll, 1, wx.EXPAND)
        
        self.SetSizer(main_box)
        self.Layout()
        
    def _display_entry(self, scroll, scroll_sizer, entry: Entry) -> None:
        entry_row = EntryRow(scroll, entry, self._command)
        self._entry_rows[entry_row.id] = entry_row
        scroll_sizer.Add(entry_row, 0, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, 1)
        
    def _clear_categories(self):
        # Get the sizer from the ScrolledWindow
        scroll_sizer = self.scroll.GetSizer()

        # Destroy all children of the ScrolledWindow
        for child in self.scroll.GetChildren():
            child.Destroy()

        # Clear the sizer
        scroll_sizer.Clear(True)

        # Layout the sizer
        scroll_sizer.Layout()
        self.Layout()
        
    def refresh(self):
        self._clear_categories()
        self._init_ui()
        self._command.selected_entry_row = None
        
    def set_colour_scheme(self, colours: ColoursDefinition) -> None:
        self.SetBackgroundColour(Colours.MID_PANEL)
        self.Refresh()
        
