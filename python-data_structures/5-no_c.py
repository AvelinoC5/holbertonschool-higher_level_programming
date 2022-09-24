#!/usr/bin/python3
def no_c(my_string):
    remove = ""
    for a in my_string:
        if a not in 'cC':
            remove += a
    return remove
