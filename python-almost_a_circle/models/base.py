#!/usr/bin/python3
"""
Base class for managing id attribute in all future classes.
"""
import json


class Base:
    """Represent the base model."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.
        If id is not provided, generated automatically."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
