"""Edit Monster - Version 1
A component to edit a monster card
Developed main structure
"""
import easygui as eg  # importing easygui as 'eg' to save time later
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


def edit_monster(card_name, card_stats):
    items = "\n".join([f"{item}: {stat}" for item, stat in card_stats.items()])  # formats text
    edit = eg.buttonbox(f"Here is the card '{card_name}':\n{items}\n\nWhat would you like to change?",
                        "Edit Card", choices=("Change Name", "Change Stats", "Cancel"))
    if edit == "Change Name":
    elif edit == "Change Stats":
    else:
        return


full_card = {"Stoneling": {"Strength": 7, "Cunning": 15, "Stealth": 25, "Speed": 1}}
card_name = "Stoneling"
card_stats = {"Strength": 7, "Cunning": 15, "Stealth": 25, "Speed": 1}
edit_monster(card_name, card_stats)
