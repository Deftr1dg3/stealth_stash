#!/usr/bin/env python3

from __future__ import annotations

import wx
import os
import sys
import subprocess
import config
import webbrowser
from data_file import Category, Entry, DataFile
from settings import Settings
from gui.colours import ColourTheme, ColoursAssignment
from gui.modals.popups import get_input, message_popup, dialog_popup, save_file_as, select_dir, select_file
from gui.modals.select_colour_scheme import launch_colour_theme_selection
from gui.modals.set_new_password import launch_set_new_password
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from gui.main_frame import MainFrame
    from gui.body_panel import BodyPanel
    from gui.topbar.top_bar_panel import TopBarPanel
    from gui.leftpanel.left_panel import LeftPanel
    from gui.leftpanel.category_row import CategoryRow
    from gui.midpanel.mid_panel import MidPanel
    from gui.midpanel.entry_row import EntryRow
    from gui.rightpanel.right_panel import RightPanel
    from gui.rightpanel.edit_panel import EditPanel
    from gui.rightpanel.notes_panel import NotesPanel


class Command:
    def __init__(self, data_file: DataFile, settings: Settings) -> None:
        self._data_file = data_file
        self._settings = settings
        self._query: str = ""
        self._main_frame: MainFrame
        self._body_panel: BodyPanel
        self._top: TopBarPanel
        self._left: LeftPanel
        self._mid: MidPanel
        self._right: RightPanel
        self._edit_panel: EditPanel
        self._notes_panel: NotesPanel
        self._selected_category_row: (CategoryRow| None) = None
        self._selected_entry_row: (EntryRow | None) = None
        self._selected_category_id: int = 0
        self._selected_entry_id: int = 0
        self._category_rows: dict[int, CategoryRow] = {}
        self._entry_rows: dict[int, EntryRow] = {}
        self._colous = ColourTheme.AVAILABLE_COLOUR_SCHEMES
    
    # Search query  ----------------------------
    @property
    def query(self) -> str:
        return self._query
    
    @query.setter
    def query(self, query: str) -> None:
        self._query = query
        
        
    # ID of the last selected entry, will appear even if currently no entry selected  ----------------------------
    @property
    def selected_entry_id(self) -> int:
        return self._selected_entry_id
    
    @selected_entry_id.setter
    def selected_entry_id(self, selected_entry_id: int) -> None:
        self._selected_entry_id = selected_entry_id
    
    
    # Currently lected entry row - EntryRow or None (if not selected)  ----------------------------
    @property
    def selected_entry_row(self) -> (EntryRow | None):
        return self._selected_entry_row
    
    @selected_entry_row.setter
    def selected_entry_row(self, entry: (EntryRow | None)) -> None:
        if entry is not None:
            if self.selected_entry_id in self._entry_rows:
                currently_selected = self.entry_rows[self.selected_entry_id]
                currently_selected.deselect_entry() 
            self.selected_entry_id = entry.id       
        self._selected_entry_row = entry
    
    
    # Entry rows - dict  ----------------------------
    @property
    def entry_rows(self) -> dict[int, EntryRow]:
        return self._entry_rows
    
    @entry_rows.setter
    def entry_rows(self, entry_rows: dict[int, EntryRow]) -> None:
        self._entry_rows = entry_rows
    
    
    # Selected category ID - int  ----------------------------
    @property
    def selected_category_id(self) -> int:
        return self._selected_category_id
    
    @selected_category_id.setter
    def selected_category_id(self, selected_category_id: int) -> None:
        self._selected_category_id = selected_category_id
    
    
    # Selected category row - CategoryRow  ----------------------------
    @property
    def selected_category_row(self) -> (CategoryRow | None):
        return self._selected_category_row
    
    @selected_category_row.setter
    def selected_category_row(self, category_row: (CategoryRow | None)) -> None:
        if category_row is not None:
            self.selected_category_id = category_row.category.id
        self._selected_category_row = category_row
    
    
    # Category rows - dict  ----------------------------
    @property
    def category_rows(self) -> dict[int, CategoryRow]:
        return self._category_rows
    
    @category_rows.setter
    def category_rows(self, category_rows: dict[int, CategoryRow]) -> None:
        self._category_rows = category_rows
    
    
    # Edit panel - EditPanel  ----------------------------
    @property
    def edit_panel(self) -> EditPanel:
        return self._edit_panel
    
    @edit_panel.setter
    def edit_panel(self, edit_panel: EditPanel) -> None:
        self._edit_panel = edit_panel
    
    
    # Notes panel - NotesPanel  ----------------------------
    @property
    def notes_panel(self) -> NotesPanel:
        return self._notes_panel
    
    @notes_panel.setter
    def notes_panel(self, notes_panel: NotesPanel) -> None:
        self._notes_panel = notes_panel
        
    
    # Main frame - wx.Frame  ----------------------------
    @property
    def main_frame(self) -> MainFrame:
        return self._main_frame
    
    @main_frame.setter
    def main_frame(self, main_frame: MainFrame) -> None:
        self._main_frame = main_frame
    
    
    # Body panel - BodyPanel  ----------------------------
    @property
    def body_panel(self) -> BodyPanel:
        return self._body_panel
    
    @body_panel.setter
    def body_panel(self, body_panel: BodyPanel) -> None:
        self._body_panel = body_panel
           
       
    # Top panel - TopBarPanel  ----------------------------                
    @property
    def top(self) -> TopBarPanel :
        return self._top
    
    @top.setter
    def top(self, panel: TopBarPanel):
        self._top = panel
    
    
    # Left panel - LeftPanel  ----------------------------
    @property
    def left(self) -> LeftPanel:
        return self._left
    
    @left.setter
    def left(self, panel: LeftPanel) -> None:
        self._left = panel
        
        
    # Middle panel - MidPanel  ----------------------------
    @property
    def mid(self) -> MidPanel:
        return self._mid
    
    @mid.setter
    def mid(self, panel: MidPanel) -> None:
        self._mid = panel
    
    
    # Right panel - RightPanel  ----------------------------
    @property
    def right(self) -> RightPanel:
        return self._right
    
    @right.setter
    def right(self, panel: RightPanel) -> None:
        self._right = panel  
           
           
    
    # Methods ----------------------------------------------------------------------------------------------------------------------------------------     
    
    
    # Category related methods ------------------------------------------------------------
        
    def list_categories(self) -> list[Category]:
        categories = self._data_file.get_categories()
        return categories
    
        
    def display_category_content(self) -> None:
        if self.selected_category_row is not None:
            self.refresh_mid()
            self.refresh_right()
            
    
    def _keep_category_row_selected(self) -> None:
        if self.selected_category_id and self.selected_category_id in self.category_rows:
            category_row = self.category_rows[self.selected_category_id]
            category_row.select_category()

    
    # ------------------------------------------------------------
    

    # Entry related methods ------------------------------------------------------------
    
    def edit_entry(self) -> None:
        if self.selected_entry_row is None:
            message_popup(config.NoEntrySelectedPopup.MESSAGE, config.NoEntrySelectedPopup.TITLE)
            return
        self.refresh_right()
        
            
    def _keep_entry_row_selected(self) -> None:
        if self._entry_rows and self.selected_entry_id:
            if self.selected_entry_id in self._entry_rows:
                entry_row = self._entry_rows[self.selected_entry_id]
                try:
                    entry_row.set_selected_colour()
                except RuntimeError as ex:
                    pass
                
                
    def _enty_row_is_selected(self) -> bool:
        if self.selected_entry_row is None:
            message_popup(config.NoEntrySelectedPopup.MESSAGE, config.NoEntrySelectedPopup.TITLE)
            return False
        return True
    
                
    # ------------------------------------------------------------
     
    

    # Refresh Panel methods ------------------------------------------------------------
    
    def refresh_left(self) -> None:
        self.left.refresh()
    
    
    def refresh_mid(self) -> None:
        self.mid.refresh()
        
        
    def refresh_right(self) -> None:
        self.right.refresh()
        
        
    def refresh_on_item_change(self) -> None:
        self.refresh_mid()
        self._keep_entry_row_selected()
    
    # ------------------------------------------------------------
    
    
    def commit(self) -> None:
        if self.selected_category_row is not None:
            self.selected_category_row.category.commit()


    def search(self) -> list[Entry]:
        results = self._data_file.search(self.query)
        return results
    
    
    def _validate_new_name(self, new_name: str) -> bool:
        namespace = self._data_file.get_categories_namespace()
        if new_name in namespace:
            return False 
        return True


    # Colours methods ------------------------------------------------------------

    def colours(self) -> ColoursAssignment:
        colours = self._colous[self._settings.COLOUR_SCHEME]
        return colours


    def choose_colour_scheme(self) -> None:
        current_colour = self._settings.COLOUR_SCHEME
        launch_colour_theme_selection(current_colour, self)
        
        
    def set_colour(self, colour: str) -> None:
        confirmed= dialog_popup(config.ChangeColourSchemeConfirmation.MESSAGE, config.ChangeColourSchemeConfirmation.TITLE)
        if confirmed:
            self._settings.COLOUR_SCHEME = colour
            self.main_frame.restart()
    
    # ------------------------------------------------------------
    
    def _swap_files_data(self, source_file: str, destination_file: str) -> None:
        with open(source_file, "r", encoding="utf-8") as f:
            source_data = f.read()
        with open(destination_file, "w", encoding="utf-8") as f:
            f.write(source_data)
    
    
               
