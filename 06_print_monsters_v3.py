"""Print Monsters - Version 3
A component to list all the cards in the system
Converted to function
Added comments
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


def print_monsters():
    print("~ ~ ~ FULL CARD LIST ~ ~ ~\n--------------------------\n")  # prints a beginning to the dictionary
    for card_name, card_stats in cards.items():  # repeats the print for each item in the dictionary
        print(f"{card_name.capitalize()}:")  # prints name of card
        for attribute, value in card_stats.items():  # for each attribute, take its value and print
            print(f"- {attribute}: {value}")
        print()
    print("--------------------------")  # print an end separation barrier
    print()
    # Display a confirmation message
    eg.msgbox("A full list of the Monster Cards has been sent to the python console.", "Cards Printed")
    return  # return to main menu


print_monsters()
