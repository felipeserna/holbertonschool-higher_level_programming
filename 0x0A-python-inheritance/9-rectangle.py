#!/usr/bin/python3
"""import BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Args:
        width: rectangle width
        height: rectangle height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method area"""
        area = self.__width * self.__height
        return (area)

    def __str__(self):
        """return a rectangle"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
