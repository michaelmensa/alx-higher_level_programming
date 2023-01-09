#!/usr/bin/python3
def no_c(my_string):
    for r in range(len(my_string) - 2):
        if (my_string[r] == 'c' or my_string[r] == 'C'):
            my_string = my_string[:r] + "" + my_string[r+1:]
    return (my_string)
