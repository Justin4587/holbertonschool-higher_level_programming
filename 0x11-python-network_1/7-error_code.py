#!/usr/bin/python3
"""I'm going to put a comment here """

if __name__ == "__main__":
    import requests
    from sys import argv

    resp = requests.get(argv[1])
    stat = resp.status_code
    if stat == requests.codes.ok:
        print("{}".format(resp.text))
    else:
        print("Error code: {}".format(stat))
