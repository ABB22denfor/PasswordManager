# Lysander

from DataCopy import copyDataToTemp
from ReadData import readFile
from WriteData import writeFile


def writeData(new_data, user):
    '''Get the current data and add the new data to it and then add the current data to UserData.json'''

    current_data_list = readFile("CurrentUser.json")
    current_data_list.append(new_data)
    
    try:
        user_data_list = readFile("UserData.json")
        user_data_list["users"][user] = current_data_list

        writeFile("UserData.json", user_data_list)

        copyDataToTemp(user)
    except KeyError:
        return False



