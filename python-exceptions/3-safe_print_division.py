#!/usr/bin/python3
def safe_print_division(a, b):
    go = 0
    try:
        go = (a / b)
    except:
        go = None
    finally:
        print("Inside result: {}".format(go))
    return (go)
