#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class
        Args:
            size (int): length of the square
            position (int, int): coordinates of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for l in range(self.__size):
                    print('#', end='')
                print()
