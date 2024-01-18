# Lysander

import json

# Delete later
def getUserList():
    '''Opens the json file with users and returns a dictionary.'''

    users = open("src/Users.json", "r")
    user_list = json.loads(users.read())
    users.close()
    return user_list



def checkUsers(user_list, username_input):
    '''Checks if the username is already in use.'''

    for users in user_list["correct"]:
        print(users)
        if username_input == users:
            return False
    else:
        return True
    

def saveUser(user_list):
    '''Opens the json file with users and saves the changes.'''

    users = open("src/Users.json", "w")

    users.write(json.dumps(user_list))

    users.close()


def signup():
    '''Checks if the user entered the same password twice then checks the username and then adds it to the list and saves it.'''

    username_input = input("Username > ")
    # TODO: Add error handling
    password_input = input("Password > ")
    repeat_password_input = input("Repeat password > ")

    # change function getUserList later
    user_list = getUserList()

    if password_input == repeat_password_input:

        if checkUsers(user_list, username_input):
            # adds the username as a new key and the password as its value.
            user_list["correct"][username_input] = password_input
            print(user_list)
            saveUser(user_list)


signup()
