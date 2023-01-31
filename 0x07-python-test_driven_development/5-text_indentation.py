#!/usr/bin/python3

'''

5-text_indentation.py - module that contains function to print a text with 2
                        two new lines after each of these characters;
                        '.', '?', and ':'

'''


def text_indentation(text):
    '''

    function - prints a text with 2 new lines after each of these characters:
                '.', '?', and ':'

    Arguments - text
                raise TypeError with message: text must be a string if text
                is not a string

                No space at the beginning nor at the end of each printed line

    '''

    if type(text) != str:
        raise TypeError('text must be a string')

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s == "" else s + "\n\n" + i + d

    print(s[:-3], end="")
