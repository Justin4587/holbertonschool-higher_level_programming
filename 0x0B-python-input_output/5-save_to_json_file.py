#!/usr/bin/python3
import json
"""save to json"""


def save_to_json_file(my_obj, filename):
    """json dump"""

    with open(filename, mode="w", encoding="UTF8") as f:
        json.dump(my_obj, f)
