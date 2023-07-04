#!/usr/bin/python3
"""
    Import for getting urls and command line args
"""
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        body = response.headers['X-Request-Id']
        print(body)