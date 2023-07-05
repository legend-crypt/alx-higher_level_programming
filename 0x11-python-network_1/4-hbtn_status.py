#!/usr/bin/python3
"""
    import for getting url request
"""
import requests
if __name__ == "__main__":
    body = requests.get("https://alx-intranet.hbtn.io/status")
    print(f"""
          Body response:
          \t- type: {type(body.text)}
          \t- content: {body.text}""")
