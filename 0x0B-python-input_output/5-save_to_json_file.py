#!/usr/bin/python3
"""save to json"""
import json


def save_to_json_file(my_obj, filename):
    """json dump"""

    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
