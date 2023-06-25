#!/usr/bin/python3
"""
An empty class
"""


class BaseGeometry():
    """
    An empty class
    """
    def area(self):
        """
        An empty method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value

        Args:
            name: name
            value: value to validate
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than or equal to 0
        Returns:
            value if it passes the validation
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
