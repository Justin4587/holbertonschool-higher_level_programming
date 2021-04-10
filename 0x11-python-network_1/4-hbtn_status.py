#!/usr/bin/python3
""" I'm going to put a comment here"""

if __name__ == "__main__":
    import requests

    resp = requests.get("https://intranet.hbtn.io/status")
    response = resp.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
