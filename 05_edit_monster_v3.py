"""Edit Monster - Version 3
A component to edit a monster card
Added stats change
Bug fixes
Prints 'cards' for testing
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
            check_card_name = eg.enterbox("What is the new name of the card?", "Enter Name")
            if check_card_name is None:
                edit_monster(new_card_name, new_card_stats)
            new_card_name = check_card_name.capitalize()
        elif edit == "Change Stats":
            edit_value = 1
            attribute_edit = eg.buttonbox("Which attribute/stat would you like to change?", "Which Attribute?",
                                          choices=("Strength", "Cunning", "Stealth", "Speed", "Cancel"))
            if attribute_edit != "Cancel":
                new_value = eg.integerbox(f"What is the new value for {attribute_edit}? (1-25)",
                                          lowerbound=1, upperbound=25)
                if new_value is None:
                    edit_monster(new_card_name, new_card_stats)
                new_card_stats.update({attribute_edit: new_value})
        else:
            if edit_value == 1:
                save = eg.buttonbox("Would you like to save your changes?", "Save?", choices=("Yes", "No"))
                if save == "Yes":
                    full_card = {new_card_name: new_card_stats}
                    print(cards)
                    cards.pop(og_card_name)
                    print(cards)
                    cards.update(full_card)
                    print(cards)
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
