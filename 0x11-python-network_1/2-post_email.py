#!/usr/bin/python3
""" I'm going to put a comment here"""

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    bulk = parse.urlencode({"email": argv[2]}).encode("utf-8")

    with request.urlopen(argv[1], bulk) as resp:
        print(resp.read().decode("utf-8"))
