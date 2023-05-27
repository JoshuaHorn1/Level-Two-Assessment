"""Complete Assembled Outcome"""

# Imports...
import pickle  # importing pickle to save the data
import easygui as eg  # importing easygui as 'eg' to save time later


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
# A list containing all the different variables of a card
attributes = ["Strength", "Cunning", "Stealth", "Speed"]


# Functions...
def none_checker(check):
    # Checks if the given variable is None (if cancel has been pressed)
    if check is None:
        # If check is None, call on the main menu function again.
        main_menu(eg.buttonbox("What would you like to do?", "MAIN MENU",
                               choices=("Find Card", "Add Card", "Print Cards",
                                        "Help", "Exit")))


def main_menu(proceed):
    confirm = ""
    while confirm != "Yes - Quit":
        # Create a 'while loop' to incorporate functions later on
        while proceed != "Exit":
            # If 'Find Card' button is pressed, will run 'Find Card' component
            if proceed == "Find Card":
                find_monster()
            elif proceed == "Add Card":  # etc...
                add_monster()
            elif proceed == "Print Cards":
                print_monsters()
            elif proceed == "Help":
                help_button()
            proceed = eg.buttonbox("How would you like to proceed?",
                                   "MAIN MENU", choices=("Find Card",
                                                         "Add Card",
                                                         "Print Cards",
                                                         "Help", "Exit"))
        if proceed == "Exit":  # if user wants to exit, ask them to confirm
            confirm = eg.buttonbox("Please confirm that you want to exit the "
                                   "program.",
                                   "Confirm Exit", choices=("Yes - Quit",
                                                            "No - Cancel"))
            # If they confirm exit, return to main menu
            if confirm == "No - Cancel":
                proceed = eg.buttonbox("How would you like to proceed?",
                                       "MAIN MENU", choices=("Find Card",
                                                             "Add Card",
                                                             "Print Cards",
                                                             "Help", "Exit"))
    save_data()  # calls save_data() function before program quits
    exit()  # exits program incase stuck in function loop


def add_monster():
    card_stats = {}  # creates a dictionary to store data for card statistics
    card_name = eg.enterbox("What is the name of the new Monster Card?",
                            "Enter Name")
    none_checker(card_name)  # calls on none checker function
    # If none checker returns nothing, capitalise the card name
    card_name = card_name.capitalize()
    # checks if user input is original or blank
    while card_name == "" or card_name in cards:
        if card_name == "":
            eg.msgbox("This box cannot be empty.", "Error")  # display error
        elif card_name in cards:
            # Displays error message (card already exists)
            eg.msgbox("This card name already exists. "
                      "Please enter a unique name.", "Error")
        # Gets user input card name again
        card_name = eg.enterbox("What is the name of the new Monster Card?",
                                "Enter Name")
        none_checker(card_name)  # calls on none checker function
        # iI none checker returns nothing, capitalise the card name
        card_name = card_name.capitalize()
    for item in attributes:  # for each attribute, get user input value
        attribute_value = eg.integerbox(f"What is {card_name}'s {item}? "
                                        f"(1-25)", f"Enter {item}",
                                        lowerbound=1, upperbound=25)
        none_checker(attribute_value)  # checks if the user ever cancels
        # If none checker returns nothing, add value to dictionary
        card_stats.update({item: attribute_value})
    finish = ""
    while finish != "Yes":
        # Join all the user details into one new dictionary
        full_card = ({card_name: card_stats})
        # Formats text
        items = "\n".join([f"{item}: {stat}"
                           for item, stat in card_stats.items()])
        # Displays the complete card and gets user input for how to proceed
        proceed = eg.buttonbox(f"Here is the card '{card_name}':\n{items}\n\n"
                               f"What would you like to do with it?",
                               "ADD CARD MENU", choices=("Use", "Edit",
                                                         "Cancel"))
        if proceed == "Use":  # checks if user clicks 'Use'
            cards.update(full_card)  # adds new card to dictionary
            eg.msgbox(f"{card_name} has been added to the dictionary.",
                      "Card Added")  # display message
            return  # returns to main menu
        elif proceed == "Edit":  # checks if user clicks 'Edit'
            # Calls on the edit_monster() function with card values
            edited_card = edit_monster(card_name, card_stats)
            # If the function doesn't return "No Changes"...
            if edited_card != "No Changes":
                card_name = list(edited_card.keys())[0]
                card_stats = edited_card[card_name]
        else:  # checks if user clicked 'Cancel'
            return  # returns to main menu


