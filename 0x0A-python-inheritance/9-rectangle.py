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

    def area(self):
        ''' returns the area of the rectangle '''
        return self.__width * self.__height

    def __str__(self):
        ''' returns the print() and str() representation of the rectangle '''
        string = '[' + str(self.__class__.__name__) + ']' + ' '
        string += str(self.__width) + '/' + str(self.__height)
        return string
