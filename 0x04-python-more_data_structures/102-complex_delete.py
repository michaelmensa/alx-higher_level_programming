#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value == 0:
        return a_dictionary
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            a_dictionary.pop(key, None)
    return a_dictionary
