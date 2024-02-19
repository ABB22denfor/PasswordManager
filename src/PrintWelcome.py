# Lysander

import os

def printWelcomeScreen():
    '''Prints the name and the logo'''
    os.system("cls" if os.name == "nt" else "clear")
    print("""
        ▄███████▄    ▄████████    ▄████████    ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄   
        ███    ███   ███    ███   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ 
        ███    ███   ███    ███   ███    █▀    ███    █▀  ███   ███   ███   ███    ███ ███   ███ 
        ███    ███   ███    ███   ███          ███        ███   ███   ███   ███    ███ ███   ███ 
      ▀█████████▀  ▀███████████ ▀███████████ ▀███████████ ███   ███   ███ ▀███████████ ███   ███ 
        ███          ███    ███          ███          ███ ███   ███   ███   ███    ███ ███   ███ 
        ███          ███    ███    ▄█    ███    ▄█    ███ ███   ███   ███   ███    ███ ███   ███ 
       ▄████▀        ███    █▀   ▄████████▀   ▄████████▀   ▀█   ███   █▀    ███    █▀   ▀█   █▀  
 """)

    with open(os.path.dirname(os.path.abspath(__file__)) + "/../data/welcomescreen.txt") as f:
        for line in f.readlines():
            print("      " , end="")
            print(line.replace("\n","").center(96))
    input()
