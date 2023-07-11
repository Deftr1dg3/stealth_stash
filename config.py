#!/usr/bin/env python3


from typing import NamedTuple
from dataclasses import dataclass
from manage_password import PasswordStrength

@dataclass(frozen=True)
class DataFilePath:
    DATA_FILE_PATH = "/Users/stasusbondevito/Documents/PYTHON/Projects/KeyKeeper"
    BACKUP_PATH = ""


@dataclass(frozen=True)
class TopBarConst:
    LEFT_PANEL_SIZE = (200, 30)
    NEW_CATEGORY_BUTTON_SIZE = (180, -1)
    NEW_CATEGORY_LABEL = "Category +"
    NEW_ENTRY_LABEL = "Entry  +"
    SEARCH_FILED_SIZE = (200, -1)
    SEARCH_PLACE_HOLDER = "Search record ..."
    RIGHT_PANEL_TITLE = "Edit Entry:"
    RIGHT_PANEL_SIZE = (250, 30)
    

@dataclass(frozen=True)
class LeftPanelConst:
    PANEL_SIZE = (200, -1)
    SCROLL_SETTINGS = (20, 20, 50, 50)
    CATEGORY_ROW_SIZE = (200, 30)
    ICON_FOLDER = "folder"
    CATEGORY_PANEL_SIZE = (170, 30)
    CATEGORY_NAME_MAX_LENGTH = 16
    EXTRA_CHARACTERS_REPLACEMENT = "..."
    

@dataclass(frozen=True)
class MidPanelConst:
    SCROLL_SETTINGS = (20, 20, 50, 50)
    ENTRY_ROW_SIZE = (-1, 30)
    DISPLAYED_STRING_LEGTH = 12
    DISPLAYED_PASSWORD_LENGTH = 8
    ENTRY_ROW_COLOUR_STEP = 2
    RECORD_PANEL_COLOUR_STEP = 1
    EXTRA_CHARACTERS_REPLACEMENT = "..."
    

@dataclass(frozen=True)
class RightPanelConst:
    PANEL_SIZE = (250, -1)
    SCROLL_SETTINGS = (20, 20, 50, 50)
    NOTES_TITLE = "Notes:"
    NOTES_FIELD_SIZE = (-1, 150)
    SHOW_PASSWORD_BUTTON_LABEL = "Show Passowrd"
    HIDE_PASSWORD_BUTTON_LABEL = "Hide Password"
    GENERATE_PASSWORD_BUTTON_LABEL = "Generate New Passowrd"
    REMOVE_ENTRY_BUTTON_LABEL = "Remove Entry"
    PASSWORD_STRENGTH = {
                        'VERY STRONG': PasswordStrength.VERY_STRONG,
                        'STRONG': PasswordStrength.STRONG,
                        'MEDIUM': PasswordStrength.MEDIUM,
                        'WEAK': PasswordStrength.WEAK,
                        'VERY WEAK': PasswordStrength.VERY_WEAK,
                        }
    ENTRY_PLACE_HOLDER = "No Entry Selected"
    DEFAULT_PASSWORD_STRENGTH = "STRONG"
    RECORD_NAME_TITLE = "Entry Name:"
    USERNAME_TITLE = "Username:"
    PASSWORD_TITLE = "Password:"
    URL_TITLE = "URL://"
    
    
@dataclass(frozen=True)
class PasswordReplacemetPopup:
    TITLE = "IMPORTANT: Confirmation"
    MESSAGE = ("If you generate a new password, " 
                "the current one will be LOST. "
                "Are you sure you want to proceed?")
            

@dataclass(frozen=True)
class CategoryExistsPopup:
    TITLE = "Error."
    MESSAGE = "Unable to create Categiry. Category with selected name --> '{}' aready exists."
    

@dataclass(frozen=True)
class NewCategoryPopup:
    TITLE = "Create New Category"
    MESSAGE = "Insert desired category name"
    
    
@dataclass(frozen=True)
class RenameCategoryPopup:
    TITLE = "Rename Category"
    MESSAGE = "Insert desired category name"
    
@dataclass(frozen=True)
class NoCategorySelectedPopup:
    TITLE = "Error."
    MESSAGE = "No Category selected."


@dataclass(frozen=True)
class NoEntrySelectedPopup:
    TITLE = "Error."
    MESSAGE = "No Entry selected."
    
@dataclass(frozen=True)
class RemoveConfirmationPopup:
    TITLE = "INPORTANT: Confirmation"
    MESSAGE = "All content of the '{}' will be permanentely LOST.\nARE YOU SURE YOU WANT TO CONTINUE?"