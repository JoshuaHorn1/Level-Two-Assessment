"""Edit Monster - Version 5
A component to edit a monster card
Bugfixes
General code change - no longer calls on the function from in the function
Removed main_menu(), trials proved no longer needed - reworked
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
attributes = ["Strength", "Cunning", "Stealth", "Speed"]  # a list containing all the different variables of a card


def edit_monster(og_card_name, og_card_stats):
    edit = ""  # creates the variable 'edit' and sets value to ""
    # Creates a value for the new card and sets it to current value, so old name can be kept
    new_card_name = og_card_name
    new_card_stats = og_card_stats
    edit_value = 0  # creates a value to detect if user ever makes an edit
    while edit != "Finish":  # a while loop detecting if the user ever wants clicks 'Finish'
        items = "\n".join([f"{item}: {stat}" for item, stat in new_card_stats.items()])  # formats text
        edit = eg.buttonbox(f"Here is the card '{new_card_name}':\n{items}\n\nWhat would you like to do?",
                            "Edit Card", choices=("Change Name", "Change Stats", "Finish"))
        if edit == "Change Name":  # if user clicks 'Change Name' button...
            edit_value = 1  # set edit value to 1 - user has made edit
            check_card_name = eg.enterbox("What is the new name of the card?", "Enter Name")  # asks for new card name
            if check_card_name is not None:  # checks if user clicked cancel
                new_card_name = check_card_name.capitalize()  # if not, capitalize the value
        elif edit == "Change Stats":  # if user clicks 'Change Stats' button...
            edit_value = 1  # set edit value to 1 - user has made edit
            # Asks user to pick a value to change, or cancel
            attribute_edit = eg.buttonbox("Which attribute/stat would you like to change?", "Which Attribute?",
                                          choices=("Strength", "Cunning", "Stealth", "Speed", "Cancel"))
            if attribute_edit != "Cancel":  # if user doesnt click cancel, get value for attribute
                new_value = eg.integerbox(f"What is the new value for {attribute_edit}? (1-25)",
                                          lowerbound=1, upperbound=25)
                if new_value is not None:  # if user doesnt click cancel, update card_stats
                    new_card_stats.update({attribute_edit: new_value})
        else:  # go here when user clicks 'Finish'
            if edit_value == 1:  # checks if user has made a change anywhere
                # Asks user if they want to save their changes to the card
                save = eg.buttonbox("Would you like to save your changes?", "Save?", choices=("Yes", "No"))
                if save == "Yes":  # if 'Yes', return new values
                    full_card = {new_card_name: new_card_stats}
                    return full_card
                else:  # if 'No', return "No Changes"
                    return "No Changes"
            else:  # if no changes were made, return "No Changes"
                return "No Changes"


def test():  # a function mimicking the data that the edit function will receive
    card_name = "Stoneling"
    card_stats = {"Strength": 7, "Cunning": 15, "Stealth": 25, "Speed": 1}
    edit_monster(card_name, card_stats)


test()
