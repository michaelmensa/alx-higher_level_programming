#!/usr/bin/python3

''' Module that inherits from list '''


class MyList(list):

    ''' Mylist inherits from list '''

    def print_sorted(self):

        '''
            Function that prints the list, but sorted (ascending sort)
        '''

        print(sorted(self))
