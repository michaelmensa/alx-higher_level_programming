#!/usr/bin/python3

'''
    Module almost a circle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class square that inherits from Rectangle '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' class constructor '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' Retrieve the size of square '''
        return self.width

    @size.setter
    def size(self, value):
        ''' sets the value of size '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        ''' overloading __str__ method shoud return:
            [Square] (<id>) <x>/<y> - <size>
        '''
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''
            assigns key/value to attributes
            kwargs is skipped if args exists and not empty
            Args:
                *args - variable number of no keyword args
                **kwargs - variable number of keyword args
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass


    def to_dictionary(self):
        ''' Returns the dictionary representation of a Square '''
        return {'id': getattr(self, 'id'),
                'x': getattr(self, 'x'),
                'size': getattr(self, 'size'),
                'y': getattr(self, 'y'),}
