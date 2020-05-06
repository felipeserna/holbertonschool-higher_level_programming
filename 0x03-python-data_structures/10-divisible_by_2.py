#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_by_2 = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            div_by_2.append(True)
        else:
            div_by_2.append(False)
        i += 1
    return(div_by_2)
