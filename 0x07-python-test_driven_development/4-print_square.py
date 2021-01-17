#!/usr/bin/python
"""it says print_square but ill be damned if those dont look like not squares"""


def print_square(size):
    """PRINTS ""SQUARES"" """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
