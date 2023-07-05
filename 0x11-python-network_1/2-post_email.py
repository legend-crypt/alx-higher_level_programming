#!/usr/bin/python3
"""
    This is the import for getting command line args and url
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    data = urlencode(value)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)
