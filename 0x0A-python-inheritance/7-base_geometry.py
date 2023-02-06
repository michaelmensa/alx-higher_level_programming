#!/usr/bin/python3

'''
    Module 7-base_geometry
'''


class BaseGeometry():

    ''' Class BaseGeometry '''

    def area(self):

        ''' method raises an Exception with message; area() is not
            implemented.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        ''' public instance method that validates value;
            assume name is always a string
            raise TypeError with message; <name> must be an integer
            if value is not an integer.
            raise ValueError with message; <name> must be greater than 0
            if value is less than or equal to 0.
        '''

        self.name = name
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        self.value = value
