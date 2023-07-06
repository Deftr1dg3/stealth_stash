#!/usr/bin/env python3

import wx 
from gui.main_panel import MainPanel
from gui.command import Command
from gui.menues.top_menu import TopBarMenu
import os 


# os.chdir("/Users/stasusbondevito/Documents/PYTHON/Projects/KeyKeeper")

class MainFrame(wx.Frame):
    def __init__(self, command: Command) -> None:
        super().__init__(None)
        self._command = command
        self.SetSize((1000, 600))
        self.SetTitle('Key Keeper')
        self.SetMinSize((800, 400))
        self._init_ui()
        # self.SetBackgroundColour(wx.Colour(0,0,0,0))
        
    def _init_ui(self) -> None:
        MainPanel(self, self._command)
        self.SetMenuBar(TopBarMenu(self, self._command))
    
        
def launch_gui(command: Command) -> None:
    app = wx.App()
    MainFrame(command).Show()
    app.MainLoop()
    
    
# if __name__ == "__main__":
#     launch_gui()