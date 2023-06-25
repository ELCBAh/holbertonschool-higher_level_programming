#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        initializes
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        prints rectangle
        """
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
