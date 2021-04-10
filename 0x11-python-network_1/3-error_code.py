#!/usr/bin/python3
""" I'm going to put a comment here"""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except error.HTTPError as uhoh:
        print("Error code: {}".format(uhoh.code))
