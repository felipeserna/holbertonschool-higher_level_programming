#!/usr/bin/python3
"""
Prints the numbers from 1 to 100 separated by a space.
"""


def fizzbuzz():
    """
    Returns: nothing
    """
    i = 1
    while i <= 100:
        # For numbers which are multiples of both three and five
        # print FizzBuzz.
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz ", end="")
        # For multiples of three print Fizz
        elif (i % 3 == 0):
            print("Fizz ", end="")
        # For multiples of five print Buzz
        elif (i % 5 == 0):
            print("Buzz ", end="")
        else:
            print("{:d} ".format(i), end="")
        i += 1
