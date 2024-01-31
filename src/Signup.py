# Lysander

from PrintInfo import removeLines
from ReadData import readFile
from WriteData import writeFile


def checkUsers(user_list: list, username_input: str) -> bool:
    '''Checks if the username is already in use. Returns False if it does'''

    for users in user_list["correct"]:
        if username_input == users:
            return False
    else:
        return True


def signup():
    '''Asks for username and password input and checks if it is valid and then saves it'''

    user_list = readFile("UserData.json")

    # Asks for a username and runs until entered a valid username
    while True:
        username_input = input("Username > ")
        if checkUsers(user_list, username_input):
            break
        print("Username already exist")
        input("Press enter to continue...")
        removeLines(3)

    # Asks for a password twice and checks if it is the same and if it is at least 8 characters long
    while True:
        password_input = input("Password > ")
        repeat_password_input = input("Repeat password > ")

        if password_input == repeat_password_input:
            if len(password_input.strip()) >= 8:
                break
            else:
                print("Password must contain at least 8 characters")
                input("Press enter to continue...")
                removeLines(4)
        else:
            print("Password does not match")
            input("Press enter to continue...")
            removeLines(4)

    # adds the username as a new key and the password as its value and saves it to UserData.json
    user_list["correct"][username_input] = password_input
    writeFile("UserData.json", user_list)
    print("Account created successfully")


