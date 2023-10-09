#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for ch in my_string:
        if ch == "c" or ch == "C":
            continue
        else:
            new_string += ch
    return (new_string)
