#!/usr/bin/python3
def uppercase(str):
    for i in str:
        newstr = ""
        num = ord(i)
        if num > 96 and num < 123:
            newstr += chr(num - 32)
        else:
            newstr += chr(num)
    print("{}".format(newstr))
