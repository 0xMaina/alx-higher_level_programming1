#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if isinstance(my_list, list):
        length = len(my_list)
        if idx < 0 or idx >= length:
            return (my_list)
        for i in range(0, len(my_list)):
            if i == idx:
                my_list.remove(my_list[i])
                break
        return (my_list)
