#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res = a / b
    except (ZeroDivisionError):
        #print("Can't divide by zero")
        res = None
    finally:
        print("Inside result: {}".format(res))
       # print("{} / {} = {}".format(a, b, res))
    return(res)
