#!/usr/bin/python3
def uppercase(str):
    newstring = ""
    i = 0
    j = len(str)
    while i < j:
        num = ord(str[i])
        if num > 96 and num < 123:
            num = num - 32
            newstring += chr(num)
            i = i + 1
        else:
            newstring += chr(num)
            i = i + 1
    print("{}".format(newstring))
