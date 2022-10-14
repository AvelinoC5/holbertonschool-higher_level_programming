#!/usr/bin/python3
""" Program open, read and write a file appending """


def append_write(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    returns the number of characters written """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
