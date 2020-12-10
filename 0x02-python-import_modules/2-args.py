#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    arg_cnt = i
    arg_pos = 1
    cnt = 1
    if i == 1:
        print("{} arguments.".format(i - 1))
    elif i == 2:
        print("{} argument:".format(i - 1))
    else:
        print("{} arguments:".format(i - 1))
    while arg_cnt > 1:
        print("{}: {}".format(cnt, sys.argv[arg_pos]))
        arg_cnt -= 1
        cnt += 1
        arg_pos += 1
