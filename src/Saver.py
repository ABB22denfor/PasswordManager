# Lysander


def askPasswordType() -> bool:
    '''Asks if the user wants to generate a password returns False if answerd y'''

    while True:
        answer = input("Do you want to generate a password? (y/N) ")

        if answer.lower() == "n" or answer.lower() == "":
            return True
        elif answer.lower() == "y":
            return False
