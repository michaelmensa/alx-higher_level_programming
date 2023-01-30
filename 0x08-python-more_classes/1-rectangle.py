#!/usr/bin/python3
'''1-rectangle.py by Michael Mensah'''i


class Rectangle:
    '''Create class Rectangle that defines a rectangle'''
    def __init__(self, width=0, height=0):
        '''Instantiation with __init__ method__'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter to retrieve width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter: width must be int, else raise TypeError.
            width must be greater than or less than 0, else
            raise ValueError
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Getter to retrieve height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter: height must be int, else raise TypeError.
            height must be greater than or less than 0, else
            raise ValueError
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
