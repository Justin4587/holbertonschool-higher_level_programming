#!/usr/bin/python3


def uniq_add(my_list=[]):
    x = 0
    new_list = set(my_list)
    ulist = list(new_list)
    for i in ulist:
        x += i
    return (x)
