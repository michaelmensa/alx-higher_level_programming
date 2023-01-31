#!/usr/bin/python3

'''

4-print_square.py by Michael Mensah

'''


def print_square(size):

    '''

    Function - prints a square with the character #

    Arguments - size
            size must be an integer, otherwise raise TypeError with msg;
            size must be an integer
            raise ValueError with msg; size must be >= 0 if size < 0
            if size is float and < 0, raise TypeError

    '''

    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        print('#' * size)
