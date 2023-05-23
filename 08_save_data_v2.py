"""Save Data - Version 2
A component to ask the user if they want to save their changes
converted code blocks to functions
Added comments
"""
import pickle
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
    }  # a dictionary containing all the monster card data


def save_data():
    # Asks user if they want to save their data
    save = eg.buttonbox("Do you want to save your data?", "SAVE DATA", choices=("Yes", "No"))
    if save == "Yes":  # if 'Yes', pickle the 'cards' dictionary into a file
        with open("saved_progress.pkl", "wb") as file:
            pickle.dump(cards, file)
        eg.msgbox("Data successfully saved, program closing.", "Data Saved")  # display confirmation
    else:  # if 'No', do nothing
        eg.msgbox("Data not saved, program closing.", "Data Not Saved")  # display confirmation


def load_data():
    global cards  # announces the variable 'cards' as global
    # Asks user if they want to import the saved data
    load = eg.buttonbox("Do you want to import the saved data?", "LOAD DATA", choices=("Yes", "No"))
    if load == "Yes":  # if 'Yes', import the saved data file
        with open("saved_progress.pkl", "rb") as file:
            cards = pickle.load(file)
        eg.msgbox("Data successfully imported.", "Saved Data Imported")  # display confirmation
    else:  # if 'No', keep the default values
        eg.msgbox("Data not imported, loading with standard values.", "Saved Data Not Imported")  # display confirmation


save_data()
load_data()
