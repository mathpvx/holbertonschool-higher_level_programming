#!/usr/bin/python3
"""
Serialization function
"""
import json


def from_json_string(my_str):
    """returns deserialized string into a data structure """
    return json.loads(my_str)
