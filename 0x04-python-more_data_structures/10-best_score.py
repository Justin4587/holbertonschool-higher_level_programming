#!/usr/bin/python3


def best_score(a_dictionary):
    best = 0
    temp = None
    if a_dictionary:
        sorted_key = sorted(a_dictionary.keys())
        for key in sorted_key:
            if a_dictionary[key] > best:
                best = a_dictionary[key] + 0
                temp = key
    return (temp)
