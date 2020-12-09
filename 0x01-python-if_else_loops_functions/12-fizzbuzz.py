#!/usr/bin/python3
def fizzbuzz():
    a = "Fizz"
    b = "Buzz"
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(a + b, end=' ')
        elif i % 3 == 0:
            print(a, end=' ')
        elif i % 5 == 0:
            print(b, end=' ')
        else:
            print(i, end=' ')
