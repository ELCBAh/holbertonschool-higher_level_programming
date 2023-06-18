#!/usr/bin/python3
"""Class Square again but better"""


class Square:
    """Private instance attribute size init to None"""

    def __init__(self, size=0):
        """Init the size of square

        Args:
            size (int): size of square
        """
        self.__size = size
