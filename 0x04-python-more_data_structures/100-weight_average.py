#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    a function that returns the weighted average of all
    integers tuple (<score>, <weight>)

    args:
        my_list: takes in a list
    Return a the average a weighted list

    """
    numerator = 0
    denomerator = 0
    if len(my_list) == 0:
        return 0
    for i in range(len(my_list)):
        numerator += my_list[i][0] * my_list[i][1]
    for i in range(len(my_list)):
        denomerator += my_list[i][1]
    return numerator / denomerator
