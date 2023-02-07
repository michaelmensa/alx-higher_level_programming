#!/usr/bin/python3
'''
    Module - Student to JSON
'''


class Student():
    ''' Class student that defines a student by;
        first_name, last_name, age
    '''
    def __init__(self, first_name, last_name, age):
        ''' istantiation with special init method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' retrieves a dictionary representation of a
            student instance
        '''
        return self.__dict__
