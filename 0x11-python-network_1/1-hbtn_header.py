#!/usr/bin/python3
""" I'm going to put a comment here """

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as resp:
        print(resp.getheader("X-Request-Id"))
