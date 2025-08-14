#!/usr/bin/python3
def weight_average(my_list=[]):
    return (sum(x["score"] * x["weight"] for x in my_list) / sum(x["weight"] for x in my_list)) if my_list else 0
