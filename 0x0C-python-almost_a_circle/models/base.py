#!/usr/bin/python3
""" base model"""


import json


class Base:
    """still base stuff"""

    __nb_objects = 0

    def __init__(self, id=None):
        """still not making circles"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    # @classmethod
    # def save_to_file(cls, list_objs):

    @staticmethod
    def from_json_string(json_string):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        if json_string is None or len(json_string) == 0:
            return[]
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """new doc string for stuff and things"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
