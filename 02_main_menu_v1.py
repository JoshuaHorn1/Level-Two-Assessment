"""Main Menu - Version 1
A component to display the main menu and branch to other components
a welcome message will be displayed the first time the main menu is opened"""

import easygui as eg  # importing easygui as 'eg' to save time later

proceed = eg.buttonbox("Hello! Welcome to the Monster Card System!\n"
                       "What would you like to do?", "MAIN MENU", choices=("Find", "Add", "List", "Help", "Exit"))
while proceed != "Exit":  # create a 'while loop' to incorporate functions later on
    if proceed == "Find":

    elif proceed == "Add":

    elif proceed == "List":

    elif proceed == "Help":
