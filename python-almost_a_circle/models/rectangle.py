#!/usr/bin/python3
""" First Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method with attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """'width' getter in private"""
        return self.__width

    @width.setter
    def width(self, value):
        """'width' setter (operations and validations)"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """'height' getter in private"""
        return self.__height

    @height.setter
    def height(self, value):
        """'height' setter (operations and validations)"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """'x' getter in private"""
        return self.__x

    @x.setter
    def x(self, value):
        """'x' setter (operations and validations)"""

        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """'y' getter in private"""
        return self.__y

    @y.setter
    def y(self, value):
        """'y' setter (operations and validations)"""

        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Area value of the 'Rectangle' instance"""
        return self.__width * self.__height

    def display(self):
        """Prints the 'Rectangle' instance with the character '#'"""

        whitespace = " "
        for whitespace in range(self.__y):
            print()
        for _ in range(self.__height):
            print(self.__x * " ", end="")
            print(self.__width * "#")

    def __str__(self):
        """Represents the class objects as a string"""

        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        args_len = len(args)

        if args:
            if args_len > 0:
                self.id = args[0]
            if args_len > 1:
                self.__width = args[1]
            if args_len > 2:
                self.__height = args[2]
            if args_len > 3:
                self.__x = args[3]
            if args_len > 4:
                self.__y = args[4]

        if args is None or args_len == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Dictionary representation of a 'Rectangle'"""
        return {"id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y}
