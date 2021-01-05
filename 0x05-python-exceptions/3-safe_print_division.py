#!/usr/bin/python3
def safe_print_division(a, b):
    dividend = None
    try:
        dividend = a / b
    except (ZeroDivisionError):
        return(None)
    finally:
        print("Inside result: {}".format(dividend))
    return(dividend)
