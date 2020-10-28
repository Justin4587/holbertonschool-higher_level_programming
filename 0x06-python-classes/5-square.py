#!/usr/bin/python3
""" letter soup """


class Square:
    """ dsdfvbuiarv """

    def __init__(self, size=0):
        """ base """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ letter soup """
        return self.__size

    @size.setter
    def size(self, value):
        """ definition """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ return area """
        return self.__size * self.__size

    def my_print(self):
        """ make shape """
        if self.__size > 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
