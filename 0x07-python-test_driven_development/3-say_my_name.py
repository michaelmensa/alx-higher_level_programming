#!/usr/bin/python3

'''

Say My Name by Heisenberg

'''


def say_my_name(first_name, last_name=""):

    '''

    Function: say_my_name - prints My name is <first name> <last name>

    Args: first_name, last_name

    Raise: Both first_name and last_name must be strings, return TypeError
        with message first_name must be a string or last_name must be a string

    '''

    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
