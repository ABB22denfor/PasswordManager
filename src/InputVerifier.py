# Lysander

from PrintInfo import removeLines

def verifier(command_list, question, error_message):
    while True:
        answer = input(question)

        removeLines(1)

        if answer.lower() in command_list:
            return answer
        else:
            print(error_message)
            input("Press enter to continue...")
            removeLines(2)
