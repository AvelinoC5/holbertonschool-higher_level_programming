#!/usr/bin/python3
import numbers
from sys import argv


def run():
    numbers = 0
    for indx in argv[1:]:
        numbers += int(indx)
    print("{}".format(numbers))


if __name__ == "__main__":
    run()
