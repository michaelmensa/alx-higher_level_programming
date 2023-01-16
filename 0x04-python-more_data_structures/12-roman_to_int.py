#!/usr/bin/python3
def value(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1

def roman_to_int(str):
    if (str != str or str is None):
        return 0
    res = 0
    i = 0
    while (i < len(str)):
        s1 = value(str[i])
        if (i < len(str)):
            res += s1
        i += 1
        if (s1 > value(str[0])):
            res = (s1 - value(str[0]))
            break
    return res
    return res
