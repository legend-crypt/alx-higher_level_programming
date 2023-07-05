#!/usr/bin/python3

"""
Import for the getting command line args and urls
"""
from urllib.error import HTTPError
from sys import argv
from urllib.request import urlopen
if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print(f"Error code: {e.code}")
