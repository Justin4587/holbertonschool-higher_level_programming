#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    i = 0
    j = 0
    if a >= 2:
        i = tuple_a[0] + i
        j = tuple_a[1] + j
    elif a == 1:
        i = tuple_a[0] + i
    if b >= 2:
        i = tuple_b[0] + i
        j = tuple_b[1] + j
    elif b == 1:
        i = tuple_b[0] + i
    return (i, j)
