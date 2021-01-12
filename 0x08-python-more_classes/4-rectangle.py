#!/usr/bin/python3
""" squares but not REAL squares """


class Rectangle:
    """ This defines the not square """

    def __init__(self, width=0, height=0):
        """really gettin into it now, gonna define the shit out of notsquare"""

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """ mns = my not square """
        mns = ""
        if self.__height == 0 or self.__width == 0:
            return 0
        for i in range(self.__height - 1):
            mns += ("#" * self.__width) + "\n"
        mns += ("#" * self.__width)
        return mns

    def __repr__(self):
        return ("Rectangle({},{})".format(self.__width, self.__height))
