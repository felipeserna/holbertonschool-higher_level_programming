#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    l = ((-1 * number) % 10) * (-1)  # last digit
else:
    l = number % 10  # last digit
if l > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, l))
elif l < 6 and l != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, l))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, l))
