#!/usr/bin/env python3


import wx
from data_file import Category
from command import Command
from gui.icons.icons import IconPanel
from gui.leftpanel.category_panel import CategoryPanel
from gui.menues.category_row_right_click import CategoryRightClickMenu
from config import LeftPanelConst


class CategoryRow(wx.Panel):
    def __init__(self, left_panel: wx.Panel, category: Category, command: Command) -> None:
        self._left_panel = left_panel
        self._category = category
        self._command = command
        self._is_selected = False
        super().__init__(self._left_panel, size=LeftPanelConst.CATEGORY_ROW_SIZE)
        
        self._colours = self._command.colours()
        
        self._background_colour = self._colours.LEFT_PANEL
        
        # Setting colours
        self._text_colour = self._colours.TEXT
        self._selection_colour = self._colours.SELECTION
        
        # Defining target and current colours
        self._target_colour = self._selection_colour
        self._current_colour = self._text_colour
        
        # Defining colour timer and colour changing step
        self._colour_step = self._colours.COLOUR_CHANGING_STEP  # Determines the speed of color transition
        self._colour_timer = wx.Timer(self)
        
        self.SetBackgroundColour(self._background_colour)
        
        # Initializing visible objects and binding events
        self._init_ui()
        self._bind_events()
        
    @property
    def category(self) -> Category:
        return self._category
        
    @property
    def is_selected(self) -> bool:
        return self._is_selected
    
    @is_selected.setter
    def is_selected(self, selected: bool) -> None:
        self._is_selected = selected
        
        
    def _init_ui(self) -> None:
        """ Function initializing visible interface. """
        
        # Create main sizer
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        
        # Create secondary sizers
        icon_box = wx.BoxSizer(wx.VERTICAL)
        category_box = wx.BoxSizer(wx.VERTICAL)
        
        # Create Icon, depending on the category name
        if set(self._category.name.lower().split()).intersection(LeftPanelConst.ICON_EMAIL):
            self._display_icon = IconPanel(self, LeftPanelConst.ICON_EMAIL, self._command)
            
        elif set(self._category.name.lower().split()).intersection(LeftPanelConst.ICON_CRYPTO):
            self._display_icon = IconPanel(self, LeftPanelConst.ICON_CRYPTO, self._command)
            
        elif set(self._category.name.lower().split()).intersection(LeftPanelConst.ICON_DEVOPS):
            self._display_icon = IconPanel(self, LeftPanelConst.ICON_DEVOPS, self._command)
        
        elif set(self._category.name.lower().split()).intersection(LeftPanelConst.ICON_DATABASE):
            self._display_icon = IconPanel(self, LeftPanelConst.ICON_DATABASE, self._command)
        
        elif set(self._category.name.lower().split()).intersection(LeftPanelConst.ICON_FUNDS):
            self._display_icon = IconPanel(self, LeftPanelConst.ICON_FUNDS, self._command)
        
        elif set(self._category.name.lower().split()).intersection(LeftPanelConst.ICON_PAYMENTS):
            self._display_icon = IconPanel(self, LeftPanelConst.ICON_PAYMENTS, self._command)
            
        elif set(self._category.name.lower().split()).intersection(LeftPanelConst.ICON_INTERNET):
            self._display_icon = IconPanel(self, LeftPanelConst.ICON_INTERNET, self._command)  
            
        else:
            self._display_icon = IconPanel(self, LeftPanelConst.ICON_FOLDER, self._command)
        
        # Create category panel object
        self._display_category = CategoryPanel(self, self._category.name, self._command)
        
        # Add gui objects to secondary sizers
        icon_box.Add(self._display_icon)
        category_box.Add(self._display_category)
        
        # Add secondary sizers to the main sizer
        main_box.Add(icon_box)
        main_box.Add(category_box)
        
        # Set main sizer to the panel
        self.SetSizer(main_box)
        
        # Refresh lauout
        self.Layout()
        
    def _bind_events(self) -> None:
        self._display_icon.Bind(wx.EVT_LEFT_DOWN, self._on_left_click)
        self._display_category.Bind(wx.EVT_LEFT_DOWN, self._on_left_click)
        self._display_icon.Bind(wx.EVT_RIGHT_DOWN, self._on_right_click)
        self._display_category.Bind(wx.EVT_RIGHT_DOWN, self._on_right_click)

        self.Bind(wx.EVT_TIMER, self._on_color_timer, self._colour_timer)
        self.Bind(wx.EVT_ENTER_WINDOW, self._on_mouse_over)
        self.Bind(wx.EVT_LEAVE_WINDOW, self._on_mouse_leave)
    
    def _on_left_click(self, event) -> None:
        self.select_row()
        if self._command.selected_category_row is not None:
            if self._command.selected_category_row is self:
                return
            self._command.selected_category_row.deselect_row()  #type: ignore
            self._command.selected_entry_id = 0
        self._command.selected_category_row = self
        self._command.display_category_content()
        
    def _on_right_click(self, event) -> None:
        self._on_left_click(None)
        right_click_menu = CategoryRightClickMenu(self, self._command, self._category)
        position_in_widget = event.GetPosition()
        position_on_screen = event.GetEventObject().ClientToScreen(position_in_widget)
        position = self.ScreenToClient(position_on_screen)
        self.PopupMenu(right_click_menu, position)
    
    def _on_mouse_over(self, event) -> None:
        if not self.is_selected:
            self._target_colour = self._selection_colour
            self._colour_timer.Start(10)
        
    def _on_mouse_leave(self, event) -> None:
        if not self.is_selected:
            self._target_colour = self._text_colour
            self._colour_timer.Start(10)
        
    def _on_color_timer(self, event) -> None:
        if not self.is_selected:
            # Calculate the new color
            r = self._move_towards(self._current_colour.Red(), self._target_colour.Red())
            g = self._move_towards(self._current_colour.Green(), self._target_colour.Green())
            b = self._move_towards(self._current_colour.Blue(), self._target_colour.Blue())

            # Set the new color
            self._current_colour = wx.Colour(r, g, b)
            self._display_category.set_colour(self._current_colour)
            # self.Refresh()

            # Stop the timer if the target color has been reached
            if self._current_colour.Red() == self._target_colour.Red() and \
            self._current_colour.Green() == self._target_colour.Green() and \
            self._current_colour.Blue() == self._target_colour.Blue():
                self._colour_timer.Stop()

    def _move_towards(self, current: int, target: int) -> int:
        # Helper function to move a color channel value towards a target value
        if current < target:
            return min(current + self._colour_step, target)
        elif current > target:
            return max(current - self._colour_step, target)
        else:
            return current
        
    def select_row(self) -> None:
        self._colour_timer.Stop()
        self.is_selected = True
        self._display_category.set_colour(self._selection_colour)
        self._current_colour = self._selection_colour
            
    def deselect_row(self) -> None:
        self.is_selected = False
        self._target_colour = self._text_colour
        self._on_mouse_leave(None)
    
    def select_category(self) -> None:
        self._on_left_click(None)