#!/usr/bin/env python

import requests

print(requests.__version__)

r = requests.get("https://raw.githubusercontent.com/terrence85561/cmput404lab1/master/main.py")
#print(dir(r))
print(r.text)
# print(r.status_code)
