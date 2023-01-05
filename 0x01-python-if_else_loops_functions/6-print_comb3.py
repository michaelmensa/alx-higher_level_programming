#!/usr/bin/python3
for x in range(0, 9):
    for y in range(1, 10):
        if (y < x or y == x):
            continue
        if (x != 8):
            print("{}{}".format(x, y), end=", ")
        else:
            print("{}{}".format(x, y))
