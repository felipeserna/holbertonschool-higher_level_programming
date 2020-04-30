#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    import add
    add(int(add.argv[1]))

a = 1
b = 2
print("{:d} + {:d} = {:d}".format(a, b, a+b))
