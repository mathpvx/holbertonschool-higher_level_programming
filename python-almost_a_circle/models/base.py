#!/usr/bin/python3
"""
Base class for managing id attribute in all future classes.
"""


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
