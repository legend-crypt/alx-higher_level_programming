#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    for  key, values in a_dictionary.items():
        if value in values:
            del a_dictionary[key]
        else:
            return a_dictionary
        return a_dictionary
