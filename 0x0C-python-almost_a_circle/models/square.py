#!/usr/bin/python3
'''square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''The class square inherits from the rectangle class/'''

    def __init__(self, size, x=0, y=0, id=None):
        '''initialisation with superclass attributes'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''getter for size'''
        return self.width

    @size.setter
    def size(self, value):
        '''settet for size'''
        self.width = value
        self.height = value

    def __str__(self):
        '''string representation fo the instance'''
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        '''this assigns attributes to the square class'''
        if args and len(args) != 0:
            count = 0
            for i in args:
                count += 1
                if count == 1:
                    if args is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = i
                elif count == 2:
                    self.size = i
                elif count == 3:
                    self.x = i
                elif count == 4:
                    self.y = i

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        ''' returns a dictionary representation of a square.'''
        return {
            "id": self.id,
            "size": self.size
            "x": self.x
            "y": self.y
        }
