#!/usr/bin/python3


def multiple_returns(sentence):
    a = 0
    b = None
    if sentence == '':
        return (a, b)
    else:
        a = len(sentence)
        b = sentence[0]
    return (a, b)
