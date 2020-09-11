#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        sorted_key = sorted(a_dictionary.keys())
        for key in sorted_key:
            if a_dictionary[key] == value:
                a_dictionary.pop(key)
    return (a_dictionary)
