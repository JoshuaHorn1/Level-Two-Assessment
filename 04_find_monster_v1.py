"""Find Monster - Version 1
A Component to find specific cards within the 'cards' dictionary.
Added 3.1 None Checker for testing (edited version)
Added 2. Main Menu for testing
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


cards_list = []
for item in cards:
    cards_list.append(item)
card_name = eg.choicebox("Here are all the cards currently in the system.", "Cards Found", choices=cards_list)
none_checker(card_name)
card_name = card_name.capitalize
card_stats = cards.get(card_name)
items = "\n".join([f"{item}: {stat}" for item, stat in card_stats.items()])
proceed = eg.buttonbox(f"Here is the card '{card_name}':\n{items}\n\nWhat would you like to do with it?",
                       "Card Details", choices=("Use", "Edit", "Cancel"))

