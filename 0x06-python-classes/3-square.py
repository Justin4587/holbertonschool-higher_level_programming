#!/usr/bin/python3
""" letter soup """


class Square:
    """ dsdfvbuiarv """

    def __init__(self, size=0):
        """ definition """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ return area """
        return self.__size * self.__size
