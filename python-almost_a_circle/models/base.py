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
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of 'list_dictionaries'"""
 
        if list_dictionaries is None or not list_dictionaries or \
                list_dictionaries == " ":
            return "[]"

        return json.dumps(list_dictionaries)


    def to_dictionary(self):
        """Dictionary representation of a 'Rectangle'"""
        return {"id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y}

    @classmethod
    def save_to_file(cls, list_objs):
        """returns an instance with all attributes already set"""
        save_list = []
        filename = f"{cls.__name__}.json"

        if list_objs is not None:
            for a in list_objs:
                save_list.append(cls.to_dictionary(a))

        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(save_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation 'json_string''"""

        list = []
        if json_string is None or not json_string or \
                json_string == " ":
            return list

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(225, 534)
            dummy.update(**dictionary)

        if cls.__name__ == "Square":
            dummy = cls(3333)
            dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        filename = f"{cls.__name__}.json"
        file_exists = exists(filename)
        list = []

        if not file_exists:
            return list
        else:
            with open(filename, "r", encoding="utf-8") as f:
                each_object = cls.from_json_string(f.read())
                for a in each_object:
                    list.append(cls.create(**a))
            return list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""

        save_list = []
        filename = f"{cls.__name__}.csv"

        if list_objs is not None:
            for a in list_objs:
                save_list.append(cls.to_dictionary(a))

        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(save_list))

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""

        filename = f"{cls.__name__}.csv"
        file_exists = exists(filename)
        list = []

        if not file_exists:
            return list
        else:
            with open(filename, "r", encoding="utf-8") as f:
                each_object = cls.from_json_string(f.read())
                for a in each_object:
                    list.append(cls.create(**a))
            return list
