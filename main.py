#!/usr/bin/env python3
import string
from sys import argv
import random

PATH = "./files"
LENFILE = 1000
FILENAMELEN = 24
SYMBOLS = string.ascii_uppercase + string.digits + string.ascii_uppercase.lower()


print(SYMBOLS)
end = len(SYMBOLS)

for i in range(0, 1000, 1):
    rand_string = ""
    for j in range(0, 10000, 1):
        rand_string += SYMBOLS[random.randrange(0, end, 1)]
    #print(rand_string)
    #print(" ")
