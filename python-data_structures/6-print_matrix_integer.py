#!/usr/bin/python3
def no_c(my_string):
    no_c = {ord('c'): "", ord('C'): ""}
    return (my_string.translate(no_c))
