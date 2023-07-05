#!/usr/bin/env python3

import wx
from data_file import Category, Row, DataFile
from modals.get_input_from_user import get_input


class Command:
    def __init__(self, data_file: DataFile) -> None:
        self._data_file = data_file
        self._top: wx.Panel
        self._left: wx.Panel
        self._mid: wx.Panel 
        self._right: wx.Panel 
        
    @property
    def top(self) -> wx.Panel:
        return self._top
    
    @top.setter
    def top(self, panel: wx.Panel) -> None:
        self._top = panel
    
    @property
    def left(self) -> wx.Panel:
        return self._left
    
    @left.setter
    def left(self, panel: wx.Panel) -> None:
        self._left = panel
        
    @property
    def mid(self) -> wx.Panel:
        return self._mid
    
    @mid.setter
    def mid(self, panel: wx.Panel) -> None:
        self._mid = panel
    
    @property
    def right(self) -> wx.Panel:
        return self._right
    
    @right.setter
    def right(self, panel: wx.Panel) -> None:
        self._right = panel
        
    def list_categories(self) -> list[Category]:
        categories = self._data_file.get_categories()
        return categories
    
    def add_category(self, parent: wx.Panel) -> None:
        hint = "Insert desired category name"
        name = get_input(parent, hint)
        if name is None:
            return
        self._data_file.add_category(name)
        self.left.refresh()   #type: ignore
        
    def remove_category(self, category: Category) -> None:
        category.remove()
        self.left.refresh()   #type: ignore
        
    def rename_category(self, parent: wx.Panel, category: Category) -> None:
        hint = "Insert desired category name"
        name = get_input(parent, hint)
        if name is None:
            return
        category.rename(name)
        self.left.refresh()   #type: ignore
        
    


        

