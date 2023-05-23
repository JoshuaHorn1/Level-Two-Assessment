"""Main Menu - Version 2
A component to display the main menu and branch to other components
Developed as buttonbox
A welcome message will be displayed the first time the main menu is opened
Trialling variable vs list code block
"""

import easygui as eg  # importing easygui as 'eg' to save time later

proceed = eg.buttonbox("Hello! Welcome to the Monster Card System!\n" "What would you like to do?",
                       "MAIN MENU", choices=("Find Card", "Add Card", "List Cards", "Help", "Exit"))
while proceed != "Exit":  # create a 'while loop' to incorporate functions later on
    if proceed == "Find Card":  # if 'Find Card' button is pressed, will run 'Find Card' component
        print(">find card<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU",
                               choices=("Find Card", "Add Card", "List Cards", "Help", "Exit"))
    elif proceed == "Add Card":  # if ' Add Card button is pressed, etc...
        print(">add card<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU",
                               choices=("Find Card", "Add Card", "List Cards", "Help", "Exit"))
    elif proceed == "List Cards":
        print(">list cards<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU",
                               choices=("Find Card", "Add Card", "List Cards", "Help", "Exit"))
    elif proceed == "Help":
        print(">show help menu<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU",
                               choices=("Find Card", "Add Card", "List Cards", "Help", "Exit"))
print(">exits program<")


options = ["Find Card", "Add Card", "List Cards", "Help", "Exit"]
proceed = eg.buttonbox("Hello! Welcome to the Monster Card System!\n" "What would you like to do?",
                       "MAIN MENU", choices=options)
while proceed != options[4]:
    if proceed == options[0]:
        print(">Find card<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=options)
    elif proceed == options[1]:
        print(">Add card<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=options)
    elif proceed == options[2]:
        print(">list cards<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=options)
    elif proceed == options[3]:
        print(">show help menu<")
        proceed = eg.buttonbox("How would you like to proceed?", "MAIN MENU", choices=options)
    else:
        exit()


