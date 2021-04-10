#!/usr/bin/python3
"""I'm going to put a comment here """

if __name__ == "__main__":
    import requests
    from sys import argv

    q = ""
    dict_new = {}
    if len(argv) > 1:
        dict_new["q"] = argv[1]
    resp = requests.post("http://0.0.0.0:5000/search_user", data=dict_new)
    try:
        jstring = resp.json()
        if jstring == {}:
            print("No result")
        else:
            print("[{}] {}".format(jstring["id"], jstring["name"]))
    except Exception as e:
        print("Not a valid JSON")
