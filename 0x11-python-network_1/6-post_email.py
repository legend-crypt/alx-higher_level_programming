#!/usr/bin/python3
"""
    imports for command line args and urls requests
"""
from sys import argv
from requests import post

if __name__ == "__main__":
    info = {"email": argv[2]}
    url = argv[1]
    response = post(url, data=info)
    print(response.text)
