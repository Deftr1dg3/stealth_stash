#!/usr/bin/env python3


import wx 
import os
from data_file import DataFile
from gui.modals.popups import dialog_popup
from exceptions import UnableToDecodeTheFile
from gui.colours import ColourTheme
from config import PassowrdWindowConst

class GetPassword(wx.Frame):
    def __init__(self, data_file: DataFile, colour_theme: str) -> None:
        super().__init__(None, style=PassowrdWindowConst.STYLE, size=PassowrdWindowConst.SIZE, title=PassowrdWindowConst.TITLE)
        
        self.SetBackgroundColour(ColourTheme.AVAILABLE_COLOUR_SCHEMES[colour_theme].MID_PANEL)
        
        self._data_file = data_file
        
        self.CenterOnScreen()
        
        self._init_ui()
        self._bind_events()
        
        
    def _init_ui(self) -> None:
        panel = wx.Panel(self)
        
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        input_box = wx.BoxSizer(wx.HORIZONTAL)
        buttons_box = wx.BoxSizer(wx.HORIZONTAL)
        
        self._password = wx.TextCtrl(panel, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER, size=(200, -1))
        self._password.SetHint(PassowrdWindowConst.PASSOWRD_HINT)
        self._password.SetFocus()
        
        self._choose_datafile = wx.Button(panel, label=PassowrdWindowConst.CHOOSE_DATAFILE_LABEL)
        
        input_box.Add(self._password, 1, wx.ALIGN_CENTER)

        main_box.Add(input_box, 1, wx.ALIGN_CENTER)
        main_box.Add(buttons_box, 1, wx.EXPAND)
        
        panel.SetSizer(main_box)
        panel.Layout()
        
        
    def _bind_events(self) -> None:
        self._choose_datafile.Bind(wx.EVT_BUTTON, self._on_choose_another_datafile)
        self._password.Bind(wx.EVT_TEXT_ENTER, self._on_key_down)
        self.Bind(wx.EVT_CLOSE, self._on_close)

        
    def _on_key_down(self, event) -> None:
        self._on_confirm(None)
        
        
    def _on_confirm(self, event) -> None:
        password = self._password.GetValue()
        try:
            self._data_file.password = password
            self._data_file.load_data()
            self.Destroy()
        except UnableToDecodeTheFile:
            another_try = dialog_popup(PassowrdWindowConst.DIALOG_MESSAGE, PassowrdWindowConst.DIALOG_TITLE, yes_default=True)
            if not another_try:
                os._exit(0)
            self._password.SetValue("")
        
    def _on_clear(self, event) -> None:
        self._password.SetValue("")
        
    def _on_choose_another_datafile(self, event) -> None:
        print("choose file")
        
    def _on_close(self, event) -> None:
        os._exit(0)


def launch_get_password(data_file: DataFile, colour_theme: str):
    app = wx.App()
    GetPassword(data_file, colour_theme).Show()
    app.MainLoop()
    
