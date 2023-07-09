#!/usr/bin/env python3


import wx
from dataclasses import dataclass
from typing import NamedTuple


app = wx.App() 
 

class ColoursDefinition(NamedTuple):
    TEXT: wx.Colour      
    SELECTION: wx.Colour 
    BODY_PANEL: wx.Colour
    TOP_BAR: wx.Colour 
    LEFT_PANEL: wx.Colour 
    MID_PANEL: wx.Colour 
    ENTRY_BACKGROUND: wx.Colour 
    RIGHT_PANEL: wx.Colour 
    PEN: wx.Colour 
    TEXTCTRL_BACKGROUND: wx.Colour
    THEM_BUTTON: str
    
    
MOON_SIMPLE = "\U0000263D"
SUN_SIMPLE = "\U00002600"

EMOJI_SUN = "\U0001F31E"
EMOJI_DARK_MOON = "\U0001F311"
EMOJI_PARTIAL_MOON = "\U0001F312"
EMOJI_LIGHT_MOON = "\U0001F315"
SUN = "🔆"

@dataclass
class ColourTheme:
    DARK = ColoursDefinition(TEXT=wx.Colour(wx.WHITE),    # RGB for wx.WHITE
                            SELECTION=wx.Colour("#763771"),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour("#252525"),
                            TOP_BAR=wx.Colour("#343434"),
                            LEFT_PANEL=wx.Colour("#343434"), 
                            MID_PANEL=wx.Colour("#252525"),
                            ENTRY_BACKGROUND=wx.Colour("#252525"), 
                            RIGHT_PANEL=wx.Colour("#343434"), 
                            PEN=wx.Colour("#343434"), 
                            TEXTCTRL_BACKGROUND = wx.Colour("#252525"),
                            THEM_BUTTON=SUN_SIMPLE
                            )
    
    LIGHT = ColoursDefinition(TEXT=wx.Colour(wx.WHITE),    # RGB for wx.WHITE
                            SELECTION=wx.Colour("#763771"),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour("#252525"),
                            TOP_BAR=wx.Colour("#343434"),
                            LEFT_PANEL=wx.Colour("#343434"), 
                            MID_PANEL=wx.Colour("#252525"),
                            ENTRY_BACKGROUND=wx.Colour("#252525"), 
                            RIGHT_PANEL=wx.Colour("#343434"), 
                            PEN=wx.Colour("#343434"), 
                            TEXTCTRL_BACKGROUND = wx.Colour("#252525"),
                            THEM_BUTTON=MOON_SIMPLE
                            )
    
  

Colours = ColourTheme.DARK