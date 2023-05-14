#!/usr/bin/python3
'''models package'''


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
