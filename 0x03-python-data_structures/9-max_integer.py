#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if my_list == []:
        return None
    for i in my_list:
        if my_list[i] > max:
            max = my_list[i] + 0
        return max
