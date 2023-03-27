#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    nums_print = 0
    try:
        for i in range(x):
            print(int(my_list[i]), end="\n")
            nums_print += 1
    except (IndexError, ValueError):
        pass
    return nums_print
