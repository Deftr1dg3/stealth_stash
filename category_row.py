#!/usr/bin/env python3


import wx
from command import Command
from icons import IconPanel
from category_panel import CategoryPanel
from data_file import Category
# from right_click.category_row_right_click import CategotyRightClickMenu
from menues.category_row_right_click import CategotyRightClickMenu

class CategoryRow(wx.Panel):
    def __init__(self, left_panel: wx.Panel, category: Category, command: Command) -> None:
        self._left_panel = left_panel
        self._category = category
        self._command = command
        super().__init__(self._left_panel, size=(200, 30))
        
        self._original_color = wx.Colour(wx.WHITE)  # RGB for "#3D4EE9"
        self._selection_color = wx.Colour(wx.BLUE)
        
        self._target_color = self._selection_color
        self._current_color = self._original_color
        self._color_step = 5  # Determines the speed of color transition
        self._color_timer = wx.Timer(self)
        
        self._init_ui()
        self._bind_events()
        
    def _init_ui(self) -> None:
        # main_box.AddStretchSpacer()
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        icon_box = wx.BoxSizer(wx.VERTICAL)
        category_box = wx.BoxSizer(wx.VERTICAL)

        self._display_icon = IconPanel(self, "folder", self._selection_color)
        self._display_category = CategoryPanel(self, self._category.name)
        
        icon_box.Add(self._display_icon)
        category_box.Add(self._display_category)
        
        main_box.Add(icon_box)
        main_box.Add(category_box)

        self.SetSizer(main_box)
        self.Layout()
        
    def _bind_events(self) -> None:
        self._display_icon.Bind(wx.EVT_LEFT_DOWN, self._on_left_click)
        self._display_category.Bind(wx.EVT_LEFT_DOWN, self._on_left_click)
        self._display_icon.Bind(wx.EVT_RIGHT_DOWN, self._on_right_click)
        self._display_category.Bind(wx.EVT_RIGHT_DOWN, self._on_right_click)
        self.Bind(wx.EVT_TIMER, self._on_color_timer, self._color_timer)
        self.Bind(wx.EVT_ENTER_WINDOW, self._on_mouse_over)
        self.Bind(wx.EVT_LEAVE_WINDOW, self._on_mouse_leave)
    
    def _on_left_click(self, event) -> None:
        ...
    
    def _on_right_click(self, event) -> None:
        right_click_menu = CategotyRightClickMenu(self, self._command, self._category)
        position = event.GetPosition()
        self.PopupMenu(right_click_menu, position)
    
    def _on_mouse_over(self, event) -> None:
        self._target_color = self._selection_color
        self._color_timer.Start(10)
        
    def _on_mouse_leave(self, event) -> None:
        self._target_color = self._original_color
        self._color_timer.Start(10)
        
    def _on_color_timer(self, event) -> None:
        # Calculate the new color
        r = self._move_towards(self._current_color.Red(), self._target_color.Red())
        g = self._move_towards(self._current_color.Green(), self._target_color.Green())
        b = self._move_towards(self._current_color.Blue(), self._target_color.Blue())

        # Set the new color
        self._current_color = wx.Colour(r, g, b)
        self._display_category.set_colour(self._current_color)
        # self.Refresh()

        # Stop the timer if the target color has been reached
        if self._current_color.Red() == self._target_color.Red() and \
        self._current_color.Green() == self._target_color.Green() and \
        self._current_color.Blue() == self._target_color.Blue():
            self._color_timer.Stop()

    def _move_towards(self, current: int, target: int) -> int:
        # Helper function to move a color channel value towards a target value
        if current < target:
            return min(current + self._color_step, target)
        elif current > target:
            return max(current - self._color_step, target)
        else:
            return current
        
        