#!/usr/bin/python3
"""Class student"""


class Student:
    """init and define student"""

    def __init__(self, first_name, last_name, age):
        """ init some stuff"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
