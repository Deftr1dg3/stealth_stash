#!/usr/bin/env python3


import wx
from dataclasses import dataclass
from typing import NamedTuple

app = wx.App() 
 
@dataclass   
class Colours:
    TEXT = wx.Colour(wx.WHITE)       # RGB for wx.WHITE
    SELECTION = wx.Colour(wx.BLUE)
    TOP_BAR = wx.Colour("#323232")   # RGB for "#51BC5F"
    LEFT_PANEL = wx.Colour("#B36179")
    MID_PANEL = wx.Colour("#614CC2")
    RIGHT_PANEL = wx.Colour("#E961DC")
    
    
