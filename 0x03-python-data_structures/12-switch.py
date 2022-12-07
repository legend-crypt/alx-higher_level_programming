#!/usr/bin/python3
a = 89
b = 10
temp_a, temp_b = a, b
a, b = temp_b, temp_a
print("a={:d} - b={:d}".format(a, b))
