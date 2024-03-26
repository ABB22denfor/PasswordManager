import json
import os

from HandleDefaultUser import getDefaultUser, setDefaultUser
from GetData import getAccountFromFile
from PrintInfo import printAccountInfo
from DataCopy import copyDataToTemp
from ReadData import readFile

def handleArgs(args: list = []) -> int:
    
    try:
        if args[1] == "-u":
            pass
        user_info = getDefaultUser()
    except KeyError:
        return print("ERROR: Default User Not Set. passman -u <username> <password> to set defaults")

    copyDataToTemp(user_info[0])

    match args[1]:
        case "-v":
            viewAccount(args[2:])
        case "-e":
            editAccount([user_info, args[2:]])
        case "-d":
            print("Delete")
        case "-u":
            setDefaultUser(args)
        case _:
            return 1
    return 0

def viewAccount(args: list):
    data = readFile("CurrentUser.json")
    chosen_account = args[0]

    if chosen_account not in getAccountFromFile():
        print(f"Account '{chosen_account}' doesn't exist.")
        return

    for account in data:
        if chosen_account == account["account"]:
            printAccountInfo(account)

def editAccount(args: list):
    data = readFile("CurrentUser.json")
    
    try:
        for account in data:
            if args[1][0] == account["account"]:
                account_data = account

            account_name = args[0][0]

            field_to_change = args[1][1]
            new_value = args[1][2] 
    except IndexError:
        print("ERROR: Not ")
        return 


    all_loaded_data = {}
    account_to_change = {}
    account_index = 0

    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Fetch data from UserData
    with open(f"{folder_path}/../data/UserData.json", "r", encoding="utf-8") as f:
        all_loaded_data = json.loads(f.read())
        for saved_account in all_loaded_data["users"][f"{account_name}"]:
            # Check if passed in account data matches saved data
            try:
                if saved_account["account"] != account_data["account"]:
                    continue
                account_to_change = saved_account
                account_index = all_loaded_data["users"][f"{account_name}"].index(account_to_change)
                break
            except KeyError:
                return print("JSONFORMATERROR")
        else:
            return print("ACCOUNTNOTFOUND")

    # Update data with changes
    account_to_change[f"{field_to_change}"] = new_value
    all_loaded_data["users"][f"{account_name}"][account_index] = account_to_change

    # Overwrite UserData
    with open(f"{folder_path}/../data/UserData.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(all_loaded_data))
