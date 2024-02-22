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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(
                cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                )
            )
