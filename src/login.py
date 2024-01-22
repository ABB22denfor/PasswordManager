# Lysander


from ReadData import readFile


def login(username_input, password_input):
    '''Gets username and password input from user and checks if it exists.'''

    user_list = readFile("UserData.json")

    # If it does exist it returns True else it returns False.
    try:
        if user_list["correct"][username_input] == password_input:
            return True
        else:
            return False
    except KeyError:
        return False


username_input = input("Username > ")
password_input = input("Password > ")

test = login(username_input, password_input)
print(test)