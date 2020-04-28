#!/usr/bin/python3
for i in range(97, 123):  # ASCII alphabet in lowercase no e nor q
    if (i != 101 and i != 113):
        print('{:s}'.format(chr(i)), end='')
