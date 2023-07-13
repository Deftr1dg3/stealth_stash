#!/usr/bin/env python3


import wx
from dataclasses import dataclass
from typing import NamedTuple


app = wx.App() 
 

class ColoursAssignment(NamedTuple):
    TEXT: wx.Colour      
    SELECTION: wx.Colour 
    BODY_PANEL: wx.Colour
    TOP_BAR: wx.Colour 
    LEFT_PANEL: wx.Colour 
    MID_PANEL: wx.Colour 
    ENTRY_BACKGROUND: wx.Colour 
    RIGHT_PANEL: wx.Colour 
    INPUT_BACKGROUND: wx.Colour
    PEN: wx.Colour 
    TEXTCTRL_BACKGROUND: wx.Colour

    
    
MOON_SIMPLE = "\U0000263D"
SUN_SIMPLE = "\U00002600"

EMOJI_SUN = "\U0001F31E"
EMOJI_DARK_MOON = "\U0001F311"
EMOJI_PARTIAL_MOON = "\U0001F312"
EMOJI_LIGHT_MOON = "\U0001F315"
SUN = "🔆"

@dataclass
class ColourTheme:
    DARK_DARK = wx.Colour("#252525")
    DARK_MEDIUM = wx.Colour("#343434")
    DARK_SELECTION = wx.Colour("#339CB4")
    DARK_TEXT = wx.Colour(wx.WHITE)
    
    DARK = ColoursAssignment(TEXT=wx.Colour(DARK_TEXT),    # RGB for wx.WHITE
                            SELECTION=wx.Colour(DARK_SELECTION),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour(DARK_DARK),
                            TOP_BAR=wx.Colour(DARK_MEDIUM),
                            LEFT_PANEL=wx.Colour(DARK_MEDIUM), 
                            MID_PANEL=wx.Colour(DARK_DARK),
                            ENTRY_BACKGROUND=wx.Colour(DARK_DARK), 
                            RIGHT_PANEL=wx.Colour(DARK_MEDIUM), 
                            INPUT_BACKGROUND=wx.Colour(DARK_DARK),
                            PEN=wx.Colour(DARK_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(DARK_DARK),
                            )
    
    LIGHT_DARK = wx.Colour("#C6C6C6")
    LIGHT_MEDIUM = wx.Colour("#EEEEEE")
    LIGHT_SELECTION = wx.Colour("#339CB4")
    LIGHT_TEXT = wx.Colour(wx.BLACK)
    
    LIGHT = ColoursAssignment(TEXT=wx.Colour(LIGHT_TEXT),    # RGB for wx.WHITE
                            SELECTION=wx.Colour(LIGHT_SELECTION),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour(LIGHT_DARK),
                            TOP_BAR=wx.Colour(LIGHT_MEDIUM),
                            LEFT_PANEL=wx.Colour(LIGHT_MEDIUM), 
                            MID_PANEL=wx.Colour(LIGHT_DARK),
                            ENTRY_BACKGROUND=wx.Colour(LIGHT_DARK), 
                            RIGHT_PANEL=wx.Colour(LIGHT_MEDIUM), 
                            INPUT_BACKGROUND=wx.Colour(LIGHT_DARK),
                            PEN=wx.Colour(LIGHT_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(LIGHT_DARK),
                            )
    
    LIGHT_GREEN_DARK = wx.Colour("#003942")
    LIGHT_GREEN_MEDIUM = wx.Colour("#004952")
    LIGHT_GREEN_SELECTION = wx.Colour("#1991A0")
    LIGHT_GREEN_TEXT = wx.Colour(wx.WHITE)
    
    LIGHT_GREEN = ColoursAssignment(TEXT=wx.Colour(LIGHT_GREEN_TEXT),    # RGB for wx.WHITE
                            SELECTION=wx.Colour(LIGHT_GREEN_SELECTION),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour(LIGHT_GREEN_DARK),
                            TOP_BAR=wx.Colour(LIGHT_GREEN_MEDIUM),
                            LEFT_PANEL=wx.Colour(LIGHT_GREEN_MEDIUM), 
                            MID_PANEL=wx.Colour(LIGHT_GREEN_DARK),
                            ENTRY_BACKGROUND=wx.Colour(LIGHT_GREEN_DARK), 
                            RIGHT_PANEL=wx.Colour(LIGHT_GREEN_MEDIUM), 
                            INPUT_BACKGROUND=wx.Colour(LIGHT_GREEN_DARK),
                            PEN=wx.Colour(LIGHT_GREEN_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(LIGHT_GREEN_DARK),
                            )
    
    BLUE_DARK = wx.Colour("#002958")
    BLUE_MEDIUM = wx.Colour("#003764")
    BLUE_SELECTION = wx.Colour("#265F8F")
    BLUE_TEXT = wx.Colour(wx.WHITE)
    
    BLUE = ColoursAssignment(TEXT=wx.Colour(BLUE_TEXT),    # RGB for wx.WHITE
                            SELECTION=wx.Colour(BLUE_SELECTION),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour(BLUE_DARK),
                            TOP_BAR=wx.Colour(BLUE_MEDIUM),
                            LEFT_PANEL=wx.Colour(BLUE_MEDIUM), 
                            MID_PANEL=wx.Colour(BLUE_DARK),
                            ENTRY_BACKGROUND=wx.Colour(BLUE_DARK), 
                            RIGHT_PANEL=wx.Colour(BLUE_MEDIUM), 
                            INPUT_BACKGROUND=wx.Colour(BLUE_DARK),
                            PEN=wx.Colour(BLUE_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(BLUE_DARK),
                            )
    
    BURGUNDY_DARK = wx.Colour("#37171E")
    BURGUNDY_MEDIUM = wx.Colour("#431B24")
    BURGUNDY_SELECTION = wx.Colour("#9C263F")
    BURGUNDY_TEXT = wx.Colour(wx.WHITE)
    
    BURGUNDY = ColoursAssignment(TEXT=wx.Colour(BURGUNDY_TEXT),    # RGB for wx.WHITE
                            SELECTION=wx.Colour(BURGUNDY_SELECTION),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour(BURGUNDY_DARK),
                            TOP_BAR=wx.Colour(BURGUNDY_MEDIUM),
                            LEFT_PANEL=wx.Colour(BURGUNDY_MEDIUM), 
                            MID_PANEL=wx.Colour(BURGUNDY_DARK),
                            ENTRY_BACKGROUND=wx.Colour(BURGUNDY_DARK), 
                            RIGHT_PANEL=wx.Colour(BURGUNDY_MEDIUM), 
                            INPUT_BACKGROUND=wx.Colour(BURGUNDY_DARK),
                            PEN=wx.Colour(BURGUNDY_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(BURGUNDY_DARK),
                            )