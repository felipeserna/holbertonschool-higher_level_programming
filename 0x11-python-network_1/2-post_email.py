#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    # variable to send in POST request
    var_email = {'email': email}
    # encode variable
    data = urllib.parse.urlencode(var_email)
    data = data.encode('ascii')
    # POST request
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        header = response.read()
        print(header.decode('utf-8'))
