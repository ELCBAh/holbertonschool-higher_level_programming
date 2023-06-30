#!/usr/bin/python3
"""
a class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle defined"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        __width = width
        __height = height
        __x = x
        __y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        pass

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        pass
