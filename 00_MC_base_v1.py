"""Monster Cards Base Code - Version 1
Components added after being tested/trialled and finalised
Added 01_monster_cards_v2
Added 02_main_menu_v5
"""

# Imports/Globals...
import easygui as eg  # importing easygui as 'eg' to save time later
global cards


# Lists/Dictionaries...
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
}


# Functions...
def main_menu(proceed):
    confirm = ""
    while confirm != "Yes - Quit":
        while proceed != "Exit":  # create a 'while loop' to incorporate functions later on
            if proceed == "Find Card":  # if 'Find Card' button is pressed, will run 'Find Card' component
                print(">find card<")
            elif proceed == "Add Card":  # if ' Add Card button is pressed, etc...
                print(">add card<")
            elif proceed == "List Cards":
                print(">list cards<")
            elif proceed == "Help":
                print(">show help menu<")
            proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU",
                                   choices=("Find Card", "Add Card", "List Cards", "Help", "Exit"))
        if proceed == "Exit":
            confirm = eg.buttonbox("Please confirm that you want to exit the program.\n\nAll progress will be lost!",
                                   "Confirm Quit", choices=("Yes - Quit", "No - Cancel"))
            if confirm == "No - Cancel":
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU",
                                       choices=("Find Card", "Add Card", "List Cards", "Help", "Exit"))


# Main code...
new_user = eg.buttonbox("Welcome to the Monster Card System!\nWould you like to a short set of instructions?",
                        "Welcome!", choices=("Yes", "No"))
if new_user == "Yes":
    eg.msgbox("This program allows stores the details of Monster Cards, and allows you to search through them, add new "
              "ones, delete ones, remake ones, or list them and export the full details to the python console."
              "\n\nFarther information about each button can be accessed from the help menu", "Instructions")
main_menu(eg.buttonbox("What would you like to do?", "MAIN MENU",
                       choices=("Find Card", "Add Card", "List Cards", "Help", "Exit")))
