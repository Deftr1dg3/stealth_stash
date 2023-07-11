#!/usr/bin/env python3

from __future__ import annotations

import wx
from gui.colours import Colours
from data_file import Category, Entry, DataFile
from gui.modals.popups import get_input, message_popup, dialog_popup
from typing import TYPE_CHECKING
from config import CategoryExistsPopup, NewCategoryPopup, NoCategorySelectedPopup, NoEntrySelectedPopup
from config import RemoveConfirmationPopup, RenameCategoryPopup


if TYPE_CHECKING:
    from gui.body_panel import BodyPanel
    from gui.topbar.top_bar_panel import TopBarPanel
    from gui.leftpanel.left_panel import LeftPanel
    from gui.leftpanel.category_row import CategoryRow
    from gui.midpanel.mid_panel import MidPanel
    from gui.midpanel.entry_row import EntryRow
    from gui.rightpanel.right_panel import RightPanel
    from gui.rightpanel.edit_panel import EditPanel


class Command:
    def __init__(self, data_file: DataFile) -> None:
        self._data_file = data_file
        self._query: str = ""
        self._body_panel: BodyPanel
        self._top: TopBarPanel
        self._left: LeftPanel
        self._mid: MidPanel
        self._right: RightPanel
        self._edit_panel: EditPanel
        self._selected_category_row: (CategoryRow| None) = None
        self._selected_entry_row: (EntryRow | None) = None
        self._selected_category_id: int = 0
        self._selected_entry_id: int = 0
        self._category_rows: dict[int, CategoryRow] = {}
        self._entry_rows: dict[int, EntryRow] = {}
    
    @property
    def query(self) -> str:
        return self._query
    
    @query.setter
    def query(self, query: str) -> None:
        self._query = query
        
    @property
    def selected_entry_id(self) -> int:
        return self._selected_entry_id
    
    @selected_entry_id.setter
    def selected_entry_id(self, selected_entry_id: int) -> None:
        self._selected_entry_id = selected_entry_id
    
    @property
    def selected_entry_row(self) -> (EntryRow | None):
        return self._selected_entry_row
    
    @selected_entry_row.setter
    def selected_entry_row(self, entry: (EntryRow | None)) -> None:
        if entry is not None:
            if self.selected_entry_id in self._entry_rows:
                currently_selected = self.entry_rows[self.selected_entry_id]
                currently_selected._smooth_deselect() 
            self.selected_entry_id = entry.id       
        self._selected_entry_row = entry
    
    @property
    def entry_rows(self) -> dict[int, EntryRow]:
        return self._entry_rows
    
    @entry_rows.setter
    def entry_rows(self, entry_rows: dict[int, EntryRow]) -> None:
        self._entry_rows = entry_rows
    
    @property
    def selected_category_id(self) -> int:
        return self._selected_category_id
    
    @selected_category_id.setter
    def selected_category_id(self, selected_category_id: int) -> None:
        self._selected_category_id = selected_category_id
    
    @property
    def selected_category_row(self) -> (CategoryRow | None):
        return self._selected_category_row
    
    @selected_category_row.setter
    def selected_category_row(self, category_row: (CategoryRow | None)) -> None:
        if category_row is not None:
            self.selected_category_id = category_row.category.id
        self._selected_category_row = category_row
    
    @property
    def category_rows(self) -> dict[int, CategoryRow]:
        return self._category_rows
    
    @category_rows.setter
    def category_rows(self, category_rows: dict[int, CategoryRow]) -> None:
        self._category_rows = category_rows

    @property
    def body_panel(self) -> BodyPanel:
        return self._body_panel
    
    @body_panel.setter
    def body_panel(self, body_panel: BodyPanel) -> None:
        self._body_panel = body_panel
    
    @property
    def edit_panel(self) -> EditPanel:
        return self._edit_panel
    
    @edit_panel.setter
    def edit_panel(self, edit_panel: EditPanel) -> None:
        self._edit_panel = edit_panel
                        
    @property
    def top(self) -> TopBarPanel :
        return self._top
    
    @top.setter
    def top(self, panel: TopBarPanel):
        self._top = panel
    
    @property
    def left(self) -> LeftPanel:
        return self._left
    
    @left.setter
    def left(self, panel: LeftPanel) -> None:
        self._left = panel
        
    @property
    def mid(self) -> MidPanel:
        return self._mid
    
    @mid.setter
    def mid(self, panel: MidPanel) -> None:
        self._mid = panel
    
    @property
    def right(self) -> RightPanel:
        return self._right
    
    @right.setter
    def right(self, panel: RightPanel) -> None:
        self._right = panel  
                
    def _validate_new_name(self, new_name: str) -> bool:
        namespace = self._data_file.get_categories_namespace()
        if new_name in namespace:
            return False 
        return True
        
    def list_categories(self) -> list[Category]:
        categories = self._data_file.get_categories()
        return categories
    
    def add_category(self, parent: (wx.Panel | wx.Frame)) -> None:
        name = get_input(NewCategoryPopup.MESSAGE, NewCategoryPopup.TITLE)
        if name is None:
            return
        valid = self._validate_new_name(name)
        if not valid:
            message_popup(CategoryExistsPopup.MESSAGE.format(name), CategoryExistsPopup.TITLE)
            return
        self._data_file.add_category(name)
        self.selected_category_row = None
        self.refresh_left()
        self.refresh_mid()
        self.refresh_right()
        
    def remove_category(self) -> None:
        if self.selected_category_row is None:
            message_popup(NoCategorySelectedPopup.MESSAGE, NoCategorySelectedPopup.TITLE)
            return
        category = self.selected_category_row.category
        result = dialog_popup(RemoveConfirmationPopup.MESSAGE.format(category.name), RemoveConfirmationPopup.TITLE)
        if result:
            category.remove()
            self.selected_category_row = None
            self.refresh_left()
            self.refresh_mid()
            self.refresh_right()

    def rename_category(self, parent: wx.Panel, category: Category) -> None:
        if self.selected_category_row is None:
            message_popup(NoCategorySelectedPopup.MESSAGE, NoCategorySelectedPopup.TITLE)
            return
        default_value = self.selected_category_row.category.name
        name = get_input(RenameCategoryPopup.MESSAGE, RenameCategoryPopup.TITLE, default_value)
        if name is None:
            return
        valid = self._validate_new_name(name)
        if not valid:
            if name == self.selected_category_row.category.name:
                return
            message_popup(CategoryExistsPopup.MESSAGE.format(name), CategoryExistsPopup.TITLE)
            return
        category.rename(name)
        self.selected_category_row = None
        self.refresh_left()
        self.refresh_mid()
        self.refresh_right()
        
    def clear_category(self) -> None:
        if self.selected_category_row is None:
            message_popup(NoCategorySelectedPopup.MESSAGE, NoCategorySelectedPopup.TITLE)
            return
        category = self.selected_category_row.category
        confirmation = dialog_popup(RemoveConfirmationPopup.MESSAGE.format(category.name), RemoveConfirmationPopup.TITLE)
        if confirmation:
            category.clear_category()
            self.refresh_mid()
            self.refresh_right()
        
    def display_category_content(self) -> None:
        if self.selected_category_row is not None:
            self.refresh_mid()
            self.refresh_right()
    
    def add_entry(self) -> None:
        if self.selected_category_row is None:
            message_popup(NoCategorySelectedPopup.MESSAGE, NoCategorySelectedPopup.TITLE)
            return 
        category = self.selected_category_row.category
        category.new_entry()
        self.refresh_mid()
        self.refresh_right()
            
    def edit_entry(self) -> None:
        if self.selected_entry_row is None:
            message_popup(NoEntrySelectedPopup.MESSAGE, NoEntrySelectedPopup.TITLE)
            return
        self.refresh_right()
        
    def remove_entry(self, entry: (Entry | None) = None) -> None:
        if self.selected_category_row is None:
            message_popup(NoCategorySelectedPopup.MESSAGE, NoCategorySelectedPopup.TITLE)
            return
        if entry is None:
            if self.selected_entry_row is None:
                message_popup(NoEntrySelectedPopup.MESSAGE, NoEntrySelectedPopup.TITLE)
                return
            entry = self.selected_entry_row.entry
        result = dialog_popup(RemoveConfirmationPopup.MESSAGE.format(entry.record_name), RemoveConfirmationPopup.TITLE)
        if result:
            self.selected_category_row.category.remove_entry(entry)
            self.refresh_mid()
            self.refresh_right()
            
    def _keep_entry_row_selected(self) -> None:
        if self._entry_rows and self.selected_entry_id:
            if self.selected_entry_id in self._entry_rows:
                entry_row = self._entry_rows[self.selected_entry_id]
                try:
                    entry_row.set_selected_colour()
                except RuntimeError as ex:
                    pass
    
    def refresh_left(self) -> None:
        self.left.refresh()
    
    def refresh_mid(self) -> None:
        self.mid.refresh()
        self._keep_entry_row_selected()
        
    def refresh_right(self) -> None:
        self.right.refresh()
    
    def manage_entry_states(self, direction: int = 1):
        self.edit_panel.manage_self_states(direction)
    
    def search(self) -> list[Entry]:
        results = self._data_file.search(self.query)
        return results