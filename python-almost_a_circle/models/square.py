#!/usr/bin/python3
"""
a square class that inherits from rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value

    def __str__(self):
        """str method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
