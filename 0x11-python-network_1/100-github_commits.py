#!/usr/bin/python3
""" I'm going to put a comment here """

if __name__ == "__main__":
    import requests
    from sys import argv

    j = 0
    resp = requests.get("https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1]))
    dict_new = {}
    dict_new = resp.json()
    for i in dict_new:
        print("{}: {}".format(i.get('sha'),i.get('commit').get('author').get('name')))
        j += 1
        if j == 10:
            break
