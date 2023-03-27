#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    for k in range(x):
        try:
            print(my_list[i], end="\n")
            i += 1
        except IndexError:
            pass
    return i
