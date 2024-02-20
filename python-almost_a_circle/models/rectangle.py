#!/usr/bin/python3
""" Rectangle class that inherits from base class """
from models.base import Base


class Rectangle(Base):
    """Rectangle class representing a rectangle shape"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.__height = value

    @property
    def x(self):
        """Getter method for x-coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x-coordinate"""
        self.__x = value

    @property
    def y(self):
        """Getter method for y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y-coordinate"""
        self.__y = value
