#!/usr/bin/python3
"""
Serialization function
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file as a JSON representation"""
    with open(filename, 'w') as json_file:
        serialized_txt = json.dumps(my_obj)
        json_file.write(serialized_txt)
