#!/usr/bin/python3
""" I'm going to put a comment here """

if __name__ == "__main__":
    import requests
    from sys import argv

    resp = requests.get("https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1]))
    dict_new = resp.json()
    for i in dict_new:
        print("{}: {}".format(i.get("sha"), i.get("commit"),
                              i.get("author"), i.get("name")))
        i++
        if i == 9:
            break
