#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    nums_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nums_print += 1
        except (ValueError, TypeError):
            pass
    print("")
    return nums_print
