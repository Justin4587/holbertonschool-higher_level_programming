#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    counter = 1
    arg_counter = num
    arg_pos = 1
    if num == 1:
        print("{} arguments.".format(num - 1))
    elif num == 2:
        print("{} argument:".format(num - 1))
    else:
        print("{} arguments:".format(num - 1))
    while arg_counter > 1:
        print("{}: {}".format(counter, sys.argv[arg_pos]))
        arg_pos = arg_pos + 1
        counter = counter + 1
        arg_counter = arg_counter - 1
