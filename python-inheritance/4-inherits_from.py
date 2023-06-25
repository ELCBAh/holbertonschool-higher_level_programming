#!/usr/bin/python3
"""
Function to check if obj is instance of class inhereted
"""


def inherits_from(obj, a_class):
    """
    Function to check if obj is instance of class inhereted
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
