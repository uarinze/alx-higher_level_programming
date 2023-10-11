#!/usr/bin/python3
'''Rectangle class which is a subclass of base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class inherits from Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        '''get height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        '''get width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        '''get x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''get y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''returns the area of the rectangle'''
        return (self.width * self.height)

    def display(self):
        '''prints in stdout the rectangle instance with the character #'''
        for j in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''prints out a formated output to stdout'''
        return "[{}] ({}) {}/{} - {}/{}".format(__class__.__name__,
                                                self.id, self.x,
                                                self.y, self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        '''assigns argument to each attribute in the class.'''
        count = 0
        for arg in args:
            count += 1
            if count == 1:
                self.id = arg
            elif count == 2:
                self.width = arg
            elif count == 3:
                self.height = arg
            elif count == 4:
                self.x = arg
            elif count == 5:
                self.y = arg
        if len(args) == 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        '''returns the dictionary reoresentation of a Rectangle'''
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
