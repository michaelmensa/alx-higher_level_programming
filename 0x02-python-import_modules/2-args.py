#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv) - 1
    if (nargs == 0):
        print("{} arguments.".format(nargs))
    elif (nargs == 1):
        print("{} argument:".format(nargs))
    else:
        print("{} arguments:".format(nargs))
    for str in range(lens(sys.argv)):
        if (str == 0):
            continue:
        print("{}: {}".format(str, sysargv[str[))
