#!/usr/bin/python3
"""
Square Class
"""


class Square:
    """
    initalization class Squiare
    """

    def __init__(self, size=0):
        """Valitation if the size is to
         integer or is a negative number"""

        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        if int(size) < 0:
            raise (ValueError("size must be >= 0"))
        self.__size = size
