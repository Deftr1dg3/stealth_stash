#!/usr/bin/env python3

import wx
from dataclasses import dataclass
from gui.colours import ColourTheme
from config import SelectColourSchemeConst

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from command import Command

    

class CirclePanel(wx.Panel):
    def __init__(self, parent: wx.Panel, colour: wx.Colour):
        super().__init__(parent)
        
        self.SetBackgroundColour(SelectColourSchemeConst.BACKGROUND_COLOUR)
        
        self._colour = colour
        self._pen_colour = wx.Colour(SelectColourSchemeConst.CIRCLE_PANEL_PEN_COLOUR)
        self._pen_size = SelectColourSchemeConst.CIRCLE_PANEL_PEN_SIZE
        
        self._bind_events()
    
    
    def _bind_events(self) -> None:
        self.Bind(wx.EVT_PAINT, self._on_paint)


    def _on_paint(self, event) -> None:
        dc = wx.PaintDC(self)
        dc.Clear()
        w, h = self.GetSize()
        dc.SetPen(wx.Pen(self._pen_colour, self._pen_size))
        dc.SetBrush(wx.Brush(self._colour))
        radius = min(w, h) // 2 - 2
        dc.DrawCircle(w // 2, h // 2, radius)



class SelectColourScheme(wx.Frame):
    def __init__(self, current_colour: str, command: "Command") -> None:
        super().__init__(None, title=SelectColourSchemeConst.TITLE, size=SelectColourSchemeConst.SIZE, style=SelectColourSchemeConst.STYLE)
        
        self._command = command
        
        self._current_colour = current_colour
        
        self.SetBackgroundColour(wx.Colour(SelectColourSchemeConst.BACKGROUND_COLOUR))
        
        self._button_confirm_label = SelectColourSchemeConst.BUTTON_CONFIRM_LABEL
        self._button_cancel_label = SelectColourSchemeConst.BUTTON_CANCEL_LABEL
        
        self._available_colours = ColourTheme.AVAILABLE_COLOUR_SCHEMES
        self._radio_buttons = {}
        
        self._slected_colour = current_colour
    
        x = len(self._available_colours) * 70
        if x > SelectColourSchemeConst.SIZE[0]:
            y = SelectColourSchemeConst.SIZE[1]
            self.SetSize((x, y))
                
        self._init_ui()
        self._bind_events()
        
        
    def _init_ui(self) -> None:
        """ Function initiates GUI """
        
        panel = wx.Panel(self)
        
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        colours_row_box = wx.BoxSizer(wx.HORIZONTAL)
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        
        for colour in self._available_colours.keys():
            colour_box = wx.BoxSizer(wx.VERTICAL)
            circle = CirclePanel(panel, self._available_colours[colour].LEFT_PANEL)
            
            radio_button = wx.RadioButton(panel)
            self._radio_buttons[radio_button.GetId()] = colour
            if colour == self._current_colour:
                radio_button.SetValue(True)
            
            radio_button_box = wx.BoxSizer(wx.HORIZONTAL)  # New box sizer for centering radio buttons
            radio_button_box.AddStretchSpacer()
            radio_button_box.Add(radio_button, 0, wx.ALL, 5)
            radio_button_box.AddStretchSpacer()
            radio_button.Bind(wx.EVT_RADIOBUTTON, self._on_radio_button)
            
            colour_box.Add(circle, 1, wx.EXPAND | wx.ALL, 10)
            colour_box.Add(radio_button_box, 0, wx.EXPAND | wx.BOTTOM, 10)
        
            colours_row_box.Add(colour_box, 1, wx.EXPAND)
            
        self._confirm = wx.Button(panel, label=self._button_confirm_label)
        self._cancel = wx.Button(panel, label=self._button_cancel_label)
        
        button_box.AddStretchSpacer()
        button_box.Add(self._cancel, 0, wx.EXPAND | wx.ALL, 10)
        button_box.Add(self._confirm, 0, wx.EXPAND | wx.ALL, 10)
        
        main_box.Add(colours_row_box, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        main_box.Add(button_box, 0, wx.EXPAND | wx.BOTTOM, 10)
        
        panel.SetSizer(main_box)
        
        self.Layout()
        
    
    def _bind_events(self) -> None:
        self._confirm.Bind(wx.EVT_BUTTON, self._on_confirm)
        self._cancel.Bind(wx.EVT_BUTTON, self._on_cancel)
        
        
    def _on_confirm(self, event) -> None:
        if not self._slected_colour == self._current_colour:
            self._command.set_colour(self._slected_colour)
        self.Destroy()

        
    def _on_cancel(self, event) -> None:
        self.Destroy()


    def _on_radio_button(self, event) -> None:
        radio_button = event.GetEventObject()
        self._slected_colour = self._radio_buttons[radio_button.GetId()]
    
    
def launch_colour_theme_selection(current_colour: str, command: "Command"):  
    app = wx.App()
    SelectColourScheme(current_colour, command).Show()
    app.MainLoop() 


