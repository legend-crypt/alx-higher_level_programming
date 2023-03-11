#!/usr/bin/python3

import sys

argv = sys.argv
argv_len = len(argv)
sum = 0

if argv_len == 1:
    print(sum)
else:
    for i in range(argv_len):
        if i == 0:
            continue
        sum += int(argv[i])
    print(sum)
