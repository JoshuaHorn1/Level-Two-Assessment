"""Find Monster - Version 4
A Component to find specific cards within the 'cards' dictionary.
Developed as choicebox
Added more comments
"""
import easygui as eg  # importing easygui as 'eg' to save time later
global cards
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


def none_checker(check):
    if check is None:  # checks if the given variable is None (if cancel has been pressed)
        quit()


def find_monster():
    cards_list = []  # create a list to enter the names of monster cards
    for item in cards:  # for each monster card, append its name to list
        cards_list.append(item)
    # Prompts user to select a monster card from the list
    card_name = eg.choicebox("Here are all the cards currently in the system.", "Cards Found", choices=cards_list)
    none_checker(card_name)  # checks if card_name = None
    card_name = card_name.capitalize()  # if not, capitalise
    card_stats = cards.get(card_name)  # import the stats from the selected card
    items = "\n".join([f"{monster}: {stat}" for monster, stat in card_stats.items()])  # formats the text
    # Display formatted details of the monster card and prompt user for input to proceed
    confirm = ""  # create a new variable
    while confirm != "Confirm":  # while loop checking when user confirms exit
        proceed = eg.buttonbox(f"Here is the card '{card_name}':\n{items}\n\nWhat would you like to do with it?",
                               "Card Details", choices=("Edit", "Delete", "Cancel"))
        if proceed == "Edit":  # if user presses the "Edit" button, edit card
            print(">edit card<")
        elif proceed == "Delete":  # if delete, ask to confirm delete
            confirm = eg.buttonbox(f"Please confirm you want to delete the card '{card_name}'.",
                                   "Confirm Delete", choices=("Confirm", "Cancel"))
            if confirm == "Confirm":  # if they confirm, delete card
                cards.pop(card_name)
                eg.msgbox(f"'{card_name}' deleted.", "Card Deleted")  # display confirmation message
                return
            elif confirm == "Cancel":
                confirm = ""
        else:  # if Cancel, return to main menu.
            return


find_monster()
