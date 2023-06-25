#!/usr/bin/python3
"""
a function that reads a text file utf8 and prints to stdout
"""


def read_file(filename=""):
    """
    this function reads and prints to stdout

    Parameters:
        filename (str): the name of the file to read
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