def find_monster():
    if len(cards) <= 0:
        eg.msgbox("There are currently no cards in the system to print.",
                  "Error - No Cards")
        return
    cards_list = []  # create a list to enter the names of monster cards
    for item in cards:  # for each monster card, append its name to list
        cards_list.append(item)
    # Prompts user to select a monster card from the list
    card_name = eg.choicebox("Here are all the cards currently in the system.",
                             "Cards Found", choices=cards_list)
    none_checker(card_name)  # checks if card_name = None
    card_name = card_name.capitalize()  # if not, capitalise
    card_stats = cards.get(card_name)  # import the stats from selected card
    # Formats the text
    items = "\n".join([f"{monster}: {stat}"
                       for monster, stat in card_stats.items()])
    # Display formatted details of the monster card and prompt user to proceed
    confirm = ""  # create a new variable
    # While loop checking when user confirms exit/delete
    while confirm != "Confirm":
        proceed = eg.buttonbox(f"Here is the card '{card_name}':\n{items}\n\n"
                               f"What would you like to do with it?",
                               "FIND CARD MENU", choices=("Edit", "Delete",
                                                          "Cancel"))
        if proceed == "Edit":  # if user presses the "Edit" button, edit card
            # Calls on the edit_monster() function with card values
            edited_card = edit_monster(card_name, card_stats)
            if edited_card != "No Changes":
                # If the function doesn't return "No Changes"...
                edited_card_name = list(edited_card.keys())[0]
                cards.pop(card_name)
                # Remove old card and add new, edited card
                cards.update(edited_card)
                eg.msgbox(f"The card '{card_name}' has been replaced with "
                          f"'{edited_card_name}' in the dictionary.\n"
                          f"(Changes have been saved and added to the main "
                          f"dictionary)")  # display confirmation
                return  # return to main menu
            else:
                return  # return to main menu
        elif proceed == "Delete":  # if delete, ask to confirm delete
            confirm = eg.buttonbox(f"Please confirm you want to delete the "
                                   f"card '{card_name}'.",
                                   "Confirm Delete", choices=("Confirm",
                                                              "Cancel"))
            if confirm == "Confirm":  # if they confirm, delete card
                cards.pop(card_name)
                # Display confirmation message
                eg.msgbox(f"'{card_name}' deleted.", "Card Deleted")
                return
            elif confirm == "Cancel":
                confirm = ""
        else:  # if Cancel, return to main menu.
            return


