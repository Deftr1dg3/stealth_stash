#!/usr/bin/env python3


import wx
import pyperclip
from gui.colours import Colours


class BaseRecordPanel(wx.Panel):
    def __init__(self, parent_panel: wx.Panel, record_value: str) -> None:
        self._record_value = record_value
        self._parent_panel = parent_panel
        self._displayed_str_length = 12
        self._displayed_password_length = 8
        super().__init__(self._parent_panel)
        
        self._text_colour = Colours.TEXT
        self._selected_text_colour = Colours.SELECTION
        self._current_colour = Colours.TEXT
        
        self._colour_step = 1  # Determines the speed of color transition
        self._colour_timer = wx.Timer(self)
        
        self._init_ui()
        self._bind_events()
        
    def _init_ui(self) -> None:
        # main_box.AddStretchSpacer()
        main_box = wx.BoxSizer(wx.HORIZONTAL)
        self._display_value = wx.StaticText(self, label=self._format_category_name(self._record_value))
        self._display_value.SetForegroundColour(self._text_colour)
        main_box.Add(self._display_value, 0, wx.TOP | wx.LEFT, 6)
        self.SetSizer(main_box)
        self.Layout()
    
    def _bind_events(self):
        self.Bind(wx.EVT_LEFT_DCLICK, self._on_left_dclick)
        self.Bind(wx.EVT_TIMER, self._on_color_timer)
    
    def _on_left_dclick(self, event):
        pyperclip.copy(self._record_value)
        self._set_text_colour(self._selected_text_colour)
        self._current_colour = self._selected_text_colour
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
            record_value = record_value[:self._displayed_str_length] + "..."
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