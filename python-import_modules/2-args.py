#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    xargs = len(sys.argv) - 1
    if (xargs == 0):
        print("{:d} arguments.".format(xargs))
    elif (xargs == 1):
        print("{:d} argument:".format(xargs))
    else:
        print("{:d} arguments:".format(xargs))
    for str in range(len(sys.argv)):
        if (str == 0):
            continue
        print("{:d}: {:s}".format(str, sys.argv[str]))
