#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
You must use the package requests
"""


import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.content.decode("utf-8"))))
    print("\t- content: {}".format(response.content.decode("utf-8")))
