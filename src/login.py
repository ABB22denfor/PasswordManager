# Lysander


from ReadData import readFile


def login(username_input: str, password_input: str) -> bool:
    '''Gets username and password input from user and checks if it exists. Returns True if it does.'''

    user_list = readFile("UserData.json")

    try:
        if user_list["correct"][username_input] == password_input:
            return True
        else:
            return False
    except KeyError:
        return False

