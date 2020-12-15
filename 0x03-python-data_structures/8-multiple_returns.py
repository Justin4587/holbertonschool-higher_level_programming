#!/usr/bin/python3
def multiple_returns(sentence):
    i = 0
    j = None
    if sentence == "":
        return (i, j)
    else:
        i = len(sentence)
        j = sentence[0]
    return (i, j)
