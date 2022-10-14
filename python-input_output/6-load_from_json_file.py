#!/usr/bin/python3
"""
Function creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Create a object with json format
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
