#!/usr/bin/python3
"""Class student"""


class Student:
    """init and define student"""

    def __init__(self, first_name, last_name, age):
        """ init some stuff"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict_new = {}
        if attrs is not None:
            for att in attrs:
                if att in self.__dict__:
                    dict_new[att] = self.__dict__[att]
            return dict_new
        else:
            return self.__dict__
