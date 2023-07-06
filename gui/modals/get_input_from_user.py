#!/usr/bin/env python3

import wx

def get_input(parent: (wx.Panel | wx.Frame), hint: str) -> (str | None):
    user_input = None
    dlg = wx.TextEntryDialog(parent, hint)
    if dlg.ShowModal() == wx.ID_OK:
        user_input = dlg.GetValue()
    dlg.Destroy()
    return user_input


