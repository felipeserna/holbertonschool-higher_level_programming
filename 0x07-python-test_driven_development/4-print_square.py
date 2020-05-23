#!/usr/bin/python3
"""
prints a square with the character #.
>>> print_square(1)
#
"""


def print_square(size):
    """
    Args: size: length of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
