#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = {key: value * 2 for (key, value) in a_dictionary.items()}
    return (n_dictionary)
