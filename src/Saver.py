# Lysander


def askPasswordType():
    '''Asks if the user wants to generate a password'''

    finished = False

    while not finished:
        answer = input("Do you want to generate a password? (y/n) ")

        if answer.lower() == "n":
            finished = True
            return True
        elif answer.lower() == "y":
            finished = True
            return False


