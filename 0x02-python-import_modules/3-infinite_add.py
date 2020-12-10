#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    arg_pos = 1
    sum = 0
    if i == 1:
        print("{}".format(sum))
        exit()
    while i > 1:
        sum += int(sys.argv[arg_pos])
        arg_pos += 1
        i -= 1
    print("{}".format(sum))