def edit_monster(og_card_name, og_card_stats):
    edit = ""  # creates the variable 'edit' and sets value to ""
    # Creates a value for the new card - set it to old card value
    new_card_name = og_card_name
    new_card_stats = og_card_stats
    edit_value = 0  # creates a value to detect if user ever makes an edit
    # A while loop detecting if the user ever wants clicks 'Finish'
    # Formats text
    while edit != "Finish":
        items = "\n".join([f"{item}: {stat}"
                           for item, stat in new_card_stats.items()])
        edit = eg.buttonbox(f"Here is the card '{new_card_name}':\n{items}\n\n"
                            f"What would you like to do?",
                            "EDIT CARD MENU", choices=("Change Name",
                                                       "Change Stats",
                                                       "Finish"))
        if edit == "Change Name":  # if user clicks 'Change Name' button...
            # Asks for new card name
            check_card_name = eg.enterbox("What is the new name of the card?",
                                          "Enter Name")
            if check_card_name is not None:  # checks if user clicked cancel
                # If not, capitalize the value
                new_card_name = check_card_name.capitalize()
                edit_value = 1  # set edit value to 1 - user has made edit
        elif edit == "Change Stats":  # if user clicks 'Change Stats' button...
            # Asks user to pick a value to change, or cancel
            attribute_edit = eg.buttonbox("Which attribute/stat would you "
                                          "like to change?",
                                          "Which Attribute?",
                                          choices=("Strength", "Cunning",
                                                   "Stealth", "Speed",
                                                   "Cancel"))
            # If user doesnt click cancel, get value for attribute
            if attribute_edit != "Cancel":
                new_value = eg.integerbox(f"What is '{new_card_name}'s' new "
                                          f"{attribute_edit} value? (1-25)",
                                          lowerbound=1, upperbound=25)
                # If user doesnt click cancel, update card_stats
                if new_value is not None:
                    edit_value = 1  # set edit value to 1 - user has made edit
                    new_card_stats.update({attribute_edit: new_value})
        else:  # go here when user clicks 'Finish'
            if edit_value == 1:  # checks if user has made a change anywhere
                # Asks user if they want to save their changes to the card
                save = eg.buttonbox("Would you like to save your changes?",
                                    "Save?", choices=("Yes", "No"))
                if save == "Yes":  # if 'Yes', return new values
                    full_card = {new_card_name: new_card_stats}
                    return full_card
                else:  # if 'No', return "No Changes"
                    return "No Changes"
            else:  # if no changes were made, return "No Changes"
                return "No Changes"


def print_monsters():
    if len(cards) <= 0:
        eg.msgbox("There are currently no cards in the system to print.",
                  "Error - No Cards")
        return
    # Prints a beginning to the dictionary
    print("~ ~ ~ FULL CARD LIST ~ ~ ~\n--------------------------\n")
    for card_name, card_stats in cards.items():
        # Repeats the print for each item in the dictionary
        print(f"{card_name.capitalize()}:")  # prints name of card
        for attribute, value in card_stats.items():
            # For each attribute, take its value and print
            print(f"- {attribute}: {value}")
        print()
    print("--------------------------")  # print an end separation barrier
    print()
    # Display a confirmation message
    eg.msgbox("A full list of the Monster Cards has been sent to the python "
              "console.", "Cards Printed")
    return  # return to main menu


