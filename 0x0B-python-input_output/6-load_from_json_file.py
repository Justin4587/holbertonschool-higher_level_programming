#!/usr/bin/python3
import json
"""json load from file"""


def load_from_json_file(filename):
    """json load command"""

    with open(filename) as f:
        return json.load(f)
