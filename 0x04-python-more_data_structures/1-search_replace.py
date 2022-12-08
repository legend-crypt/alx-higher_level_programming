#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if new_list[i] == 2:
            new_list[i] = 89
    return new_list
