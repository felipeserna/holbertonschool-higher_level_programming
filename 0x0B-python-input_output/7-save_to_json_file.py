#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args: my_obj: object
    filename: string
    """
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
