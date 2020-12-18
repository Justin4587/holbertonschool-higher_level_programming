#!/usr/bin/python3
def best_score(a_dictionary):
    sum = 0
    if a_dictionary:
        key = sorted(a_dictionary.keys())
        for i in key:
            if a_dictionary[i] > sum:
                sum = a_dictionary[i] + 0
    return (sum)
