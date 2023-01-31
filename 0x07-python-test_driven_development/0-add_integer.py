#!/usr/bin/python3

'''

Module - integers addition by Michael Mensah

'''


def add_integer(a, b=98):
    '''

    Function adds a and b. a, b must be int or floats else, raise
    TypeError: a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float

    '''

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if (type(a) is not int):
        raise TypeError('a must be an integer')
    if (type(b) is not int):
        raise TypeError('b must be an integer')

    return (a + b)
