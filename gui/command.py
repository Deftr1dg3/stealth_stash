#!/usr/bin/env python3

from __future__ import annotations

import wx
from data_file import Category, Entry, DataFile
from gui.modals.popups import get_input, message_popup, dialog_popup
from typing import TYPE_CHECKING


if TYPE_CHECKING:
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
        self._top: TopBarPanel
        self._left: LeftPanel
        self._mid: MidPanel
        self._right: RightPanel
        self._category_row_list: list[CategoryRow] = []
        self._selected_category_row: (CategoryRow| None) = None
        self._selected_entry_row: (EntryRow | None) = None
        
    @property
    def category_row_list(self) -> list[CategoryRow]:
        return self._category_row_list
    
    @category_row_list.setter
    def category_row_list(self, category_row_list: list[CategoryRow]) -> None:
        self._category_row_list = category_row_list
        
    @property
    def selected_category_row(self) -> (CategoryRow | None):
        return self._selected_category_row
    
    @selected_category_row.setter
    def selected_category_row(self, category_row: (CategoryRow | None)) -> None:
        self._selected_category_row = category_row
        
    @property
    def selected_entry_row(self) -> (EntryRow | None):
        return self._selected_entry_row
    
    @selected_entry_row.setter
    def selected_entry_row(self, entry: (EntryRow | None)) -> None:
        self._selected_entry_row = entry
        
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
        hint = "Insert desired category name"
        title = "CREATE NEW CATEGORY"
        name = get_input(hint, title)
        if name is None:
            return
        valid = self._validate_new_name(name)
        if not valid:
            title = "Categoty Already Exists Error."
            message = f"Unable to create Categiry. Category with selected name --> '{name}' aready exists."
            message_popup(message, title)
            return
        self._data_file.add_category(name)
        self.selected_category_row = None
        self.left.refresh()  
        self.mid.refresh()  
        self.right.refresh()
        
    def remove_category(self, parent: wx.Panel, category: Category) -> None:
        result = dialog_popup(f"Are you sure you want to completely remove '{category.name}' category including all its data?", "Confirmation")
        if result:
            category.remove()
            self.selected_category_row = None
            self.left.refresh() 
            self.mid.refresh()  
            self.right.refresh()

    def rename_category(self, parent: wx.Panel, category: Category) -> None:
        if self.selected_category_row is None:
            message_popup("No Categoty selected.", "Error.")
            return
        hint = "Insert desired category name"
        title = "RENAME CATEGORY"
        default_value = self.selected_category_row.category.name
        name = get_input(hint, title, default_value)
        if name is None:
            return
        valid = self._validate_new_name(name)
        if not valid:
            title = "Categoty Already Exists Error."
            message = f"Unable to create Categiry. Category with selected name --> '{name}' aready exists."
            message_popup(message, title)
            return
        category.rename(name)
        self.selected_category_row = None
        self.left.refresh()
        self.mid.refresh() 
        self.right.refresh()   
        
    def display_category_content(self) -> None:
        if self.selected_category_row is not None:
            self.mid.refresh()
            self.right.refresh()
    
    def add_entry(self) -> None:
        if self.selected_category_row is None:
            message_popup('No Category selected.', 'Error.')
            return 
        category = self.selected_category_row.category
        category.new_entry()
        self.mid.refresh()
        self.right.refresh()
            
    def edit_entry(self) -> None:
        if self.selected_entry_row is None:
            message_popup("No Entry selected.", "Error.")
            return
        self.right.refresh()
        
    def remove_entry(self, parent: wx.Panel, entry: Entry) -> None:
        if self.selected_category_row is None:
            message_popup("No Categoty selected.", "Error.")
            return
        result = dialog_popup(f"Are you sure you want to completely remove this Entry? All Entry data will be lost.", "Confirmation")
        if result:
            self.selected_category_row.category.remove_entry(entry)
            self.mid.refresh()
            self.right.refresh()
    
    def refresh_mid(self):
        self.mid.refresh()
        
        
       
        
    

