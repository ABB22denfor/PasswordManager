# Lysander

from PrintInfo import removeLines

def verifier(command_list: list, question: str, error_message:str) -> str:
    '''Verifies if the input is in the command_list and returns the input when it is'''

    #Checks if the input is the same as a valid command
    while True:
        answer = input(question)

        removeLines(1)

        if answer.lower() in command_list:
            return answer
        else:
            print(error_message)
            input("Press enter to continue...")
            removeLines(2)
