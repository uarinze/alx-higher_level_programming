#!/usr/bin/python3
'''function that returns the JSON representation of an object (string)'''
import json


def to_json_string(my_obj):
    '''function that returns the JSON representation of an object (string)'''
    jstr = json.dumps(my_obj)
    return jstr
