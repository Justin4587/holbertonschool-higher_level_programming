#!/usr/bin/python3
def best_score(a_dictionary):
    sum = 0
    name = None
    if a_dictionary:
        key = sorted(a_dictionary.keys())
        for names in key:
            if a_dictionary[names] > sum:
                sum = a_dictionary[names] + 0
                name = names
    return (name)
