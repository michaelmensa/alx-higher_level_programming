#!/usr/bin/python3

'''
    Module - Exact same object
'''


def is_same_class(obj, a_class):

    '''
        Function that returns True if object is exactly an instance
        of the specified class; otherwise False.
    '''

    return (type(obj) == a_class)
