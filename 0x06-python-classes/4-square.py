#!/usr/bin/python3
# 4-square.py by Michael Mensah
'''Defines a square by: (based on 3-square.py)'''


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

    def area(self):
        '''Public instance/object method
           Returns the current square area
        '''
        return(self.__size ** 2)

    @property
    def size(self):
        '''Getter to retrieve '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter to set value
            raise TypeError if value is not int
            raise ValueError if value > 0
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
