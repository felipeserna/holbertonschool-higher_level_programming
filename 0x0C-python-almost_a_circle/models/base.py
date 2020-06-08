#!/usr/bin/python3
"""Base class"""
import json


class Base():
    """first class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        Args:
        id: integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args: list_dictionaries: list of dictionaries
        If list_dictionaries is None or empty, return the string: "[]"
        Otherwise, return the JSON string representation
        of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")

        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + ".json", 'w') as my_file:
            if list_objs is None:
                json.dump([], my_file)

            else:
                list_of_dict = []
                for dictionary in list_objs:
                    list_of_dict.append(dictionary.to_dictionary())
                j_list_objs = Base.to_json_string(list_of_dict)
                my_file.write(j_list_objs)
                return (my_file)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args: json_string is a string representing a list of dictionaries.
        - If json_string is None or empty, return an empty list.
        - Otherwise, return the list represented by json_string"""
        if json_string is None or json_string == "":
            return ([])

        else:
            return (json.loads(json_string))
