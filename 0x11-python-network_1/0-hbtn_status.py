#!/usr/bin/python3
""" I'm going to put a comment here """

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
        words = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(words)))
        print("\t- content: {}".format(words))
        print("\t- utf8 content: {}".format(words.decode("utf-8")))
