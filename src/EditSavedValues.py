#Dennis
'''Module for saving edited data'''
import os
import json
from DataCopy import copyDataToTemp

def editSavedValue(account_name: str, account_data: dict, edited_value: list):
    '''(account_name: str, account_data: dict, edited_value: list [Val to Edit, New Val])
    Write edited data to UserData.json and update CurrentUser.json
    '''
    val_to_edit = edited_value[0]
    new_val = edited_value[1]

    all_loaded_data = {}
    account_to_change = {}
    account_index = 0

    folder_path = os.path.dirname(os.path.abspath(__file__))


    with open(f"{folder_path}/UserData.json", "r", encoding="utf-8") as f:
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

    account_to_change[f"{val_to_edit}"] = new_val
    all_loaded_data["users"][f"{account_name}"][account_index] = account_to_change

    with open(f"{folder_path}/UserData.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(all_loaded_data))

    copyDataToTemp(account_name)