#!/usr/bin/python3
"""json load from file"""
import json


def load_from_json_file(filename):
    """json load command"""

    with open(filename) as f:
        return json.load(f)
