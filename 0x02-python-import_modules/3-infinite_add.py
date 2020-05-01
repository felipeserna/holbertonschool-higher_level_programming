#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_length = len(sys.argv)
    addition = 0
    if argv_length > 1:
        for i in range(1, argv_length):
            addition += int(sys.argv[i])
        print("{:d}".format(addition))
    elif argv_length == 1:
        print("{:d}".format(0))
