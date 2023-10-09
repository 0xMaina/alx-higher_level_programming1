#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = []
    if idx < 0 or idx >= length:
        new_list = my_list
    else:
        for i in range(0, length):
            if i == idx:
                new_list.append(element)
            else:
                new_list.append(my_list[i])
    return (new_list)
