#!/usr/bin/python3
"""import Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""

    def __init__(self, size):
        """Args:
        size: length of the square
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """method area"""
        area = self.__size ** 2
        return (area)
