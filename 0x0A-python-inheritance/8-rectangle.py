#!/usr/bin/python3

'''
    Module Rectangle derived from class BaseGeometry(7-base_geometry)
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    '''
        Class Rectangle that inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        '''
            width and height must be private. No getter nor setter
            width and height must be validated by integer_validator
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
