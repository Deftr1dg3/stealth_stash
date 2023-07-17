#!/usr/bin/env python3

import wx
from dataclasses import dataclass
from manage_password import PasswordStrength
app = wx.App()



@dataclass(frozen=True)
class GeneralConst:
    DATAFILE_EXTENSION = ".kkdf"
    DEFAULT_DATAFILE_NAME = "KeyKeeper"
    

@dataclass(frozen=True)
class PassowrdStrengthConst:
    VERY_WEAK = "VERY WEAK"
    WEAK = "WEAK"
    MEDIUM = "MEDIUM"
    STRONG = "STRONG"
    VERY_STRONG = "VERY STRONG"

    
@dataclass(frozen=True)
class SetNewPasswordConst:
    TITLE = "Create New Password"
    CONFIRM_LABEL = "Confirm"
    CANCEL_LABEL = "Cancel"
    PASSWORD_STRENGTH_TITLE_LABEL = "Password strength:"
    NEW_PASSOWRD_HINT = "Insert new password"
    CONFIRM_NEW_PASSWORD_HINT = "Confirm new password"
    VERY_WEAK_COLOUR = "#9B0602"
    WEAK_COLOUR = "#B03B03"
    MEDIUM_COLOUR = "#C8B903"
    STRONG_COLOUR = "#11D900"
    VERY_STROG_COLOUR = "#1CE500"
    INPUT_FIELD_SIZE = (200, -1)
    DISTANCE_BETWEEN_BUTTONS = 10
    

@dataclass(frozen=True)
class NewLaunchConst:
    TITLE = "Key Keeper"
    WRONG_EXTENSION_TITLE = "Wrong File Extension"
    WRONG_EXTENSION_MESSAGE = "Provided file has wrong extension and most probably is incompatible with current app. Do you wish to proceed anyway?"
    CREATE_NEW_LABEL = "Create new DataFile"
    IMPORT_DATAFILE_LABEL = "Import existing DataFile"
    
@dataclass(frozen=True)
class PassowrdWindowConst:
    TITLE = "Key Keeper"
    SIZE = (400, 200)
    STYLE = wx.CLOSE_BOX
    PASSOWRD_HINT = "Insert password ... "
    CHOOSE_DATAFILE_LABEL = "^ Choose another DataFile"
    DIALOG_MESSAGE = "Either the file is not correct or password. Do you wish to try again?"
    DIALOG_TITLE = "Unable to decode the file."
    
    
@dataclass(frozen=True)
class MainFrameConst:
    TITLE = "Key Keeper"
    SIZE = (1100, 600)
    MIN_SIZE = (800, 400)


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
    THEME_BUTTON_LABEL = "Colour Theme"
    

@dataclass(frozen=True)
class LeftPanelConst:
    PANEL_SIZE = (200, -1)
    SCROLL_SETTINGS = (20, 20, 50, 50)
    CATEGORY_ROW_SIZE = (200, 30)
    ICON_INTERNET = {"internet", "connection", "connections", "online", "www", "world wide web", "account", "accounts"}
    ICON_EMAIL = {"mail", "mails", "email", "emails"}
    ICON_CRYPTO = {"crypto", "btc", "bitcoin", "bitcoins"}
    ICON_DEVOPS = {"development", "c", "c++", "python", "java", "javascript", "rust", "ruby", "php", "git-hub", "github", "git_hub", "dev", "devops", "gamedev"}
    ICON_DATABASE = {"database", "databases", "data", "mysql", "psql", "postgres", "postgresql", "sql", "storage"}
    ICON_FUNDS = {"funds", "fund", "bank", "banks", "paypal", "pay-pal", "pay_pal"}
    ICON_PAYMENTS = {"payments", "payment"}
    ICON_FOLDER = {"folder",}
    CATEGORY_PANEL_SIZE = (170, 30)
    CATEGORY_NAME_MAX_LENGTH = 16
    EXTRA_CHARACTERS_REPLACEMENT = "..."
    

@dataclass(frozen=True)
class MidPanelConst:
    SCROLL_SETTINGS = (20, 20, 50, 50)
    ENTRY_ROW_SIZE = (-1, 30)
    DISPLAYED_STRING_LEGTH = 12
    DISPLAYED_PASSWORD_LENGTH = 8
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
class SelectColourSchemeConst:
    TITLE = "Select Colour Scheme"
    SIZE = (300, 190)
    STYLE = wx.CLOSE_BOX
    BACKGROUND_COLOUR = "#202020"
    CIRCLE_PANEL_PEN_COLOUR = "GREY"
    CIRCLE_PANEL_PEN_SIZE = 2
    BUTTON_CONFIRM_LABEL = "Confirm"
    BUTTON_CANCEL_LABEL = "Cancel"
    

