#!/usr/bin/env python3


import wx
from data_file import Category
from gui.colours import Colours
from gui.leftpanel.category_row import CategoryRow
from gui.command import Command

class LeftPanel(wx.Panel):
    def __init__(self, body_panel: wx.Panel, command: Command) -> None:
        self._command = command
        self._body_panel = body_panel
        self._category_row_list: list = []
        super().__init__(self._body_panel, size=(200, -1))
        
        self._background_colour = Colours.LEFT_PANEL
        
        self.SetBackgroundColour(self._background_colour)
        self._init_ui()
    
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(20, 20, 50, 50)

        # Sizer for scrolled window
        scroll_sizer = wx.BoxSizer(wx.VERTICAL)
        
        for category in self._command.list_categories():
            self._display_category(self.scroll, scroll_sizer, category)  

        self._command.category_row_list = self._category_row_list
        
        self.scroll.SetSizer(scroll_sizer)
        main_box.Add(self.scroll, 1, wx.EXPAND)
        
        self.SetSizer(main_box)
        self.Layout()
        
    def _display_category(self, scroll, scroll_sizer, category: Category) -> None:
        category_row = CategoryRow(scroll, category, self._command)
        self._category_row_list.append(category_row)
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
