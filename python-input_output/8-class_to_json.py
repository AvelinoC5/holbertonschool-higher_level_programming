#!/usr/bin/python3
""" Dumps class to Json """


def class_to_json(obj):
    """ function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    """
    return (obj.__dict__)
