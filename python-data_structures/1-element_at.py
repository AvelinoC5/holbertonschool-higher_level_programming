#!/usr/bin/python3
from array import array


def element_at(my_list, idx):
    for arry in range(len(my_list)):
        if ((idx < 0) or (idx > len(my_list))):
            return (None)
        elif (idx == arry):
            return (my_list[arry])
