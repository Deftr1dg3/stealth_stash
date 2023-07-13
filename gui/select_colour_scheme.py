

import wx
from dataclasses import dataclass
# from config import SelectColourSchemeConst


@dataclass(frozen=True)
class SelectColourSchemeConst:
    TITLE = "Select Colour Scheme"
    SIZE = (400, 200)
    STYLE = wx.CLOSE_BOX
    

class CirclePanel(wx.Panel):
    def __init__(self, parent: wx.Panel, colour: wx.Colour):
        super().__init__(parent)
        
        self.SetBackgroundColour(wx.Colour("#202020"))
        
        self._colour = colour
        
        
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        

    def OnSize(self, event):
        self.Refresh()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.Clear()
        w, h = self.GetSize()
        dc.SetPen(wx.Pen("GREY", 2))
        dc.SetBrush(wx.Brush(self._colour))
        radius = min(w, h) // 2 - 2
        dc.DrawCircle(w // 2, h // 2, radius)

class SelectColourScheme(wx.Frame):
    def __init__(self):
        super().__init__(None, title=SelectColourSchemeConst.TITLE, size=SelectColourSchemeConst.SIZE, style=SelectColourSchemeConst.STYLE)
        self._radio_buttons = []
        
        self.SetBackgroundColour(wx.Colour("#202020"))
        
        self._colours = ["#343434", "#EEEEEE", "#004952", "#003764", "#431B24", "#004952", "#003764", "#431B24"]
        
        x = len(self._colours) * 70
        y = 190
        
        self.SetSize((x, y))
                
        self._init_ui()
        
    def _init_ui(self):
        """ Function initiates GUI """
        
        panel = wx.Panel(self)
        
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        row_box = wx.BoxSizer(wx.HORIZONTAL)
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        
        for colour in self._colours:
            colour_box = wx.BoxSizer(wx.VERTICAL)
            circle = CirclePanel(panel, wx.Colour(colour))
            radio_button = wx.RadioButton(panel)
            
            radio_button_box = wx.BoxSizer(wx.HORIZONTAL)  # New box sizer for centering radio buttons
            radio_button_box.AddStretchSpacer()
            radio_button_box.Add(radio_button, 0, wx.CENTER)
            radio_button_box.AddStretchSpacer()
            
            colour_box.Add(circle, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 7)
            colour_box.Add(radio_button_box, 0, wx.EXPAND | wx.ALL, 10)
        
            
            row_box.Add(colour_box, 1, wx.EXPAND)
            
        self._confirm = wx.Button(panel, label="Confirm")
        self._cancel = wx.Button(panel, label="Cancel")
        
        button_box.AddStretchSpacer()
        button_box.Add(self._cancel, 0, wx.EXPAND | wx.ALL, 10)
        button_box.Add(self._confirm, 0, wx.EXPAND | wx.ALL, 10)
        
        main_box.Add(row_box, 1, wx.EXPAND)
        main_box.Add(button_box, 0, wx.EXPAND | wx.BOTTOM, 10)
        
        panel.SetSizer(main_box)
        
        self.Layout()



    # def on_radiobutton(self, event):
    #     selected = event.GetEventObject()
    #     for rb in self._radio_buttons:
    #         if rb != selected:
    #             rb.SetValue(False)

if __name__ == "__main__":
    app = wx.App()
    SelectColourScheme().Show()
    app.MainLoop()

