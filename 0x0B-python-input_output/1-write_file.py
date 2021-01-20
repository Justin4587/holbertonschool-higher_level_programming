#!/usr/bin/python3
"""write"""


def write_file(filename="", text=""):
    """write"""

    with open(filename, mode="w") as f:
        working_file = f.write(text)
        return working_file
