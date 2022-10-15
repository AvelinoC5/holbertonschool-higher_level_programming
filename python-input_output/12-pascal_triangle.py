#!/usr/bin/python3
""" Program that define a Student with filter """


class Student:
    """ class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        dic = {}
        if (type(attrs) is not list):
            return (self.__dict__)
        else:
            for i in attrs:
                if (i in self.__dict__):
                    dic[i] = self.__dict__[i]
            return (dic)

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for i in json:
            self.__dict__[i] = json[i]
