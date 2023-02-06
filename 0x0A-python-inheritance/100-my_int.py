#!/usr/bin/python3

'''
    Module - My integer
'''


class MyInt(int):

    '''
        MyInt inherits from int.
    '''

    def __eq__(self, value):
        ''' inverts to give not equal to '''
        return self.real != value

    def __ne__(self, value):
        ''' inverts to give equal to '''
        return self.real == value
