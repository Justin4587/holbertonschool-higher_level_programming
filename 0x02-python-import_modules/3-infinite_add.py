#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    nums = sys.argv
    sum = 0
    counter = 1
    if num == 1:
        print("{}".format(sum))
        exit()
    while num > 1:
        sum += int(nums[counter])
        counter = counter + 1
        num = num - 1
    print("{}".format(sum))
