#!/usr/bin/python3

import sys
if __name__ == "__main__":
    argv = sys.argv
    argv_len = len(argv)

    if argv_len < 2:
        print("{} arguments.".format(argv_len - 1))

    elif argv_len < 3:
        print("{} argument:".format(argv_len - 1))
        print("{}: {}".format(argv_len - 1, argv[1]))

    else:
        print("{} arguments:".format(argv_len - 1))
        for i in range(argv_len):
            if i == 0:
                continue
            print("{}: {}".format(i, argv[i]))
