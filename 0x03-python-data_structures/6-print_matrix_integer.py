#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j + 1 in i:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j))
    if matrix == [[]]:
        print()
