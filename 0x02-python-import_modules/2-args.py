#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_length = len(sys.argv)
    if argv_length == 1:
            print("0 arguments.")
    elif argv_length == 2:
            print("1 argument:")
            print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_length - 1))
        i = 1
        while i < argv_length:
            print("{:d}: {}".format(i, sys.argv[i]))
            i += 1
