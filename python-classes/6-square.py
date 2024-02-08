#!/usr/bin/python3
"""creates class Square with
private instance attribute size and position and
public instance methods to calculate area and print square"""


class Square:
    """defines class with private instance attributes size and position
and public instance methods to calculate area and print square."""

    def __init__(self, size=0, position=(0, 0)):
        """instantiates attribute size to 0 and position to (0, 0)"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the private instance attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the private instance attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets the private instance attribute position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the private instance attribute position"""
        check = 0
        while 1:
            if type(value) is not tuple or len(value) is not 2:
                check += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                check += 1
                break
            if value[0] < 0 or value[1] < 0:
                check += 1
            break
        if check is 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculates and returns current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints square of size self.__size using #"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
