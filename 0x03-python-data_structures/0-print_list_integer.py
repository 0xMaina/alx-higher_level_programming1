#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for item in my_list:
        if isinstance(item, int):
            print("{}".format(item))