#   TOP MENUE ----------------------------------------------------------------------------------------------------------------------

    
    # "APP" menu --------------------------------------------------------------------
         
    def exit_app(self) -> None:
        self.main_frame.Destroy()
        sys.exit(0)
        
         

    # "File" menu --------------------------------------------------------------------
    
    def add_category(self, parent: (wx.Panel | wx.Frame)) -> None:
        name = get_input(config.NewCategoryPopup.MESSAGE, config.NewCategoryPopup.TITLE)
        if name is None:
            return
        valid = self._validate_new_name(name)
        if not valid:
            message_popup(config.CategoryExistsPopup.MESSAGE.format(name), config.CategoryExistsPopup.TITLE)
            return
        self._data_file.add_category(name)
        self.selected_category_row = None
        self.refresh_left()
        self.refresh_mid()
        self.refresh_right()
        self._keep_category_row_selected()
        
    
    def add_entry(self) -> None:
        if self.selected_category_row is None:
            message_popup(config.NoCategorySelectedPopup.MESSAGE, config.NoCategorySelectedPopup.TITLE)
            return 
        category = self.selected_category_row.category
        category.new_entry()
        self.refresh_mid()
        self.refresh_right()
        
    
    def remove_category(self) -> None:
        if self.selected_category_row is None:
            message_popup(config.NoCategorySelectedPopup.MESSAGE, config.NoCategorySelectedPopup.TITLE)
            return
        category = self.selected_category_row.category
        result = dialog_popup(config.RemoveConfirmationPopup.MESSAGE.format(category.name), config.RemoveConfirmationPopup.TITLE)
        if result:
            category.remove()
            self.selected_category_row = None
            self.refresh_left()
            self.refresh_mid()
            self.refresh_right()
            self._keep_category_row_selected()
            
        
    def remove_entry(self, entry: (Entry | None) = None) -> None:
        if self.selected_category_row is None:
            message_popup(config.NoCategorySelectedPopup.MESSAGE, config.NoCategorySelectedPopup.TITLE)
            return
        if entry is None:
            if self.selected_entry_row is None:
                message_popup(config.NoEntrySelectedPopup.MESSAGE, config.NoEntrySelectedPopup.TITLE)
                return
            entry = self.selected_entry_row.entry
        confirmed = dialog_popup(config.RemoveConfirmationPopup.MESSAGE.format(entry.record_name), config.RemoveConfirmationPopup.TITLE)
        if confirmed:
            self.selected_category_row.category.remove_entry(entry)
            self.refresh_mid()
            self.refresh_right()
            
        
    def rename_category(self) -> None:
        if self.selected_category_row is None:
            message_popup(config.NoCategorySelectedPopup.MESSAGE, config.NoCategorySelectedPopup.TITLE)
            return
        category = self.selected_category_row.category
        default_value = category.name
        name = get_input(config.RenameCategoryPopup.MESSAGE, config.RenameCategoryPopup.TITLE, default_value)
        if name is None:
            return
        valid = self._validate_new_name(name)
        if not valid:
            if name == self.selected_category_row.category.name:
                return
            message_popup(config.CategoryExistsPopup.MESSAGE.format(name), config.CategoryExistsPopup.TITLE)
            return
        category.rename(name)
        self.selected_category_row = None
        self.refresh_left()
        self.refresh_mid()
        self.refresh_right()
        self._keep_category_row_selected()
            
    
    def clear_category(self) -> None:
        if self.selected_category_row is None:
            message_popup(config.NoCategorySelectedPopup.MESSAGE, config.NoCategorySelectedPopup.TITLE)
            return
        category = self.selected_category_row.category
        confirmed = dialog_popup(config.RemoveConfirmationPopup.MESSAGE.format(category.name), config.RemoveConfirmationPopup.TITLE)
        if confirmed:
            category.clear_category()
            self.refresh_mid()
            self.refresh_right()
            self._keep_category_row_selected()
            
            
    def set_new_password(self) -> None:
        launch_set_new_password(self._data_file, self._settings, change_password=True)
            
        
    def show_datafile_in_folder(self) -> None:
        datafile_path = self._settings.DATAFILE_PATH
        script = """
                    tell application "Finder"
                        run
                        activate
                        reveal POSIX file "%s"
                    end tell
        """ % (datafile_path)
        subprocess.call(["osascript", "-e", script])
        
    
    def change_datafile_directory(self) -> None:
        new_dir_path = select_dir()
        if new_dir_path is None:
            return
        confirmed = dialog_popup(config.ConfirmDirectoryPopup.MESSAGE.format(new_dir_path), config.ConfirmDirectoryPopup.TITLE)
        if confirmed:
            save_as = new_dir_path + os.sep + config.GeneralConst.DEFAULT_DATAFILE_NAME + config.GeneralConst.DATAFILE_EXTENSION
            self._data_file.datafile = save_as
            self._settings.DATAFILE_PATH = save_as
            self._data_file.commit()
            message_popup(config.ChangeDatafileDirectoryPopup.MESSAGE.format(save_as), config.ChangeDatafileDirectoryPopup.TITLE)
        
    
    def change_datafile(self) -> None:
        new_file = select_file()
        if new_file is not None:
            self._settings.DATAFILE_PATH = new_file
            self._main_frame.restart()
            
            
    def save_datafile_as(self) -> None:
        save_as = save_file_as()
        if save_as is not None:
            datafile_path = self._data_file.datafile
            with open(datafile_path, "r", encoding="utf-8") as f:
                data = f.read()
            with open(save_as, "w", encoding="utf-8") as f:
                f.write(data)
            message_popup(config.FileSavedPopup.MESSAGE.format(save_as), config.FileSavedPopup.TITLE)
            
    
    def restore_from_backup(self) -> None:
        datafile_path = self._settings.DATAFILE_PATH
        backup_dir = self._settings.BACKUP_PATH
        available_backups = os.listdir(backup_dir)
        if available_backups:
            chosen_backup_file = select_file(default_dir=backup_dir)
            if chosen_backup_file is not None:
                backup_file_name = os.path.basename(chosen_backup_file)
                confirmed = dialog_popup(config.RestoreFromBackupPopup.MESSAGE.format(backup_file_name), config.RestoreFromBackupPopup.TITLE)
                if confirmed:
                    self._data_file.back_up()
                    self._swap_files_data(chosen_backup_file, datafile_path)
                    self.main_frame.restart()
        else:
            message_popup(config.NoBackupsAvailablePopup.MESSAGE, config.NoBackupsAvailablePopup.TITLE)
            

        
    
    # "Edit" menu --------------------------------------------------------------------
                
    def copy_password(self) -> None:   
        if self.selected_entry_row is None:
            message_popup(config.NoEntrySelectedPopup.MESSAGE, config.NoEntrySelectedPopup.TITLE)
            return 
        self.selected_entry_row.copy_password()
    
    
    def copy_username(self) -> None:
        if self.selected_entry_row is None:
            message_popup(config.NoEntrySelectedPopup.MESSAGE, config.NoEntrySelectedPopup.TITLE)
            return 
        self.selected_entry_row.copy_username()
        
        
    def copy_url(self) -> None: 
        if self.selected_entry_row is None:
            message_popup(config.NoEntrySelectedPopup.MESSAGE, config.NoEntrySelectedPopup.TITLE)
            return 
        self.selected_entry_row.copy_url() 
                         
    
    def manage_entry_states(self, direction: int = 1):
        self.edit_panel.manage_self_states(direction)
        
    
    def move_category_up(self) -> None:
        if self.selected_category_row is None:
            message_popup(config.NoCategorySelectedPopup.MESSAGE, config.NoCategorySelectedPopup.TITLE)
            return
        category = self.selected_category_row.category
        category.move_category_up()
        self.selected_category_row = None
        self.refresh_left()
        self._keep_category_row_selected()
    
    
    def move_category_down(self) -> None:
        if self.selected_category_row is None:
            message_popup(config.NoCategorySelectedPopup.MESSAGE, config.NoCategorySelectedPopup.TITLE)
            return
        category = self.selected_category_row.category
        category.move_category_down()
        self.selected_category_row = None
        self.refresh_left()
        self._keep_category_row_selected()
        
        
    def move_entry_up(self) -> None:
        if self.selected_category_row is None:
            message_popup(config.NoCategorySelectedPopup.MESSAGE, config.NoCategorySelectedPopup.TITLE)
            return
        if self.selected_entry_row is None:
            message_popup(config.NoEntrySelectedPopup.MESSAGE, config.NoEntrySelectedPopup.TITLE)
            return
        entry = self.selected_entry_row.entry
        self.selected_category_row.category.move_entry_up(entry)
        self.refresh_mid()
        self._keep_entry_row_selected()
    
    
    def move_entry_down(self) -> None:
        if self.selected_category_row is None:
            message_popup(config.NoCategorySelectedPopup.MESSAGE, config.NoCategorySelectedPopup.TITLE)
            return
        if self.selected_entry_row is None:
            message_popup(config.NoEntrySelectedPopup.MESSAGE, config.NoEntrySelectedPopup.TITLE)
            return
        entry = self.selected_entry_row.entry
        self.selected_category_row.category.move_entry_down(entry)
        self.refresh_mid()
        self._keep_entry_row_selected()
        
    
            
            
            
    # "Help" menu --------------------------------------------------------------------
         
    
    def help(self) -> None:
        webbrowser.open(config.GeneralConst.GIT_HUB)
            
                

