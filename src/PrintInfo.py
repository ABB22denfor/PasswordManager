# Author: Lucas Axberg
'''Module for terminal based printing and clearing'''

import os
from GetData import getAccountFromFile

def printHeader():
    '''Prints the header of the program'''

    # Top line
    print("".center(30, "-"))

    # Name and side-bars
    print("|", end="")
    print("PASS-MAN".center(28), end="")
    print("|")
        
    # Bottom bar
    print("".center(30, "-"))

def removeLines(lines: int):
    '''Removes a certain amount of lines above and including the current cursor position'''

    # Defines the ANSI escape code for moving the cursor up
    cursor_up = "\033[A"

    # Saves the terminal width (in charachters) as a variable
    width = os.get_terminal_size()[0]

    # Moves cursor up the amount of lines specified and prints blank lines
    print(cursor_up * lines, end="")
    print("\n".rjust(width, " ")*lines, end="")

    # Moves the cursor back up to the first empty line
    print(cursor_up * lines, end="")
    
def printAccountInfo(account: dict):

    # Prints header
    print("Account info:".center(30))
    print("".center(30, "-"))

    # Prints account information
    for i in account:
        print(f"* {i.title()}: {account[i]}")
    print("".center(30, "-"))
    
