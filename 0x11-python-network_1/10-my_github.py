#!/usr/bin/python3
""" I'm going to put a comment here """

if __name__ == "__main__":
    import requests
    from sys import argv

    resp = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print("{}".format(resp.json().get("id")))
