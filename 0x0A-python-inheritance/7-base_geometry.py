#!/usr/bin/python3
"""empty class BaseGeometry"""


class BaseGeometry:
    """empty class BaseGeometry"""

    def area(self):
        """Defines area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
