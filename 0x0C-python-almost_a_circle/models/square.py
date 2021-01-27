#!/usr/bin/python3
""" this has to be the most pointless part"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ if height and width are even call it a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """making boxes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return self.width

    @size.setter
    def size(self, value):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        place = 1
        if len(args):
            for i in args:
                if place == 1:
                    self.id = i
                if place == 2:
                    self.size = i
                if place == 3:
                    self.x = i
                if place == 4:
                    self.y = i
                place += 1
        elif len(kwargs):
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ I'm nervous about not having a doc string
        so now you can read this same line everywhere """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
