"""Main Menu - Version 5
A component to display the main menu and branch to other components
Trialling 2.1 Exit Button Integrated vs Non-integrated
Incorporated component 2.1 Exit Button
Added function-loop break
"""

import easygui as eg  # importing easygui as 'eg' to save time later


# Integrated code...
def main_menu_integrated(proceed):
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
        if proceed == "Exit":  # if user wants to exit, ask them to confirm exit
            confirm = eg.buttonbox("Please confirm that you want to exit the program.\n\nAll progress will be lost!",
                                   "Confirm Quit", choices=("Yes - Quit", "No - Cancel"))
            if confirm == "No - Cancel":  # if they cancel the exit, return to main menu
                proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU",
                                       choices=("Find Card", "Add Card", "List Cards", "Help", "Exit"))
    exit()  # as a backup, will exit if user confirms exit, in case program is stuck in function loop


def exit_button(proceed):
    if proceed == "Exit":  # if user wants to exit, ask them to confirm exit
        confirm = eg.buttonbox("Please confirm that you want to exit the program.\n\nAll progress will be lost!",
                               "Confirm Quit", choices=("Yes - Quit", "No - Cancel"))
        if confirm == "No - Cancel":  # if they cancel the exit, return to main menu
            proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU",
                                   choices=("Find Card", "Add Card", "List Cards", "Help", "Exit"))
            return proceed


# Non-integrated code...
def main_menu_non_integrated(proceed):
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
    exit_button(proceed)


new_user = eg.buttonbox("Welcome to the Monster Card System!\nWould you like to a short set of instructions?",
                        "Welcome!", choices=("Yes", "No"))
if new_user == "Yes":
    eg.msgbox("This program allows stores the details of Monster Cards, and allows you to search through them, add new "
              "ones, delete ones, remake ones, or list them and export the full details to the python console."
              "\n\nFarther information about each button can be accessed from the help menu", "Instructions")
main_menu_non_integrated(eg.buttonbox("What would you like to do?", "MAIN MENU",
                                      choices=("Find Card", "Add Card", "List Cards", "Help", "Exit")))
main_menu_integrated(eg.buttonbox("What would you like to do?", "MAIN MENU",
                                  choices=("Find Card", "Add Card", "List Cards", "Help", "Exit")))
