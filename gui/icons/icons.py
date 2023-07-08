#!/usr/bin/env python3


import wx
from gui.colours import Colours

class IconPanel(wx.Panel):
    def __init__(self, parent: wx.Panel, icon: str, colour: wx.Colour) -> None:
        super().__init__(parent, size=(30, 30))
        self._icon = icon
        self._icon_colour = colour
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        # self.SetBackgroundColour("yellow")
        
    def _get_icon_function(self):
        match self._icon:
            case "folder":
                return self._folder_icon
            case _:
                raise TypeError(f"{self._icon} -> Unsupported Icon name!")
    
    def OnPaint(self, event) -> None:
        icon = self._get_icon_function()
        dc = wx.PaintDC(self)
        icon(dc)
        
    def _folder_icon(self, dc: wx.PaintDC) -> None:
        dc.SetPen(wx.Pen(wx.Colour(Colours.PEN), 1))
        dc.SetBrush(wx.Brush(self._icon_colour))
        dc.DrawRoundedRectangle(9, 6, 10, 10, 2)
        dc.DrawRoundedRectangle(7, 8, 23, 15, 3)
        
        