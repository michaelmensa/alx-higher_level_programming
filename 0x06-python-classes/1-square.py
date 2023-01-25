#!/usr/bin/python3
# 1-square.py by Michael Mensah
'''Defines a square by: (based on 0-square.py)'''


class Square:
    '''Defines a square
        with private instance attribute: size'''

    def __init__(self, size):
        '''initializes the square class
            Args: size - reps the size of the square'''
        self.__size = size
