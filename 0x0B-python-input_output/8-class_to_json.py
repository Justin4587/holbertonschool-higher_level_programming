#!/usr/bin/python3
"""return json dict"""


def class_to_json(obj):
    """return JSON serialization"""
    return obj.__dict__
