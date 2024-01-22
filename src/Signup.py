# Lysander

from PrintInfo import removeLines
from ReadData import readFile
from WriteData import writeFile


def checkUsers(user_list, username_input):
    '''Checks if the username is already in use.'''

    for users in user_list["correct"]:
        if username_input == users:
            return False
    else:
        return True


def signup():
    '''Checks if the user entered the same password twice then checks the username and then adds it to the list and saves it.'''

    wrong_password = True

    user_list = readFile("UserData.json")

    while True:
        username_input = input("Username > ")
        if checkUsers(user_list, username_input):
            break
        print("Username already exist")
        input("Press enter to continue...")
        removeLines(3)

    while wrong_password:
        password_input = input("Password > ")
        repeat_password_input = input("Repeat password > ")

        if password_input == repeat_password_input:
            if len(password_input.strip()) >= 8:
                wrong_password = False
            else:
                print("Password must contain at least 8 characters")
                input("Press enter to continue...")
                removeLines(4)
        else:
            print("Password does not match")
            input("Press enter to continue...")
            removeLines(4)

    # adds the username as a new key and the password as its value.
    user_list["correct"][username_input] = password_input
    writeFile("UserData.json", user_list)
    print("Account created successfully")


signup()
