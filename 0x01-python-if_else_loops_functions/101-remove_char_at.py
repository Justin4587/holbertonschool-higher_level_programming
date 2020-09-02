#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ''
    i = 0
    while i < len(str):
        if i == n:
            i = i + 1
            continue
        else:
            cpy += str[i]
            i = i + 1
    return cpy
