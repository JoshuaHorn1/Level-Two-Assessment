"""Find Monster - Version 2
A Component to find specific cards within the 'cards' dictionary.
Developed as function
Text changes
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
        return


def find_monster_1():
    cards_list = []
    for item in cards:
        cards_list.append(item)
    card_name = eg.choicebox("Here are all the cards currently in the system.", "Cards Found", choices=cards_list)
    none_checker(card_name)
    card_name = card_name.capitalize()
    card_stats = cards.get(card_name)
    items = "\n".join([f"{monster}: {stat}" for monster, stat in card_stats.items()])
    proceed = eg.buttonbox(f"Here is the card '{card_name}':\n{items}\n\nWhat would you like to do with it?",
                           "Card Details", choices=("Edit", "Delete", "Cancel"))
    if proceed == "Edit":
        print(">edit card<")
    elif proceed == "Delete":
        confirm = eg.buttonbox(f"Please confirm you want to delete the card '{card_name}'.",
                               "Confirm Delete", choices=("Confirm", "Cancel"))
        if confirm == "Confirm":
            cards.pop(card_name)
            eg.msgbox(f"'{card_name}' deleted.", "Card Deleted")
    else:
        return


def find_monster_2():
    query = eg.enterbox("Enter the card name to search for:", "Enter Query")
    none_checker(query)
    query = query.upper()
    proceed = ""
    while proceed != "Cancel":
        if query in cards:
            searched_for = cards.get(query)
            items = "\n".join([f"{monster}: {stat}" for monster, stat in searched_for.items()])
            proceed = eg.buttonbox(f"Here is the combo, {query.capitalize()}:\n"
                                   f"{items}\n"
                                   f"\n"
                                   f"What would you like to do with it?", "Query Found",
                                   choices=("Edit", "Delete", "Cancel"))
            if proceed == "Edit":
                print(">Edit card<")
            elif proceed == "Delete":
                print(">Delete card<")
            else:
                quit()


find_monster_1()
find_monster_2()
