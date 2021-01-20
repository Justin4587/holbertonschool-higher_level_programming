#!/usr/bin/python3
"""read"""


def read_file(filename=""):
    """open and read"""

    with open("{}".format(filename), encoding="UTF8") as f:
        working_file = f.read()
        print(working_file, end="")