def help_button():
    # Asks user what they need help with
    user_help = eg.buttonbox("What do you need help with?", "HELP MENU",
                             choices=("'Find'", "'Add'", "'Edit'", "'Delete'",
                                      "'Print'", "'Help'", "'Exit'", "Cancel"))
    # A while loop checking that the user hasn't clicked 'Cancel'
    while user_help != "Cancel":
        # If user clicks 'Find', display information about 'Find' Button
        if user_help == "'Find'":
            eg.msgbox("This is accessed from a button on the main menu called "
                      "'Find Card'. Clicking it will display a list of all "
                      "the cards in the system. Selecting a card will then "
                      "display two options. 'Edit' or 'Delete'. Clicking "
                      "'Edit' will allow you to edit the details of the card, "
                      "and clicking delete will delete it. You can cancel at "
                      "any point to return to the main menu. If there are no "
                      "cards in the system, an error message will be "
                      "displayed.", "'Find' Help")
        elif user_help == "'Add'":  # if user clicks 'Add', display...
            eg.msgbox("This is accessed from a button on the main menu called "
                      "'Add Card'. Clicking it will allow you to create a new "
                      "monster card. It will prompt you for the name of the "
                      "card, and a value for each of its four attributes. "
                      "Once created you will be prompted with two options, "
                      "'Edit' or 'Use'. Clicking 'Edit' will allow you to "
                      "edit its details if you made a mistake, and 'Use' will "
                      "add it to the system. You can cancel at any point to "
                      "return to the main menu.", "'Add' Help")
        elif user_help == "'Edit'":  # etc...
            eg.msgbox("This is accessed through buttons on the 'Add Card' and "
                      "'Find Card' menus. Clicking it will allow you to "
                      "choose whether to edit the name of a monster card or "
                      "its stats. You can choose which stat to edit and then "
                      "the new value. You can cancel at any point to return "
                      "to the Edit Menu. If you make no changes to the card "
                      "and click 'Finish' in the Edit Menu, it will return no "
                      "changes to the previous component. If you do make "
                      "changes, you will be asked whether or not you want to "
                      "save those changes.", "'Edit Help'")
        elif user_help == "'Delete'":
            eg.msgbox("This is accessed from a button in the Find Card menu "
                      "called 'Delete'. When clicking it, it will ask you to "
                      "confirm that you want to delete the card. If you do "
                      "confirm, it will be removed from the cards dictionary. "
                      "If you don't confirm, it will return to the Find Menu.",
                      "'Delete' Help")
        elif user_help == "'Print'":
            eg.msgbox("This is accessed from a button on the main menu called "
                      "'Print Cards'. Clicking it will send a full list of "
                      "all the monster cards currently in the system so that "
                      "it can be printed/exported. A confirmation message "
                      "will pop up, and then you will be sent back to the "
                      "main menu. If there are no cards in the system, an "
                      "error message will be displayed.'", "Print' Help")
        elif user_help == "'Help'":
            eg.msgbox("This is accessed from a button on the main menu called "
                      "'Help'. Clicking it will display a Help Menu, from "
                      "which you can view helpful tips about each part of "
                      "the program in case you are confused or stuck.",
                      "'Help' Help")
        elif user_help == "'Exit'":
            eg.msgbox("This is accessed from a button on the main menu called "
                      "'Exit'. Clicking it will prompt you to confirm that "
                      "you want to exit the program.\n\n*Important Notice* - "
                      "You will be prompted on whether or not you want to "
                      "save your progress after quitting. Only one set of "
                      "data can be saved at a time. Upon starting the program "
                      "up again, you will be prompted for if you want to "
                      "import the saved data. Clicking yes will load saved "
                      "data, clicking no will load the default values that "
                      "are saved to the dictionary.", "'Exit' Help")
        # Prompts for next help input
        user_help = eg.buttonbox("What do you need help with?", "HELP MENU",
                                 choices=("'Find'", "'Add'", "'Edit'",
                                          "'Delete'", "'Print'", "'Help'",
                                          "'Exit'", "Cancel"))
    return  # when user clicks cancel, return to main menu


def save_data():
    # Asks user if they want to save their data
    save = eg.buttonbox("Do you want to save your data?", "SAVE DATA",
                        choices=("Yes", "No"))
    if save == "Yes":  # if 'Yes', pickle the 'cards' dictionary into a file
        with open("saved_progress.pkl", "wb") as file:
            pickle.dump(cards, file)
        # Display confirmation
        eg.msgbox("Data successfully saved, program closing.", "Data Saved")
    else:  # if 'No', do nothing
        # Display confirmation
        eg.msgbox("Data not saved, program closing.", "Data Not Saved")


def load_data():
    global cards  # announces the variable 'cards' as global
    # Asks user if they want to import the saved data
    load = eg.buttonbox("Do you want to import the saved data?", "LOAD DATA",
                        choices=("Yes", "No"))
    if load == "Yes":  # if 'Yes', import the saved data file
        with open("saved_progress.pkl", "rb") as file:
            cards = pickle.load(file)
        # Display confirmation
        eg.msgbox("Data successfully imported.", "Saved Data Imported")
    else:  # if 'No', keep the default values
        # Display confirmation
        eg.msgbox("Data not imported, loading with standard values.",
                  "Saved Data Not Imported")


# Main code...
# Checks if the user wants to see instructions
new_user = eg.buttonbox("Welcome to the Monster Card System!\nWould you like "
                        "to a short set of instructions?",
                        "Welcome!", choices=("Yes", "No"))
if new_user == "Yes":  # if yes, show instructions
    eg.msgbox("This program stores the names and details of different Monster Cards, as well as allowing you to search "
              "through the cards, add new cards, delete cards, edit cards, or list them and export the full details to "
              "the python console.\n\nFarther information about each button can be accessed from the help menu",
              "Instructions")
load_data()  # call on the load_data() function
# Call on main menu function with user input
main_menu(eg.buttonbox("What would you like to do?", "MAIN MENU",
                       choices=("Find Card", "Add Card", "Print Cards",
                                "Help", "Exit")))
