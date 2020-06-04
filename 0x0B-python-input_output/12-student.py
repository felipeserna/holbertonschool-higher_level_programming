#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a
        Student instance (same as 10-class_to_json.py):
        - If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return (self.__dict__)
        if all(attrs):
            a_dict = {}
            for names in attrs:
                if names in self.__dict__:
                    a_dict[names] = self.__dict__[names]
            return (a_dict)
