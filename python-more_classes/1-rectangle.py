#!/usr/bin/python3
"""

Defining class rectangle

"""


class Rectangle:
    """

    Empty class rectangle

    """

    def __init__(self, width=0):
        """

        Initializing values and checking

        Args: width (int): width of the rectangle

        """

        self.__width = width
    
    @property
    def width(self):
        """
        
        getter for width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """

        setter for width

        Args: value (int): width of the rectangle

        """
        if value != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
