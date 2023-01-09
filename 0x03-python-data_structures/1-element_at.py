#!/usr/bin/python3
def element_at(my_list, idx):
    for x in range(len(my_list)):
        if ((idx < 0) or (idx > len(my_list))):
            return (None)
        elif (idx == x):
            return (my_list[x])
