#!/usr/bin/env python3


import wx 
from gui.command import Command
from gui.colours import Colours
from config import TopBarConst


class TopLeftPanel(wx.Panel):
    def __init__(self, top_bar: wx.Panel, command: Command):
        self._top_bar = top_bar
        self._command = command 
        super().__init__(self._top_bar, size=TopBarConst.LEFT_PANEL_SIZE)
        
        self._init_ui()
        self._bind_events()
        
        self.SetBackgroundColour(Colours.TOP_BAR)
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        
        main_box.AddStretchSpacer()
        self.new_category = wx.Button(self, label=TopBarConst.NEW_CATEGORY_LABEL, size=TopBarConst.NEW_CATEGORY_BUTTON_SIZE)
        main_box.Add(self.new_category, 0, wx.ALIGN_CENTRE)
        main_box.AddStretchSpacer()
        
        self.SetSizer(main_box)
        self.Layout()
        
    def _bind_events(self):
        self.new_category.Bind(wx.EVT_BUTTON, self._add_category)
        
    def _add_category(self, event):
        self._command.add_category(self)
        