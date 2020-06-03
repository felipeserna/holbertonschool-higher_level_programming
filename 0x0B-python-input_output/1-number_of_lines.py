#!/usr/bin/python3
"""Number of lines"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file
    Args:
        filename: str
    Return:
        [int]: number of lines in the file
    """
    with open("{}".format(filename), encoding='utf-8') as a_file:
        total_lines = 0
        for line in a_file:
            total_lines = total_lines + 1
        return total_lines
