# Lysander

from DataCopy import copyDataToTemp
from ReadData import readFile
from WriteData import writeFile


def writeData(new_data: dict, user: str):
    '''Updates the current data with the new data'''

    # Adds the new data to the current data
    current_data_list = readFile("CurrentUser.json")
    current_data_list.append(new_data)
    
    # Replaces the old data with the new current data in the UserData.json file.
    user_data_list = readFile("UserData.json")
    user_data_list["users"][user] = current_data_list

    writeFile("UserData.json", user_data_list)

    copyDataToTemp(user)
