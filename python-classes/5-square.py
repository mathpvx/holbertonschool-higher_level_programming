#!/usr/bin/python3
"""A class for Square"""


class Square:
    """construct attributes"""
    def __init__(self, size=0):
        """raise error if not int"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """raise error if negative"""
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2

    def my_print(self):
        for column in range(self.__size):
            for row in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """Getter method for retrieving the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
