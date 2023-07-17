#!/usr/bin/env python3


import os
import sys
import wx 
from command import Command
from gui.main_panel import MainPanel
from gui.menues.top_menu import TopBarMenu
from config import MainFrameConst


class MainFrame(wx.Frame):
    def __init__(self, command: Command) -> None:
        super().__init__(None)
        self._command = command
        self._command.main_frame = self
        
        self._colours = self._command.colours()
        
        self.SetBackgroundColour(self._colours.MID_PANEL)
        
        self.SetSize(MainFrameConst.SIZE)
        self.SetTitle(MainFrameConst.TITLE)
        self.SetMinSize(MainFrameConst.MIN_SIZE)
        
        self._init_ui()
        
    def _init_ui(self) -> None:
        MainPanel(self, self._command)
        self.SetMenuBar(TopBarMenu(self, self._command))
        
        self.Bind(wx.EVT_CLOSE, self._on_close)
        
    def _on_close(self, event) -> None:
        sys.exit(0)

    def restart(self) -> None:
        python = sys.executable
        os.execl(python, python, * sys.argv)
    

def launch_gui(command: Command) -> None:
    app = wx.App()
    MainFrame(command).Show()
    app.MainLoop()