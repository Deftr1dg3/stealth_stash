#!/usr/bin/env python3


import wx
from data_file import Entry
from gui.command import Command
from gui.colours import Colours
from gui.midpanel.record_panel import RecordName, Username, Password, URL
from gui.menues.entry_row_right_click import EntryRightClickMenu


class EntryRow(wx.Panel):
    def __init__(self, scroll_panel: wx.Panel, entry: Entry, command: Command) -> None:
        self._scroll_panel = scroll_panel
        self._entry = entry
        self._command = command
        self._is_selected = False
        super().__init__(self._scroll_panel, size=(-1, 30))
        
        self._text_colour = Colours.TEXT
        self._selection_colour = Colours.SELECTION
        self._background_colour = Colours.ENTRY_BACKGROUND
        
        self._target_colour = self._selection_colour
        self._current_colour = self._background_colour
        
        self._colour_step = 3  # Determines the speed of color transition
        self._colour_timer = wx.Timer(self)
        
        self._init_ui()
        self._bind_events()
        
        self.SetBackgroundColour(self._background_colour)
        
    @property
    def entry(self) -> Entry:
        return self._entry
        
    @property
    def is_selected(self) -> bool:
        return self._is_selected
    
    @is_selected.setter
    def is_selected(self, selected: bool) -> None:
        self._is_selected = selected
        
        
    def _init_ui(self) -> None:
        # main_box.AddStretchSpacer()
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        record_box = wx.BoxSizer(wx.VERTICAL)
        username_box = wx.BoxSizer(wx.VERTICAL)
        password_box = wx.BoxSizer(wx.VERTICAL)
        url_box = wx.BoxSizer(wx.VERTICAL)

        self._record_name = RecordName(self, self._entry.record_name)
        self._username = Username(self, self._entry.username)
        self._password = Password(self, self._entry.password)
        self._url = URL(self, self._entry.url)
        
        record_box.Add(self._record_name, proportion=1, flag=wx.EXPAND | wx.LEFT, border=0)
        username_box.Add(self._username, proportion=1, flag=wx.EXPAND | wx.LEFT, border=0)
        password_box.Add(self._password, proportion=1, flag=wx.EXPAND | wx.LEFT, border=0)
        url_box.Add(self._url, proportion=1, flag=wx.EXPAND | wx.LEFT, border=0)
        record_box.AddStretchSpacer()
        
        main_box.Add(record_box, proportion=1, flag=wx.EXPAND)
        main_box.Add(username_box, proportion=1, flag=wx.EXPAND)
        main_box.Add(password_box, proportion=1, flag=wx.EXPAND)
        main_box.Add(url_box, proportion=1, flag=wx.EXPAND)

        self.SetSizer(main_box)
        self.Layout()
        
        # self._bind_events()
        
        
    def _bind_events(self) -> None:
        self._record_name.Bind(wx.EVT_LEFT_DOWN,self._on_left_click)
        self._username.Bind(wx.EVT_LEFT_DOWN,self._on_left_click)
        self._password.Bind(wx.EVT_LEFT_DOWN,self._on_left_click)
        self._url.Bind(wx.EVT_LEFT_DOWN,self._on_left_click)
        
        self._record_name.Bind(wx.EVT_RIGHT_DOWN,self._on_right_click)
        self._username.Bind(wx.EVT_RIGHT_DOWN,self._on_right_click)
        self._password.Bind(wx.EVT_RIGHT_DOWN,self._on_right_click)
        self._url.Bind(wx.EVT_RIGHT_DOWN,self._on_right_click)
        
        self.Bind(wx.EVT_TIMER, self._on_color_timer, self._colour_timer)
        # self.Bind(wx.EVT_ENTER_WINDOW, self._smooth_select)
        # self.Bind(wx.EVT_LEAVE_WINDOW, self._smooth_deselect)
    
    def _on_left_click(self, event) -> None:
        self.select_entry()
        
    def _on_right_click(self, event) -> None:
        self.select_entry()
        right_click_menu = EntryRightClickMenu(self, self._command, self._entry)
        position_in_widget = event.GetPosition()
        position_on_screen = event.GetEventObject().ClientToScreen(position_in_widget)
        position = self.ScreenToClient(position_on_screen)
        self.PopupMenu(right_click_menu, position)
    
    def _smooth_select(self) -> None:
        self._target_colour = self._selection_colour
        self._colour_timer.Start(10)
        
    def _smooth_deselect(self) -> None:
        self._target_colour = self._background_colour
        self._colour_timer.Start(10)
        
    def _on_color_timer(self, event) -> None:
        # Calculate the new color
        r = self._move_towards(self._current_colour.Red(), self._target_colour.Red())
        g = self._move_towards(self._current_colour.Green(), self._target_colour.Green())
        b = self._move_towards(self._current_colour.Blue(), self._target_colour.Blue())

        # Set the new color
        self._current_colour = wx.Colour(r, g, b)
        self.SetBackgroundColour(self._current_colour)
        self.Refresh()

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
        
    def select_entry(self) -> None:
        self.is_selected = True 
        if self._command.selected_entry_row is not None:
            self._command.selected_entry_row.deselect_entry()
        self._command.selected_entry_row = self
        self._command.edit_entry()
        self._smooth_select()
            
    def deselect_entry(self) -> None:
        self.is_selected = False 
        self._smooth_deselect()