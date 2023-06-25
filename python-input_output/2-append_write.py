#!/usr/bin/python3
"""
function that appends a string at the end of file

returns number of characters added
"""


def append_write(filename="", text=""):
    """
    appends text at end of file
    """
    with open(filename, 'a+') as f:
        f.append(text)
        return f.write(text)
