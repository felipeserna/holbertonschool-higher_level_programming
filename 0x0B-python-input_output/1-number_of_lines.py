#!/usr/bin/python3
"""Number of lines"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file
    Args: filename: string
    """
    number_of_lines = 0

    with open("my_file_0.txt", mode='r', encoding="utf-8") as my_file:
        while (my_file.readline() != ''):
            number_of_lines += 1
        return number_of_lines
