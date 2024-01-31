# Lysander

from DataCopy import copyDataToTemp
from ReadData import readFile
from WriteData import writeFile


def writeData(new_data: dict, user: str) -> bool:
    '''Updates the current data with the new data and returns False if the user does not exist else it returns True'''

    # Adds the new data to the current data
    current_data_list = readFile("CurrentUser.json")
    current_data_list.append(new_data)
    
    # Tries to replace the old data with the new current data in the UserData.json file.
    try:
        user_data_list = readFile("UserData.json")
        user_data_list["users"][user] = current_data_list

        writeFile("UserData.json", user_data_list)

        copyDataToTemp(user)
    except KeyError:
        return False
    
    return True