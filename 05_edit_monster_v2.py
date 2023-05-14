"""Edit Monster - Version 2
A component to edit a monster card
Created while loop to check for Finish
Added an edited version of 3.1 None Checker for testing
developed a new version of 3.1 None Checker specifically for this component (3.2 None Checker Edit)
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


def edit_monster(og_card_name, og_card_stats):
    edit = ""
    new_card_name = og_card_name
    new_card_stats = og_card_stats
    edit_value = 0
    while edit != "Finish":
        items = "\n".join([f"{item}: {stat}" for item, stat in new_card_stats.items()])  # formats text
        edit = eg.buttonbox(f"Here is the card '{new_card_name}':\n{items}\n\nWhat would you like to do?",
                            "Edit Card", choices=("Change Name", "Change Stats", "Finish"))
        if edit == "Change Name":
            edit_value = 1
            new_card_name = eg.enterbox("What is the new name of the card?", "Enter Name")
            if new_card_name is None:
                return
            new_card_name = new_card_name.capitalize()
        elif edit == "Change Stats":
            edit_value = 1
        else:
            if edit_value == 1:
                save = eg.buttonbox("Would you like to save your changes?", "Save?", choices=("Yes", "No"))
                if save == "Yes":
                    full_card = {new_card_name: new_card_stats}
                    cards.pop(og_card_name)
                    cards.update(full_card)
                    return
                else:
                    return
            else:
                return


def test():
    full_card = {"Stoneling": {"Strength": 7, "Cunning": 15, "Stealth": 25, "Speed": 1}}
    card_name = "Stoneling"
    card_stats = {"Strength": 7, "Cunning": 15, "Stealth": 25, "Speed": 1}
    edit_monster(card_name, card_stats)


test()
