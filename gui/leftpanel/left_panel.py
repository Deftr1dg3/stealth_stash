#!/usr/bin/env python3


import wx
from command import Command
from data_file import Category
from gui.leftpanel.category_row import CategoryRow
from config import LeftPanelConst

class LeftPanel(wx.Panel):
    def __init__(self, body_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._body_panel = body_panel
        self._category_rows: dict[int, CategoryRow] = {}
        
        self._panel_size = LeftPanelConst.PANEL_SIZE
        self._scroll_settings = LeftPanelConst.SCROLL_SETTINGS
        
        super().__init__(self._body_panel, size=self._panel_size)
        
        self._colours = self._command.colours()
        self._background_colour = self._colours.LEFT_PANEL
        
        self.SetBackgroundColour(self._background_colour)

        # Initializing visible objects
        self._init_ui()

    
    def _init_ui(self):
        """ Function initializing visible interface. """
        
        # Create main sizer
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        # Create ScrolledWindow
        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(*self._scroll_settings)
        
        # Create secondary sizer for ScrolledWindow
        scroll_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create GUI objects
        for category in self._command.list_categories():
            self._display_category(self.scroll, scroll_sizer, category) 
             
        # Relay category_row list to the Command module
        self._command.category_rows = self._category_rows
        
        # Rest category rows dict 
        self._category_rows = {}
        
        # Add sizer to ScrolledWindow
        self.scroll.SetSizer(scroll_sizer)
        
        # Add scroll window to the main sizer
        main_box.Add(self.scroll, 1, wx.EXPAND)
        
        # Set main sizer to the panel
        self.SetSizer(main_box)
        
        # Refresh layout
        self.Layout()
        
    def _display_category(self, scroll, scroll_sizer, category: Category) -> None:
        category_row = CategoryRow(scroll, category, self._command)
        self._category_rows[category.id] = category_row
        scroll_sizer.Add(category_row, 0, wx.EXPAND)
        
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
        self._command.selected_category_row = None