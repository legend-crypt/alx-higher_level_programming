#!/bin/python3
"""import sys and argv"""
from sys import argv
import requests


def get_commits():
    repo_name = argv[1]
    repo_owner = argv[2]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    header = {
        "Authorization": "Bearer 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"
    }
    res = requests.get(url, headers=header)
    datas = res.json()
    for i in range(0, 10):
        sha = datas[i].get('sha')
        name = datas[i]["commit"]["author"]["name"]
        print("{}: {}".format(
            sha, name)
        )


if __name__ == "__main__":
    get_commits()
