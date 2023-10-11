#!/usr/bin/python3
'''models package'''
import json


class Base:
    '''Base class for all other classes in this project'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''class constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
