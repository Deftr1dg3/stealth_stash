#!/usr/bin/env python3

import wx 
from config import CopyPopupConst


# Starts here iubj oihbnn oihn ;oihn


class CopyPopup(wx.Frame):
    def __init__(self, parent: wx.Panel) -> None:
        super().__init__(parent, size=CopyPopupConst.SIZE, style=wx.NO_BORDER | wx.STAY_ON_TOP)
        
        self.SetBackgroundColour(wx.Colour(CopyPopupConst.FRAME_BACKGROUND_COLOUR))
        
        self.CenterOnScreen()
        self._transparency_timer = wx.Timer(self)
        self._transparency = CopyPopupConst.CURRENT_TRANSPARENCY
        self._transparency_timer.Start(CopyPopupConst.TRANSFORMATION_SPEED)
        
        self._init_ui()
        self._bind_events()
    
    def _init_ui(self) -> None:
        
        main_box = wx.BoxSizer(wx.VERTICAL)
        message_box = wx.BoxSizer(wx.HORIZONTAL)
        
        text = wx.StaticText(self, -1, CopyPopupConst.MESSAGE, style=wx.ALIGN_CENTER)
        font = wx.Font(CopyPopupConst.FONT_SIZE, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        text.SetForegroundColour(wx.Colour(CopyPopupConst.TEXT_COLOUR))
        text.SetFont(font)
        
        message_box.Add(text, 1, wx.ALIGN_CENTER)
        main_box.Add(message_box, 1, wx.EXPAND | wx.ALL, 10)
        
        self.SetSizer(main_box)
        self.Layout()
        
    
    def _bind_events(self) -> None:
        self.Bind(wx.EVT_TIMER, self._on_timer)
        self.Bind(wx.EVT_PAINT, self._on_paint)
        
    def _on_paint(self, event) -> None:
        x, y = CopyPopupConst.SIZE
        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush(CopyPopupConst.BACKGROUND_COLOR))
        dc.SetPen(wx.Pen(CopyPopupConst.BACKGROUND_COLOR))
        dc.DrawRoundedRectangle(0, 0, x, y, CopyPopupConst.ROUND_ANGLE_RADIUS)
    
    def _on_timer(self, event) -> None:
        self._transparency -= CopyPopupConst.TRANSFORMATION_STEP
        if self._transparency < 0:
            self.Destroy()
        self.SetTransparent(self._transparency)
        

def launch_copy_poup(parent: wx.Panel) -> None:
    app = wx.App()
    CopyPopup(parent).Show()
    app.MainLoop()