"""Monster Cards Base Code - Version 1
Components added after being tested/trialled and finalised
Added 03_add_monster_v5 (and 3.1 None Checker Component)
Added 'attributes' list from 03_add_monster_v5 component
Calls add_monster() function from main menu
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
}  # a dictionary containing all the monster card data
attributes = ["Strength", "Cunning", "Stealth", "Speed"]  # a list containing all the different variables of a card


# Functions...
def none_checker(check):
    if check is None:  # checks if the given variable is None (if cancel has been pressed)
        # If check is None, call on the main menu function again. If not, do nothing
        main_menu(eg.buttonbox("What would you like to do?", "MAIN MENU",
                               choices=("Find Card", "Add Card", "List Cards", "Help", "Exit")))


def main_menu(proceed):
    confirm = ""
    while confirm != "Yes - Quit":
        while proceed != "Exit":  # create a 'while loop' to incorporate functions later on
            if proceed == "Find Card":  # if 'Find Card' button is pressed, will run 'Find Card' component
                print(">find card<")
            elif proceed == "Add Card":  # if ' Add Card button is pressed, etc...
                add_monster()
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


def add_monster():
    card_stats = {}  # creates a dictionary to store data for card statistics
    card_name = eg.enterbox("What is the name of the new Monster Card?", "Enter Name")
    none_checker(card_name)  # calls on none checker function
    card_name = card_name.capitalize()  # if none checker returns nothing, capitalise the card name
    while card_name == "" or card_name in cards:  # checks if user input is original or blank
        if card_name == "":
            eg.msgbox("This box cannot be empty.", "Error")  # display error message (card blank)
        elif card_name in cards:
            # Displays error message (card already exists)
            eg.msgbox("This card name already exists. Please enter a unique name.", "Error")
        # Gets user input card name again
        card_name = eg.enterbox("What is the name of the new Monster Card?", "Enter Name")
        none_checker(card_name)  # calls on none checker function
        card_name = card_name.capitalize()  # if none checker returns nothing, capitalise the card name
    for item in attributes:  # for each attribute, get user input value
        attribute_value = eg.integerbox(f"What is {card_name}'s {item}? (1-25)",
                                        f"Enter {item}", lowerbound=1, upperbound=25)
        none_checker(attribute_value)  # checks if the user ever cancels
        card_stats.update({item: attribute_value})  # if none checker returns nothing, add value to dictionary
    full_card = ({card_name: card_stats})  # join all the user details into one new dictionary
    items = "\n".join([f"{item}: {stat}" for item, stat in card_stats.items()])  # formats text
    # Displays the complete card and gets user input for how to proceed
    proceed = eg.buttonbox(f"Here is the card '{card_name}':\n{items}\n\nWhat would you like to do with it?",
                           "Card Details", choices=("Use", "Edit", "Cancel"))
    if proceed == "Use":  # checks if user clicks 'Use'
        cards.update(full_card)  # adds new card to dictionary
        eg.msgbox(f"{card_name} has been added to the dictionary.", "Card Added")  # display message
        return  # returns to main menu
    elif proceed == "Edit":  # checks if user clicks 'Edit'
        print(">edit card<")
    else:  # checks if user clicked 'Cancel'
        return  # returns to main menu


# Main code...
new_user = eg.buttonbox("Welcome to the Monster Card System!\nWould you like to a short set of instructions?",
                        "Welcome!", choices=("Yes", "No"))  # checks if the user wants to see instructions
if new_user == "Yes":  # if yes, show instructions
    eg.msgbox("This program allows stores the details of Monster Cards, and allows you to search through them, add new "
              "ones, delete ones, remake ones, or list them and export the full details to the python console."
              "\n\nFarther information about each button can be accessed from the help menu", "Instructions")
# Call on main menu function with user input
main_menu(eg.buttonbox("What would you like to do?", "MAIN MENU",
                       choices=("Find Card", "Add Card", "List Cards", "Help", "Exit")))
