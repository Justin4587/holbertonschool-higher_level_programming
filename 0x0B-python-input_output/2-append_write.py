#!/usr/bin/python3
"""write"""


def append_write(filename="", text=""):
    """write"""

    with open(filename, mode="a") as f:
        working_file = f.write(text)
        return working_file
