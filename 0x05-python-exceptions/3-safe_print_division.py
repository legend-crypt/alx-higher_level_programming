#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div_result = a / b
    except ZeroDivisionError:
        div_result = None
    finally:
        if div_result is None:
            print("Inside result: {}".format(div_result))
        else:
            print("Inside result: {:.1f}".format(div_result))
