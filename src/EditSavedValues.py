#Dennis
account = {
    "username": "bob",
    "password": "5697605",
    "account": "YouTube"
}

def main():
    editSavedValue(["password", "354354353"])

def editSavedValue(edited_value: list):
    '''(editedValue: list [Val to Edit, New Val])'''
    val_to_edit = edited_value[0]
    new_val = edited_value[1]
    account[f"{val_to_edit}"] = new_val
    print(account)

if __name__ == "__main__":
    main()
