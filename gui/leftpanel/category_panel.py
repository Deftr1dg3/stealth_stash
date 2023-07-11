#!/usr/bin/env python3


import wx
from gui.colours import Colours
from config import LeftPanelConst


class CategoryPanel(wx.Panel):
    def __init__(self, left_panel: wx.Panel, category_name: str) -> None:
        self._name = self._format_category_name(category_name)
        self._left_panel = left_panel
        super().__init__(self._left_panel, size=LeftPanelConst.CATEGORY_PANEL_SIZE)
        # Initializing visible objects
        self._init_ui()
        
    def _init_ui(self) -> None:
        """ Function initializing visible interface. """
        # Create main sizer
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        # Create gui object
        self._category_name = wx.StaticText(self, label=self._name)
        self._category_name.SetForegroundColour(Colours.TEXT)
        # Add gui object to the main sizer
        main_box.Add(self._category_name, 0, wx.TOP | wx.LEFT, 6)
        # Set main sizer to the panel
        self.SetSizer(main_box)
        # Refresh lauout
        self.Layout()
        
    def _format_category_name(self, category_name: str) -> str:
        if len(category_name) > LeftPanelConst.CATEGORY_NAME_MAX_LENGTH:
            category_name = category_name[:LeftPanelConst.CATEGORY_NAME_MAX_LENGTH] + LeftPanelConst.EXTRA_CHARACTERS_REPLACEMENT
        return category_name
    
    def set_colour(self, colour: wx.Colour) -> None:
        self._category_name.SetForegroundColour(colour)
        self.Refresh()  