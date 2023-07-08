#!/usr/bin/env python3


import wx 
from gui.command import Command
from gui.colours import Colours


class TopRightPanel(wx.Panel):
    def __init__(self, top_bar: wx.Panel, command: Command):
        self._top_bar = top_bar
        self._command = command 
        super().__init__(self._top_bar, size=(250, 30))
        
        self._init_ui()
        self._bind_events()
        
        self.SetBackgroundColour(Colours.TOP_BAR)
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        title_box = wx.BoxSizer(wx.VERTICAL)
        # button_box = wx.BoxSizer(wx.VERTICAL)
  
        entry_edit_title = wx.StaticText(self, label="Edit Entry:")
        # self._theme_button =  wx.Button(self, label=Colours.THEM_BUTTON, size=(30, -1))
        
        title_box.Add(entry_edit_title, 0, wx.TOP | wx.LEFT, 7)
        # button_box.Add(self._theme_button, 0, wx.TOP | wx.RIGHT, 5)
        
        main_box.Add(title_box, 0, wx.EXPAND)
        main_box.AddStretchSpacer()
        # main_box.Add(button_box, 0, wx.EXPAND)
        
        self.SetSizer(main_box)
        self.Layout()
        
    def _bind_events(self):
        # self._theme_button.Bind(wx.EVT_BUTTON, self._change_colour_theme)
        ...
        
    def _change_colour_theme(self, event):
        self._command.chnage_theme()