#Dennis
'''Module for saving edited data'''
import os, json
from DataCopy import copyDataToTemp

account = {
    "username": "Bob",
    "password": "5697605",
    "account": "Youtube"
}

def main():
    editSavedValue("Bob", account, ["password", "354354353"])

def editSavedValue(account_name, account_data, edited_value: list):
    '''(editedValue: list [Val to Edit, New Val]) Write edited data to UserData.json and update temp user'''
    val_to_edit = edited_value[0]
    new_val = edited_value[1]

    all_loaded_data = {}
    loaded_user_data = {}
    account_to_change = {}

    folder_path = os.path.dirname(os.path.abspath(__file__))


    with open(f"{folder_path}/UserData.json", "r", encoding="utf-8") as f:
        all_loaded_data = json.loads(f.read())
        for saved_account in all_loaded_data["users"][f"{account_name}"]:
            if saved_account["account"] == account_data["account"]:
                account_to_change = saved_account
                loaded_data = all_loaded_data["users"][f"{account_name}"][all_loaded_data["users"][f"{account_name}"].index(saved_account)]
 
    loaded_data[f"{val_to_edit}"] = new_val
    all_loaded_data["users"][f"{account_name}"][all_loaded_data["users"][f"{account_name}"].index(account_to_change)] = loaded_data

    with open(f"{folder_path}/UserData.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(all_loaded_data))

#    copyDataToTemp(account["username"])
    # Call copyDataToTemp(account) from module DataCopy

if __name__ == "__main__":
    main()
