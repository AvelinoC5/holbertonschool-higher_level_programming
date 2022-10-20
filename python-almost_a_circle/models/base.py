#!/usr/bin/python3
""" Base class of all other classes in this project"""

import json
from os.path import exists

class Base:
    """First class atributtes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id =id
        
        else:
            Base-__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of 'list_dictionaries'"""
 
        if list_dictionaries is None or not list_dictionaries or \
                list_dictionaries == " ":
            return "[]"

        return json.dumps(list_dictionaries)
