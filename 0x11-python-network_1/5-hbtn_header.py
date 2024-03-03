#!/usr/bin/python3
"""
    imports for getting command line args and url
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    url = argv[1]
    body = get(url)
    head = body.headers.get('X-Request-Id')
    print(head)
