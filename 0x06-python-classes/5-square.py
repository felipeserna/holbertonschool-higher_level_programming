#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the class
        Args:
            size (int): length of the square
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square"""
        area = self.__size**2
        return int(area)

    def my_print(self):
        """prints the square with # or empty line
        if size is equal to 0"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
