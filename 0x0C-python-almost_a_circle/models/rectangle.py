#!/usr/bin/python3
"""Neither square or circle"""


from models.base import Base


class Rectangle(Base):
    """ Not sure who named this project"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """stillll not making a circle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return self.__width

    @property
    def height(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return self.__height

    @property
    def x(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return self.__x

    @property
    def y(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return self.__y

    @width.setter
    def width(self, value):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return self.__width * self.__height

    def display(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        for blank_row in range(self.__y):
            print("")
        for i in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def __str__(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        place = 1
        if len(args):
            for i in args:
                if place == 1:
                    self.id = i
                if place == 2:
                    self.width = i
                if place == 3:
                    self.height = i
                if place == 4:
                    self.x = i
                if place == 5:
                    self.y = i
                place += 1
        elif len(kwargs):
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
