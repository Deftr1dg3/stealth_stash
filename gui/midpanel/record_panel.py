#!/usr/bin/env python3


import wx
import pyperclip
from gui.colours import Colours
from config import MidPanelConst
from gui.command import Command


class BaseRecordPanel(wx.Panel):
    def __init__(self, parent_panel: wx.Panel, record_value: str, command: Command) -> None:
        self._record_value = record_value
        self._parent_panel = parent_panel
        self._command = command
        self._displayed_str_length = MidPanelConst.DISPLAYED_STRING_LEGTH
        self._displayed_password_length = MidPanelConst.DISPLAYED_PASSWORD_LENGTH
        self._extra_characters_replacement = MidPanelConst.EXTRA_CHARACTERS_REPLACEMENT
        super().__init__(self._parent_panel)
        
        self._colours = self._command.colours()
        
        self._text_colour = self._colours.TEXT
        self._selection_colour = self._colours.SELECTION
        self._current_colour = self._colours.TEXT
        
        self._colour_step = MidPanelConst.RECORD_PANEL_COLOUR_STEP  # Determines the speed of color transition
        self._colour_timer = wx.Timer(self)
        
        self._init_ui()
        self._bind_events()
        
    def _init_ui(self) -> None:
        """ Function initializing visible interface. """
        
        # Create main sizer
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        
        # Create GUI object
        self._display_value = wx.StaticText(self, label=self._format_category_name(self._record_value))
        self._display_value.SetForegroundColour(self._text_colour)
        
        # Add GUI object to the main sizer
        main_box.Add(self._display_value, 0, wx.TOP | wx.LEFT, 6)
        
        # Set main sizer to the panel
        self.SetSizer(main_box)
        
        # Refresh lauout
        self.Layout()
    
    def _bind_events(self):
        self.Bind(wx.EVT_LEFT_DCLICK, self._on_left_dclick)
        self.Bind(wx.EVT_TIMER, self._on_color_timer)
    
    def _on_left_dclick(self, event):
        pyperclip.copy(self._record_value)
        self._set_text_colour(self._selection_colour)
        self._current_colour = self._selection_colour
        self._colour_timer.Start(10)
        
    def _on_color_timer(self, event) -> None:
        # Calculate the new color
        r = self._move_towards(self._current_colour.Red(), self._text_colour.Red())
        g = self._move_towards(self._current_colour.Green(), self._text_colour.Green())
        b = self._move_towards(self._current_colour.Blue(), self._text_colour.Blue())

        # Set the new color
        self._current_colour = wx.Colour(r, g, b)
        self._set_text_colour(self._current_colour)

        # Stop the timer if the target color has been reached
        if self._current_colour.Red() == self._text_colour.Red() and \
        self._current_colour.Green() == self._text_colour.Green() and \
        self._current_colour.Blue() == self._text_colour.Blue():
            self._colour_timer.Stop()

    def _move_towards(self, current: int, target: int) -> int:
        # Helper function to move a color channel value towards a target value
        if current < target:
            return min(current + self._colour_step, target)
        elif current > target:
            return max(current - self._colour_step, target)
        else:
            return current 
        
    def _format_category_name(self, record_value: str) -> str:
        if len(record_value) > self._displayed_str_length:
            record_value = record_value[:self._displayed_str_length] + self._extra_characters_replacement
        return record_value
    
    def _set_text_colour(self, colour: wx.Colour) -> None:
        self._display_value.SetForegroundColour(colour)
        self.Refresh() 
    

class RecordName(BaseRecordPanel):
    ...
    
    
class Username(BaseRecordPanel):
    ...
    
    
class Password(BaseRecordPanel):
    def _format_category_name(self, record_value: str) -> str:
        value_to_display = "*" * self._displayed_password_length
        return value_to_display
    
    
class URL(BaseRecordPanel):
    ...