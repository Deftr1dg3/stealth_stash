#!/usr/bin/env python3


import wx
from data_file import Entry
from command import Command 
from gui.midpanel.entry_row import EntryRow
from config import MidPanelConst


class MidPanel(wx.Panel):
    def __init__(self, body_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._body_panel = body_panel
        self._entry_rows: dict[int, EntryRow] = {}
        super().__init__(self._body_panel)
        
        self._scroll_settings = MidPanelConst.SCROLL_SETTINGS
        
        # Initializing visible objects
        self._init_ui()
        
    def _init_ui(self):
        """ Function initializing visible interface. """
        
        # Create main sizer
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        # Create ScrolledWindow
        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(*self._scroll_settings)
        
        # Sizer for ScrolledWindow.
        scroll_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # If query is not None, will be dispayed search results
        if self._command.query:
            self._command.refresh_left()
            entries = self._command.search()
            for entry in entries:
                # Create visible EntryRow object
                self._display_entry(self.scroll, scroll_sizer, entry)
                
            # Relay entry_row dict to the Command module
            self._command.entry_rows = self._entry_rows
            
            #clear self._entry_rows after each cycle to store entries only from current cycle
            self._entry_rows = {}
            
        # Else will be dispayed category content, if selected else Nothing
        else:
            if self._command.selected_category_row is not None:
                entries = self._command.selected_category_row.category.get_content()
                for entry in entries:
                    # Create visible EntryRow object
                    self._display_entry(self.scroll, scroll_sizer, entry)
                    
                # Relay entry_row dict to the Command module
                self._command.entry_rows = self._entry_rows
                # Clear self._entry_rows after each cycle to store entries only from current cycle
                
                self._entry_rows = {}
                
        # Add sizer to ScrolledWindow
        self.scroll.SetSizer(scroll_sizer)
        
        # Add scroll window to the main sizer
        main_box.Add(self.scroll, 1, wx.EXPAND)
        
        # Set main sizer to the panel
        self.SetSizer(main_box)
        
        # Refresh lauout
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