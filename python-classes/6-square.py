#!/usr/bin/python3
"""A class for Square"""


class Square:
    """construct attributes"""
    def __init__(self, size=0, position=(0, 0)):
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
        """prints square of size area using #"""
        if self.__size > 0:
            for column in range(self.__size):
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
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

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Updates the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
