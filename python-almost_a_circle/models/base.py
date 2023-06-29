#!/usr/bin/python3
"""
'base' class for all other classes

manages id attribute in all future classes

avoid duplicating same code
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
