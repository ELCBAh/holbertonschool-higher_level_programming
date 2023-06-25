#!/usr/bin/python3
"""
a function that creates object from JSON file
"""


def load_from_json_file(filename):
    """
    a function that creates object from JSON file
    """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
