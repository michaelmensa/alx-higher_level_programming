#!/usr/bin/python3

'''
    Module Write to a file
'''


def write_file(filename="", text=""):
    ''' Function that writes a string to as text file and returns the
        number of characters written
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
