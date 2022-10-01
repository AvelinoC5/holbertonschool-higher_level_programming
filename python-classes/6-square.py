#!/usr/bin/python3
"""
Square Class
"""


class Square:
    """initalization class Squiare"""

    def __init__(self, size=0, position=(0, 0)):
        """Method initalization: Square object args: size of the square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise (TypeError("size must be an integer"))
        if int(value) < 0:
            raise (ValueError("size must be >= 0"))

        self.__size = value

    @property
    def position(self):
        """getter for position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter for position"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not isinstance(value[0], int) \
                or not isinstance(value[1], int) \
                or value[0] < 0 or value[1] < 0:
            raise (TypeError("position must be a tuple of 2 positive integers"))

        self.__position = value


    def my_print(self):
        if self.__size == 0:
            print()
        for idx in range(self.__position[1]):
            print()
        for indx in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)


    def area(self):
        """Return area of the Square"""
        area_sqr = self.__size**2
        return (area_sqr)
