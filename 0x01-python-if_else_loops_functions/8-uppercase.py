#!/usr/bin/python3
def uppercase(str):
    for element in (str):
        num = ord(element)
        if num > 96 and num < 123:
            num = num - 32
            element = chr(num)
            print("{}".format(element), end='')
        else:
            print(element, end='')
    print("\n")
