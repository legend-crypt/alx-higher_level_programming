#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print("--")

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print("--")
