# Author: Lucas Axberg

import os

def printHeader():
    print("".center(30, "-"))

    print("|", end="")
    print("PASS-MAN".center(28), end="")
    print("|")
        
    print("".center(30, "-"))

def removeLines(lines):
    cursor_up = "\033[A"
    width = os.get_terminal_size()[0]

    print(cursor_up * lines, end="")
    print("\n".rjust(width, " ")*lines, end="")
    
    print(cursor_up * lines, end="")
    
removeLines(4)
