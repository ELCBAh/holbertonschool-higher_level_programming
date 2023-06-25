#!/usr/bin/python3
"""
a function that writes obj to text file using JSON
"""


def save_to_json_file(my_obj, filename):
    """
    a function that writes obj to text file using JSON
    """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
    return
