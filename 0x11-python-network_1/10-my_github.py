#!/usr/bin/python3
"""Takes your Github credentials (username and password) and
uses the Github API to display your id"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    print(res.json().get('id'))
