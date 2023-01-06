#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv)
    for str in range(argc):
        if (argc != 4):
            print("Usage: {} <a> <operator> <b>".format(sys.argv[str]))
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if (sys.argv[2] == '+'):
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif (sys.argv[2] == '-'):
                print("{} - {} = {}".format(a, b, sub(a, b)))
            elif (sys.argv[2] == '*'):
                print("{} + {} = {}".format(a, b, add(a, b)))
            elif (sys.argv[2] == '/'):
                print("{} + {} = {}".format(a, b, add(a, b)))
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
            exit(0)
     
     
     
     
