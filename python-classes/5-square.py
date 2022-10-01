#!/usr/bin/python3
"""
Square Class
"""


class Square:
    """initalization class Squiare"""

    def __init__(self, size=0):
        """Method initalization: Square object args: size of the square"""
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise (TypeError("size must be an integer"))
        if int(value) < 0:
            raise (ValueError("size must be >= 0"))

        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for indx in range(self.__size):
            print("#" * self.__size)

    def area(self):
        """Return area of the Square"""
        area_sqr = self.__size**2
        return (area_sqr)
