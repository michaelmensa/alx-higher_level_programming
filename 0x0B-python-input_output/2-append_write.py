#!/usr/bin/python3

'''
    Module - Append to a file
'''


def append_write(filename="", text=""):
    ''' Function that appends a string to as text file and returns the
        number of characters written
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
