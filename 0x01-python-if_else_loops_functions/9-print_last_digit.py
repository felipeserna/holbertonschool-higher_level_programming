#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
            l = (-1 * number) % 10
            print("{:d}".format(l), end="")
            return (l)
    else:
            l = number % 10
            print("{:d}".format(l), end="")
            return (l)
