#!/usr/bin/python3
"""
class square inheriting from rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class
    """
    def __init__(self, size):
        """
        initializing
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        area
        """
        return self.__size ** 2
