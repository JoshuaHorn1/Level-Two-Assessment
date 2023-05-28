"""Add Monster - Version 2
A component to add a new monster card to dictionary
Developed method 2 after trialling
Displays created card details and asks for user proceed prompt
"""
import easygui as eg
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
}
card_stats = {}
attributes = ["Strength", "Cunning", "Stealth", "Speed"]

card_name = eg.enterbox("What is the name of the new Monster Card?", "Enter Name").capitalize()
while card_name == "" or card_name in cards:
    if card_name == "":
        eg.msgbox("This box cannot be empty.", "Error")
    elif card_name in cards:
        eg.msgbox("This card name already exists. Please enter a unique name.", "Error")
    card_name = eg.enterbox("What is the name of the new Monster Card?", "Enter Name").capitalize()
for item in attributes:
    attribute_value = eg.integerbox(f"What is {card_name}'s {item}? (1-25)", "Enter Attribute", lowerbound=1, upperbound=25)
    card_stats.update({item: attribute_value})
full_card = ({card_name: card_stats})
items = "\n".join([f"{item}: {stat}" for item, stat in card_stats.items()])
proceed = eg.buttonbox(f"Here is the card '{card_name}':\n{items}\n\nWhat would you like to do with it?",
                       "Card Details", choices=("Use", "Edit", "Cancel"))
