#!/usr/bin/env python3


import wx


class TopBarMenu(wx.MenuBar):
    def __init__(self, frame):
        super().__init__()

        # Create "File" menu
        file_menu = wx.Menu()
        open_item = file_menu.Append(wx.ID_OPEN, "&Open\tCtrl+O")
        save_item = file_menu.Append(wx.ID_SAVE, "&Save\tCtrl+S")
        exit_item = file_menu.Append(wx.ID_EXIT, "&Exit\tCtrl+Q")

        frame.Bind(wx.EVT_MENU, self.on_open, open_item)
        frame.Bind(wx.EVT_MENU, self.on_save, save_item)
        frame.Bind(wx.EVT_MENU, self.on_exit, exit_item)

        self.Append(file_menu, "&File")

        # Create "Edit" menu
        edit_menu = wx.Menu()
        copy_item = edit_menu.Append(wx.ID_COPY, "&Copy\tCtrl+C")
        paste_item = edit_menu.Append(wx.ID_PASTE, "&Paste\tCtrl+V")

        frame.Bind(wx.EVT_MENU, self.on_copy, copy_item)
        frame.Bind(wx.EVT_MENU, self.on_paste, paste_item)

        self.Append(edit_menu, "&Edit")

    def on_open(self, event):
        print("Open clicked!")

    def on_save(self, event):
        print("Save clicked!")

    def on_exit(self, event):
        frame = wx.GetApp().GetTopWindow()
        frame.Close()

    def on_copy(self, event):
        print("Copy clicked!")

    def on_paste(self, event):
        print("Paste clicked!")