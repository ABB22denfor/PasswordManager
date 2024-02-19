# Lysander

import os
import json


def writeFile(file: str, data: list):
    '''opens a file and saves the data in it'''

    path = os.path.dirname(os.path.abspath(__file__)+"/../data")

    with open(f"{path}/{file}", "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
