#!/usr/bin/python3
# 2-square.py by Michael Mensah
'''Defines a square by: (based on 1-square.py)'''


class Square:
    '''Defines a square
        with private instance attribute: size'''

    def __init__(self, size=0):
        '''initializes the square class
            Args: size - reps the size of the square
            Raises: TypeError: if size is not integer
                    ValueError: if size is less than zero
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
