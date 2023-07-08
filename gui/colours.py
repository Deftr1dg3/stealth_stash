#!/usr/bin/env python3


import wx
from dataclasses import dataclass
from typing import NamedTuple
from gui.command import Command

app = wx.App() 
 

class ColoursDefinition(NamedTuple):
    TEXT: wx.Colour      
    SELECTION: wx.Colour 
    TOP_BAR: wx.Colour 
    LEFT_PANEL: wx.Colour 
    MID_PANEL: wx.Colour 
    ENTRY_BACKGROUND: wx.Colour 
    RIGHT_PANEL: wx.Colour 
    PEN: wx.Colour 
    THEM_BUTTON: str
    
    
MOON_SIMPLE = "\U0000263D"
SUN_SIMPLE = "\U00002600"

EMOJI_SUN = "\U0001F31E"
EMOJI_DARK_MOON = "\U0001F311"
EMOJI_PARTIAL_MOON = "\U0001F312"
EMOJI_LIGHT_MOON = "\U0001F315"
SUN = "🔆"


class ColourTheme:
    def _light(self) -> ColoursDefinition:
        TEXT = wx.Colour(wx.BLACK)       # RGB for wx.WHITE
        SELECTION = wx.Colour(wx.BLUE)
        TOP_BAR = wx.Colour("#323232")   # RGB for "#51BC5F"
        LEFT_PANEL = wx.Colour("#B36179")
        MID_PANEL = wx.Colour("#614CC2")
        ENTRY_BACKGROUND = wx.Colour("#614CC2")
        RIGHT_PANEL = wx.Colour("#E961DC")
        PEN = wx.Colour("#323232")
        THEM_BUTTON = MOON_SIMPLE
        colours = ColoursDefinition(TEXT=TEXT, SELECTION=SELECTION,\
            TOP_BAR=TOP_BAR, LEFT_PANEL=LEFT_PANEL, MID_PANEL=MID_PANEL,\
            ENTRY_BACKGROUND=ENTRY_BACKGROUND, RIGHT_PANEL=RIGHT_PANEL, PEN=PEN, THEM_BUTTON=THEM_BUTTON)
        return colours
        
    def _dark(self) -> ColoursDefinition:
        TEXT = wx.Colour(wx.WHITE)       # RGB for wx.WHITE
        SELECTION = wx.Colour("#763771")
        TOP_BAR = wx.Colour("#343434")   # RGB for "#51BC5F"
        LEFT_PANEL = wx.Colour("#343434")
        MID_PANEL = wx.Colour("#252525")
        ENTRY_BACKGROUND = wx.Colour("#252525")
        RIGHT_PANEL = wx.Colour("#343434")
        PEN = wx.Colour("#343434")
        THEM_BUTTON = SUN_SIMPLE
        colours = ColoursDefinition(TEXT=TEXT, SELECTION=SELECTION,\
            TOP_BAR=TOP_BAR, LEFT_PANEL=LEFT_PANEL, MID_PANEL=MID_PANEL,\
            ENTRY_BACKGROUND=ENTRY_BACKGROUND, RIGHT_PANEL=RIGHT_PANEL, PEN=PEN, THEM_BUTTON=THEM_BUTTON)
        return colours
    
    def get_colours(self, theme: bool) -> ColoursDefinition:
        if theme:
            return self._dark()
        else:
            return self._light()
        
  
theme = ColourTheme()  
Colours = theme.get_colours(True)