#!/usr/bin/python3
"""
a function that reads a text file utf8 and prints to stdout
"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
