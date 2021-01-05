#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elms = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elms += 1
        except (IndexError):
            pass
    print()
    return(elms)
