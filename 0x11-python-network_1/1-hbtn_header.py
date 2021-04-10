#!/usr/bin/python3
""" I'm going to put a comment here """

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with request.urlopen(argv[1]) as resp:
        print(resp.getheader("X-Request-Id"))
