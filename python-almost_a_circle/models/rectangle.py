#!/usr/bin/python3
"""
a class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle defined"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        __width = width
        __height = height
        __x = x
        __y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
