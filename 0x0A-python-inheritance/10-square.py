#!/usr/bin/python3

'''
    Module Square #1 derived from Rectangle(9-rectangle)
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    '''
        Class Square that inherits from Rectangle
    '''

    def __init__(self, size):
        ''' self instantiation. must be validated by
            integer_validator
        '''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
