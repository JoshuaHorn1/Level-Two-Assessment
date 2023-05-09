"""Main Menu - Version 4
A component to display the main menu and branch to other components
Added instructions if user is using for first time
Shortened code - more efficient
"""

import easygui as eg  # importing easygui as 'eg' to save time later


def main_menu(proceed):
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
    print(">exits program<")


new_user = eg.buttonbox("Welcome to the Monster Card System!\nWould you like to a short set of instructions?",
                        "Welcome!", choices=("Yes", "No"))
if new_user == "Yes":
    eg.msgbox("This program allows stores the details of Monster Cards, and allows you to search through them, add new "
              "ones, delete ones, remake ones, or list them and export the full details to the python console."
              "\n\nFarther information about each button can be accessed from the help menu", "Instructions")
main_menu(eg.buttonbox("What would you like to do?", "MAIN MENU",
                       choices=("Find Card", "Add Card", "List Cards", "Help", "Exit")))


