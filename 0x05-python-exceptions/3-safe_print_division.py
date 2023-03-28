#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div_result = a / b
        return div_result
    except ZeroDivisionError:
        div_result = None
        return div_result
    finally:
        if div_result is None:
            print("Inside result: {}".format(div_result))
        else:
            print("Inside result: {:.1f}".format(div_result))
