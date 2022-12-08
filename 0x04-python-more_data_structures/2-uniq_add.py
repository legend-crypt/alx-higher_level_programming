#!/usr/bin/python3

def uniq_add(my_list =[]):
    new_list = my_list.copy()
    new_list = set(new_list)
    new_list = list(new_list)
    result = 0
    for i in new_list:
        result += i
    return result
