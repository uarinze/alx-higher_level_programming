#!/usr/bin/python3
'''student class that defines a student'''


class Student:
    '''student class that defines a student'''

    def __init__(self, first_name, last_name, age):
        '''student class that defines a student

        Args
            first_name: firstname
            last_name: last_name
            age: age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''that retrieves a dictionary representation of a Student instance

        Argv:
            attrs: optional attibutes to show if available
        '''
        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        ''' that replaces all attributes of the Student instance

        Argv:
            json (dict): the key/value pair to replace attributes with.
        '''
        for k, v in json.items():
            setattr(self, k, v)
