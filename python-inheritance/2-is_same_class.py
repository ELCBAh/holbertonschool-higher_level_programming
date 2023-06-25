#!/usr/bin/python3
"""
A function that returns True if object is exactly an instance
"""


def is_same_class(obj, a_class):
    """
    Returns True if object is exactly an instance of specified class
    
    Args:
		obj (any): Object to compare
		a_class (any): Class to compare
    """
    return type(obj) == a_class
