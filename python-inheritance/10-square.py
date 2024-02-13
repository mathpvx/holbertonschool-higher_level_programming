#!/usr/bin/python3
"""
===================================
module with class Rectangle
===================================
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """constructs with size attribute"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method"""
        return self.__size ** 2
