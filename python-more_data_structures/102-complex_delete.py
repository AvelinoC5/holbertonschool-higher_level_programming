#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for j in list(a_dictionary.keys()):
        if a_dictionary[j] is value:
            del a_dictionary[j]
    return a_dictionary
