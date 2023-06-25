#!/usr/bin/python3
"""
a function that returns an object represented by JSON string
"""


def from_json_string(my_str):
    """
    returns an object represented by JSON string
    """
    import json
    return json.loads(my_str)
