#!/usr/bin/python3
"""
function that appends a string at the end of file

returns number of characters added
"""


def append_write(filename="", text=""):
    """
    appends text at end of file

    Args:
        filename: name of file
        text: text to append
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
