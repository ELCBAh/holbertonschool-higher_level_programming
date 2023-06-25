#!/usr/bin/python3
"""
a function that writes to text utf-8

returns num of character written
"""


def write_file(filename="", text=""):
    """
    write_file function

    create file if does not exists

    overwrite content if file exists

    Parameters:
    filename (str): file name
    text (str): text to write
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
