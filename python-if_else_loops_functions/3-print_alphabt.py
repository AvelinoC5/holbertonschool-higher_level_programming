#!/usr/bin/python3
for j in range(97, 123):
    if (j == 101 or j == 113):
        continue
    print("{}".format(chr(j)), end="")
