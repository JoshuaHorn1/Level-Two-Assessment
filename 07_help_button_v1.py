"""Help Button - Version 1
A component to display help about each section of each component if needed
"""
import easygui as eg  # importing easygui as 'eg' to save time later
cards = {
    "Stoneling": {
        "Strength": 7,
        "Cunning": 15,
        "Stealth": 25,
        "Speed": 1
    },
    "Vexscream": {
        "Strength": 1,
        "Cunning": 19,
        "Stealth": 21,
        "Speed": 6
    },
    "Dawnmirage": {
        "Strength": 5,
        "Cunning": 22,
        "Stealth": 18,
        "Speed": 15
    },
    "Blazegolem": {
        "Strength": 15,
        "Cunning": 6,
        "Stealth": 23,
        "Speed": 20
    },
    "Websnake": {
        "Strength": 7,
        "Cunning": 5,
        "Stealth": 10,
        "Speed": 15
    },
    "Moldvine": {
        "Strength": 21,
        "Cunning": 5,
        "Stealth": 14,
        "Speed": 18
    },
    "Vortexwing": {
        "Strength": 19,
        "Cunning": 2,
        "Stealth": 19,
        "Speed": 13
    },
    "Rotthing": {
        "Strength": 16,
        "Cunning": 12,
        "Stealth": 4,
        "Speed": 7
    },
    "Froststep": {
        "Strength": 14,
        "Cunning": 4,
        "Stealth": 17,
        "Speed": 14
    },
    "Wispghoul": {
        "Strength": 17,
        "Cunning": 2,
        "Stealth": 3,
        "Speed": 19
    },
}  # a dictionary containing all the monster card data


def help_button():
    user_help = eg.buttonbox("What do you need help with?", "HELP MENU",
                             choices=("'Find'", "'Add'", "'Edit'", "'Delete'", "'Print'", "'Help'", "'Exit'", "Cancel"))
    if user_help == "'Find'":
        eg.msgbox("This is accessed from a button on the main menu called 'Find Card'. Clicking it will display a list "
                  "of all the cards in the system. Selecting a card will then display two options. 'Edit' or 'Delete'. "
                  "Clicking 'Edit' will allow you to edit the details of the card, and clicking delete will delete it. "
                  "You can cancel at any point to return to the main menu.", "'Find' Help")
    elif user_help == "'Add'":
        eg.msgbox("This is accessed from a button on the main menu called 'Add Card'. Clicking it will allow you to "
                  "create a new monster card. It will prompt you for the name of the card, and a value for each of its "
                  "four attributes. Once created you will be prompted with two options, 'Edit' or 'Use'. Clicking "
                  "'Edit' will allow you to edit its details if you made a mistake, and 'Use' will add it to the "
                  "system. You can cancel at any point to return to the main menu.", "'Add' Help")
    elif user_help == "'Edit'":
        eg.msgbox("This is accessed through the 'Add Card' and 'Find Card' buttons.", "'Edit Help'")
