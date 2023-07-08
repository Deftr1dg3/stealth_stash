#!/usr/bin/env python3

import wx

def get_input(hint: str, title: str, default_value: str = "") -> (str | None):
    user_input = None
    dlg = wx.TextEntryDialog(None, hint, title, default_value)
    if dlg.ShowModal() == wx.ID_OK:
        user_input = dlg.GetValue()
    dlg.Destroy()
    return user_input

def message_popup(message: str, title: str) -> None:
        dlg = wx.MessageDialog(None, message, title, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
def dialog_popup(message: str, title: str) -> bool:
    dialog = wx.MessageDialog(None, message, title, wx.YES_NO | wx.ICON_QUESTION | wx.NO_DEFAULT)
    result = dialog.ShowModal()
    dialog.Destroy()
    if result == wx.ID_YES:
        return True
    return False
