#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout.
    Args: filename: string
    """
    with open("my_file_0.txt", mode='r', encoding="utf-8") as my_file:
        print(my_file.read())
