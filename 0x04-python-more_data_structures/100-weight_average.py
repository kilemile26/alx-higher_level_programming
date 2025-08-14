#!/usr/bin/python3
def weight_average(my_list=[]):
    total = sum(x[0] * x[1] for x in my_list)
    return (total / sum(x[1] for x in my_list)) if my_list else 0
