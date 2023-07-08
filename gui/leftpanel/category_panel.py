#!/usr/bin/env python3


import wx
from gui.colours import Colours


class CategoryPanel(wx.Panel):
    def __init__(self, left_panel: wx.Panel, category_name: str) -> None:
        self._name = self._format_category_name(category_name)
        self._left_panel = left_panel
        super().__init__(self._left_panel, size=(200, 30))
        self._init_ui()
        
    def _init_ui(self) -> None:
        # main_box.AddStretchSpacer()
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        self._category_name = wx.StaticText(self, label=self._name)
        self._category_name.SetForegroundColour(Colours.TEXT)
        main_box.Add(self._category_name, 0, wx.TOP | wx.LEFT, 6)
        self.SetSizer(main_box)
        self.Layout()
        
    def _format_category_name(self, category_name: str) -> str:
        if len(category_name) > 21:
            category_name = category_name[:21] + "..."
        return category_name
    
    def set_colour(self, colour: wx.Colour) -> None:
        self._category_name.SetForegroundColour(colour)
        self.Refresh()  