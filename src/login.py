# Lysander

import os
import json

# Delete later
def getUserList():
    '''Opens the json file with users and returns a dictionary.'''

    path = os.path.dirname(os.path.abspath(__file__))

    users = open(path + "/UserData.json", "r")
    user_list = json.loads(users.read())
    users.close()
    return user_list


def login(username_input, password_input):
    '''Gets username and password input from user and checks if it exists.'''

    user_list = getUserList()

    # If it does exist it returns True else it returns False.
    try:
        if user_list["correct"][username_input] == password_input:
            return True
        else:
            return False
    except KeyError:
        return False


