# Author: Lucas Axberg

import os
import json

def readFile(file):
    '''
        Reads a .json file and returns the value of it in the form of dict or list
    '''

    folder_path = os.path.dirname(os.path.abspath(__file__))

    with open(f"{folder_path}/{file}", "r", encoding="utf-8") as f:
        data = f.read()
        
    formatted_data = json.loads(data) 
    return formatted_data    

