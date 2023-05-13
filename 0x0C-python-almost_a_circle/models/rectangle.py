#!/usr/bin/python3
'''Rectangle class which is a subclass of base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class inherits from Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
    
    @property
    def height(self):
        '''get height'''
        return self.__height

    @height.setter
    def height(self, height):
        '''set height'''
        self.__height = height

    @property
    def width(self):
        '''get width'''
        return self.__width

    @width.setter
    def width(self, width):
        '''set width'''
        self.__width = width

    @property
    def x(self):
        '''get x'''
        return self.__x

    @x.setter
    def x(self, x):
        '''set x'''
        self.__x = x

    @property
    def y(self):
        '''get y'''
        return self.__y

    @y.setter
    def y(self, y):
        '''set y'''
        self.__y = y
