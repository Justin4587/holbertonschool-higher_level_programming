#!/usr/bin/env python3
def islower(c):
    numval = ord(c)
    if numval > 96 and numval < 123:
        return True
    else:
        return False
