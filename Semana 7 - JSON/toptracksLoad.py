# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 20:38:01 2021

@author: USUARIO
"""

import json

toptracks = open("toptracks.json","r")

data = json.loads(toptracks.read())

#print(data["tracks"][0])

print(len(data["tracks"]))

for i in range(len(data["tracks"])):
    print(i)
    y = data["tracks"][i]
    print(y["name"])