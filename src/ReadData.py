# Author: Lucas Axberg
'''Module for reading and formatting json data'''
import os
import json

def readFile(file: str):
    '''Reads a .json file and returns the value of it in the form of dict or list'''

    # Gets the path to the directory of all the files
    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Reads the file
    with open(f"{folder_path}/{file}", "r", encoding="utf-8") as f:
        data = f.read()
        
    # Formatts the file to json object and returns it
    formatted_data = json.loads(data) 
    return formatted_data    

