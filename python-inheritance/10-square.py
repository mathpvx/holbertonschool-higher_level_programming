#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
module with class BaseGeometry
===================================
"""


class Square(Rectangle):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, size):
        """ constructor with size attribute """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area method"""
        return self.__size**2
