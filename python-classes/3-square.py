#!/usr/bin/python3
"""
Square Class this module defines
"""


class Square:
    """initalization class Squiare"""

    def __init__(self, size=0):
        """Method: Square object
        args: size of the square"""
        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        if int(size) < 0:
            raise (ValueError("size must be >= 0"))

        self.__size = size

    def area(self):
        """Return area of the Square"""
        area_sqr = self.__size**2
        return (area_sqr)