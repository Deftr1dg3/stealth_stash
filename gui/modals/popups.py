#!/usr/bin/env python3

import wx
from config import GeneralConst, SaveAsPopup, SelectFilePopup, SelectDirectoryPopup

def get_input(hint: str = "", title: str = "", default_value: str = "", parent: (wx.Panel | None) = None) -> (str | None):
    user_input = None
    dlg = wx.TextEntryDialog(parent, hint, title, default_value)
    if dlg.ShowModal() == wx.ID_OK:
        user_input = dlg.GetValue()
    dlg.Destroy()
    return user_input


def message_popup(message: str = "", title: str = "", parent: (wx.Panel | None) = None) -> None:
        dlg = wx.MessageDialog(parent, message, title, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        
        
def dialog_popup(message: str = "", title: str = "", yes_default=False, parent: (wx.Panel | None) = None) -> bool:
    if yes_default:
        dialog = wx.MessageDialog(None, message, title, wx.YES_NO | wx.ICON_QUESTION | wx.YES_DEFAULT)
    else:
        dialog = wx.MessageDialog(None, message, title, wx.YES_NO | wx.ICON_QUESTION | wx.NO_DEFAULT)
    result = dialog.ShowModal()
    dialog.Destroy()
    if result == wx.ID_YES:
        return True
    return False


def select_file(default_dir: str = SelectFilePopup.DEFAULT_DIRECTORY) -> (str | None):
    file_dialog = wx.FileDialog(None, SelectFilePopup.TITLE, wildcard=SelectFilePopup.WILDCARD, style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST, defaultDir=default_dir)
    if file_dialog.ShowModal() == wx.ID_OK:
        file_path = file_dialog.GetPath()
        file_dialog.Destroy()
        return file_path
    file_dialog.Destroy()
    
    
def save_file_as() -> (str | None):
    default_file_name = GeneralConst.DEFAULT_DATAFILE_NAME + GeneralConst.DATAFILE_EXTENSION
    file_dialog = wx.FileDialog(None, SaveAsPopup.TITLE, 
                            defaultFile=default_file_name, 
                            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
    if file_dialog.ShowModal() == wx.ID_OK:
        save_path = file_dialog.GetPath()
        file_dialog.Destroy()
        return save_path
    file_dialog.Destroy()


def select_dir() -> (str | None):
    dir_dialog = wx.DirDialog(None, SelectDirectoryPopup.TITLE)
    if dir_dialog.ShowModal() == wx.ID_OK:
        dir_path = dir_dialog.GetPath()
        dir_dialog.Destroy()
        return dir_path
    dir_dialog.Destroy()


