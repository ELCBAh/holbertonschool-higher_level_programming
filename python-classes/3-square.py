#!/usr/bin/python3
"""Class Square again but better"""


class Square:
    """Private instance attribute size init to None"""

    def __init__(self, size=0):
        """Init the size of square

        Args:
            size (int): size of square
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the square area"""
        return self.__size ** 2
