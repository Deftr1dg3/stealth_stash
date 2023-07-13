#!/usr/bin/env python3


import os
import sys
import wx 
from gui.main_panel import MainPanel
from gui.command import Command
from gui.menues.top_menu import TopBarMenu


class MainFrame(wx.Frame):
    def __init__(self, command: Command) -> None:
        super().__init__(None)
        self._command = command
        self._command.main_frame = self
        self.SetSize((1100, 600))
        self.SetTitle('Key Keeper')
        self.SetMinSize((800, 400))
        self._init_ui()
        
    def _init_ui(self) -> None:
        MainPanel(self, self._command)
        self.SetMenuBar(TopBarMenu(self, self._command))
        
    def restart(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
    

def launch_gui(command: Command) -> None:
    app = wx.App()
    MainFrame(command).Show()
    app.MainLoop()