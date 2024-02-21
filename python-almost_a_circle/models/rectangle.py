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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x-coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x-coordinate"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y-coordinate"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle with '#' characters"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """String representation of Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        """Update attributes with arguments"""
        num_args = len(args)
        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.width = args[1]
        if num_args >= 3:
            self.height = args[2]
        if num_args >= 4:
            self.x = args[3]
        if num_args >= 5:
            self.y = args[4]
