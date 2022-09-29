#!/usr/bin/python3
from multiprocessing.sharedctypes import Value


def safe_print_list(my_list=[], x=0):
    value = 0
    if (x > 0):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                value += 1
            except:
                break
    print('')
    return (value)
