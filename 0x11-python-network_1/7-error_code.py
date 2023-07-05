#!/usr/bin/python3

"""
import for getting command line args and urls request
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    if response.status_code < 400:
        print(response)
    else:
        print(f"Error code: {response.status_code}")
