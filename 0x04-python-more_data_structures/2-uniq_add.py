#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    newer_list = list(new_list)
    i = 0
    for j in newer_list:
        i += j
    return i
