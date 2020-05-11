#!/usr/bin/env python3
import string
from sys import argv
import random
import os

PATH = "./files/"
LENFILE = 16384     # Count symbols in file
FILENAMELEN = 32    # Count symbols in file name
SYMBOLS = '{}{}{}'.format(string.ascii_uppercase, string.digits, string.ascii_uppercase.lower())   # Symbols for generate name and content

end = len(SYMBOLS)

COUNTFILES = int(argv[1])   # Count files - is first argument

# for each file
for i in range(0, COUNTFILES, 1):
    rand_string = ""
    file_name = ""

    # Generate content
    for j in range(0, LENFILE, 1):
        rand_string += SYMBOLS[random.randrange(0, end, 1)]

    # Generate filename
    for j in range(0, FILENAMELEN, 1):
        file_name += SYMBOLS[random.randrange(0, end, 1)]

    f = open(PATH+file_name, "w")
    f.write(rand_string)
    f.close()
