#!/usr/bin/python3
"""base"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ret area"""
        return self.__width * self.__height

    def __str__(self):
        """desc"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
