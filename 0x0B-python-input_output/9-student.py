#!/usr/bin/python3
'''student class that defines a student'''


class Student:
    '''student class that defines a student

    Args
        first_name: firstname
        last_name: last_name
        age: age
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
