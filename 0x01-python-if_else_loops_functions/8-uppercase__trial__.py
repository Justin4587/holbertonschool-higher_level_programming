#!/usr/bin/python3
def uppercase(str):
    for element in (str):
        newstring = ""
        num = ord(element)
        if num > 96 and num < 123:
            newstring += chr(num - 32)
        else:
                newstring += chr(num - 0)
    print("{}".format(newstring))
    print("")
