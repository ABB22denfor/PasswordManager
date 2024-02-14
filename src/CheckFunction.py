# Author: Lucas Axberg

def checkFunction(value: str, register: int = 0) -> bool:
    '''Function for checking if a mode name is valid. 
    0 = Checks if it is valid
    1 = Checks view
    2 = Checks create
    3 = Checks edit
    4 = Checks delete'''

    # Define the list to check
    checkList = [["view", "v"],["create", "c"],["edit", "e"],["delete", "d"]]

    if register:
        # Check in a certain
        return value in checkList[register - 1]
    else:
        # Check in all lists
        return any(value in sub_list for sub_list in checkList)

