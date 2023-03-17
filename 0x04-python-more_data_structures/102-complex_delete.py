#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    for keys, values in list(a_dictionary.items()):
        if values == value:
            del a_dictionary[keys]
    return a_dictionary
