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
