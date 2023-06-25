#!/usr/bin/python3
"""
a function that returns the dictionary description with data structure

JSON serialization of an obj
"""


def class_to_json(obj):
    """
    dict description of obj
    """
    return obj.__dict__
