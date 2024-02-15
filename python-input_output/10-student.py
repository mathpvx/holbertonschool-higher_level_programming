#!/usr/bin/python3
"""
Class Module
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """initialize method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if isinstance(i, str) and hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict
