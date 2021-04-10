#!/usr/bin/python3
"""I'm going to put a comment here """

if __name__ == "__main__":
    import requests
    from sys import argv

    resp = requests.post(argv[1], data={"email": argv[2]})
    print("{}".format(resp.text))
