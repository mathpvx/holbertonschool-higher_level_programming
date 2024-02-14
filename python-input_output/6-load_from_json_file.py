#!/usr/bin/python3
"""
Serialization function
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        content = json.load(file)
        return content
