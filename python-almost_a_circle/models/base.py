#!/usr/bin/python3
"""
base class for all other classes

manages id attribute in all future classes

avoid duplicating same code
"""
import json


class Base:
    """base defined"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation of list_objs to file"""
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns list of json string representation dictionary"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
