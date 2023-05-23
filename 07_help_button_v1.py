"""Help Button - Version 1
A component to display help about each section of each component if needed
Developed code
Added comments
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
    # Asks user what they need help with
    user_help = eg.buttonbox("What do you need help with?", "HELP MENU",
                             choices=("'Find'", "'Add'", "'Edit'", "'Delete'", "'Print'", "'Help'", "'Exit'", "Cancel"))
    while user_help != "Cancel":  # a while loop checking that the user hasn't clicked 'Cancel'
        if user_help == "'Find'":  # If user clicks 'Find', display information about 'Find' Button
            eg.msgbox("This is accessed from a button on the main menu called 'Find Card'. Clicking it will display a "
                      "list of all the cards in the system. Selecting a card will then display two options. 'Edit' or "
                      "'Delete'. Clicking 'Edit' will allow you to edit the details of the card, and clicking delete "
                      "will delete it. You can cancel at any point to return to the main menu.", "'Find' Help")
        elif user_help == "'Add'":  # if user clicks 'Add', display...
            eg.msgbox("This is accessed from a button on the main menu called 'Add Card'. Clicking it will allow you "
                      "to create a new monster card. It will prompt you for the name of the card, and a value for each "
                      "of its four attributes. Once created you will be prompted with two options, 'Edit' or 'Use'. "
                      "Clicking 'Edit' will allow you to edit its details if you made a mistake, and 'Use' will add it "
                      "to the system. You can cancel at any point to return to the main menu.", "'Add' Help")
        elif user_help == "'Edit'":  # etc...
            eg.msgbox("This is accessed through buttons on the 'Add Card' and 'Find Card' menus. Clicking it will "
                      "allow you to choose whether to edit the name of a monster card or its stats. You can choose "
                      "which stat to edit and then the new value. You can cancel at any point to return to the Edit "
                      "Menu. If you make no changes to the card and click 'Finish' in the Edit Menu, it will return no "
                      "changes to the previous component. If you do make changes, you will be asked whether or not you "
                      "want to save those changes.", "'Edit Help'")
        elif user_help == "'Delete'":
            eg.msgbox("This is accessed from a button in the Find Card menu called 'Delete'. When clicking it, it "
                      "will ask you to confirm that you want to delete the card. If you do confirm, it will be removed "
                      "from the cards dictionary. If you don't confirm, it will return to the Find Menu.",
                      "'Delete' Help")
        elif user_help == "'Print'":
            eg.msgbox("This is accessed from a button on the main menu called 'Print Cards'. Clicking it will send a "
                      "full list of all the monster cards currently in the system so that it can be printed/exported. "
                      "A confirmation message will pop up, and then you will be sent back to the main menu.",
                      "'Print' Help")
        elif user_help == "'Help'":
            eg.msgbox("This is accessed from a button on the main menu called 'Help'. Clicking it will display a Help "
                      "Menu, from which you can view helpful tips about each part of the program in case you are "
                      "confused or stuck.", "'Help' Help")
        elif user_help == "'Exit'":
            eg.msgbox("This is accessed from a button on the main menu called 'Exit'. Clicking it will prompt you to "
                      "confirm that you want to exit the program.\n\n*Important Notice* - Changes are not saved when "
                      "you exit the program.", "'Exit' Help")
        user_help = eg.buttonbox("What do you need help with?", "HELP MENU",
                                 choices=("'Find'", "'Add'", "'Edit'", "'Delete'",
                                          "'Print'", "'Help'", "'Exit'", "Cancel"))  # prompts for next help input
    return  # when user clicks cancel, return to main menu


help_button()
