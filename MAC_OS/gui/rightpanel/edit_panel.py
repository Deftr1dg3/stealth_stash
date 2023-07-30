#!/usr/bin/env python3


import wx 
from command import Command
from data_file import Entry
from gui.modals.popups import message_popup, dialog_popup
from manage_password import GeneratePassword, ValidatePassword
from gui.rightpanel.entry_state import EntryState
from gui.rightpanel.entry_state import EntrySnapshot
from gui.modals.popups import message_popup
from config import RightPanelConst, PasswordReplacemetPopup, UndoUnavailable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.rightpanel.right_panel import RightPanel


class EditPanel(wx.Panel):
    def __init__(self, right_panel: "RightPanel", command: Command) -> None:
        self._right_panel = right_panel
        self._command = command

        super().__init__(self._right_panel)
        
        self._undo_available = False
        
        self._show_password_ind = False
        self._show_password_label = RightPanelConst.SHOW_PASSWORD_BUTTON_LABEL
        self._hide_password_label = RightPanelConst.HIDE_PASSWORD_BUTTON_LABEL
        self._generate_password_label = RightPanelConst.GENERATE_PASSWORD_BUTTON_LABEL
        self._PASSWORD_STRENGTH = RightPanelConst.PASSWORD_STRENGTH
        self._remove_entry_label = RightPanelConst.REMOVE_ENTRY_BUTTON_LABEL
        
        self._entry: Entry
        self._entry_state: (EntryState | None) = None
        self._undo_in_progress = False
        
        self._placeholder = RightPanelConst.ENTRY_PLACE_HOLDER
        
        self._dropdown_options = list(self._PASSWORD_STRENGTH.keys())
        self._current_password_strength = RightPanelConst.DEFAULT_PASSWORD_STRENGTH
        
        self._record_name_title = RightPanelConst.RECORD_NAME_TITLE
        self._username_title = RightPanelConst.USERNAME_TITLE
        self._password_title = RightPanelConst.PASSWORD_TITLE
        self._url_title = RightPanelConst.URL_TITLE
        
        self._colours = self._command.colours()
        self._text_colour = self._colours.TEXT
        self._input_background_colour = self._colours.INPUT_BACKGROUND
        
        self._password_validator = ValidatePassword()
        
        # Initializing visible objects and binding events
        self._init_ui()
        self._bind_events()
        
    @property
    def undo_available(self) -> bool:
        return self._undo_available

    @undo_available.setter
    def undo_available(self, arg: bool) -> None:
        self._undo_available = arg
    

    @property
    def entry(self) -> Entry:
        return self._entry
    
    @entry.setter
    def entry(self, entry: Entry) -> None:
        self._entry = entry
        
        
    def _init_ui(self):
        """ Function initializing visible interface. """
        
        # Create main sizer
        main_box = wx.BoxSizer(wx.VERTICAL)
        
        # Create ScrolledWindow
        self._scroll = wx.ScrolledWindow(self, -1)
        self._scroll.SetScrollbars(20, 20, 50, 50)
        
        # Sizer for ScrolledWindow.
        self._scroll_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create GUI objects
        record_name_title = wx.StaticText(self._scroll, label=self._record_name_title)
        record_name_title.SetForegroundColour(self._text_colour)
        self._record_name = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER)
        self._record_name.SetForegroundColour(self._text_colour)
        self._record_name.SetBackgroundColour(self._input_background_colour)
        
        username_title = wx.StaticText(self._scroll, label=self._username_title)
        username_title.SetForegroundColour(self._text_colour)
        self._username = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER)
        self._username.SetForegroundColour(self._text_colour)
        self._username.SetBackgroundColour(self._input_background_colour)
        
        password_title = wx.StaticText(self._scroll, label=self._password_title)
        password_title.SetForegroundColour(self._text_colour)
        self._password = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER | wx.TE_PASSWORD)
        self._password.SetForegroundColour(self._text_colour)
        self._password.SetBackgroundColour(self._input_background_colour)
        
        self._reveal_password = wx.Button(self._scroll, label=self._show_password_label)
        
        self._password_strength = wx.ComboBox(self._scroll, choices=self._dropdown_options, style=wx.CB_READONLY)
        self._password_strength.SetForegroundColour(self._text_colour)
        self._password_strength.SetBackgroundColour(self._input_background_colour)
        
        self._generate_password_button = wx.Button(self._scroll, label=self._generate_password_label)
        
        url_title = wx.StaticText(self._scroll, label=self._url_title)
        url_title.SetForegroundColour(self._text_colour)
        self._url = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER)
        self._url.SetForegroundColour(self._text_colour)
        self._url.SetBackgroundColour(self._input_background_colour)
        
        self._remove_entry = wx.Button(self._scroll, label=self._remove_entry_label)
        
        # Add GUI objects to the ScrolledWindow sizer
        self._scroll_sizer.Add(record_name_title, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._record_name, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(username_title, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._username, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(password_title, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._password, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._reveal_password, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._password_strength, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._generate_password_button, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(url_title, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._url, 0, wx.EXPAND | wx.ALL, 5)
        self._scroll_sizer.Add(self._remove_entry, 0, wx.EXPAND | wx.ALL, 5)
        
        # Alter GUI objects depending if an EntryRow was selected or not
        if self._command.selected_entry_row is None:
            self._record_name.Disable()
            self._username.Disable()
            self._password.Disable()
            self._reveal_password.Disable()
            self._password_strength.Disable()
            self._generate_password_button.Disable()
            self._url.Disable()
            self._record_name.SetValue(self._placeholder)
            self._username.SetValue(self._placeholder)
            self._password.SetValue(self._placeholder)
            self._url.SetValue(self._placeholder)
            self._remove_entry.Disable()
        else:
            self.entry = self._command.selected_entry_row.entry
            self._command.edit_panel = self
            
            self._entry_state = EntryState(self.entry.id)
            self.make_snapshot()
            
            entry_name = self.entry.record_name
            username = self.entry.username
            password = self.entry.password
            url = self.entry.url
            self._record_name.SetValue(entry_name)
            self._username.SetValue(username)
            self._password.SetValue(password)
            self._validate_password_strength(None)
            self._url.SetValue(url)

        # Set sizer to the ScrolledWindow
        self._scroll.SetSizer(self._scroll_sizer)
        
        # Add Scrolled Window to the main sizer
        main_box.Add(self._scroll, 1, wx.EXPAND)
        
        # Set the main sizer to the panel
        self.SetSizer(main_box)
        
        # Refresh layout
        self.Layout()
        
        # Create dummy element to Kill Focus in main elements
        self.dummy_panel = wx.Panel(self, size=(0, 0))
        
        
    def _bind_events(self):
        self._record_name.Bind(wx.EVT_TEXT, self._on_record_name)
        self._username.Bind(wx.EVT_TEXT, self._on_username)
        self._password.Bind(wx.EVT_TEXT, self._on_password)
        self._url.Bind(wx.EVT_TEXT, self._on_url)
        
        self._record_name.Bind(wx.EVT_TEXT_ENTER, self._on_enter_pressed)
        self._username.Bind(wx.EVT_TEXT_ENTER, self._on_enter_pressed)
        self._password.Bind(wx.EVT_TEXT_ENTER, self._on_enter_pressed)
        self._url.Bind(wx.EVT_TEXT_ENTER, self._on_enter_pressed)
        
        self._reveal_password.Bind(wx.EVT_BUTTON, self._on_show_password)
        self._generate_password_button.Bind(wx.EVT_BUTTON, self._on_generate_password)
        self._password_strength.Bind(wx.EVT_COMBOBOX, self._on_select_password_strength)
        self._remove_entry.Bind(wx.EVT_BUTTON, self._on_remove_entry)
        
        self._record_name.Bind(wx.EVT_SET_FOCUS, self._on_set_focus)
        self._username.Bind(wx.EVT_SET_FOCUS, self._on_set_focus)
        self._password.Bind(wx.EVT_SET_FOCUS, self._on_set_focus)
        self._url.Bind(wx.EVT_SET_FOCUS, self._on_set_focus)
       
    
    def _on_enter_pressed(self, event) -> None:
        obj = event.GetEventObject()
        if obj.HasFocus():
            self.dummy_panel.SetFocus()
            
        
    def _on_set_focus(self, event) -> None:
        self._undo_available = True

        
    def _on_record_name(self, event) -> None:
        value = self._record_name.GetValue()
        self.entry.record_name = value
        self._on_enter(None)
    
    
    def _on_username(self, event) -> None:
        value = self._username.GetValue()
        self.entry.username = value
        self._on_enter(None)
    
    
    def _on_password(self, event) -> None:
        value = self._password.GetValue()
        self.entry.password = value
        self._validate_password_strength(None)
        self._on_enter(None)
    
    
    def _on_url(self, event) -> None:
        value = self._url.GetValue()
        self.entry.url = value
        self._on_enter(None)
        
        
    def _on_enter(self, event) -> None:
        if self._entry_state is not None and not self._undo_in_progress:
            self.make_snapshot()
        self._command.refresh_on_item_change()
    
    
    def _on_remove_entry(self, event):
        self._command.remove_entry(self.entry)
        
        
    def _validate_password_strength(self, event) -> None:
        password = self.entry.password
        result = self._password_validator.validate_password(password)
        self._current_password_strength = result 
        self._password_strength.SetValue(self._current_password_strength)
        
    def _on_select_password_strength(self, event) -> None:
        self._current_password_strength = self._password_strength.GetValue()
    
    
    def _on_generate_password(self, event) -> None:
        confirmation = dialog_popup(PasswordReplacemetPopup.MESSAGE, PasswordReplacemetPopup.TITLE)
        if confirmation:
            self.make_snapshot()
            self._undo_available = True
            g = GeneratePassword()
            password = g.generate_password(self._PASSWORD_STRENGTH[self._current_password_strength])  
            self._password.SetValue(password)
        
        
    def _on_show_password(self, event):
        if not self._show_password_ind:
            self._show_password_ind = not self._show_password_ind
            self._on_password(None)
            self._password.Destroy()
            self._password = wx.TextCtrl(self._scroll, style=wx.TE_PROCESS_ENTER)
            self._password.Bind(wx.EVT_TEXT_ENTER, self._on_enter)
            self._password.Bind(wx.EVT_KILL_FOCUS, self._on_enter)
            self._password.Bind(wx.EVT_TEXT, self._on_password)
            self._password.SetForegroundColour(self._text_colour)
            self._password.SetBackgroundColour(self._input_background_colour)
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
            self._password.SetForegroundColour(self._text_colour)
            self._password.SetBackgroundColour(self._input_background_colour)
            self._scroll_sizer.Insert(5, self._password, 0, wx.EXPAND | wx.ALL, 5)
            self._password.SetValue(self.entry.password)
            self._reveal_password.SetLabel(self._show_password_label)
            self.Layout()

            
            
    def manage_self_states(self, direction: int = 1):
        if not self._undo_available:
            message_popup(UndoUnavailable.MESSAGE, UndoUnavailable.TITLE)
            return
        
        if self._entry_state is None:
            return 
        
        if direction:
            state = self._entry_state.undo()
        else:
            state = self._entry_state.reverse_undo()
        
        self._undo_in_progress = True
        self._right_panel.undo_in_progress_notes(True)
        
        self._set_values_to_entry(state)
        
        try:
            self._record_name.SetValue(state.record_name)
            self._record_name.SetInsertionPointEnd()
            self._username.SetValue(state.username)
            self._username.SetInsertionPointEnd()
            self._password.SetValue(state.password)
            self._password.SetInsertionPointEnd()
            self._url.SetValue(state.url)
            self._url.SetInsertionPointEnd()
            self._right_panel.set_notes_value(state.notes)
        except RuntimeError:
            pass
        
        self._undo_in_progress = False
        self._right_panel.undo_in_progress_notes(False)
        
        
    def make_snapshot(self) -> None:
        if self._entry_state is not None:
            snapshot = EntrySnapshot(record_name=self.entry.record_name, username=self.entry.username,
                password=self.entry.password, url=self.entry.url, notes=self.entry.notes)
            self._command.commit()
            self._entry_state.snapshot(snapshot)
    
    
    def _set_values_to_entry(self, snapshot: EntrySnapshot) -> None:
        self.entry.record_name = snapshot.record_name
        self.entry.username = snapshot.username
        self.entry.password = snapshot.password
        self.entry.url = snapshot.url
        self.entry.notes = snapshot.notes
        self._command.commit()