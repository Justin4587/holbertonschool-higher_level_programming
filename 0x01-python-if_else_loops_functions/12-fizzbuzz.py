#!/usr/bin/python3
def fizzbuzz():
    a = "Fizz"
    b = "Buzz"
    i = 0
    tmp = range(1, 101)
    while i < len(tmp):
        if tmp[i] % 3 == 0 and tmp[i] % 5 == 0:
            print(a + b, end=' ')
            i = i + 1
            continue
        if tmp[i] % 3 == 0:
            print(a, end=' ')
            i = i + 1
            continue
        if tmp[i] % 5 == 0:
            print(b, end=' ')
            i = i + 1
            continue
        else:
            print(tmp[i], end=' ')
        i = i + 1
