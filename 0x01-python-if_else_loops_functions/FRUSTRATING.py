#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
a = print("Last digit of {} is {} and is greater than 5".format(number, digit))
b = print("Last digit of {} is {} and is 0".format(number, digit))
c = print("Last digit of {} is {} and is less than 6 and not 0".format(number, digit))
#print("{} {}".format(number, digit))
if number > 5:
    print("{}".format(a))
elif number == 0:
    print(b)
elif number < 6:
    print(c)
#print(type(number))
