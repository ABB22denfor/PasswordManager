# Lysander

import json

def getUserList():
    users = open("src/users.json", "r")
    user_list = json.loads(users.read())
    users.close()
    return user_list


def checkExistingUsers():
    username_input = input("Username > ")
    password_input = input("Password > ")

    user_list = getUserList()

    try:
        if user_list["correct"][username_input] == password_input:
            return True
        else:
            return False
    except KeyError:
        return False