#!/usr/bin/python3
i = range(122, 97, -2)
j = range(89, 64, -2)
tick = 0

while tick < 13:
    print("{:c}{:c}".format(i[tick], j[tick]), end='')
    tick = tick + 1
