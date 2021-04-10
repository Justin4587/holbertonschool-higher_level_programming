#!/usr/bin/python3
"""I'm going to put a comment here """

if __name__ == "__main__":
    import requests
    from sys import argv

    resp = requests.get(argv[1])
    print("{}".format(resp.headers.get("X-Request-Id")))
