#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    for str in range(lens(sys.argv)):
        if (str == 0):
            continue
        else:
            res = res + int(sys.argv[str])
    print("{}".format(res))
