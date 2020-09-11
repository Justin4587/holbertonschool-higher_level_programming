#!/usr/bin/python3
def weight_average(my_list=[]):
    scores = 0
    weights = 0
    if my_list != []:
        for sw in my_list:
            scores = scores + sw[0] * sw[1]
            weights = weights + sw[1]
        avg = scores / weights
        return (avg)
    else:
        return (0)
