# Lysander

from DataCopy import copyDataToTemp
from ReadData import readFile
import os
import json


def saveData(path, new_data):
    '''Saves the data'''

    user_data = open(path + "/UserData.json", "w")
    user_data.write(json.dumps(new_data))
    user_data.close()    


def writeData(new_data, user):
    '''Get the current data and add the new data to it and then add the current data to UserData.json'''

    path = os.path.dirname(os.path.abspath(__file__))

    current_data_list = readFile("CurrentUser.json")
    current_data_list.append(new_data)
    
    try:
        user_data_list = readFile("UserData.json")
        user_data_list["users"][user] = current_data_list

        saveData(path, user_data_list)

        copyDataToTemp(user)
    except KeyError:
        return False



new_data = {"username": "test", "password": "test", "account": "test"}
user = "Hej"

writeData(new_data, user)