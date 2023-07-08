#!/usr/bin/env python3


import wx 
from gui.command import Command
from data_file import Entry


class EditPanel(wx.Panel):
    def __init__(self, right_panel: wx.Panel, command: Command) -> None:
        self._right_panel = right_panel
        self._command = command
        super().__init__(self._right_panel)
        
        self._show_password_ind = False
        self._show_password_label = "Show Passowrd"
        self._hide_password_label = "Hide Password"
        
        self._entry: Entry
        
        self._placeholder = "No Entry Selected"
        
        self._init_ui()
        self._bind_events()
        
    
    @property
    def entry(self) -> Entry:
        return self._entry
    
    @entry.setter
    def entry(self, entry: Entry) -> None:
        self._entry = entry
        
    def _init_ui(self):
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        self._scroll = wx.ScrolledWindow(self, -1)
        self._scroll.SetScrollbars(20, 20, 50, 50)
        
        self._scroll_sizer = wx.BoxSizer(wx.VERTICAL)

        record_name_title = wx.StaticText(self._scroll, label="Entry Name:")
        self._record_name = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER)
        username_title = wx.StaticText(self._scroll, label="Username:")
        self._username = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER)
        password_title = wx.StaticText(self._scroll, label="Password:")
        self._password = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER | wx.TE_PASSWORD)
        self._reveal_password = wx.Button(self._scroll, label=self._show_password_label)
        url_title = wx.StaticText(self._scroll, label="Password:")
        self._url = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER)
        
        self._scroll_sizer.Add(record_name_title, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._record_name, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(username_title, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._username, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(password_title, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._password, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._reveal_password, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(url_title, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._url, 0, wx.EXPAND | wx.ALL, 5)
        
        if self._command.selected_entry_row is None:
            self._record_name.Disable()
            self._username.Disable()
            self._password.Disable()
            self._reveal_password.Disable()
            self._url.Disable()
            self._record_name.SetValue(self._placeholder)
            self._username.SetValue(self._placeholder)
            self._password.SetValue(self._placeholder)
            self._url.SetValue(self._placeholder)
        else:
            self.entry = self._command.selected_entry_row.entry
            entry_name = self.entry.record_name
            username = self.entry.username
            password = self.entry.password
            url = self.entry.url
            self._record_name.SetValue(entry_name)
            self._username.SetValue(username)
            self._password.SetValue(password)
            self._url.SetValue(url)
     
        self._scroll.SetSizer(self._scroll_sizer)
        main_box.Add(self._scroll, 1, wx.EXPAND)
        
        self.SetSizer(main_box)
        self.Layout()
        
    def _bind_events(self):
        self._record_name.Bind(wx.EVT_TEXT, self._on_record_name)
        self._username.Bind(wx.EVT_TEXT, self._on_username)
        self._password.Bind(wx.EVT_TEXT, self._on_password)
        self._url.Bind(wx.EVT_TEXT, self._on_url)
        
        self._reveal_password.Bind(wx.EVT_BUTTON, self._show_password)
        
    def _on_record_name(self, event):
        value = self._record_name.GetValue()
        self.entry.record_name = value
        self._on_enter(None)
    
    def _on_username(self, event):
        value = self._username.GetValue()
        self.entry.username = value
        self._on_enter(None)
    
    def _on_password(self, event):
        value = self._password.GetValue()
        self.entry.password = value
        self._on_enter(None)
    
    def _on_url(self, event):
        value = self._url.GetValue()
        self.entry.url = value
        self._on_enter(None)
        
    def _on_enter(self, event):
        self._command.refresh_mid()
    
    def _show_password(self, event):
        if not self._show_password_ind:
            self._show_password_ind = not self._show_password_ind
            self._on_password(None)
            self._password.Destroy()
            self._password = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER)
            self._password.Bind(wx.EVT_TEXT_ENTER, self._on_enter)
            self._password.Bind(wx.EVT_KILL_FOCUS, self._on_enter)
            self._password.Bind(wx.EVT_TEXT, self._on_password)
            self._scroll_sizer.Insert(5, self._password, 0, wx.EXPAND | wx.ALL, 5)
            self._password.SetValue(self.entry.password)
            self._reveal_password.SetLabel(self._hide_password_label)
            self.Layout()
        else:
            self._show_password_ind = not self._show_password_ind
            self._on_password(None)
            self._password.Destroy()
            self._password = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER | wx.TE_PASSWORD)
            self._password.Bind(wx.EVT_TEXT_ENTER, self._on_enter)
            self._password.Bind(wx.EVT_KILL_FOCUS, self._on_enter)
            self._password.Bind(wx.EVT_TEXT, self._on_password)
            self._scroll_sizer.Insert(5, self._password, 0, wx.EXPAND | wx.ALL, 5)
            self._password.SetValue(self.entry.password)
            self._reveal_password.SetLabel(self._show_password_label)
            self.Layout()