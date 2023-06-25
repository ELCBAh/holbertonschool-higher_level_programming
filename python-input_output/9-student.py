#!/usr/bin/python3
"""
a class Student that defines a student
"""


class Student:
    """
    a class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        init
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves dict representation of Student instance
        """
        return self.__dict__
