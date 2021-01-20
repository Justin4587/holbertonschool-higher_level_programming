#!/usr/bin/python3
"""base"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """4 fucking sides"""

    def __init__(self, size):
        """init"""

        self.integer_validator("size", size)
        super().__init__(size, size)
