#!/usr/bin/env python3

from __future__ import annotations
import wx
from data_file import Category, Entry, DataFile
from gui.modals.get_input_from_user import get_input
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.topbar.top_bar_panel import TopBarPanel
    from gui.leftpanel.left_panel import LeftPanel
    from gui.leftpanel.category_row import CategoryRow
    from gui.midpanel.mid_panel import MidPanel
    from gui.rightpanel.right_panel import RightPanel


class Command:
    def __init__(self, data_file: DataFile) -> None:
        self._data_file = data_file
        self._top: (TopBarPanel | None) = None
        self._left: (LeftPanel | None) = None
        self._mid: (MidPanel | None) = None
        self._right: (RightPanel | None) = None
        self._category_row_list: list[CategoryRow] = []
        self._selected_category_row: (CategoryRow| None) = None
        self._selected_entry: (Entry | None) = None
        
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
    def selected_entry(self) -> (Entry | None):
        return self._selected_entry
    
    @selected_entry.setter
    def selected_entry(self, entry: Entry) -> None:
        self._selected_entry = entry
        
    @property
    def top(self) -> (TopBarPanel | None):
        return self._top
    
    @top.setter
    def top(self, panel: TopBarPanel):
        self._top = panel
    
    @property
    def left(self) -> (LeftPanel | None):
        return self._left
    
    @left.setter
    def left(self, panel: LeftPanel) -> None:
        self._left = panel
        
    @property
    def mid(self) -> (MidPanel | None):
        return self._mid
    
    @mid.setter
    def mid(self, panel: MidPanel) -> None:
        self._mid = panel
    
    @property
    def right(self) -> (RightPanel | None):
        return self._right
    
    @right.setter
    def right(self, panel: RightPanel) -> None:
        self._right = panel
        
    def list_categories(self) -> list[Category]:
        categories = self._data_file.get_categories()
        return categories
    
    def add_category(self, parent: (wx.Panel | wx.Frame)) -> None:
        if self.left is None:
            return
        hint = "Insert desired category name"
        name = get_input(parent, hint)
        if name is None:
            return
        self._data_file.add_category(name)
        self.left.refresh()   
        
    def remove_category(self, parent: wx.Panel, category: Category) -> None:
        if self.left is None:
            return
        dialog = wx.MessageDialog(parent, f"Are you sure you want to completely remove '{category.name}' category including all its data?", "Confirmation", 
                                  wx.YES_NO | wx.ICON_QUESTION | wx.NO_DEFAULT)
        result = dialog.ShowModal()
        if result == wx.ID_YES:
            category.remove()
            self.left.refresh()   
        dialog.Destroy()
        
    def rename_category(self, parent: wx.Panel, category: Category) -> None:
        if self.left is None:
            return
        hint = "Insert desired category name"
        name = get_input(parent, hint)
        if name is None:
            return
        category.rename(name)
        self.left.refresh()   
        
    def display_category_content(self):
        if self.selected_category_row is not None:
            print(f"Display content of --> {self.selected_category_row.category.name}") 
        
        
    

