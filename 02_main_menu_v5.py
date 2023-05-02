"""Main Menu - Version 5
A component to display the main menu and branch to other components
Incorporated component 2.1 Exit Button
"""

import easygui as eg  # importing easygui as 'eg' to save time later


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


new_user = eg.buttonbox("Welcome to the Monster Card System!\nWould you like to a short set of instructions?",
                        "Welcome!", choices=("Yes", "No"))
if new_user == "Yes":
    eg.msgbox("This program allows stores the details of Monster Cards, and allows you to search through them, add new "
              "ones, delete ones, remake ones, or list them and export the full details to the python console."
              "\n\nFarther information about each button can be accessed from the help menu", "Instructions")
main_menu(eg.buttonbox("What would you like to do?", "MAIN MENU",
                       choices=("Find Card", "Add Card", "List Cards", "Help", "Exit")))