@dataclass(frozen=True)
class MenueConst:
    # Fields in top menu
    FIRST_FIELD_LABEL = "File"
    SECONDFIELD_LABEL = "Edit"
    
    # Under first field
    NEW_CATEGORY_LABEL = "New Category"
    NEW_CATEGORY_SHORTCUT = "Shift+Ctrl+N"
    REMOVE_CATEGORY_LABEL = "Remove Category"
    REMOVE_CATEGORY_SHORTCUT = "Shift+Ctrl+D" 
    RENAME_CATEGORY_LABEL = "Rename Category"
    NEW_ENTRY_LABEL = "New Entry"
    NEW_ENTRY_SHORTCUT = "Ctrl+N"
    REMOVE_ENTRY_LABEL = "Remove Entry"
    REMOVE_ENTRY_SHORTCUT = "Ctrl+D"
    CLEAR_CATEGORY_LABEL = "Clear Category"
    CHANGE_PASSOWRD_LABEL = "Change Password"
    SHOW_DATAFILE_IN_FOLDER_LABEL = "Show DataFile in Folder"
    CHANGE_DATAFILE_DIRECTORY_LABEL = "Change Datafile Directory to ..."
    CHANGE_DATAFILE_LABEL = "Choose Another DataFile"
    EXIT_LABEL = "Exit"
    EXIT_SHORTCUT = "Ctrl+Q"
    
    # Under second field
    COPY_USERNALE_LABEL = "Copy Username"
    COPY_USERNAME_SHORTCUT = "Ctrl+A"
    COPY_PASSOWRD_LABEL = "Copy Password"
    COPY_PASSOWRD_SHORTCUT = "Ctrl+X"
    COPY_URL_LABEL = "Copy URL"
    COPY_URL_SHORTCUT = "Ctrl+W"
    UNDO_LABLE = "Undo"
    UNDO_SHORTCUT = "Ctrl+Z"
    REDO_LABLE = "Reverse Undo"
    REDO_SHORTCUT = "Shift+Ctrl+Z"

    

    
    
#  POPUPS ------------------------------------------------------------------------ 
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
    
@dataclass(frozen=True)
class WrongExtensionPopup:
    TITLE = "Wrong File Extension"
    MESSAGE = "Provided file has wrong extension and most probably is incompatible with current app. Do you wish to proceed anyway?"
    

@dataclass(frozen=True)
class PasswordDoesNotMatchPopup:
    TITLE = "Error."
    MESSAGE = "Confirmation of password does not match."
    
    
@dataclass(frozen=True)
class PasswordCreatedPopup:
    TITLE = "The password has been applied"
    MESSAGE = "IMPORTANT.\nPlease remember this passowrd. There is no way to restore it."
    

@dataclass(frozen=True)
class SaveAsPopup:
    TITLE = "Save KeyKeeper Datafile As..."



@dataclass(frozen=True)
class SelectFilePopup:
    TITLE = "Choose a file"
    WILDCARD = "*.*"
    DEFAULT_DIRECTORY = "./"
    
@dataclass(frozen=True)
class SelectDirectoryPopup:
    TITLE = "Choose a directory:"
    
    
    

    
@dataclass(frozen=True)
class UndoUnavailable:
    TITLE = "Unable to change current state."
    MESSAGE = "Please select one of the fields first."
    
@dataclass(frozen=True)
class ChangeColourSchemeConfirmation:
    TITLE = "Confirmation"
    MESSAGE = "In order to change the colour scheme the app has to be restarted. Do you want to proceed?"
    

@dataclass(frozen=True)
class CopyPopupConst:
    FRAME_BACKGROUND_COLOUR = "#00000000"
    SIZE = (200, 200)
    ROUND_ANGLE_RADIUS = 10
    MESSAGE = "Copied..."
    FONT_SIZE = 30
    TRANSFORMATION_SPEED = 25
    TRANSFORMATION_STEP = 5
    CURRENT_TRANSPARENCY = 250
    BACKGROUND_COLOR = "#101010"
    TEXT_COLOUR = "white"