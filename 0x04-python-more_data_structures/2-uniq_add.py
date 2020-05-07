#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = 0
    unique = list(dict.fromkeys(my_list))
    unique = sum(unique)
    return(unique)
