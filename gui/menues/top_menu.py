#!/usr/bin/env python3


import wx
import sys
from command import Command
from config import MenueConst

class TopBarMenu(wx.MenuBar):
    def __init__(self, main_frame: wx.Frame, command: Command):
        super().__init__()
        self._main_frame = main_frame
        self._command = command
        self._init_menu()
        self._bind_events()
        
    def _init_menu(self):
        # Create "File" menu
        file_menu = wx.Menu()
        file_menu.Append(1, f"&{MenueConst.NEW_CATEGORY_LABEL}\t{MenueConst.NEW_CATEGORY_SHORTCUT}")
        file_menu.Append(2, f"&{MenueConst.NEW_ENTRY_LABEL}\t{MenueConst.NEW_ENTRY_SHORTCUT}")
        file_menu.Append(3, f"&{MenueConst.REMOVE_CATEGORY_LABEL}\t{MenueConst.REMOVE_CATEGORY_SHORTCUT}")
        file_menu.Append(4, f"&{MenueConst.REMOVE_ENTRY_LABEL}\t{MenueConst.REMOVE_ENTRY_SHORTCUT}")
        file_menu.Append(22, f"&{MenueConst.RENAME_CATEGORY_LABEL}")
        file_menu.AppendSeparator()
        file_menu.Append(5, f"&{MenueConst.CLEAR_CATEGORY_LABEL}")
        file_menu.AppendSeparator()
        file_menu.Append(6, f"&{MenueConst.CHANGE_PASSOWRD_LABEL}")
        file_menu.Append(7, f"&{MenueConst.SHOW_DATAFILE_IN_FOLDER_LABEL}")
        file_menu.Append(8, f"&{MenueConst.CHANGE_DATAFILE_DIRECTORY_LABEL}")
        file_menu.Append(9, f"&{MenueConst.CHANGE_DATAFILE_LABEL}")
        file_menu.AppendSeparator()
        file_menu.Append(30, f"&{MenueConst.EXIT_LABEL}\t{MenueConst.EXIT_SHORTCUT}")

        self.Append(file_menu, f"&{MenueConst.FIRST_FIELD_LABEL}")

        # Create "Edit" menu
        edit_menu = wx.Menu()
        edit_menu.Append(41, f"&{MenueConst.COPY_PASSOWRD_LABEL}\t{MenueConst.COPY_PASSOWRD_SHORTCUT}")
        edit_menu.Append(42, f"&{MenueConst.COPY_USERNALE_LABEL}\t{MenueConst.COPY_USERNAME_SHORTCUT}")
        edit_menu.Append(43, f"&{MenueConst.COPY_URL_LABEL}\t{MenueConst.COPY_URL_SHORTCUT}")
        edit_menu.AppendSeparator()
        edit_menu.Append(31, f"&{MenueConst.UNDO_LABLE}\t{MenueConst.UNDO_SHORTCUT}")
        edit_menu.Append(32, f"&{MenueConst.REDO_SHORTCUT}\t{MenueConst.REDO_SHORTCUT}")

        self.Append(edit_menu, f"&{MenueConst.SECONDFIELD_LABEL}")
        
    def _bind_events(self):
        # Bind "File" menu
        self._main_frame.Bind(wx.EVT_MENU, self._on_add_category, id=1)
        self._main_frame.Bind(wx.EVT_MENU, self._on_add_entry, id=2)
        self._main_frame.Bind(wx.EVT_MENU, self._on_remove_category, id=3)
        self._main_frame.Bind(wx.EVT_MENU, self._on_remove_entry, id=4)
        self._main_frame.Bind(wx.EVT_MENU, self._on_clear_category, id=5)
        self._main_frame.Bind(wx.EVT_MENU, self._on_change_file_password, id=6)
        self._main_frame.Bind(wx.EVT_MENU, self._on_show_datafile_in_folder, id=7)
        self._main_frame.Bind(wx.EVT_MENU, self._on_change_datafile_directory, id=8)
        self._main_frame.Bind(wx.EVT_MENU, self._on_change_datafile, id=9)
        
        self._main_frame.Bind(wx.EVT_MENU, self._on_rename_category, id=22)
        self._main_frame.Bind(wx.EVT_MENU, self._on_exit, id=30)
        
        # Bind "Edit" menu
        self._main_frame.Bind(wx.EVT_MENU, self._on_copy_password, id=41)
        self._main_frame.Bind(wx.EVT_MENU, self._on_copy_username, id=42)
        self._main_frame.Bind(wx.EVT_MENU, self._on_copy_url, id=43)
        self._main_frame.Bind(wx.EVT_MENU, self._on_undo, id=31)
        self._main_frame.Bind(wx.EVT_MENU, self._on_reverse_undo, id=32)
        
    def _on_change_datafile(self, event) -> None:
        self._command.change_datafile()
        
    def _on_change_datafile_directory(self, event) -> None:
        self._command.change_datafile_directory()
        
    def _on_show_datafile_in_folder(self, event) -> None:
        self._command.show_datafile_in_folder()
    
    def _on_change_file_password(self, event) -> None:
        self._command.set_new_password()
        
    def _on_copy_password(self, event) -> None:
        self._command.copy_to_clipboard(1)
        
    def _on_copy_username(self, event) -> None:
        self._command.copy_to_clipboard(2)
    
    def _on_copy_url(self, event) -> None:
        self._command.copy_to_clipboard(3)

    def _on_add_category(self, event) -> None:
        self._command.add_category(self._main_frame)
        
    def _on_remove_category(self, event) -> None:
        self._command.remove_category()
        
    def _on_rename_category(self, event) -> None:
        self._command.rename_category()
    
    def _on_clear_category(self, event) -> None:
        self._command.clear_category()

    def _on_add_entry(self, event) -> None:
        self._command.add_entry()
    
    def _on_remove_entry(self, event) -> None:
        self._command.remove_entry()

    def _on_exit(self, event) -> None:
        self._main_frame.Destroy()
        sys.exit(0)
    
    def _on_undo(self, event) -> None:
        try:
            self._command.manage_entry_states()
        except AttributeError:
            pass
    
    def _on_reverse_undo(self, event) -> None:
        try:
            self._command.manage_entry_states(0)
        except AttributeError:
            pass