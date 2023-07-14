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
    COLOUR_CHANGING_STEP: int

    
class ColourTheme:
    
    DARK_DARK = wx.Colour("#252525")
    DARK_MEDIUM = wx.Colour("#343434")
    DARK_INPUT_BACKGROUND = wx.Colour("#252525")
    DARK_SELECTION = wx.Colour("#3739D7")
    DARK_TEXT = wx.Colour(wx.WHITE)
    
    DARK = ColoursAssignment(TEXT=wx.Colour(DARK_TEXT),    # RGB for wx.WHITE
                            SELECTION=wx.Colour(DARK_SELECTION),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour(DARK_DARK),
                            TOP_BAR=wx.Colour(DARK_MEDIUM),
                            LEFT_PANEL=wx.Colour(DARK_MEDIUM), 
                            MID_PANEL=wx.Colour(DARK_DARK),
                            ENTRY_BACKGROUND=wx.Colour(DARK_DARK), 
                            RIGHT_PANEL=wx.Colour(DARK_MEDIUM), 
                            INPUT_BACKGROUND=wx.Colour(DARK_INPUT_BACKGROUND),
                            PEN=wx.Colour(DARK_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(DARK_DARK),
                            COLOUR_CHANGING_STEP = 6
                            )
    
    LIGHT_DARK = wx.Colour("#C6C6C6")
    LIGHT_MEDIUM = wx.Colour("#EEEEEE")
    LIGHT_INPUT_BACKGROUND = wx.Colour("#C6C6C6")
    LIGHT_SELECTION = wx.Colour("#0011FF")
    LIGHT_TEXT = wx.Colour(wx.BLACK)
    
    LIGHT = ColoursAssignment(TEXT=wx.Colour(LIGHT_TEXT),    # RGB for wx.WHITE
                            SELECTION=wx.Colour(LIGHT_SELECTION),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour(LIGHT_DARK),
                            TOP_BAR=wx.Colour(LIGHT_MEDIUM),
                            LEFT_PANEL=wx.Colour(LIGHT_MEDIUM), 
                            MID_PANEL=wx.Colour(LIGHT_DARK),
                            ENTRY_BACKGROUND=wx.Colour(LIGHT_DARK), 
                            RIGHT_PANEL=wx.Colour(LIGHT_MEDIUM), 
                            INPUT_BACKGROUND=wx.Colour(LIGHT_INPUT_BACKGROUND),
                            PEN=wx.Colour(LIGHT_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(LIGHT_DARK),
                            COLOUR_CHANGING_STEP = 6
                            )
    
    LIGHT_GREEN_DARK = wx.Colour("#003942")
    LIGHT_GREEN_MEDIUM = wx.Colour("#004952")
    LIGHT_GREEN_INPUT_BACKGROUND = wx.Colour("#002B34")
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
                            INPUT_BACKGROUND=wx.Colour(LIGHT_GREEN_INPUT_BACKGROUND),
                            PEN=wx.Colour(LIGHT_GREEN_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(LIGHT_GREEN_DARK),
                            COLOUR_CHANGING_STEP = 3
                            )
    
    BLUE_DARK = wx.Colour("#002958")
    BLUE_MEDIUM = wx.Colour("#003764")
    BLUE_INPUT_BACKGROUND = wx.Colour("#002958")
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
                            INPUT_BACKGROUND=wx.Colour(BLUE_INPUT_BACKGROUND),
                            PEN=wx.Colour(BLUE_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(BLUE_DARK),
                            COLOUR_CHANGING_STEP = 3
                            )
    
    BURGUNDY_DARK = wx.Colour("#37171E")
    BURGUNDY_MEDIUM = wx.Colour("#431B24")
    BURGUNDY_INPUT_BACKGROUND = wx.Colour("#37171E")
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
                            INPUT_BACKGROUND=wx.Colour(BURGUNDY_INPUT_BACKGROUND),
                            PEN=wx.Colour(BURGUNDY_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(BURGUNDY_DARK),
                            COLOUR_CHANGING_STEP = 3
                            )
    # Change starts here juugbh  iubhjh iubjbn
    PURPLE_DARK = wx.Colour("#350C63")
    PURPLE_MEDIUM = wx.Colour("#471183")
    PURPLE_INPUT_BACKGROUND = wx.Colour("#270053")
    PURPLE_SELECTION = wx.Colour("#963AFD")
    PURPLE_TEXT = wx.Colour(wx.WHITE)
    
    PURPLE = ColoursAssignment(TEXT=wx.Colour(PURPLE_TEXT),    # RGB for wx.WHITE
                            SELECTION=wx.Colour(PURPLE_SELECTION),   # RGB for "#51BC5F"
                            BODY_PANEL = wx.Colour(PURPLE_DARK),
                            TOP_BAR=wx.Colour(PURPLE_MEDIUM),
                            LEFT_PANEL=wx.Colour(PURPLE_MEDIUM), 
                            MID_PANEL=wx.Colour(PURPLE_DARK),
                            ENTRY_BACKGROUND=wx.Colour(PURPLE_DARK), 
                            RIGHT_PANEL=wx.Colour(PURPLE_MEDIUM), 
                            INPUT_BACKGROUND=wx.Colour(PURPLE_INPUT_BACKGROUND),
                            PEN=wx.Colour(PURPLE_MEDIUM), 
                            TEXTCTRL_BACKGROUND = wx.Colour(PURPLE_DARK),
                            COLOUR_CHANGING_STEP = 5
                            )
    
    
    AVAILABLE_COLOUR_SCHEMES= {"DARK": DARK, 
                                "LIGHT": LIGHT,
                                "LIGHT_GREEN": LIGHT_GREEN,
                                "BLUE": BLUE,
                                "BURGUNDY": BURGUNDY,
                                "PURPLE": PURPLE
                                }