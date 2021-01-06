#!/usr/bin/python3
""" I'm not sure how to make a docstring """


class Square:
    """ another one nother one """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ area """
        return (self.__size * self.__size)
