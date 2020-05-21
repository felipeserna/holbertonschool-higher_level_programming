#!/usr/bin/python3
def add_integer(a, b=98):
    """My addition function
    Args:
        a: first integer
        b: second integer
    Returns:
        The return value. a + b
    """
    if a is not int:
        raise TypeError("a must be an integer")
    if a is not float:
        raise TypeError("a must be an integer")
    if b is not int:
        raise TypeError("b must be an integer")
    if b is not float:
        raise TypeError("b must be an integer")
    #if a is float:
    #    int(a)
    #if b is float:
    #    int(b)
    return (int(a) + int(b))
