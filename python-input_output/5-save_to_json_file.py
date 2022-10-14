#!/usr/bin/python3
"""
File with save_to_json_file(my_obj, filename)
Writes an object(data struct) to txt
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that returns the JSON representation of an object (string)
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
