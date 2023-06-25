#!/usr/bin/python3

"""

a class MyList that inherits from list and prints in asc order

"""


class MyList(list):
    """
    A class inheriting from list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """
        prints the list in asc order
        """
        print(sorted(self))
