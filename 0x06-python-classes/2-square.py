#!/usr/bin/python3
""" letter soup """


class Square:
    """ dsdfvbuiarv """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        else:
            self._square__size = size
