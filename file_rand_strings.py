#!/usr/bin/env python3
import string
from sys import argv
import random
import os

PATH= "./files2/"
LENFILE = 64
FILENAMELEN = 32
SYMBOLS = string.ascii_uppercase + string.digits + string.ascii_uppercase.lower()
end = len(SYMBOLS)

file_name = ""


for j in range(0, FILENAMELEN, 1):
    file_name += SYMBOLS[random.randrange(0, end, 1)]

for i in range(0, 100000, 1):
    rand_string = ""
    for j in range(0, LENFILE, 1):
        rand_string += SYMBOLS[random.randrange(0, end, 1)]

    f = open(PATH + file_name, "a")
    f.write(rand_string+"\n")
    print(i)
    f.close()